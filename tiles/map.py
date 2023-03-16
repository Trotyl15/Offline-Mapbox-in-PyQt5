import sys
import io
import os
import folium  # pip install folium
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView  # pip install PyQtWebEngine
from PyQt5 import QtCore
from PyQt5.QtCore import QUrl

"""
Folium in PyQt5
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 35px;
        }
    ''')

    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')
