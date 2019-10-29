import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt

class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()
        self.writeScoreDB()
#        self.doScoreDB()

    def initUI(self):
        self.setGeometry(300, 300, 900, 500)
        self.setWindowTitle('Assignment6')
        VBox = QVBoxLayout()
        InputBox = QHBoxLayout()
        ButtonBox = QHBoxLayout()
        ResultBox = QHBoxLayout()

        VBox.addLayout(InputBox)

        VBox.addLayout(ButtonBox)
        ResultLabel = QLabel("Result: ")
        VBox.addWidget(ResultLabel)
        VBox.addLayout(ResultBox)
        #Label & Value
        NameLabel = QLabel("Name: ")
        NameValue = QLineEdit()

        AgeLabel = QLabel("Age: ")
        AgeValue = QLineEdit()

        ScoreLabel = QLabel("Score: ")
        ScoreValue = QLineEdit()

        AmountLabel = QLabel("Amount: ")
        AmountValue = QLineEdit()

        KeyLabel = QLabel("Key: ")
        KeyValue = QComboBox()
        KeyValue.addItems(["Name", "Age", "Score"])

        #Button
        addButton = QPushButton("Add")
        delButton = QPushButton("Del")
        findButton = QPushButton("Find")
        incButton = QPushButton("Inc")
        showButton = QPushButton("Show")
        ResultTextWindow = QTextEdit()

        #Box's Widget add

        InputBox.addWidget(NameLabel)
        InputBox.addWidget(NameValue)
        InputBox.addStretch(1)
        InputBox.addWidget(AgeLabel)
        InputBox.addWidget(AgeValue)
        InputBox.addStretch(1)
        InputBox.addWidget(ScoreLabel)
        InputBox.addWidget(ScoreValue)
        InputBox.addStretch(1)
        InputBox.addWidget(AmountLabel)
        InputBox.addWidget(AmountValue)
        InputBox.addStretch(1)
        InputBox.addWidget(KeyLabel)
        InputBox.addWidget(KeyValue)

        ButtonBox.addWidget(addButton)
        ButtonBox.addWidget(delButton)
        ButtonBox.addWidget(findButton)
        ButtonBox.addWidget(incButton)
        ButtonBox.addWidget(showButton)

        ResultBox.addWidget(ResultTextWindow)

#        hbox.addWidget(addButton)
        self.setLayout(VBox)
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        if sender.text() == 'Add':
            pass
            self.writeScoreDB()
        elif sender.text() == 'Del':
            pass
        elif sender.text() == 'Find':
            pass
        elif sender.text() == 'Inc':
            pass
        elif sender.text() == 'Show':
            pass
            self.showScroeDB()

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb = pickle.load(fH)
        except:
            print("Empty DB: ", self.dbfilename)
        else:
            print("Open DB: ", self.dbfilename)
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = ScoreDB()
    sys.exit(app.exec_())
