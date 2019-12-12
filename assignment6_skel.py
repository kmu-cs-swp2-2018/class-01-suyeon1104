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
        self.doScoreDB()

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
        self.NameValue = QLineEdit()

        AgeLabel = QLabel("Age: ")
        self.AgeValue = QLineEdit()

        ScoreLabel = QLabel("Score: ")
        self.ScoreValue = QLineEdit()

        AmountLabel = QLabel("Amount: ")
        self.AmountValue = QLineEdit()

        KeyLabel = QLabel("Key: ")
        self.KeyValue = QComboBox()
        self.KeyValue.addItems(["Name", "Age", "Score"])

        #Button
        addButton = QPushButton("Add")
        delButton = QPushButton("Del")
        findButton = QPushButton("Find")
        incButton = QPushButton("Inc")
        showButton = QPushButton("Show")
        
        addButton.clicked.connect(self.buttonClicked)
        delButton.clicked.connect(self.buttonClicked)
        findButton.clicked.connect(self.buttonClicked)
        incButton.clicked.connect(self.buttonClicked)
        showButton.clicked.connect(self.buttonClicked)
        
        self.ResultTextWindow = QTextEdit()

        #Box's Widget add

        InputBox.addWidget(NameLabel)
        InputBox.addWidget(self.NameValue)
        InputBox.addStretch(1)
        InputBox.addWidget(AgeLabel)
        InputBox.addWidget(self.AgeValue)
        InputBox.addStretch(1)
        InputBox.addWidget(ScoreLabel)
        InputBox.addWidget(self.ScoreValue)
        InputBox.addStretch(1)
        InputBox.addWidget(AmountLabel)
        InputBox.addWidget(self.AmountValue)
        InputBox.addStretch(1)
        InputBox.addWidget(KeyLabel)
        InputBox.addWidget(self.KeyValue)

        ButtonBox.addWidget(addButton)
        ButtonBox.addWidget(delButton)
        ButtonBox.addWidget(findButton)
        ButtonBox.addWidget(incButton)
        ButtonBox.addWidget(showButton)

        ResultBox.addWidget(self.ResultTextWindow)

#        hbox.addWidget(addButton)
        self.setLayout(VBox)
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        if sender.text() == 'Add':
            self.scoredb += [{'Name': self.NameValue.text(), 'Age': int(self.AgeValue.text()),
                             'Score': int(self.ScoreValue.text())}]
            self.showScoreDB()
        elif sender.text() == 'Del':
            li = []
            for i in range(len(self.scoredb)):
                if self.scoredb[i]['Name'] != self.NameValue.text():
                    li.append(self.scoredb[i])
            self.scoredb = li
        elif sender.text() == 'Find':
            s = ""
            for dict in self.scoredb:
                if dict['Name'] == self.NameValue.text():
                    for key in dict:
                        s += "" + str(key) + "=" + str(dict[key]) + "    "
                    s += "\n"
            self.ResultTextWindow.setText(s)

        elif sender.text() == 'Inc':
            s = ""
            for dict in self.scoredb:
                if dict['Name'] == self.NameValue.text():
                    dict['Score'] += int(self.AmountValue.text())
            self.showScoreDB()

        elif sender.text() == 'Show':
            self.showScoreDB()

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
        self.scoredb.sort(key = lambda x: x[self.KeyValue.currentText()])

        s = ""
        for dict in self.scoredb:
            for key in dict:
                s += "" + str(key) + "=" + str(dict[key]) + "    "
            s += "\n"
        self.ResultTextWindow.setText(s)

    def doScoreDB(self):
        pass

if __name__ == '__main__':    
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = ScoreDB()
    sys.exit(app.exec_())

