# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyside-remake/BitMask.ui',
# licensing of 'pyside-remake/BitMask.ui' applies.
#
# Created: Fri Sep 20 03:05:54 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import re


class BitPushButton(QtWidgets.QPushButton):

    BitToggled = QtCore.Signal(int)

    def __init__(self, parent, index, bit_value, *args, **kwargs):
        super(BitPushButton, self).__init__(parent, *args, **kwargs)
        self._index = index
        self._bit_value = bit_value
        self.setText(str(self._bit_value))

    @property
    def index(self):
        return self._index

    @property
    def bit_value(self):
        return self._bit_value

    @index.setter
    def index(self, new_index):
        self._index = new_index

    @bit_value.setter
    def bit_value(self, new_bit_value):
        self._bit_value = new_bit_value

    def get_value(self):
        return (self._bit_value << self._index)

    def button_click_slot(self):
        self.BitToggled.emit(self._index)

    def toggle_bit_value(self):
        self._bit_value = (self._bit_value ^ 1)


class Ui_BitMask32(object):

    def setupUi(self, BitMask32):

        self.mainWindow = BitMask32
        BitMask32.setObjectName("BitMask32")
        BitMask32.setEnabled(True)
        BitMask32.resize(573, 424)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BitMask32.sizePolicy().hasHeightForWidth())
        BitMask32.setSizePolicy(sizePolicy)
        BitMask32.setMaximumSize(QtCore.QSize(573, 424))
        BitMask32.setAutoFillBackground(False)

        self.root = QtWidgets.QWidget(BitMask32)
        self.root.setEnabled(True)
        self.root.setObjectName("root")
        self.mainFrame = QtWidgets.QFrame(self.root)
        self.mainFrame.setGeometry(QtCore.QRect(10, 10, 551, 381))
        self.mainFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setLineWidth(1)
        self.mainFrame.setObjectName("mainFrame")

        self.frameByte1 = QtWidgets.QFrame(self.mainFrame)
        self.frameByte1.setGeometry(QtCore.QRect(270, 40, 271, 91))
        self.frameByte1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frameByte1.setFrameShape(QtWidgets.QFrame.Box)
        self.frameByte1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frameByte1.setLineWidth(1)
        self.frameByte1.setObjectName("frameByte1")

        self.frameByte2 = QtWidgets.QFrame(self.mainFrame)
        self.frameByte2.setGeometry(QtCore.QRect(10, 40, 261, 91))
        self.frameByte2.setFrameShape(QtWidgets.QFrame.Box)
        self.frameByte2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frameByte2.setObjectName("frameByte2")

        self.frameByte3 = QtWidgets.QFrame(self.mainFrame)
        self.frameByte3.setGeometry(QtCore.QRect(10, 130, 261, 91))
        self.frameByte3.setFrameShape(QtWidgets.QFrame.Box)
        self.frameByte3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frameByte3.setObjectName("frameByte3")

        self.frameByte4 = QtWidgets.QFrame(self.mainFrame)
        self.frameByte4.setGeometry(QtCore.QRect(270, 130, 271, 91))
        self.frameByte4.setFrameShape(QtWidgets.QFrame.Box)
        self.frameByte4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frameByte4.setObjectName("frameByte4")

        self.bit_buttons = [BitPushButton(index=i, parent=self.frameByte1, bit_value=0) for i in range(0, 8)] + \
                           [BitPushButton(index=i, parent=self.frameByte2, bit_value=0) for i in range(8, 16)] + \
                           [BitPushButton(index=i, parent=self.frameByte4, bit_value=0) for i in range(16, 24)] + \
                           [BitPushButton(index=i, parent=self.frameByte3, bit_value=0) for i in range(24, 32)]

        for button in self.bit_buttons:
            button.BitToggled.connect(self.pushButtonBitXX_clicked_slot)

        self.register_value = 0

        self.pushButtonBit00 = self.bit_buttons[0]
        self.pushButtonBit00.setGeometry(QtCore.QRect(230, 50, 32, 32))
        self.pushButtonBit00.setToolTip("Bit 0")
        self.pushButtonBit00.setAutoExclusive(False)
        self.pushButtonBit00.setAutoDefault(False)
        self.pushButtonBit00.setDefault(False)
        self.pushButtonBit00.setFlat(False)
        self.pushButtonBit00.setObjectName("pushButtonBit00")

        self.pushButtonBit01 = self.bit_buttons[1]
        self.pushButtonBit01.setGeometry(QtCore.QRect(200, 50, 32, 32))
        self.pushButtonBit01.setToolTip("Bit 1")
        self.pushButtonBit01.setAutoExclusive(False)
        self.pushButtonBit01.setAutoDefault(False)
        self.pushButtonBit01.setDefault(False)
        self.pushButtonBit01.setFlat(False)
        self.pushButtonBit01.setObjectName("pushButtonBit01")

        self.pushButtonBit02 = self.bit_buttons[2]
        self.pushButtonBit02.setGeometry(QtCore.QRect(170, 50, 32, 32))
        self.pushButtonBit02.setToolTip("Bit 2")
        self.pushButtonBit02.setAutoExclusive(False)
        self.pushButtonBit02.setAutoDefault(False)
        self.pushButtonBit02.setDefault(False)
        self.pushButtonBit02.setFlat(False)
        self.pushButtonBit02.setObjectName("pushButtonBit02")

        self.pushButtonBit03 = self.bit_buttons[3]
        self.pushButtonBit03.setGeometry(QtCore.QRect(140, 50, 32, 32))
        self.pushButtonBit03.setToolTip("Bit 3")
        self.pushButtonBit03.setAutoExclusive(False)
        self.pushButtonBit03.setAutoDefault(False)
        self.pushButtonBit03.setDefault(False)
        self.pushButtonBit03.setFlat(False)
        self.pushButtonBit03.setObjectName("pushButtonBit03")

        self.pushButtonBit04 = self.bit_buttons[4]
        self.pushButtonBit04.setGeometry(QtCore.QRect(110, 50, 32, 32))
        self.pushButtonBit04.setToolTip("Bit 4")
        self.pushButtonBit04.setAutoExclusive(False)
        self.pushButtonBit04.setAutoDefault(False)
        self.pushButtonBit04.setDefault(False)
        self.pushButtonBit04.setFlat(False)
        self.pushButtonBit04.setObjectName("pushButtonBit04")

        self.pushButtonBit05 = self.bit_buttons[5]
        self.pushButtonBit05.setGeometry(QtCore.QRect(80, 50, 32, 32))
        self.pushButtonBit05.setToolTip("Bit 5")
        self.pushButtonBit05.setAutoExclusive(False)
        self.pushButtonBit05.setAutoDefault(False)
        self.pushButtonBit05.setDefault(False)
        self.pushButtonBit05.setFlat(False)
        self.pushButtonBit05.setObjectName("pushButtonBit05")

        self.pushButtonBit06 = self.bit_buttons[6]
        self.pushButtonBit06.setGeometry(QtCore.QRect(50, 50, 32, 32))
        self.pushButtonBit06.setToolTip("Bit 6")
        self.pushButtonBit06.setAutoExclusive(False)
        self.pushButtonBit06.setAutoDefault(False)
        self.pushButtonBit06.setDefault(False)
        self.pushButtonBit06.setFlat(False)
        self.pushButtonBit06.setObjectName("pushButtonBit06")

        self.pushButtonBit07 = self.bit_buttons[7]
        self.pushButtonBit07.setGeometry(QtCore.QRect(20, 50, 32, 32))
        self.pushButtonBit07.setToolTip("Bit 7")
        self.pushButtonBit07.setAutoExclusive(False)
        self.pushButtonBit07.setAutoDefault(False)
        self.pushButtonBit07.setDefault(False)
        self.pushButtonBit07.setFlat(False)
        self.pushButtonBit07.setObjectName("pushButtonBit07")

        self.pushButtonBit08 = self.bit_buttons[8]
        self.pushButtonBit08.setGeometry(QtCore.QRect(220, 50, 32, 32))
        self.pushButtonBit08.setToolTip("Bit 8")
        self.pushButtonBit08.setAutoExclusive(False)
        self.pushButtonBit08.setAutoDefault(False)
        self.pushButtonBit08.setDefault(False)
        self.pushButtonBit08.setFlat(False)
        self.pushButtonBit08.setObjectName("pushButtonBit08")

        self.pushButtonBit09 = self.bit_buttons[9]
        self.pushButtonBit09.setGeometry(QtCore.QRect(190, 50, 32, 32))
        self.pushButtonBit09.setToolTip("Bit 9")
        self.pushButtonBit09.setAutoExclusive(False)
        self.pushButtonBit09.setAutoDefault(False)
        self.pushButtonBit09.setDefault(False)
        self.pushButtonBit09.setFlat(False)
        self.pushButtonBit09.setObjectName("pushButtonBit09")

        self.pushButtonBit10 = self.bit_buttons[10]
        self.pushButtonBit10.setGeometry(QtCore.QRect(160, 50, 32, 32))
        self.pushButtonBit10.setToolTip("Bit 10")
        self.pushButtonBit10.setAutoExclusive(False)
        self.pushButtonBit10.setAutoDefault(False)
        self.pushButtonBit10.setDefault(False)
        self.pushButtonBit10.setFlat(False)
        self.pushButtonBit10.setObjectName("pushButtonBit10")

        self.pushButtonBit11 = self.bit_buttons[11]
        self.pushButtonBit11.setGeometry(QtCore.QRect(130, 50, 32, 32))
        self.pushButtonBit11.setToolTip("Bit 11")
        self.pushButtonBit11.setAutoExclusive(False)
        self.pushButtonBit11.setAutoDefault(False)
        self.pushButtonBit11.setDefault(False)
        self.pushButtonBit11.setFlat(False)
        self.pushButtonBit11.setObjectName("pushButtonBit11")

        self.pushButtonBit12 = self.bit_buttons[12]
        self.pushButtonBit12.setGeometry(QtCore.QRect(100, 50, 32, 32))
        self.pushButtonBit12.setToolTip("Bit 12")
        self.pushButtonBit12.setAutoExclusive(False)
        self.pushButtonBit12.setAutoDefault(False)
        self.pushButtonBit12.setDefault(False)
        self.pushButtonBit12.setFlat(False)
        self.pushButtonBit12.setObjectName("pushButtonBit12")

        self.pushButtonBit13 = self.bit_buttons[13]
        self.pushButtonBit13.setGeometry(QtCore.QRect(70, 50, 32, 32))
        self.pushButtonBit13.setToolTip("Bit 13")
        self.pushButtonBit13.setAutoExclusive(False)
        self.pushButtonBit13.setAutoDefault(False)
        self.pushButtonBit13.setDefault(False)
        self.pushButtonBit13.setFlat(False)
        self.pushButtonBit13.setObjectName("pushButtonBit13")

        self.pushButtonBit14 = self.bit_buttons[14]
        self.pushButtonBit14.setGeometry(QtCore.QRect(40, 50, 32, 32))
        self.pushButtonBit14.setToolTip("Bit 14")
        self.pushButtonBit14.setAutoExclusive(False)
        self.pushButtonBit14.setAutoDefault(False)
        self.pushButtonBit14.setDefault(False)
        self.pushButtonBit14.setFlat(False)
        self.pushButtonBit14.setObjectName("pushButtonBit14")

        self.pushButtonBit15 = self.bit_buttons[15]
        self.pushButtonBit15.setGeometry(QtCore.QRect(10, 50, 32, 32))
        self.pushButtonBit15.setToolTip("Bit 15")
        self.pushButtonBit15.setAutoExclusive(False)
        self.pushButtonBit15.setAutoDefault(False)
        self.pushButtonBit15.setDefault(False)
        self.pushButtonBit15.setFlat(False)
        self.pushButtonBit15.setObjectName("pushButtonBit15")

        self.pushButtonBit16 = self.bit_buttons[16]
        self.pushButtonBit16.setGeometry(QtCore.QRect(230, 50, 32, 32))
        self.pushButtonBit16.setToolTip("Bit 16")
        self.pushButtonBit16.setAutoExclusive(False)
        self.pushButtonBit16.setAutoDefault(False)
        self.pushButtonBit16.setDefault(False)
        self.pushButtonBit16.setFlat(False)
        self.pushButtonBit16.setObjectName("pushButtonBit16")

        self.pushButtonBit17 = self.bit_buttons[17]
        self.pushButtonBit17.setGeometry(QtCore.QRect(200, 50, 32, 32))
        self.pushButtonBit17.setToolTip("Bit 17")
        self.pushButtonBit17.setAutoExclusive(False)
        self.pushButtonBit17.setAutoDefault(False)
        self.pushButtonBit17.setDefault(False)
        self.pushButtonBit17.setFlat(False)
        self.pushButtonBit17.setObjectName("pushButtonBit17")

        self.pushButtonBit18 = self.bit_buttons[18]
        self.pushButtonBit18.setGeometry(QtCore.QRect(170, 50, 32, 32))
        self.pushButtonBit18.setToolTip("Bit 18")
        self.pushButtonBit18.setAutoExclusive(False)
        self.pushButtonBit18.setAutoDefault(False)
        self.pushButtonBit18.setDefault(False)
        self.pushButtonBit18.setFlat(False)
        self.pushButtonBit18.setObjectName("pushButtonBit18")

        self.pushButtonBit19 = self.bit_buttons[19]
        self.pushButtonBit19.setGeometry(QtCore.QRect(140, 50, 32, 32))
        self.pushButtonBit19.setToolTip("Bit 19")
        self.pushButtonBit19.setAutoExclusive(False)
        self.pushButtonBit19.setAutoDefault(False)
        self.pushButtonBit19.setDefault(False)
        self.pushButtonBit19.setFlat(False)
        self.pushButtonBit19.setObjectName("pushButtonBit19")

        self.pushButtonBit20 = self.bit_buttons[20]
        self.pushButtonBit20.setGeometry(QtCore.QRect(110, 50, 32, 32))
        self.pushButtonBit20.setToolTip("Bit 20")
        self.pushButtonBit20.setAutoExclusive(False)
        self.pushButtonBit20.setAutoDefault(False)
        self.pushButtonBit20.setDefault(False)
        self.pushButtonBit20.setFlat(False)
        self.pushButtonBit20.setObjectName("pushButtonBit20")

        self.pushButtonBit21 = self.bit_buttons[21]
        self.pushButtonBit21.setGeometry(QtCore.QRect(80, 50, 32, 32))
        self.pushButtonBit21.setToolTip("Bit 21")
        self.pushButtonBit21.setAutoExclusive(False)
        self.pushButtonBit21.setAutoDefault(False)
        self.pushButtonBit21.setDefault(False)
        self.pushButtonBit21.setFlat(False)
        self.pushButtonBit21.setObjectName("pushButtonBit21")

        self.pushButtonBit22 = self.bit_buttons[22]
        self.pushButtonBit22.setGeometry(QtCore.QRect(50, 50, 32, 32))
        self.pushButtonBit22.setToolTip("Bit 22")
        self.pushButtonBit22.setAutoExclusive(False)
        self.pushButtonBit22.setAutoDefault(False)
        self.pushButtonBit22.setDefault(False)
        self.pushButtonBit22.setFlat(False)
        self.pushButtonBit22.setObjectName("pushButtonBit22")

        self.pushButtonBit23 = self.bit_buttons[23]
        self.pushButtonBit23.setGeometry(QtCore.QRect(20, 50, 32, 32))
        self.pushButtonBit23.setToolTip("Bit 23")
        self.pushButtonBit23.setAutoExclusive(False)
        self.pushButtonBit23.setAutoDefault(False)
        self.pushButtonBit23.setDefault(False)
        self.pushButtonBit23.setFlat(False)
        self.pushButtonBit23.setObjectName("pushButtonBit23")

        self.pushButtonBit24 = self.bit_buttons[24]
        self.pushButtonBit24.setGeometry(QtCore.QRect(220, 50, 32, 32))
        self.pushButtonBit24.setToolTip("Bit 24")
        self.pushButtonBit24.setAutoExclusive(False)
        self.pushButtonBit24.setAutoDefault(False)
        self.pushButtonBit24.setDefault(False)
        self.pushButtonBit24.setFlat(False)
        self.pushButtonBit24.setObjectName("pushButtonBit24")

        self.pushButtonBit25 = self.bit_buttons[25]
        self.pushButtonBit25.setGeometry(QtCore.QRect(190, 50, 32, 32))
        self.pushButtonBit25.setToolTip("Bit 25")
        self.pushButtonBit25.setAutoExclusive(False)
        self.pushButtonBit25.setAutoDefault(False)
        self.pushButtonBit25.setDefault(False)
        self.pushButtonBit25.setFlat(False)
        self.pushButtonBit25.setObjectName("pushButtonBit25")

        self.pushButtonBit26 = self.bit_buttons[26]
        self.pushButtonBit26.setGeometry(QtCore.QRect(160, 50, 32, 32))
        self.pushButtonBit26.setToolTip("Bit 26")
        self.pushButtonBit26.setAutoExclusive(False)
        self.pushButtonBit26.setAutoDefault(False)
        self.pushButtonBit26.setDefault(False)
        self.pushButtonBit26.setFlat(False)
        self.pushButtonBit26.setObjectName("pushButtonBit26")

        self.pushButtonBit27 = self.bit_buttons[27]
        self.pushButtonBit27.setGeometry(QtCore.QRect(130, 50, 32, 32))
        self.pushButtonBit27.setToolTip("Bit 27")
        self.pushButtonBit27.setAutoExclusive(False)
        self.pushButtonBit27.setAutoDefault(False)
        self.pushButtonBit27.setDefault(False)
        self.pushButtonBit27.setFlat(False)
        self.pushButtonBit27.setObjectName("pushButtonBit27")

        self.pushButtonBit28 = self.bit_buttons[28]
        self.pushButtonBit28.setGeometry(QtCore.QRect(100, 50, 32, 32))
        self.pushButtonBit28.setToolTip("Bit 28")
        self.pushButtonBit28.setAutoExclusive(False)
        self.pushButtonBit28.setAutoDefault(False)
        self.pushButtonBit28.setDefault(False)
        self.pushButtonBit28.setFlat(False)
        self.pushButtonBit28.setObjectName("pushButtonBit28")

        self.pushButtonBit29 = self.bit_buttons[29]
        self.pushButtonBit29.setGeometry(QtCore.QRect(70, 50, 32, 32))
        self.pushButtonBit29.setToolTip("Bit 29")
        self.pushButtonBit29.setAutoExclusive(False)
        self.pushButtonBit29.setAutoDefault(False)
        self.pushButtonBit29.setDefault(False)
        self.pushButtonBit29.setFlat(False)
        self.pushButtonBit29.setObjectName("pushButtonBit29")

        self.pushButtonBit30 = self.bit_buttons[30]
        self.pushButtonBit30.setGeometry(QtCore.QRect(40, 50, 32, 32))
        self.pushButtonBit30.setToolTip("Bit 30")
        self.pushButtonBit30.setAutoExclusive(False)
        self.pushButtonBit30.setAutoDefault(False)
        self.pushButtonBit30.setDefault(False)
        self.pushButtonBit30.setFlat(False)
        self.pushButtonBit30.setObjectName("pushButtonBit30")

        self.pushButtonBit31 = self.bit_buttons[31]
        self.pushButtonBit31.setGeometry(QtCore.QRect(10, 50, 32, 32))
        self.pushButtonBit31.setToolTip("Bit 31")
        self.pushButtonBit31.setAutoExclusive(False)
        self.pushButtonBit31.setAutoDefault(False)
        self.pushButtonBit31.setDefault(False)
        self.pushButtonBit31.setFlat(False)
        self.pushButtonBit31.setObjectName("pushButtonBit31")

        self.pushButtonCopyHexValue = QtWidgets.QPushButton(self.mainFrame)
        self.pushButtonCopyHexValue.setGeometry(QtCore.QRect(370, 230, 161, 28))
        self.pushButtonCopyHexValue.setObjectName("pushButtonCopyHexValue")

        self.pushButtonClear = QtWidgets.QPushButton(self.mainFrame)
        self.pushButtonClear.setGeometry(QtCore.QRect(100, 340, 93, 28))
        self.pushButtonClear.setObjectName("pushButtonClear")

        self.pushButtonCopyDeciValue = QtWidgets.QPushButton(self.mainFrame)
        self.pushButtonCopyDeciValue.setGeometry(QtCore.QRect(370, 280, 161, 28))
        self.pushButtonCopyDeciValue.setObjectName("pushButtonCopyDeciValue")

        self.pushButtonExit = QtWidgets.QPushButton(self.mainFrame)
        self.pushButtonExit.setGeometry(QtCore.QRect(290, 340, 93, 28))
        self.pushButtonExit.setObjectName("pushButtonExit")

        self.lineEditHexValue = QtWidgets.QLineEdit(self.mainFrame)
        self.lineEditHexValue.setGeometry(QtCore.QRect(190, 231, 113, 28))
        self.lineEditHexValue.setObjectName("lineEditHexValue")
        self.lineEditHexValue.setText("0x"+hex(self.register_value)[2:].upper().zfill(8))

        self.lineEditDeciValue = QtWidgets.QLineEdit(self.mainFrame)
        self.lineEditDeciValue.setGeometry(QtCore.QRect(190, 280, 113, 28))
        self.lineEditDeciValue.setObjectName("lineEditDeciValue")
        self.lineEditDeciValue.setText(str(self.register_value))

        self.checkBoxAOT = QtWidgets.QCheckBox(self.mainFrame)
        self.checkBoxAOT.setGeometry(QtCore.QRect(10, 10, 121, 20))
        self.checkBoxAOT.setObjectName("checkBoxAOT")

        self.clipBoard = QtGui.QClipboard()
        self.original_text = self.clipBoard.text()

        self.labelDeciValue = QtWidgets.QLabel(self.mainFrame)
        self.labelDeciValue.setGeometry(QtCore.QRect(20, 280, 121, 28))
        self.labelDeciValue.setObjectName("labelDeciValue")

        self.labelHexValue = QtWidgets.QLabel(self.mainFrame)
        self.labelHexValue.setGeometry(QtCore.QRect(20, 230, 121, 28))
        self.labelHexValue.setObjectName("labelHexValue")

        self.labelBit23 = QtWidgets.QLabel(self.frameByte4)
        self.labelBit23.setGeometry(QtCore.QRect(20, 20, 30, 30))
        self.labelBit23.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit23.setObjectName("labelBit23")

        self.labelBit16 = QtWidgets.QLabel(self.frameByte4)
        self.labelBit16.setGeometry(QtCore.QRect(230, 20, 30, 30))
        self.labelBit16.setTextFormat(QtCore.Qt.AutoText)
        self.labelBit16.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit16.setObjectName("labelBit16")

        self.labelBit19 = QtWidgets.QLabel(self.frameByte4)
        self.labelBit19.setGeometry(QtCore.QRect(140, 20, 30, 30))
        self.labelBit19.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit19.setObjectName("labelBit19")

        self.labelBit20 = QtWidgets.QLabel(self.frameByte4)
        self.labelBit20.setGeometry(QtCore.QRect(110, 20, 30, 30))
        self.labelBit20.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit20.setObjectName("labelBit20")

        self.labelBit17 = QtWidgets.QLabel(self.frameByte4)
        self.labelBit17.setGeometry(QtCore.QRect(200, 20, 30, 30))
        self.labelBit17.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit17.setObjectName("labelBit17")

        self.labelBit22 = QtWidgets.QLabel(self.frameByte4)
        self.labelBit22.setGeometry(QtCore.QRect(50, 20, 30, 30))
        self.labelBit22.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit22.setObjectName("labelBit22")

        self.labelBit21 = QtWidgets.QLabel(self.frameByte4)
        self.labelBit21.setGeometry(QtCore.QRect(80, 20, 30, 30))
        self.labelBit21.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit21.setObjectName("labelBit21")

        self.labelBit18 = QtWidgets.QLabel(self.frameByte4)
        self.labelBit18.setGeometry(QtCore.QRect(170, 20, 30, 30))
        self.labelBit18.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit18.setObjectName("labelBit18")

        self.labelBit31 = QtWidgets.QLabel(self.frameByte3)
        self.labelBit31.setGeometry(QtCore.QRect(10, 20, 30, 30))
        self.labelBit31.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit31.setObjectName("labelBit31")

        self.labelBit30 = QtWidgets.QLabel(self.frameByte3)
        self.labelBit30.setGeometry(QtCore.QRect(40, 20, 30, 30))
        self.labelBit30.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit30.setObjectName("labelBit30")

        self.labelBit26 = QtWidgets.QLabel(self.frameByte3)
        self.labelBit26.setGeometry(QtCore.QRect(160, 20, 30, 30))
        self.labelBit26.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit26.setObjectName("labelBit26")

        self.labelBit24 = QtWidgets.QLabel(self.frameByte3)
        self.labelBit24.setGeometry(QtCore.QRect(220, 20, 30, 30))
        self.labelBit24.setTextFormat(QtCore.Qt.AutoText)
        self.labelBit24.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit24.setObjectName("labelBit24")

        self.labelBit27 = QtWidgets.QLabel(self.frameByte3)
        self.labelBit27.setGeometry(QtCore.QRect(130, 20, 30, 30))
        self.labelBit27.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit27.setObjectName("labelBit27")

        self.labelBit25 = QtWidgets.QLabel(self.frameByte3)
        self.labelBit25.setGeometry(QtCore.QRect(190, 20, 30, 30))
        self.labelBit25.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit25.setObjectName("labelBit25")

        self.labelBit28 = QtWidgets.QLabel(self.frameByte3)
        self.labelBit28.setGeometry(QtCore.QRect(100, 20, 30, 30))
        self.labelBit28.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit28.setObjectName("labelBit28")

        self.labelBit29 = QtWidgets.QLabel(self.frameByte3)
        self.labelBit29.setGeometry(QtCore.QRect(70, 20, 30, 30))
        self.labelBit29.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit29.setObjectName("labelBit29")

        self.labelBit15 = QtWidgets.QLabel(self.frameByte2)
        self.labelBit15.setGeometry(QtCore.QRect(10, 20, 30, 30))
        self.labelBit15.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit15.setObjectName("labelBit15")

        self.labelBit10 = QtWidgets.QLabel(self.frameByte2)
        self.labelBit10.setGeometry(QtCore.QRect(160, 20, 30, 30))
        self.labelBit10.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit10.setObjectName("labelBit10")

        self.labelBit11 = QtWidgets.QLabel(self.frameByte2)
        self.labelBit11.setGeometry(QtCore.QRect(130, 20, 30, 30))
        self.labelBit11.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit11.setObjectName("labelBit11")

        self.labelBit13 = QtWidgets.QLabel(self.frameByte2)
        self.labelBit13.setGeometry(QtCore.QRect(70, 20, 30, 30))
        self.labelBit13.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit13.setObjectName("labelBit13")

        self.labelBit12 = QtWidgets.QLabel(self.frameByte2)
        self.labelBit12.setGeometry(QtCore.QRect(100, 20, 30, 30))
        self.labelBit12.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit12.setObjectName("labelBit12")

        self.labelBit09 = QtWidgets.QLabel(self.frameByte2)
        self.labelBit09.setGeometry(QtCore.QRect(190, 20, 30, 30))
        self.labelBit09.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit09.setObjectName("labelBit09")

        self.labelBit14 = QtWidgets.QLabel(self.frameByte2)
        self.labelBit14.setGeometry(QtCore.QRect(40, 20, 30, 30))
        self.labelBit14.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit14.setObjectName("labelBit14")

        self.labelBit08 = QtWidgets.QLabel(self.frameByte2)
        self.labelBit08.setGeometry(QtCore.QRect(220, 20, 30, 30))
        self.labelBit08.setTextFormat(QtCore.Qt.AutoText)
        self.labelBit08.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit08.setObjectName("labelBit08")

        self.labelBit07 = QtWidgets.QLabel(self.frameByte1)
        self.labelBit07.setGeometry(QtCore.QRect(20, 20, 30, 30))
        self.labelBit07.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit07.setObjectName("labelBit07")

        self.labelBit05 = QtWidgets.QLabel(self.frameByte1)
        self.labelBit05.setGeometry(QtCore.QRect(80, 20, 30, 30))
        self.labelBit05.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit05.setObjectName("labelBit05")

        self.labelBit03 = QtWidgets.QLabel(self.frameByte1)
        self.labelBit03.setGeometry(QtCore.QRect(140, 20, 30, 30))
        self.labelBit03.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit03.setObjectName("labelBit03")

        self.labelBit06 = QtWidgets.QLabel(self.frameByte1)
        self.labelBit06.setGeometry(QtCore.QRect(50, 20, 30, 30))
        self.labelBit06.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit06.setObjectName("labelBit06")

        self.labelBit01 = QtWidgets.QLabel(self.frameByte1)
        self.labelBit01.setGeometry(QtCore.QRect(200, 20, 30, 30))
        self.labelBit01.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit01.setObjectName("labelBit01")

        self.labelBit02 = QtWidgets.QLabel(self.frameByte1)
        self.labelBit02.setGeometry(QtCore.QRect(170, 20, 30, 30))
        self.labelBit02.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit02.setObjectName("labelBit02")

        self.labelBit00 = QtWidgets.QLabel(self.frameByte1)
        self.labelBit00.setGeometry(QtCore.QRect(230, 20, 30, 30))
        self.labelBit00.setTextFormat(QtCore.Qt.AutoText)
        self.labelBit00.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit00.setObjectName("labelBit00")

        self.labelBit04 = QtWidgets.QLabel(self.frameByte1)
        self.labelBit04.setGeometry(QtCore.QRect(110, 20, 30, 30))
        self.labelBit04.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit04.setObjectName("labelBit04")

        self.label = QtWidgets.QLabel(self.frameByte1)
        self.label.setGeometry(QtCore.QRect(10, 0, 55, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.frameByte2)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 55, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.frameByte3)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 55, 16))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.frameByte4)
        self.label_4.setGeometry(QtCore.QRect(10, 0, 55, 16))
        self.label_4.setObjectName("label_4")

        BitMask32.setCentralWidget(self.root)

        self.statusBar = QtWidgets.QStatusBar(BitMask32)
        self.statusBar.setObjectName("statusBar")
        BitMask32.setStatusBar(self.statusBar)

        self.retranslateUi(BitMask32)
        QtCore.QMetaObject.connectSlotsByName(BitMask32)

        BitMask32.setTabOrder(self.pushButtonBit00, self.pushButtonBit01)
        BitMask32.setTabOrder(self.pushButtonBit01, self.pushButtonBit02)
        BitMask32.setTabOrder(self.pushButtonBit02, self.pushButtonBit03)
        BitMask32.setTabOrder(self.pushButtonBit03, self.pushButtonBit04)
        BitMask32.setTabOrder(self.pushButtonBit04, self.pushButtonBit05)
        BitMask32.setTabOrder(self.pushButtonBit05, self.pushButtonBit06)
        BitMask32.setTabOrder(self.pushButtonBit06, self.pushButtonBit07)
        BitMask32.setTabOrder(self.pushButtonBit07, self.pushButtonBit08)
        BitMask32.setTabOrder(self.pushButtonBit08, self.pushButtonBit09)
        BitMask32.setTabOrder(self.pushButtonBit09, self.pushButtonBit10)
        BitMask32.setTabOrder(self.pushButtonBit10, self.pushButtonBit11)
        BitMask32.setTabOrder(self.pushButtonBit11, self.pushButtonBit12)
        BitMask32.setTabOrder(self.pushButtonBit12, self.pushButtonBit13)
        BitMask32.setTabOrder(self.pushButtonBit13, self.pushButtonBit14)
        BitMask32.setTabOrder(self.pushButtonBit14, self.pushButtonBit15)
        BitMask32.setTabOrder(self.pushButtonBit15, self.pushButtonBit16)
        BitMask32.setTabOrder(self.pushButtonBit16, self.pushButtonBit17)
        BitMask32.setTabOrder(self.pushButtonBit17, self.pushButtonBit18)
        BitMask32.setTabOrder(self.pushButtonBit18, self.pushButtonBit19)
        BitMask32.setTabOrder(self.pushButtonBit19, self.pushButtonBit20)
        BitMask32.setTabOrder(self.pushButtonBit20, self.pushButtonBit21)
        BitMask32.setTabOrder(self.pushButtonBit21, self.pushButtonBit22)
        BitMask32.setTabOrder(self.pushButtonBit22, self.pushButtonBit23)
        BitMask32.setTabOrder(self.pushButtonBit23, self.pushButtonBit24)
        BitMask32.setTabOrder(self.pushButtonBit24, self.pushButtonBit25)
        BitMask32.setTabOrder(self.pushButtonBit25, self.pushButtonBit26)
        BitMask32.setTabOrder(self.pushButtonBit26, self.pushButtonBit27)
        BitMask32.setTabOrder(self.pushButtonBit27, self.pushButtonBit28)
        BitMask32.setTabOrder(self.pushButtonBit28, self.pushButtonBit29)
        BitMask32.setTabOrder(self.pushButtonBit29, self.pushButtonBit30)
        BitMask32.setTabOrder(self.pushButtonBit30, self.pushButtonBit31)
        BitMask32.setTabOrder(self.pushButtonBit31, self.lineEditHexValue)
        BitMask32.setTabOrder(self.lineEditHexValue, self.pushButtonCopyHexValue)
        BitMask32.setTabOrder(self.pushButtonCopyHexValue, self.lineEditDeciValue)
        BitMask32.setTabOrder(self.lineEditDeciValue, self.pushButtonCopyDeciValue)
        BitMask32.setTabOrder(self.pushButtonCopyDeciValue, self.pushButtonClear)
        BitMask32.setTabOrder(self.pushButtonClear, self.pushButtonExit)
        BitMask32.setTabOrder(self.pushButtonExit, self.checkBoxAOT)

    def retranslateUi(self, BitMask32):

        BitMask32.setWindowTitle(QtWidgets.QApplication.translate("BitMask32", "Bit Mask 32", None, -1))
        self.checkBoxAOT.setText(QtWidgets.QApplication.translate("BitMask32", "Always On Top", None, -1))
        self.labelBit23.setText(QtWidgets.QApplication.translate("BitMask32", "23", None, -1))
        self.pushButtonBit21.setText(QtWidgets.QApplication.translate("BitMask32", "0", None, -1))
        self.pushButtonBit16.setText(QtWidgets.QApplication.translate("BitMask32", "0", None, -1))
        self.pushButtonBit22.setText(QtWidgets.QApplication.translate("BitMask32", "0", None, -1))
        self.pushButtonBit23.setText(QtWidgets.QApplication.translate("BitMask32", "0", None, -1))
        self.pushButtonBit18.setText(QtWidgets.QApplication.translate("BitMask32", "0", None, -1))
        self.labelBit16.setText(QtWidgets.QApplication.translate("BitMask32", "16", None, -1))
        self.labelBit19.setText(QtWidgets.QApplication.translate("BitMask32", "19", None, -1))
        self.pushButtonBit20.setText(QtWidgets.QApplication.translate("BitMask32", "0", None, -1))
        self.labelBit20.setText(QtWidgets.QApplication.translate("BitMask32", "20", None, -1))
        self.pushButtonBit19.setText(QtWidgets.QApplication.translate("BitMask32", "0", None, -1))
        self.labelBit17.setText(QtWidgets.QApplication.translate("BitMask32", "17", None, -1))
        self.labelBit22.setText(QtWidgets.QApplication.translate("BitMask32", "22", None, -1))
        self.pushButtonBit17.setText(QtWidgets.QApplication.translate("BitMask32", "0", None, -1))
        self.labelBit21.setText(QtWidgets.QApplication.translate("BitMask32", "21", None, -1))
        self.labelBit18.setText(QtWidgets.QApplication.translate("BitMask32", "18", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("BitMask32", "Byte 2", None, -1))
        self.pushButtonCopyHexValue.setText(QtWidgets.QApplication.translate("BitMask32", "Copy hex value", None, -1))
        self.pushButtonClear.setText(QtWidgets.QApplication.translate("BitMask32", "Clear", None, -1))
        self.labelBit31.setText(QtWidgets.QApplication.translate("BitMask32", "31", None, -1))
        self.labelBit30.setText(QtWidgets.QApplication.translate("BitMask32", "30", None, -1))
        self.pushButtonBit25.setText(QtWidgets.QApplication.translate("BitMask32", "0", None, -1))
        self.pushButtonBit26.setText(QtWidgets.QApplication.translate("BitMask32", "0", None, -1))
        self.labelBit26.setText(QtWidgets.QApplication.translate("BitMask32", "26", None, -1))
        self.pushButtonBit30.setText(QtWidgets.QApplication.translate("BitMask32", "0", None, -1))
        self.pushButtonBit29.setText(QtWidgets.QApplication.translate("BitMask32", "0", None, -1))
        self.pushButtonBit24.setText(QtWidgets.QApplication.translate("BitMask32", "0", None, -1))
        self.labelBit24.setText(QtWidgets.QApplication.translate("BitMask32", "24", None, -1))
        self.pushButtonBit28.setText(QtWidgets.QApplication.translate("BitMask32", "0", None, -1))
        self.pushButtonBit31.setText(QtWidgets.QApplication.translate("BitMask32", "0", None, -1))
        self.labelBit27.setText(QtWidgets.QApplication.translate("BitMask32", "27", None, -1))
        self.labelBit25.setText(QtWidgets.QApplication.translate("BitMask32", "25", None, -1))
        self.labelBit28.setText(QtWidgets.QApplication.translate("BitMask32", "28", None, -1))
        self.labelBit29.setText(QtWidgets.QApplication.translate("BitMask32", "29", None, -1))
        self.pushButtonBit27.setText(QtWidgets.QApplication.translate("BitMask32", "0", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("BitMask32", "Byte 3", None, -1))
        self.labelBit15.setText(QtWidgets.QApplication.translate("BitMask32", "15", None, -1))
        self.pushButtonBit09.setText(QtWidgets.QApplication.translate("BitMask32", "0", None, -1))
        self.labelBit10.setText(QtWidgets.QApplication.translate("BitMask32", "10", None, -1))
        self.labelBit11.setText(QtWidgets.QApplication.translate("BitMask32", "11", None, -1))
        self.labelBit13.setText(QtWidgets.QApplication.translate("BitMask32", "13", None, -1))
        self.pushButtonBit08.setText(QtWidgets.QApplication.translate("BitMask32", "0", None, -1))
        self.labelBit12.setText(QtWidgets.QApplication.translate("BitMask32", "12", None, -1))
        self.pushButtonBit10.setText(QtWidgets.QApplication.translate("BitMask32", "0", None, -1))
        self.pushButtonBit12.setText(QtWidgets.QApplication.translate("BitMask32", "0", None, -1))
        self.labelBit09.setText(QtWidgets.QApplication.translate("BitMask32", "9", None, -1))
        self.labelBit14.setText(QtWidgets.QApplication.translate("BitMask32", "14", None, -1))
        self.labelBit08.setText(QtWidgets.QApplication.translate("BitMask32", "8", None, -1))
        self.pushButtonBit14.setText(QtWidgets.QApplication.translate("BitMask32", "0", None, -1))
        self.pushButtonBit15.setText(QtWidgets.QApplication.translate("BitMask32", "0", None, -1))
        self.pushButtonBit13.setText(QtWidgets.QApplication.translate("BitMask32", "0", None, -1))
        self.pushButtonBit11.setText(QtWidgets.QApplication.translate("BitMask32", "0", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("BitMask32", "Byte 1", None, -1))
        self.labelHexValue.setText(QtWidgets.QApplication.translate("BitMask32", "Hex decimal value", None, -1))
        self.pushButtonCopyDeciValue.setText(QtWidgets.QApplication.translate("BitMask32", "Copy decimal value", None, -1))
        self.pushButtonBit07.setText(QtWidgets.QApplication.translate("BitMask32", "0", None, -1))
        self.pushButtonBit00.setText(QtWidgets.QApplication.translate("BitMask32", "0", None, -1))
        self.pushButtonBit05.setText(QtWidgets.QApplication.translate("BitMask32", "0", None, -1))
        self.pushButtonBit02.setText(QtWidgets.QApplication.translate("BitMask32", "0", None, -1))
        self.pushButtonBit03.setText(QtWidgets.QApplication.translate("BitMask32", "0", None, -1))
        self.pushButtonBit04.setText(QtWidgets.QApplication.translate("BitMask32", "0", None, -1))
        self.pushButtonBit06.setText(QtWidgets.QApplication.translate("BitMask32", "0", None, -1))
        self.pushButtonBit01.setText(QtWidgets.QApplication.translate("BitMask32", "0", None, -1))
        self.labelBit07.setText(QtWidgets.QApplication.translate("BitMask32", "7", None, -1))
        self.labelBit05.setText(QtWidgets.QApplication.translate("BitMask32", "5", None, -1))
        self.labelBit03.setText(QtWidgets.QApplication.translate("BitMask32", "3", None, -1))
        self.labelBit06.setText(QtWidgets.QApplication.translate("BitMask32", "6", None, -1))
        self.labelBit01.setText(QtWidgets.QApplication.translate("BitMask32", "1", None, -1))
        self.labelBit02.setText(QtWidgets.QApplication.translate("BitMask32", "2", None, -1))
        self.labelBit00.setText(QtWidgets.QApplication.translate("BitMask32", "0", None, -1))
        self.labelBit04.setText(QtWidgets.QApplication.translate("BitMask32", "4", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("BitMask32", "Byte 0", None, -1))
        self.pushButtonExit.setText(QtWidgets.QApplication.translate("BitMask32", "Exit", None, -1))
        self.labelDeciValue.setText(QtWidgets.QApplication.translate("BitMask32", "Decimal value", None, -1))

    def connectSignals(self):
        for bit_button in self.bit_buttons:
            bit_button.clicked.connect(bit_button.button_click_slot)

        self.pushButtonClear.clicked.connect(self.pushButtonClear_clicked_slot)

        self.lineEditHexValue.editingFinished.connect(self.lineEditHexValue_editingFinished_slot)
        self.lineEditDeciValue.editingFinished.connect(self.lineEditDeciValue_editingFinished_slot)

        self.pushButtonCopyHexValue.clicked.connect(self.pushButtonCopyHexa_clicked_slot)
        self.pushButtonCopyDeciValue.clicked.connect(self.pushButtonCopyDecimal_clicked_slot)

        self.pushButtonExit.clicked.connect(self.pushButtonExit_clicked_slot)
        self.checkBoxAOT.clicked.connect(self.checkBoxAOT_checked_slot)

    def update_buttons_values(self):
        for bit_index in range(0, 32):
            new_bit_value = ((self.register_value >> bit_index) & 1)
            self.bit_buttons[bit_index].bit_value = new_bit_value
            self.bit_buttons[bit_index].setText(str(new_bit_value))

    def update_register_value(self):
        self.register_value = 0
        for button in self.bit_buttons:
            self.register_value |= (button.bit_value << button.index)

    def update_line_edit_values(self):
        self.lineEditDeciValue.setText(str(self.register_value))
        self.lineEditHexValue.setText("0x" + hex(self.register_value)[2:].zfill(8))

    def toggle_bit(self, bit_index):
        current_bit_value = self.bit_buttons[bit_index].bit_value
        new_bit_value = current_bit_value ^ 1
        self.bit_buttons[bit_index].bit_value = new_bit_value
        self.bit_buttons[bit_index].setText(str(new_bit_value))

    @QtCore.Slot(int)
    def pushButtonBitXX_clicked_slot(self, index):
        self.toggle_bit(index)
        self.update_register_value()
        self.update_line_edit_values()
        self.show_warning("", 0)

    @QtCore.Slot()
    def pushButtonClear_clicked_slot(self):
        for bit_index in range(0, 32):
            self.bit_buttons[bit_index].bit_value = 0
            self.bit_buttons[bit_index].setText(str(0))

        self.update_register_value()
        self.update_line_edit_values()
        self.show_warning("", 0)

    @QtCore.Slot()
    def lineEditHexValue_editingFinished_slot(self):
        hex_string = self.lineEditHexValue.text()
        if self.validate_hex_string(hex_string):
            self.show_warning("", 0)
            self.register_value = int(hex_string, 16)
            self.update_buttons_values()
            self.update_line_edit_values()
        else:
            self.show_warning(warning="Invalid hexadecimal number!", time_ms=3000)

    @QtCore.Slot()
    def lineEditDeciValue_editingFinished_slot(self):
        deci_string = self.lineEditDeciValue.text()
        if self.validate_decimal_string(deci_string):
            self.show_warning("", 0)
            self.register_value = int(deci_string)
            self.update_buttons_values()
            self.update_line_edit_values()
        else:
            self.show_warning(warning="Invalid decimal number!", time_ms=3000)

    @QtCore.Slot()
    def pushButtonCopyHexa_clicked_slot(self):
        self.clipBoard.setText(self.lineEditHexValue.text())
        self.show_warning("Hexa decimal value copied to clipboard!", 3000)

    @QtCore.Slot()
    def pushButtonCopyDecimal_clicked_slot(self):
        self.clipBoard.setText(self.lineEditDeciValue.text())
        self.show_warning("Decimal value copied to clipboard!", 3000)

    @QtCore.Slot()
    def checkBoxAOT_checked_slot(self):
        if self.checkBoxAOT.isChecked():
            self.mainWindow.setWindowFlags(
                self.mainWindow.windowFlags() | QtCore.Qt.WindowStaysOnTopHint
            )
        else:
            self.mainWindow.setWindowFlags(
                self.mainWindow.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint
            )
        self.mainWindow.show()

    @QtCore.Slot()
    def pushButtonExit_clicked_slot(self):
        self.clipBoard.setText(self.original_text)
        sys.exit(0)

    def show_warning(self, warning, time_ms):
        if time_ms > 0:
            self.statusBar.showMessage(warning, time_ms)

    @staticmethod
    def validate_hex_string(string):
        string = string.lower()
        hex_pattern = r"^0x[0-9a-fA-F]{0,8}$"
        return bool(re.match(hex_pattern, string))

    @staticmethod
    def validate_decimal_string(string):
        return string.isdigit()

    @staticmethod
    def deci_to_hex(string):
        return hex(int(string))

    @staticmethod
    def hex_to_deci(string):
        return int(string, 16)


if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    BitMask32 = QtWidgets.QMainWindow()
    ui = Ui_BitMask32()
    ui.setupUi(BitMask32)
    ui.connectSignals()
    BitMask32.show()
    sys.exit(app.exec_())

