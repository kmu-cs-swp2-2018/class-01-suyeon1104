import pickle
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QFont

class Auction(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label = QLabel("판매자: 김수연")
        #label.font().setBold(True)
        label2 = QLabel("판매물품: 도시락")
        label3 = QLabel("현재가격: 10000 원")
        self.startAmount = 10000
        self.currentAmount = self.startAmount
        self.myAmount = 0
        print()
        qfont = QFont('Gulim', 15, label.font().weight(), label.font().italic())
        qfont.setBold(True)
        #qfont2 = QFont('Batang', 30, label2.font().weight(), label2.font().italic())
        #qfont3 =QFont('Cronix', 30, label3.font().weight(), label3.font().italic())
        label.setFont(qfont)
        label2.setFont(qfont)
        label3.setFont(qfont)


        pixmap1 = QPixmap('tiger.jpg')
        label4 = QLabel()
        label4.setPixmap(pixmap1)
        #label4.resize(100, 100) 판매물품 이미지 크기 조정
        self.auctionProgressList = QTextEdit()
        self.purchaseTextEdit = QLineEdit()
        self.purchaseButton = QPushButton("구매")
        self.purchaseButton.clicked.connect(self.setAmount)

        lvbox = QVBoxLayout()
        lvbox.addWidget(label)
        lvbox.addSpacing(10)
        lvbox.addWidget(label2)
        lvbox.addSpacing(10)
        lvbox.addWidget(label3)
        lvbox.addWidget(label4)

        rhbox = QHBoxLayout()
        rhbox.addWidget(self.purchaseTextEdit)
        rhbox.addWidget(self.purchaseButton)

        rvbox = QVBoxLayout()
        rvbox.addWidget(self.auctionProgressList)
        rvbox.addLayout(rhbox)

        hbox = QHBoxLayout()
        hbox.addLayout(lvbox)
        hbox.addStretch(1)
        hbox.addLayout(rvbox)


        #lvbox.addStretch(1)
        #hbox.addStretch(1)

        self.setLayout(hbox)

        self.setGeometry(300, 300, 800, 500)
        self.setWindowTitle("Kookmin Auction")
        #self.resize(500, 300)
        self.show()

#    def buttonClicked(self):
#        sender = self.sender()
#        print(sender.text())
    def setAmount(self):
        self.myAmount = int(self.purchaseTextEdit.text())
        print(self.myAmount, self.purchaseTextEdit.text())

        if self.myAmount > self.currentAmount:
            self.currentAmount = self.myAmount
            print("야야")
            #self.auctionProgressList.setText(self.auctionProgressList.text() + "고현성 님이" + str(self.myAmount) + "원으로 구입하기를 희망합니다.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    auction = Auction()
    sys.exit(app.exec_())