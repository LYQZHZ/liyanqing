# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import sys

from PyQt5 import QtWidgets

import gongneng

# 按间距中的绿色按钮以运行脚本。
from UI import Ui_MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 固定的，表示程序应用
    ui = gongneng.gongneng()  # 实例化Ui_MainWindow
    ui.show() # 调用ui的show()以显示。同样show()是源于父类QtWidgets.QWidget的
    sys.exit(app.exec_())

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
