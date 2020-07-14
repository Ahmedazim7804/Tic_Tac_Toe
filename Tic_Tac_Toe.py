import pdb,sys,random
from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
import ctypes

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(qtc.QSize(450,450))
        self.main = qtw.QWidget()
        self.setCentralWidget(self.main)
        self.setWindowTitle("Tic Tac Toe")
        self.setWindowIcon(qtg.QIcon("C:\\users\\M\\Downloads\\tic3.png"))
        myappid = 'mycompany.myproduct.subproduct.version'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        #FileMenu
        self.file_menu = qtw.QMenuBar()
        self.file_menu_help = self.file_menu.addMenu("Help")
        self.file_menu_help.addAction("Rules",self.help)
        self.file_menu_help.addAction("About",self.about)
        self.file_menu_help.addAction("Exit",self.close)
        self.setMenuBar(self.file_menu)


        #Buttons
        self.button_1 = qtw.QPushButton(enabled=False,clicked=self.game);self.button_1.setSizePolicy(qtw.QSizePolicy.Expanding,qtw.QSizePolicy.Expanding);self.button_1.setIconSize(qtc.QSize(60,60))
        self.button_2 = qtw.QPushButton(enabled=False,clicked=self.game);self.button_2.setSizePolicy(qtw.QSizePolicy.Expanding,qtw.QSizePolicy.Expanding);self.button_2.setIconSize(qtc.QSize(60,60))
        self.button_3 = qtw.QPushButton(enabled=False,clicked=self.game);self.button_3.setSizePolicy(qtw.QSizePolicy.Expanding,qtw.QSizePolicy.Expanding);self.button_3.setIconSize(qtc.QSize(60,60))
        self.button_4 = qtw.QPushButton(enabled=False,clicked=self.game);self.button_4.setSizePolicy(qtw.QSizePolicy.Expanding,qtw.QSizePolicy.Expanding);self.button_4.setIconSize(qtc.QSize(60,60))
        self.button_5 = qtw.QPushButton(enabled=False,clicked=self.game);self.button_5.setSizePolicy(qtw.QSizePolicy.Expanding,qtw.QSizePolicy.Expanding);self.button_5.setIconSize(qtc.QSize(60,60))
        self.button_6 = qtw.QPushButton(enabled=False,clicked=self.game);self.button_6.setSizePolicy(qtw.QSizePolicy.Expanding,qtw.QSizePolicy.Expanding);self.button_6.setIconSize(qtc.QSize(60,60))
        self.button_7 = qtw.QPushButton(enabled=False,clicked=self.game);self.button_7.setSizePolicy(qtw.QSizePolicy.Expanding,qtw.QSizePolicy.Expanding);self.button_7.setIconSize(qtc.QSize(60,60))
        self.button_8 = qtw.QPushButton(enabled=False,clicked=self.game);self.button_8.setSizePolicy(qtw.QSizePolicy.Expanding,qtw.QSizePolicy.Expanding);self.button_8.setIconSize(qtc.QSize(60,60))
        self.button_9 = qtw.QPushButton(enabled=False,clicked=self.game);self.button_9.setSizePolicy(qtw.QSizePolicy.Expanding,qtw.QSizePolicy.Expanding);self.button_9.setIconSize(qtc.QSize(60,60))
        self.reset_button = qtw.QPushButton("Reset",clicked=self.reset)
        self.singleplayer_button = qtw.QPushButton("SinglePlayer",clicked=self.sp)
        self.multiplayer_button = qtw.QPushButton("Multiplayer",clicked=self.mp)
        #StatusBar
        self.status_bar = self.statusBar()
        self.status_bar.addWidget(qtw.QLabel("Player 1 : X"))
        self.status_bar.addPermanentWidget(qtw.QLabel("Player 2 : O"))
        #Other
        self.turn = 1
        self.list_all = [self.button_1,self.button_2,self.button_3,self.button_4,self.button_5,self.button_6,self.button_7,self.button_8,self.button_9]
        self.list_1 = []
        self.type = 0
        self.temp = None
        self.bestmove = 0
        self.icon_x = qtg.QIcon("C:\\users\\M\\Pictures\\X.png")
        self.icon_o = qtg.QIcon("C:\\users\\M\\Pictures\\O.png")
        self.dict_2 = {self.button_1 : "",self.button_2 : "",self.button_3 : "",self.button_4 : "",self.button_5 : "",self.button_6 : "",self.button_7 : "",self.button_8 : "",self.button_9 : ""}
        #Label
        self.label_1 = qtw.QLabel("",font=qtg.QFont("Times",18))
        self.label_2 = qtw.QLabel(f"",font=qtg.QFont("Times",18))
        #Layout
        self.main_layout = qtw.QGridLayout()
        self.main_layout.addWidget(self.button_1, 0, 0)
        self.main_layout.addWidget(self.button_2, 0, 1)
        self.main_layout.addWidget(self.button_3, 0, 2)
        self.main_layout.addWidget(self.button_4, 1, 0)
        self.main_layout.addWidget(self.button_5, 1, 1)
        self.main_layout.addWidget(self.button_6, 1, 2)
        self.main_layout.addWidget(self.button_7, 2, 0)
        self.main_layout.addWidget(self.button_8, 2, 1)
        self.main_layout.addWidget(self.button_9, 2, 2)
        self.main_layout.addWidget(self.label_1,3,0)
        self.main_layout.addWidget(self.label_2,3,2,alignment=qtc.Qt.AlignRight)
        self.main_layout.addWidget(self.singleplayer_button,4,0)
        self.main_layout.addWidget(self.reset_button,4,1)
        self.main_layout.addWidget(self.multiplayer_button,4,2)
        self.main.setLayout(self.main_layout)

    def help(self):
        qtw.QMessageBox.information(self,"Help",f"RULES OF TIC TAC TOE \n"
                                                f"1. The game is played on a grid that's 3 squares by 3 squares \n"
                                                f"2. You are X, your friend (or the computer in this case) is O. Players take turns putting their marks in empty squares \n"
                                                f"3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner"
                                                f"\n 4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.")
    def about(self):
        qtw.QMessageBox.information(self,"About",f"Created By : Ajeem Ahmad \nContact Email : Ahmedazim7804@gmail.com")

    def game(self):
        if self.type == 1:
            self.singleplayer()
        elif self.type == 2:
            self.multiplayer()

    def reset(self):
        for i in self.list_all:
            i.setIcon(qtg.QIcon())
        self.list_1 = []
        self.dict_2 = {}
        self.turn = 1
        self.count = 0
        self.dict_2 = {self.button_1: "", self.button_2: "", self.button_3: "", self.button_4: "", self.button_5: "",self.button_6: "", self.button_7: "", self.button_8: "", self.button_9: ""}

    def other(self):
        qtw.QMessageBox.about(self, "Result", f"{self.dict[self.turn]['name']} Wins")
        self.dict[self.turn]["wins"] = self.dict[self.turn]["wins"] + 1
        self.dict[self.turn]["label_name"].setText(f"{self.dict[self.turn]['name']} : {self.dict[self.turn]['wins']}")

    def conditions(self):
        if self.dict_2[self.button_1] == self.dict_2[self.button_2] == self.dict_2[self.button_3] == self.dict[self.turn]['sign']:
            return True
        elif self.dict_2[self.button_4] == self.dict_2[self.button_5] == self.dict_2[self.button_6] == self.dict[self.turn]['sign']:
            return True
        elif self.dict_2[self.button_7] == self.dict_2[self.button_8] == self.dict_2[self.button_9] == self.dict[self.turn]['sign']:
            return True
        elif self.dict_2[self.button_1] == self.dict_2[self.button_4] == self.dict_2[self.button_7] == self.dict[self.turn]['sign']:
            return True
        elif self.dict_2[self.button_2] == self.dict_2[self.button_5] == self.dict_2[self.button_8] == self.dict[self.turn]['sign']:
            return True
        elif self.dict_2[self.button_3] == self.dict_2[self.button_6] == self.dict_2[self.button_9] == self.dict[self.turn]['sign']:
            return True
        elif self.dict_2[self.button_1] == self.dict_2[self.button_5] == self.dict_2[self.button_9] == self.dict[self.turn]['sign']:
            return True
        elif self.dict_2[self.button_3] == self.dict_2[self.button_5] == self.dict_2[self.button_7] == self.dict[self.turn]['sign']:
            return True

        return False

    def mp(self):
        for i in self.list_all:
            i.setEnabled(True)
        self.type = 2
        self.list_1 = []
        self.list_all = [self.button_1,self.button_2,self.button_3,self.button_4,self.button_5,self.button_6,self.button_7,self.button_8,self.button_9]
        self.dict = {1:{"sign" : "X","name" : "Player 1","icon" : self.icon_x,"wins" : 0},2:{"sign" : "O","name" : "Player 2","icon" : self.icon_o,"wins" : 0}}
        self.label_1.setText(f"{self.dict[1]['name']} : {self.dict[1]['wins']}")
        self.label_2.setText(f"{self.dict[2]['name']} : {self.dict[2]['wins']}")
        self.dict[1]["label_name"] = self.label_1
        self.dict[2]["label_name"] = self.label_2
        self.reset()

    def multiplayer(self):
        sender = self.sender()
        if sender in self.list_1:
            return
        else:
            sender.setIcon(self.dict[self.turn]['icon'])
            self.dict_2[sender] = self.dict[self.turn]['sign']
            self.count += 1
            self.list_1.append(sender)
            if self.conditions():
                self.other()
                self.reset()
            else:
                if self.turn == 1: self.turn = 2
                else: self.turn = 1
                if self.count >= 9:
                    qtw.QMessageBox.about(self,"Result","Game Tied")
                    self.reset()

    def sp(self):
        for i in self.list_all:
            i.setEnabled(True)
        self.type = 1
        self.list_1 = []
        self.list_all = [self.button_1,self.button_2,self.button_3,self.button_4,self.button_5,self.button_6,self.button_7,self.button_8,self.button_9]
        self.dict = {1:{"sign" : "X","name" : "Player","icon" : self.icon_x,"wins" : 0},2:{"sign" : "O","name" : "Cpu","icon" : self.icon_o,"wins" : 0}}
        self.label_1.setText(f"{self.dict[1]['name']} : {self.dict[1]['wins']}")
        self.label_2.setText(f"{self.dict[2]['name']} : {self.dict[2]['wins']}")
        self.dict[1]["label_name"] = self.label_1
        self.dict[2]["label_name"] = self.label_2
        self.reset()

    def sp_player(self,sender):
        self.turn = 1
        if sender not in self.list_1:
            sender.setIcon(self.dict[self.turn]["icon"])
            self.dict_2[sender] = self.dict[self.turn]['sign']
            self.list_1.append(sender)
            self.count += 1
            if self.conditions():
                self.temp = "T"
                return
            else:
                self.temp = "F"
                return
        else:
            self.temp = "N"

    def sp_cpu(self):
        if self.count == 9:
            qtw.QMessageBox.about(self,"Result","Game Tied")
            self.reset()
            return True
        self.turn = 2

        if self.count < 2:
            move = self.list_all[random.randint(0,8)]
            while move in self.list_1:
                move = self.list_all[random.randint(0,8)]
            move.setIcon(self.dict[self.turn]['icon'])
            self.dict_2[move] = self.dict[self.turn]['sign']
        elif self.best_move():
            move = self.bestmove
            move.setIcon(self.dict[self.turn]['icon'])
            self.dict_2[move] = self.dict[self.turn]['sign']
        else:
            move = self.list_all[random.randint(0,8)]
            while move in self.list_1:
                move = self.list_all[random.randint(0,8)]
            move.setIcon(self.dict[self.turn]['icon'])
            self.dict_2[move] = self.dict[self.turn]['sign']

        self.list_1.append(move)
        self.count += 1
        if self.conditions():
            self.other()
            return False
        else:
            return True

    def singleplayer(self):
        sender = self.sender()
        self.sp_player(sender)
        if self.temp == "T":
            self.other()
            self.reset()
        elif self.temp == "F":
            if self.sp_cpu():
                pass
            else:
                self.reset()
        elif self.temp == "N":
            return

    def best_move(self):
        self.list_2 = list(set(self.list_all) - set(self.list_1))
        for i in range(len(self.list_2)):
            self.turn = 2
            self.list_2[i].setIcon(self.icon_o)
            self.dict_2[self.list_2[i]] = "O"
            if self.conditions():
                self.bestmove = self.list_2[i]
                return True

            self.turn = 1
            self.list_2[i].setIcon(self.icon_x)
            self.dict_2[self.list_2[i]] = "X"
            if self.conditions():
                self.turn = 2
                self.bestmove = self.list_2[i]
                return True
            self.list_2[i].setIcon(qtg.QIcon())
            self.dict_2[self.list_2[i]] = ""

        self.turn = 2
        return False

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())