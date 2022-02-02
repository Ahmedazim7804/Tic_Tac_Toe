import sys
import random
import base64
from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        self.setFixedSize(qtc.QSize(450,450))
        self.main = qtw.QWidget()
        self.setCentralWidget(self.main)

        self.setWindowIcon(qtg.QIcon(TIC_pixmap))
        self.setWindowTitle("Tic Tac Toe")

        # For Icon in Taskbar for Windows
        # import ctypes
        # myappid = 'mycompany.myproduct.subproduct.version'
        # ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(#myappid)
        

        #FileMenu
        self.file_menu = qtw.QMenuBar()
        self.file_menu_help = self.file_menu.addMenu("Help")
        self.file_menu_help.addAction("Rules", self.help)
        self.file_menu_help.addAction("About", self.about)
        self.file_menu_help.addAction("Exit", self.close)
        self.setMenuBar(self.file_menu)


        class QCustomButton(qtw.QPushButton):
            def __init__(self, *args, **kwargs):
                qtw.QPushButton.__init__(self, *args, **kwargs)
                policy = qtw.QSizePolicy(qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Expanding)
                self.setSizePolicy(policy)
                self.setIconSize(qtc.QSize(60, 60))


        #Buttons
        self.button_1 = QCustomButton(enabled=False,clicked=self.game)
        self.button_2 = QCustomButton(enabled=False,clicked=self.game)
        self.button_3 = QCustomButton(enabled=False,clicked=self.game)
        self.button_4 = QCustomButton(enabled=False,clicked=self.game)
        self.button_5 = QCustomButton(enabled=False,clicked=self.game)
        self.button_6 = QCustomButton(enabled=False,clicked=self.game)
        self.button_7 = QCustomButton(enabled=False,clicked=self.game)
        self.button_8 = QCustomButton(enabled=False,clicked=self.game)
        self.button_9 = QCustomButton(enabled=False,clicked=self.game)
        self.reset_button = qtw.QPushButton("Reset",clicked=self.reset)
        self.singleplayer_button = qtw.QPushButton("SinglePlayer",clicked=self.sp)
        self.multiplayer_button = qtw.QPushButton("Multiplayer",clicked=self.mp)

        # StatusBar
        self.status_bar = self.statusBar()
        self.status_bar.addWidget(qtw.QLabel("Player 1 : X"))
        self.status_bar.addPermanentWidget(qtw.QLabel("Player 2 : O"))

        # Other
        self.turn = 1
        self.list_all = [self.button_1,self.button_2,self.button_3,self.button_4,self.button_5,self.button_6,self.button_7,self.button_8,self.button_9]
        self.list_1 = []
        self.type = 0
        self.temp = None
        self.bestmove = 0


        self.setWindowIcon(qtg.QIcon(TIC_pixmap))
        
        self.icon_x = qtg.QIcon(X_pixmap) 
        self.icon_o = qtg.QIcon(O_pixmap)
        
        self.dict_2 = {self.button_1 : "",self.button_2 : "",self.button_3 : "",self.button_4 : "",self.button_5 : "",self.button_6 : "",self.button_7 : "",self.button_8 : "",self.button_9 : ""}
        #Label
        self.label_1 = qtw.QLabel("",font=qtg.QFont("Times",18))
        self.label_2 = qtw.QLabel("",font=qtg.QFont("Times",18))
        
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
        qtw.QMessageBox.about(self, "Result", f"<b><i>{self.dict[self.turn]['name']} Wins<b><i>")
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

    X_data = b'<?xml version="1.0" standalone="no"?>\n<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN"\n "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">\n<svg version="1.0" xmlns="http://www.w3.org/2000/svg"\n width="512.000000pt" height="512.000000pt" viewBox="0 0 512.000000 512.000000"\n preserveAspectRatio="xMidYMid meet">\n\n<g transform="translate(0.000000,512.000000) scale(0.100000,-0.100000)"\nfill="#000000" stroke="none">\n<path d="M355 5103 c-43 -13 -69 -34 -187 -151 -122 -123 -138 -143 -152 -191\n-21 -73 -20 -119 5 -188 20 -55 65 -102 998 -1035 l976 -978 -976 -978 c-933\n-933 -978 -980 -998 -1035 -25 -69 -26 -115 -5 -188 14 -48 30 -68 152 -191\n123 -122 143 -138 191 -152 73 -21 119 -20 188 5 55 20 102 65 1036 998 l977\n976 978 -976 c933 -933 980 -978 1035 -998 69 -25 115 -26 188 -5 48 14 68 30\n191 152 122 123 138 143 152 191 21 73 20 119 -5 188 -20 55 -65 102 -998\n1035 l-976 978 976 977 c933 934 978 981 998 1036 25 69 26 115 5 188 -14 48\n-30 68 -152 191 -123 122 -143 138 -191 152 -73 21 -119 20 -188 -5 -55 -20\n-102 -65 -1035 -998 l-978 -976 -977 976 c-934 933 -981 978 -1036 998 -67 24\n-122 26 -192 4z"/>\n</g>\n</svg>\n'
    X_pixmap = qtg.QPixmap()
    X_pixmap.loadFromData(X_data)
    O_data = b'<?xml version="1.0" standalone="no"?>\n<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN"\n "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">\n<svg version="1.0" xmlns="http://www.w3.org/2000/svg"\n width="512.000000pt" height="512.000000pt" viewBox="0 0 512.000000 512.000000"\n preserveAspectRatio="xMidYMid meet">\n\n<g transform="translate(0.000000,512.000000) scale(0.100000,-0.100000)"\nfill="#000000" stroke="none">\n<path d="M2321 5110 c-497 -48 -990 -251 -1376 -565 -114 -92 -294 -274 -384\n-387 -229 -287 -417 -675 -495 -1023 -49 -218 -60 -325 -60 -575 0 -250 11\n-357 60 -575 79 -355 272 -749 509 -1040 92 -114 274 -294 387 -384 287 -229\n675 -417 1023 -495 218 -49 325 -60 575 -60 250 0 357 11 575 60 261 58 603\n204 828 353 389 259 688 599 893 1016 125 255 196 484 241 775 24 161 24 539\n0 700 -45 291 -116 520 -241 775 -134 272 -283 480 -498 692 -211 209 -404\n346 -673 478 -252 124 -486 197 -765 240 -126 19 -468 27 -599 15z m539 -655\nc623 -105 1137 -483 1420 -1044 131 -262 194 -538 194 -851 0 -254 -30 -431\n-114 -661 -191 -524 -615 -948 -1139 -1139 -230 -84 -407 -114 -661 -114 -254\n0 -431 30 -661 114 -524 191 -948 615 -1139 1139 -84 230 -114 407 -114 661 0\n254 30 431 114 661 191 524 615 948 1139 1139 157 57 291 88 501 114 71 9 368\n-4 460 -19z"/>\n</g>\n</svg>\n'
    O_pixmap = qtg.QPixmap()
    O_pixmap.loadFromData(O_data)
    TIC_data = b'<?xml version="1.0" standalone="no"?>\n<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN"\n "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">\n<svg version="1.0" xmlns="http://www.w3.org/2000/svg"\n width="512.000000pt" height="512.000000pt" viewBox="0 0 512.000000 512.000000"\n preserveAspectRatio="xMidYMid meet">\n\n<g transform="translate(0.000000,512.000000) scale(0.100000,-0.100000)"\nfill="#000000" stroke="none">\n<path d="M501 5105 c-110 -24 -226 -89 -311 -175 -250 -250 -252 -649 -5 -895\n122 -121 256 -183 419 -192 292 -16 560 170 649 452 31 99 31 271 0 370 -101\n318 -428 510 -752 440z m290 -346 c67 -36 98 -68 137 -143 22 -43 26 -64 26\n-136 1 -78 -2 -90 -33 -148 -38 -70 -70 -100 -145 -140 -43 -22 -64 -26 -136\n-26 -72 0 -93 4 -136 26 -75 40 -107 70 -145 140 -31 58 -34 70 -33 148 0 100\n24 160 89 225 100 100 249 121 376 54z"/>\n<path d="M1576 5098 c-22 -13 -49 -39 -60 -58 -21 -34 -21 -49 -24 -722 l-3\n-687 -687 -3 c-673 -3 -688 -3 -722 -24 -52 -30 -82 -88 -77 -147 5 -54 27\n-91 77 -124 l33 -23 688 0 689 0 0 -750 0 -750 -689 0 -688 0 -33 -22 c-48\n-33 -72 -70 -77 -120 -7 -58 23 -118 74 -149 l38 -24 687 -3 687 -3 3 -687 3\n-687 24 -38 c31 -51 91 -81 149 -74 50 5 87 29 120 77 l22 33 0 688 0 689 750\n0 750 0 0 -689 0 -688 23 -33 c32 -48 69 -72 119 -77 58 -7 118 23 149 74 l24\n38 3 687 3 687 687 3 687 3 38 24 c51 31 81 91 74 149 -5 50 -29 87 -77 120\nl-33 22 -688 0 -689 0 0 750 0 750 689 0 688 0 33 23 c48 32 72 69 77 119 7\n58 -23 118 -74 149 l-38 24 -687 3 -687 3 -3 687 -3 687 -24 38 c-31 51 -91\n81 -149 74 -50 -5 -87 -29 -119 -77 l-23 -33 0 -688 0 -689 -750 0 -750 0 0\n689 0 688 -22 33 c-53 77 -139 100 -212 58z m1729 -2538 l0 -745 -745 0 -745\n0 -3 735 c-1 404 0 741 3 748 3 10 158 12 747 10 l743 -3 0 -745z"/>\n<path d="M2421 3185 c-110 -24 -226 -89 -311 -175 -250 -250 -252 -649 -5\n-895 122 -121 256 -183 419 -192 292 -16 560 170 649 452 31 99 31 271 0 370\n-101 318 -428 510 -752 440z m290 -346 c67 -36 98 -68 137 -143 22 -43 26 -64\n26 -136 1 -78 -2 -90 -33 -148 -38 -70 -70 -100 -145 -140 -43 -22 -64 -26\n-136 -26 -72 0 -93 4 -136 26 -75 40 -107 70 -145 140 -31 58 -34 70 -33 148\n0 100 24 160 89 225 100 100 249 121 376 54z"/>\n<path d="M3947 4896 c-49 -18 -64 -32 -88 -77 -45 -89 -25 -131 145 -299 75\n-74 136 -139 136 -144 0 -6 -65 -76 -144 -156 -155 -156 -167 -175 -151 -257\n9 -49 69 -109 118 -118 82 -16 101 -4 257 151 80 79 150 144 156 144 5 0 70\n-61 144 -136 169 -170 210 -190 300 -144 68 35 100 107 79 183 -9 34 -37 68\n-155 187 l-143 145 143 145 c119 119 146 153 155 188 31 115 -76 222 -191 191\n-35 -9 -69 -36 -188 -155 l-146 -144 -134 136 c-74 74 -146 141 -160 149 -41\n22 -92 26 -133 11z"/>\n<path d="M3935 1266 c-41 -18 -83 -69 -91 -111 -15 -79 -2 -100 152 -255 79\n-80 144 -150 144 -156 0 -5 -61 -70 -136 -144 -170 -169 -190 -210 -144 -300\n35 -68 107 -100 183 -79 34 9 68 36 187 155 l145 143 145 -143 c119 -118 153\n-146 188 -155 115 -31 222 76 191 191 -9 35 -36 69 -155 188 l-143 145 143\n145 c119 119 146 153 155 187 21 76 -11 148 -79 183 -90 46 -131 26 -300 -144\n-74 -75 -139 -136 -145 -136 -6 0 -71 61 -145 136 -74 75 -149 142 -167 150\n-40 17 -89 17 -128 0z"/>\n</g>\n</svg>\n'
    TIC_pixmap = qtg.QPixmap()
    TIC_pixmap.loadFromData(TIC_data)


    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())