import sys
import io
import os
import json
import random
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView  # pip install PyQtWebEngine
from PyQt5 import QtCore
from PyQt5.QtCore import *


"""
Mapbox in PyQt5
"""


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Mapbox in PyQt Example')
        self.window_width, self.window_height = 600, 400
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        webView = QWebEngineView()
        webView.load(QUrl('http://localhost:8888/map.html'))
        layout.addWidget(webView)
        with open("map.json", "r") as jsonFile:
            data = json.load(jsonFile)

        data["coordinate"] = [-71.6516848, 48.5107057]
        
        with open("map.json", "w") as jsonFile:
            json.dump(data, jsonFile)


def reloadMap():
    with open("map.json", "r") as jsonFile:
        data = json.load(jsonFile)

    data["coordinate"] = [data["coordinate"][0]+0.00001,data["coordinate"][1]+0.00001]
    
    with open("map.json", "w") as jsonFile:
        json.dump(data, jsonFile)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 35px;
        }
    ''')
    timer = QTimer()
    timer.timeout.connect(reloadMap)  # execute `reloadMap`
    timer.setInterval(50)  # 1000ms = 1s
    timer.start()
    myApp = MyApp()

    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')
