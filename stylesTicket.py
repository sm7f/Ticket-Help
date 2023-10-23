from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMessageBox
from datetime import datetime
import schedule
import win32clipboard
import os


class AddStyles:
    def __init__(self):
        # Estabelecer a conexão com o banco de dados
        (
        )

    def style_top(self):
        return (
            "border-radius: 0px;\n"
            "background: #141414;\n"
            "box-shadow: 25px 25px 58px #2dba63, -25px -25px 58px #41ff91;"
        )
    def style_registro_area(self):
        return "background:#3a3668;"

    def style_op_left(self):
        return """
            #op_left QFrame {
                border-radius: 10px;
                background-color: rgb(255, 255, 255);
            }
            #op_left QPushButton {
                font: 87 8pt "Arial Black";
                color: rgb(255, 255, 255);
                background: #141414;
            }
            #op_left QPushButton:hover {
                background-color: #58fe81;
                color: black;
                border: 2px solid rgb(60,60,60);
            }
            #op_left QPushButton:focus {
                background-color: #58fe81;
                color: black;
                border: 2px solid black;
            }
        """

    def style_op_right(self):
        return """
            #op_right QFrame {
                border-radius: 10px;
                background-color: rgb(255, 255, 255);
            }
            #op_right QPushButton {
                font: 87 8pt "Arial Black";
                color: rgb(255, 255, 255);
                background: #141414;
            }
            #op_right QPushButton:hover {
                background-color: #58fe81;
                color: black;
                border: 2px solid rgb(60,60,60);
            }
            #op_right QPushButton:focus {
                background-color: #58fe81;
                color: black;
                border: 2px solid black;
            }
        """