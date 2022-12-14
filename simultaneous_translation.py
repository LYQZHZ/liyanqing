# -*- coding:utf-8 -*-
import _thread as thread
import base64
import datetime
import hashlib
import hmac
import ssl
import time
from datetime import datetime
from time import mktime
from urllib.parse import urlencode
from wsgiref.handlers import format_date_time
import websocket
import json
from tool import pcm2wav

'''
 1、同声传译接口，可以将音频流实时翻译为不同语种的文本，并输对应的音频内容，广泛应用于国际论坛、智能会议、智慧教育、跨国交流等场景。
 '''

STATUS_FIRST_FRAME = 0  # 第一帧的标识
STATUS_CONTINUE_FRAME = 1  # 中间帧标识
STATUS_LAST_FRAME = 2  # 最后一帧的标识


class Ws_Param(object):
    # 初始化
    encoding = 'raw'

    def __init__(self, AudioFile):
        # 控制台鉴权信息
        self.APPID = '27e70702'
        self.APISecret = 'MDJhZmNhM2YzMGI1MTQ4ZWRlMDAwODA5'
        self.APIKey = '3a9cd2838e85effa589be2c6d7eb4012'
        self.Host = "ws-api.xf-yun.com"
        self.HttpProto = "HTTP/1.1"
        self.HttpMethod = "GET"
        self.RequestUri = "/v1/private/simult_interpretation"
        self.Algorithm = "hmac-sha256"
        self.url = "ws://" + self.Host + self.RequestUri
        #self.encoding = 'raw'

        # 设置测试音频文件
        self.AudioFile = AudioFile
        print("函数1")

    # 生成url
    def create_url(self):
        url = self.url
        # 生成RFC1123格式的时间戳
        now = datetime.now()
        print(now)
        date = format_date_time(mktime(now.timetuple()))
        print(date)
        signature_origin = "host: " + self.Host + "\n"
        signature_origin += "date: " + date + "\n"
        signature_origin += "GET " + self.RequestUri + " HTTP/1.1"
        signature_sha = hmac.new(self.APISecret.encode('utf-8'), signature_origin.encode('utf-8'),
                                 digestmod=hashlib.sha256).digest()
        signature_sha = base64.b64encode(signature_sha).decode(encoding='utf-8')
        authorization_origin = "api_key=\"%s\", algorithm=\"%s\", headers=\"%s\", signature=\"%s\"" % (
            self.APIKey, "hmac-sha256", "host date request-line", signature_sha)
        authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')
        v = {
            "authorization": authorization,
            "date": date,
            "host": self.Host,
            "serviceId": "simult_interpretation"
        }
        url = url + '?' + urlencode(v)
        print("函数2")
        return url

    @staticmethod
    def create_params(appid, status, audio):
        param = {
            "header": {
                "app_id": appid,
                "status": status,
            },
            "parameter": {
                "ist": {
                    "accent": "mandarin",
                    "domain": "ist_ed_open",
                    "language": "zh_cn",
                    "vto": 15000,
                    "eos": 150000
                },
                "streamtrans": {
                    "from": "cn",
                    "to": "en"
                },
                "tts": {
                    "vcn": "x2_catherine",
                    "tts_results": {
                        "encoding": "raw",
                        "sample_rate": 16000,
                        "channels": 1,
                        "bit_depth": 16,
                        "frame_size": 0
                    }
                }
            },

            "payload": {
                "data": {
                    "audio": str(base64.b64encode(audio).decode('utf-8')),
                    "encoding": "raw",
                    "sample_rate": 16000,
                    "seq": 1,
                    "status": status
                }
            }
        }
        print("函数3")
        return param

    # 收到websocket消息的处理
    def on_message(self, ws, message):
        try:
            print(f"收到的消息：{message}")

        except Exception as e:
            print("receive msg,but parse exception:", e)

        # 对结果进行解析
        message = json.loads(message)
        status = message["header"]["status"]
        sid = message["header"]["sid"]
        # 接收到的识别结果写到文本
        if "recognition_results" in message['payload']:
            result = message['payload']['recognition_results']['text']
            asrresult = base64.b64decode(result).decode()
            file1 = open('output\\text\\asr.txt', "a", encoding="UTF-8")
            file1.write(asrresult)
            file1.close()

        # 接收到的翻译结果写到文本
        if "streamtrans_results" in message['payload']:
            result = message['payload']['streamtrans_results']['text']
            transresult = base64.b64decode(result).decode()
            file1 = open('output\\text\\trans.txt', "a", encoding="UTF-8")
            file1.write(transresult)
            file1.close()

        # 把接收到的音频流合成PCM
        if "tts_results" in message['payload']:
            audio = message['payload']['tts_results']['audio']
            audio = base64.b64decode(audio)
            with open('output\\audio\\trans.pcm', 'ab') as f:
                f.write(audio)

        if status == 2:
            print("session end ")
            print("本次请求的sid==》 " + sid)
            print("数据处理完毕，等待实时转译结束！同传后的音频文件请到output/audio/目录查看...")
            time.sleep(1)
            ws.close()
        print("函数5")

    # 收到websocket错误的处理
    def on_error(self, ws, error):
        print("### error:", error)
        pass

    # 收到websocket关闭的处理
    def on_close(self, ws):
        print("### closed ###")

    # 收到websocket连接建立的处理
    def on_open(self, ws):
        print("函数6.0")

        def run(*args):
            print("函数6.1")
            frameSize = 8000  # 每一帧的音频大小
            print("函数6.2")
            intervel = 0.04  # 发送音频间隔(单位:s)
            print("函数6.3")
            status = STATUS_FIRST_FRAME  # 音频的状态信息，标识音频是第一帧，还是中间帧、最后一帧
            print("函数6.4")
            with open(self.AudioFile, "rb") as fp:
                print("函数6.5")
                while True:
                    buf = fp.read(frameSize)
                    print("函数6.6")
                    # 文件结束
                    if not buf:
                        print("函数6.9")
                        status = STATUS_LAST_FRAME
                        print("函数6.7")
                    # 第一帧处理
                    # 发送第一帧音频，带business 参数
                    # appid 必须带上，只需第一帧发送
                    if status == STATUS_FIRST_FRAME:
                        # print(wsParam.create_params(ws.appid, status, buf))
                        ws.send(json.dumps(self.create_params(ws.appid, status, buf)))
                        print('第一帧已发送...')
                        status = STATUS_CONTINUE_FRAME
                    # 中间帧处理
                    elif status == STATUS_CONTINUE_FRAME:
                        ws.send(json.dumps(self.create_params(ws.appid, status, buf)))
                        #print('中间帧已发送...')
                    # 最后一帧处理
                    elif status == STATUS_LAST_FRAME:
                        print('最后一帧已发送...')
                        ws.send(json.dumps(self.create_params(ws.appid, status, buf)))
                        break

                    # 模拟音频采样间隔
                    time.sleep(intervel)
                    print("函数6.8")
            # ws.close()

        print("函数6")
        thread.start_new_thread(run, ())

    def get_audio_text(self):
        websocket.enableTrace(False)
        wsUrl = self.create_url()
        # 创建转写、转译的text文本和传译的音频
        open('output\\text\\asr.txt', 'w')
        open('output\\text\\trans.txt', 'w')
        open('output\\audio\\trans.pcm', 'w')
        print("函数7.1")
        ws = websocket.WebSocketApp(wsUrl, on_message=self.on_message, on_error=self.on_error, on_close=self.on_close)
        print("函数7.2")
        ws.on_open = self.on_open
        print("函数7.3")
        ws.appid = self.APPID
        print("函数7.4")
        ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
        print("函数7.5")

        # 输出wav格式音频
        pcm2wav.pcm_2_wav("output\\audio\\trans.pcm", "output\\audio\\trans.wav")
        print("函数7")


def tongshengchuanyi():
    APPID = '27e70702'
    APISecret = 'MDJhZmNhM2YzMGI1MTQ4ZWRlMDAwODA5'
    APIKey = '3a9cd2838e85effa589be2c6d7eb4012'
    # 音频路径
    audio_path = r'lyq.pcm'
    demo = Ws_Param(audio_path)
    demo.get_audio_text()
    print("中")
