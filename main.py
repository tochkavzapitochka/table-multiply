import io
import sqlite3
import sys
from random import choice
import datetime as dt
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import (QApplication, QMainWindow)
import io
import random
from PyQt6 import uic  # Импортируем uic

template1 = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>283</width>
    <height>332</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Авторизация</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>10</y>
      <width>221</width>
      <height>266</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <widget class="QLabel" name="label">
       <property name="enabled">
        <bool>true</bool>
       </property>
       <property name="text">
        <string>Имя пользователя</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLineEdit" name="lineEdit"/>
     </item>
     <item>
      <widget class="QLabel" name="label_2">
       <property name="text">
        <string>Пароль</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLineEdit" name="lineEdit_2"/>
     </item>
     <item>
      <widget class="QPushButton" name="pushButton_2">
       <property name="text">
        <string>Войти</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="pushButton">
       <property name="text">
        <string>Регистрация</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>283</width>
     <height>24</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>727</width>
    <height>379</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Таблица Умножения</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>20</y>
      <width>181</width>
      <height>132</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <widget class="QComboBox" name="comboBox">
       <item>
        <property name="text">
         <string>2</string>
        </property>
       </item>
       <item>
        <property name="text">
         <string>3</string>
        </property>
       </item>
       <item>
        <property name="text">
         <string>4</string>
        </property>
       </item>
       <item>
        <property name="text">
         <string>5</string>
        </property>
       </item>
       <item>
        <property name="text">
         <string>6</string>
        </property>
       </item>
       <item>
        <property name="text">
         <string>7</string>
        </property>
       </item>
       <item>
        <property name="text">
         <string>8</string>
        </property>
       </item>
       <item>
        <property name="text">
         <string>9</string>
        </property>
       </item>
       <item>
        <property name="text">
         <string>10</string>
        </property>
       </item>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="pushButton">
       <property name="text">
        <string>Выбрать</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="pushButton_2">
       <property name="text">
        <string>Случайный режим</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="pushButton_3">
       <property name="text">
        <string>На время</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="horizontalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>220</x>
      <y>90</y>
      <width>251</width>
      <height>81</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
     </font>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout">
     <item>
      <widget class="QLabel" name="label">
       <property name="font">
        <font>
         <pointsize>16</pointsize>
        </font>
       </property>
       <property name="text">
        <string> </string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="label_2">
       <property name="font">
        <font>
         <pointsize>16</pointsize>
        </font>
       </property>
       <property name="text">
        <string> </string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="label_3">
       <property name="font">
        <font>
         <pointsize>16</pointsize>
        </font>
       </property>
       <property name="text">
        <string> </string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="label_4">
       <property name="font">
        <font>
         <pointsize>16</pointsize>
        </font>
       </property>
       <property name="text">
        <string> </string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QLabel" name="label_5">
    <property name="geometry">
     <rect>
      <x>400</x>
      <y>20</y>
      <width>16</width>
      <height>16</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="text">
     <string>0</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_6">
    <property name="geometry">
     <rect>
      <x>220</x>
      <y>20</y>
      <width>161</width>
      <height>16</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Правильных ответов</string>
    </property>
   </widget>
   <widget class="QTextEdit" name="textEdit">
    <property name="geometry">
     <rect>
      <x>500</x>
      <y>90</y>
      <width>181</width>
      <height>81</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
     </font>
    </property>
   </widget>
   <widget class="QLabel" name="label_7">
    <property name="geometry">
     <rect>
      <x>470</x>
      <y>20</y>
      <width>181</width>
      <height>16</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Неправильных ответов</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_8">
    <property name="geometry">
     <rect>
      <x>660</x>
      <y>20</y>
      <width>31</width>
      <height>16</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="text">
     <string>0</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_9">
    <property name="geometry">
     <rect>
      <x>220</x>
      <y>220</y>
      <width>60</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Время</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_10">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>170</y>
      <width>181</width>
      <height>121</height>
     </rect>
    </property>
    <property name="layoutDirection">
     <enum>Qt::RightToLeft</enum>
    </property>
    <property name="text">
     <string>Фото</string>
    </property>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget_2">
    <property name="geometry">
     <rect>
      <x>500</x>
      <y>220</y>
      <width>187</width>
      <height>100</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout_2">
     <item>
      <widget class="QPushButton" name="pushButton_5">
       <property name="text">
        <string>Ответить</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="pushButton_6">
       <property name="text">
        <string>Закончить</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="pushButton_7">
       <property name="text">
        <string>Сменить пользователя</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>727</width>
     <height>24</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class Autorisation(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        f1 = io.StringIO(template1)
        uic.loadUi(f1, self)  # Загружаем дизайн

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)  # Загружаем дизайн
        # Обратите внимание: имя элемента такое же как в QTDesigner
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.label.setText("OK")
        self.second_form = Autorisation(self, 'text')
        self.second_form.show()
        self.hide()

        # Имя элемента совпадает с objectName в QTDesigner


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())



