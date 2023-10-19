# coding: utf-8
import sys
import time
import json
import threading
# import pyttsx3
import numpy as np
from pathlib import Path
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import QCursor, QIcon, QMovie
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
import random 
import pickle

with open("intents/intents.json") as file:
    data = json.load(file)

with open("settings/json_file_chooser.txt", "r") as file:
    file_name = file.read()
    file.close()
with open(f"settings/{file_name}", "r") as j:
    json_data = json.loads(j.read())
    j.close()

# Load the AI model
model = keras.models.load_model('chat_model')
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
with open('label_encoder.pickle', 'rb') as enc:
    lbl_encoder = pickle.load(enc)
max_len = 20

state = 0

color1 = json_data['color1']
color2 = json_data['color2']
color3 = json_data['color3']
color4 = json_data['color4']
color5 = json_data['color5']
color6 = json_data['color6']
color7 = json_data['color7']
color8 = json_data['color8']
color9 = json_data['color9']
color10 = json_data['color10']
color11 = json_data['color11']
color12 = json_data['color12']
color13 = json_data['color13']
color14 = json_data['color14']
sp1 = json_data['sp1']
sp2 = json_data['sp2']
opc = json_data['opc']

# def talk(text):
    # engine = pyttsx3.init()
    # # voice = engine.getProperty('voices')
    # # engine.setProperty('voice', voice[2].id)
    # engine.setProperty('rate', 150)
    # engine.say(text)
    # engine.runAndWait()

class HelpWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.WIDTH = 400
        self.HEIGHT = 350
        self.resize(self.WIDTH, self.HEIGHT)
        self.centralwidget = QWidget(self)
        self.centralwidget.resize(self.WIDTH, self.HEIGHT)

        # Stylesheet
        self.setStyleSheet(f'''
        QPushButton{{
            color: {color1};
            font-size: 20px;
            font-weight: bold;
            font-family: Georgia;
            background: {color2};
            border-radius: 20px;
        }}
        QPushButton:hover{{
            color: {color3};
            background: {color4};
        }}
        QPushButton::pressed{{
            background: {color5};
        }}
        QLabel{{
            color: {color6};
            background: {color7};
            font-size: 20px;
            font-family: Georgia;
        }}
        ''')

        self.close_button = QPushButton('x', self)
        self.close_button.clicked.connect(self.close_ap)
        self.close_button.setGeometry(350, 10, 40, 40)

        self.lbl = QLabel("Help Guid", self)
        self.lbl.setGeometry(140, 20, 165, 40)

        self.help_list = QListWidget(self)
        self.help_list.setStyleSheet(
        f"""
        border: None;
        background-color: {color1};
        color: {color2};
        font-size: 20px;
        font-family: Georgia;
        QListWidget::item{{
            border: None;
        }}
        """
        )
        self.help_list.setGeometry(20, 60, 360, 250)

        help_scroll_bar = QScrollBar(self)
        help_scroll_bar.setStyleSheet(
        f"""
        QScrollBar:vertical{{
            background-color: {color1};
            width: 2px;
            border: 1px transparent;
            border-radius: 5px;
        }}
        QScrollBar::handle:vertical{{
            background-color: blue;
            min-height: 5px;
            border-radius: 4px;
        }}
        QScrollBar::sub-line:vertical{{
            subcontrol-position: top;
            subcontrol-origin: margin;
        }}
        
        """
        )
        self.help_list.setVerticalScrollBar(help_scroll_bar)
        self.help_list.setWordWrap(True)

        self.help_list.addItem(QListWidgetItem("* Enter your questions in the box given bellow and hit enter. Then the bot will reply."))
        self.help_list.addItem(QListWidgetItem("* If you need any further details abot this bot, please visit my github page to see the details."))

        # Initial
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(0.8)
        # self.setWindowOpacity(1)

        self.centralwidget.setStyleSheet(
            f"""
            background:{sp1};
            border-top-left-radius:30px;
            border-bottom-left-radius:30px;
            border-top-right-radius:30px;
            border-bottom-right-radius:30px;
            """
        )

    def close_ap(self):
        self.close()

class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.WIDTH = 400
        self.HEIGHT = 350
        self.resize(self.WIDTH, self.HEIGHT)
        self.centralwidget = QWidget(self)
        self.centralwidget.resize(self.WIDTH, self.HEIGHT)

        # Stylesheet
        self.setStyleSheet(f'''
        QPushButton{{
            color: {color1};
            font-size: 20px;
            font-weight: bold;
            font-family: Georgia;
            background: {color2};
            border-radius: 20px;
        }}
        QPushButton:hover{{
            color: {color3};
            background: {color4};
        }}
        QPushButton::pressed{{
            background: {color5};
        }}
        QLabel{{
            color: {color6};
            background: {color7};
            font-size: 20px;
            font-family: Georgia;
        }}
        ''')

        self.close_button = QPushButton('x', self)
        self.close_button.clicked.connect(self.close_ap)
        self.close_button.setGeometry(350, 10, 40, 40)

        self.lbl = QLabel("Settings", self)
        self.lbl.setGeometry(120, 20, 165, 40)

        self.white_theme_button = QPushButton('WhiteTheme', self)
        self.white_theme_button.clicked.connect(self.settings_changed_white)
        self.white_theme_button.setGeometry(100, 100, 200, 40)

        self.black_theme_button = QPushButton('Black Theme', self)
        self.black_theme_button.clicked.connect(self.settings_changed_black)
        self.black_theme_button.setGeometry(100, 150, 200, 40)

        self.opacityy = QLineEdit(self)
        self.opacityy.setStyleSheet(f"""
            color: {color2};
            font-weight: bold;
            font-family: Georgia;
            font-size: 15px;
            background: transparent;
            border: 5px solid {color2};
            border-radius: 20px;
        """)
        self.opacityy.setText(str(opc))
        self.opacityy.setGeometry(100, 200, 200, 40)

        self.opc_button = QPushButton('Set Opacity', self)
        self.opc_button.clicked.connect(self.settings_changed_opc)
        self.opc_button.setGeometry(100, 250, 200, 40)

        # Initial
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(0.8)
        # self.setWindowOpacity(1)

        self.centralwidget.setStyleSheet(
            f"""
            background:{sp1};
            border-top-left-radius:30px;
            border-bottom-left-radius:30px;
            border-top-right-radius:30px;
            border-bottom-right-radius:30px;
            """
        )

    def close_ap(self):
        self.close()

    def settings_changed_opc(self):
        with open("settings/white.json", "r") as j:
            data__ = json.load(j)
        opaci = self.opacityy.text()
        data__["opc"] = float(opaci)
        nd = json.dumps(data__)
        with open("settings/white.json", 'w') as json_:
            json_.write(nd)
            json_.close()
        with open("settings/black.json", "r") as j:
            data__ = json.load(j)
        opaci = self.opacityy.text()
        data__["opc"] = float(opaci)
        nd = json.dumps(data__)
        with open("settings/black.json", 'w') as json_:
            json_.write(nd)
            json_.close()

    def settings_changed_white(self):
        with open("settings/json_file_chooser.txt", "w") as file:
            file.write("white.json")
            file.close()

    def settings_changed_black(self):
        with open("settings/json_file_chooser.txt", "w") as file:
            file.write("black.json")
            file.close()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.sw = None
        self.hw = None

        # Window size
        self.WIDTH = 1000
        self.HEIGHT = 800
        self.resize(self.WIDTH, self.HEIGHT)

        # Stylesheet
        self.setStyleSheet(f'''
        QPushButton{{
            color: {color8};
            font-size: 20px;
            font-weight: bold;
            font-family: Georgia;
            background: {color9};
            border-radius: 20px;
        }}
        QPushButton:hover{{
            color: {color10};
            background: {color11};
        }}
        QPushButton::pressed{{
            background: {color12};
        }}
        QLineEdit{{
            color: {color13};
            font-weight: bold;
            font-family: Georgia;
            font-size: 20px;
            background: transparent;
            border: 5px solid {color14};
            border-radius: 20px;
        }}
        ''')

        # Widget
        self.centralwidget = QWidget(self)
        self.centralwidget.resize(self.WIDTH, self.HEIGHT)

        # Button
        self.help_button = QPushButton('H', self)
        self.help_button.setStatusTip("   Close")
        self.help_button.clicked.connect(self.help_show)
        self.help_button.setGeometry(10, 10, 40, 40)

        self.close_button = QPushButton('x', self)
        self.close_button.setStatusTip("   Close")
        self.close_button.clicked.connect(self.close_ap)
        self.close_button.setGeometry(950, 10, 40, 40)

        self.mini_button = QPushButton('_' ,self)
        self.mini_button.clicked.connect(self.showMinimized)
        self.mini_button.setStatusTip("   Minimize")
        self.mini_button.setGeometry(905, 10, 40, 40)

        self.settings_button = QPushButton('*' ,self)
        self.settings_button.clicked.connect(self.settings_window_open)
        self.settings_button.setStatusTip("   Settings")
        self.settings_button.setGeometry(850, 10, 40, 40)

        self.MovieLabel = QLabel(self)
        # Set gif content to be same size as window (600px / 400px)
        self.MovieLabel.setGeometry(QtCore.QRect(300, 50, 600, 400))
        self.movie = QMovie("imgs/BOT.gif")
        self.MovieLabel.setMovie(self.movie)
        self.movie.start()

        self.msg_list = QListWidget(self)
        self.msg_list.setStyleSheet(
        f"""
        border: None;
        background-color: {color2};
        color: {color1};
        font-size: 20px;
        font-family: Georgia;
        QListWidget::item{{
            border: None;
        }}
        """
        )
        self.msg_list.setGeometry(250, 500, 500, 150)

        scroll_bar = QScrollBar(self)
        scroll_bar.setStyleSheet(
        f"""
        QScrollBar:vertical{{
            background-color: {color1};
            width: 2px;
            border: 1px transparent;
            border-radius: 5px;
        }}
        QScrollBar::handle:vertical{{
            background-color: blue;
            min-height: 5px;
            border-radius: 4px;
        }}
        QScrollBar::sub-line:vertical{{
            subcontrol-position: top;
            subcontrol-origin: margin;
        }}
        
        """
        )
        self.msg_list.setVerticalScrollBar(scroll_bar)
        self.msg_list.setWordWrap(True)

        # text area
        self.text_area = QLineEdit(self)
        # self.text_area.setGeometry(200, 100, 300, 50)
        self.text_area.returnPressed.connect(self.navigate_url)
        self.text_area.setGeometry(250, 700, 500, 55)

        # Menu
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.right_menu)

        # Initial
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(opc)

        self.centralwidget.setStyleSheet(
            f"""
            background:{sp2};
            border: 5px solid blue;
            border-top-left-radius:30px;
            border-bottom-left-radius:30px;
            border-top-right-radius:30px;
            border-bottom-right-radius:30px;
            """
        )
        self.add_msg("IDA: Welcome!")

    def help_show(self):
        try:
            if self.hw is None:
                self.hw = HelpWindow()
            self.hw.show()
        except Exception:
            pass

    def add_msg(self, msg):
        self.msg_list.addItem(QListWidgetItem(msg))
        self.msg_list.scrollToBottom()

    def close_ap(self):
        sys.exit(0)

    def right_menu(self, pos):
        menu = QMenu()
        exit_option = menu.addAction('Exit')
        exit_option.triggered.connect(lambda: exit(0))
        menu.exec_(self.mapToGlobal(pos))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moveFlag = True
            self.movePosition = event.globalPos() - self.pos()
            self.setCursor(QCursor(Qt.OpenHandCursor))
            event.accept()

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.moveFlag:
            self.move(event.globalPos() - self.movePosition)
            event.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.moveFlag = False
        self.setCursor(Qt.CrossCursor)


    def settings_window_open(self, checked):
        try:
            if self.sw is None:
                self.sw = SettingsWindow()
            self.sw.show()
        except Exception:
            pass

    def update_text_area(self):
        self.text_area.setText("")
        self.text_area.setCursorPosition(0)

    def navigate_url(self):
        self.add_msg("")
        inp = self.text_area.text()
        self.add_msg("You: " + inp)
        if inp.lower() == 'quit' or inp.lower() == 'exit':
            self.close_ap()
        result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]), truncating='post', maxlen=max_len))
        tag = lbl_encoder.inverse_transform([np.argmax(result)])
        for i in data['intents']:
            if i['tag'] == tag:
                prase = np.random.choice(i['responses'])
                self.add_msg("IDA: " + prase)
        self.update_text_area()

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())