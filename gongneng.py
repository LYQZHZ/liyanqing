import os
import sys
import time

from PyQt5.QtWidgets import QMainWindow, QFileDialog

import WebITS
import iat_ws_python3
import igr_ws
import ise_ws_python3_demo
import tts_ws_python3_demo
import ttsfortscy
from UI import Ui_MainWindow
import luyin2
import simultaneous_translation
from wav2pcm import wav_to_pcm


class gongneng(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(gongneng, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('语音识别-李岩青')
        self.setWindowIconText("🎙️")

    def yuyinshibie(self):
        fname, _ = QFileDialog.getOpenFileName(self, '请选择wav格式文件且必须为16000hz采样，16位深度', 'D:\\', "wav file(*.wav)")
        self.wenjianlujingxianshikuang.setText(fname)
        if fname != '':
            result = iat_ws_python3.zhu(fname)
            self.yuyinshibiejieguoxianshikuang.clear()
            self.yuyinshibiejieguoxianshikuang.setText(result)
        else:
            self.yuyinshibiejieguoxianshikuang.clear()
            self.yuyinshibiejieguoxianshikuang.setText("请选择用于语音识别的文件！")

    def yuyinhecheng(self):

        text = self.yuyinshibiejieguoxianshikuang.toPlainText()
        yusu = self.yusutiaojietiao.value()
        fayanren = self.fayanrenlan.currentText()

        print(text)
        if text != '':
            result = tts_ws_python3_demo.yuyinhecheng(text,yusu,fayanren)
            self.yuyinshibiejieguoxianshikuang.setText(result)
        else:
            self.yuyinshibiejieguoxianshikuang.clear()
            self.yuyinshibiejieguoxianshikuang.setText("请输入文字！")

    def yusuzhishezhi(self):
        self.yusuzhi.setText(str(self.yusutiaojietiao.value()))

    def xingbienianlingfenxi(self):
        fname, _ = QFileDialog.getOpenFileName(self, '请选择wav格式文件且必须为16000hz采样，16bit', 'D:\\', "wav file(*.wav)")
        self.wenjianlujingxianshikuang.setText(fname)
        if fname != '':
            result = igr_ws.xingbienianlingfenxi(fname)
            print(result)
            self.yuyinshibiejieguoxianshikuang.clear()
            self.yuyinshibiejieguoxianshikuang.setText(str(result['all']))
        else:
            self.yuyinshibiejieguoxianshikuang.clear()
            self.yuyinshibiejieguoxianshikuang.setText("请选择用于性别分析的文件！")

    def juzifenxianniu(self):
        text = self.yuyinshibiejieguoxianshikuang.toPlainText()
        yuzhong = self.yuzhonglan.currentText()
        nianling = self.nianlingleixinglan.currentText()
        print(text)
        if text != '':
            if yuzhong=='cn_vip':
                fname, _ = QFileDialog.getOpenFileName(self, '请选择wav格式文件且必须为16000hz采样，16bit', 'D:\\', "wav file(*.wav)")
                if fname != '':
                    self.wenjianlujingxianshikuang.setText(fname)
                    result = ise_ws_python3_demo.juzifenxi(fname, '\uFEFF' + text, yuzhong, nianling,"read_sentence")
                    self.yuyinshibiejieguoxianshikuang.setText(result)
                else:
                    self.yuyinshibiejieguoxianshikuang.clear()
                    self.yuyinshibiejieguoxianshikuang.setText("请选择用于句子分析的文件！")
            if yuzhong == 'en_vip':
                fname, _ = QFileDialog.getOpenFileName(self, '请选择wav格式文件且必须为16000hz采样，16bit', 'D:\\', "wav file(*.wav)")
                if fname != '':
                    self.wenjianlujingxianshikuang.setText(fname)
                    result = ise_ws_python3_demo.juzifenxi(fname, '\uFEFF' + text, yuzhong, nianling, "read_chapter")
                    self.yuyinshibiejieguoxianshikuang.setText(result)
                else:
                    self.yuyinshibiejieguoxianshikuang.clear()
                    self.yuyinshibiejieguoxianshikuang.setText("请选择用于句子分析的文件！")

        else:
            self.yuyinshibiejieguoxianshikuang.clear()
            self.yuyinshibiejieguoxianshikuang.setText("请输入文字！")

    def fanyi(self):
        yuan = self.yuanyuzhongxialalan.currentText()
        if("汉语普通话"==yuan):
            yuanyuzhong="cn"
        elif("英语"==yuan):
            yuanyuzhong = "en"
        elif ("俄语" == yuan):
            yuanyuzhong = "ru"
        elif ("日语" == yuan):
            yuanyuzhong = "ja"
        elif ("丹麦语" == yuan):
            yuanyuzhong = "da"
        mubiao = self.mubiaoyuzhongxialalan.currentText()
        if ("汉语普通话" == mubiao):
            mubiaoyuzhong = "cn"
        elif ("英语" == mubiao):
            mubiaoyuzhong = "en"
        elif ("俄语" == mubiao):
            mubiaoyuzhong = "ru"
        elif ("日语" == mubiao):
            mubiaoyuzhong = "ja"
        elif ("丹麦语" == mubiao):
            mubiaoyuzhong = "da"
        text = self.yuanyuzhongshurukuang.toPlainText()
        if text != '':
            result = WebITS.fanyi(text,yuanyuzhong,mubiaoyuzhong)
            self.mubiaoyuzhongxianshikuang.setText(result)
        else:
            self.yuyinshibiejieguoxianshikuang.clear()
            self.yuyinshibiejieguoxianshikuang.setText("请输入文字！")

    def tongshengchuanyianxia(self):
        print("按下")
        luyin2.rec = luyin2.Recorder()
        luyin2.begin = time.time()
        print("Start recording")
        luyin2.rec.start()
        self.yuyinshibiejieguoxianshikuang.setText('录音开始，请靠近麦克风讲话。如果你说完了就请松开按钮。')


    def tongshengchnuayitaiqi(self):
        print("抬起")
        print("Stop recording")

        luyin2.rec.stop()
        luyin2.fina = time.time()
        t = luyin2.fina - luyin2.begin
        luyin2.rec.save("lyq.wav")
        wav_to_pcm("lyq.wav")
        print("前")
        fname="lyq.wav"
        self.wenjianlujingxianshikuang.setText(fname)
        if fname != '':
            result = iat_ws_python3.zhu(fname)
            self.yuyinshibiejieguoxianshikuang.clear()
            self.yuyinshibiejieguoxianshikuang.setText(result)
            yuan = self.tscyyuanyuzhongxialalan.currentText()
            if ("汉语普通话" == yuan):
                yuanyuzhong = "cn"
            elif ("英语" == yuan):
                yuanyuzhong = "en"
            elif ("俄语" == yuan):
                yuanyuzhong = "ru"
            elif ("日语" == yuan):
                yuanyuzhong = "ja"
            elif ("丹麦语" == yuan):
                yuanyuzhong = "da"
            mubiao = self.tscymubiaoyuzhongxialalan.currentText()
            if ("汉语普通话" == mubiao):
                mubiaoyuzhong = "cn"
            elif ("英语" == mubiao):
                mubiaoyuzhong = "en"
            elif ("俄语" == mubiao):
                mubiaoyuzhong = "ru"
            elif ("日语" == mubiao):
                mubiaoyuzhong = "ja"
            elif ("丹麦语" == mubiao):
                mubiaoyuzhong = "da"
            text = self.yuyinshibiejieguoxianshikuang.toPlainText()
            if text != '':
                result = WebITS.fanyi(text, yuanyuzhong, mubiaoyuzhong)
                text = result
                yusu = 50
                fayanren = self.tscyfayanrenlan.currentText()

                print(text)
                if text != '':
                    if os.path.exists("./output/audio/demo.pcm"):
                        os.remove("./output/audio/demo.pcm")
                    else:
                        print("The file does not exist")
                    result2 = ttsfortscy.tscy(text, yusu, fayanren)
                    self.yuyinshibiejieguoxianshikuang.setText("翻译结果："+result+'\n'+'录音时间为%ds.' % t +'\n'+'数据处理完毕，等待实时转译结束！' +'\n'+'同传后的音频文件请到output/audio/目录查看...')
                else:
                    self.yuyinshibiejieguoxianshikuang.clear()
                    self.yuyinshibiejieguoxianshikuang.setText("没有接收到声音！请在按钮按下后稍等1秒等待系统调用麦克后方可录音！")
            else:
                self.yuyinshibiejieguoxianshikuang.clear()
                self.yuyinshibiejieguoxianshikuang.setText("没有接收到声音！请在按钮按下后稍等1秒等待系统调用麦克后方可录音！")
        else:
            self.yuyinshibiejieguoxianshikuang.clear()
            self.yuyinshibiejieguoxianshikuang.setText("没有接收到声音！请在按钮按下后稍等1秒等待系统调用麦克后方可录音！")
        print("后")


    def dakaitongshengchuanyimulu(self):
        path = r'\output\audio'
        print(os.path.abspath('..')+path)
        os.system("start explorer "+os.path.abspath('.')+path)

    def dakaiyuyinhechengmulu(self):
        path = r'\output\yuyinhecheng'
        os.system("start explorer "+os.path.abspath('.')+path)