from tkinter import *
import keyboard
from random import randint


class Application(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.ponto = 0
        self.velocidade = 5.2
        self.pos_player_x = 50
        self.pos_player_y = 50
        self.cont_comi = 0
        self.pos_tudo = {'comida0': [0, 0, False], 'comida1': [0, 0, False], 'comida2': [0, 0, False],
                         'comida3': [0, 0, False], 'comida4': [0, 0, False], 'comida5': [0, 0, False],
                         'comida6': [0, 0, False], 'comida7': [0, 0, False], 'comida8': [0, 0, False],
                         'comida9': [0, 0, False]}

        self.comida0 = Canvas(width=10, height=10, background="yellow")
        self.comida1 = Canvas(width=10, height=10, background="yellow")
        self.comida2 = Canvas(width=10, height=10, background="yellow")
        self.comida3 = Canvas(width=10, height=10, background="yellow")
        self.comida4 = Canvas(width=10, height=10, background="yellow")
        self.comida5 = Canvas(width=10, height=10, background="yellow")
        self.comida6 = Canvas(width=10, height=10, background="yellow")
        self.comida7 = Canvas(width=10, height=10, background="yellow")
        self.comida8 = Canvas(width=10, height=10, background="yellow")
        self.comida9 = Canvas(width=10, height=10, background="yellow")

        self.player = Canvas(width=50, height=50, background="red")
        self.player.place(x=self.pos_player_x, y=self.pos_player_y)

        self.mos_pon = Canvas(width=self.ponto, height=5, background="black")

        self.master.bind("<KeyPress>", self.Move)

    def Move(self, i):

        if keyboard.is_pressed('space') and self.ponto < 0:
            self.velocidade = 9.2
            self.ponto = self.ponto - 0.6
            self.mos_pon['width'] = self.ponto
        else:
            self.velocidade = 5.2

        if keyboard.is_pressed('a') and self.pos_player_x > 2:
            self.pos_player_x = self.pos_player_x - self.velocidade

        if keyboard.is_pressed('d') and self.pos_player_x < root.winfo_screenwidth() - 75:
            self.pos_player_x = self.pos_player_x + self.velocidade

        if keyboard.is_pressed('s') and self.pos_player_y < root.winfo_screenheight() - 135:
            self.pos_player_y = self.pos_player_y + self.velocidade

        if keyboard.is_pressed('w') and self.pos_player_y > 2:
            self.pos_player_y = self.pos_player_y - self.velocidade

        Application.CriarComida(self)
        Application.VerPos(self)
        self.mos_pon.place(x=self.pos_player_x, y=self.pos_player_y - 15)
        self.player.place(x=self.pos_player_x, y=self.pos_player_y)

    def CriarComida(self):
        self.cont_comi = self.cont_comi + 0.2
        if 5 <= self.cont_comi <= 18 and not self.pos_tudo['comida0'][2]:
            x = randint(20, 1500)
            y = randint(20, 800)
            self.comida0.place(x=x, y=y)
            self.pos_tudo[f'comida0'][0] = x
            self.pos_tudo[f'comida0'][1] = y
            self.pos_tudo[f'comida0'][2] = True

        elif 20 <= self.cont_comi <= 28 and not self.pos_tudo['comida1'][2]:
            x = randint(20, 1500)
            y = randint(20, 750)
            self.comida1.place(x=x, y=y)
            self.pos_tudo[f'comida1'][0] = x
            self.pos_tudo[f'comida1'][1] = y
            self.pos_tudo[f'comida1'][2] = True

        elif 30 <= self.cont_comi <= 38 and not self.pos_tudo['comida2'][2]:
            x = randint(20, 1500)
            y = randint(20, 750)
            self.comida2.place(x=x, y=y)
            self.pos_tudo[f'comida2'][0] = x
            self.pos_tudo[f'comida2'][1] = y
            self.pos_tudo[f'comida2'][2] = True

        elif 40 <= self.cont_comi <= 48 and not self.pos_tudo['comida3'][2]:
            x = randint(20, 1500)
            y = randint(20, 750)
            self.comida3.place(x=x, y=y)
            self.pos_tudo[f'comida3'][0] = x
            self.pos_tudo[f'comida3'][1] = y
            self.pos_tudo[f'comida3'][2] = True

        elif 50 <= self.cont_comi <= 58 and not self.pos_tudo['comida4'][2]:
            x = randint(20, 1500)
            y = randint(20, 750)
            self.comida4.place(x=x, y=y)
            self.pos_tudo[f'comida4'][0] = x
            self.pos_tudo[f'comida4'][1] = y
            self.pos_tudo[f'comida4'][2] = True

        elif 60 <= self.cont_comi <= 68 and not self.pos_tudo['comida5'][2]:
            x = randint(20, 1500)
            y = randint(20, 750)
            self.comida5.place(x=x, y=y)
            self.pos_tudo[f'comida5'][0] = x
            self.pos_tudo[f'comida5'][1] = y
            self.pos_tudo[f'comida5'][2] = True

        elif 70 <= self.cont_comi <= 78 and not self.pos_tudo['comida6'][2]:
            x = randint(20, 1500)
            y = randint(20, 750)
            self.comida6.place(x=x, y=y)
            self.pos_tudo[f'comida6'][0] = x
            self.pos_tudo[f'comida6'][1] = y
            self.pos_tudo[f'comida6'][2] = True

        elif 80 <= self.cont_comi <= 88 and not self.pos_tudo['comida7'][2]:
            x = randint(20, 1500)
            y = randint(20, 750)
            self.comida7.place(x=x, y=y)
            self.pos_tudo[f'comida7'][0] = x
            self.pos_tudo[f'comida7'][1] = y
            self.pos_tudo[f'comida7'][2] = True

        elif 90 <= self.cont_comi <= 98 and not self.pos_tudo['comida8'][2]:
            x = randint(20, 1500)
            y = randint(20, 750)
            self.comida8.place(x=x, y=y)
            self.pos_tudo[f'comida8'][0] = x
            self.pos_tudo[f'comida8'][1] = y
            self.pos_tudo[f'comida8'][2] = True

        elif 100 <= self.cont_comi <= 118 and not self.pos_tudo['comida9'][2]:
            x = randint(20, 1500)
            y = randint(20, 750)
            self.comida9.place(x=x, y=y)
            self.pos_tudo[f'comida9'][0] = x
            self.pos_tudo[f'comida9'][1] = y
            self.pos_tudo[f'comida9'][2] = True
            self.cont_comi = 0

    def VerPos(self):
        for i in self.pos_tudo:
            if self.pos_tudo[i][2] and self.pos_player_x <= self.pos_tudo[i][0] <= self.pos_player_x + 50 and \
                    self.pos_player_y <= self.pos_tudo[i][1] <= self.pos_player_y + 50:
                self.pos_tudo[i][2] = False
                if len(i) == 7:
                    if self.ponto <= 48:
                        self.ponto = self.ponto + 10
                        self.mos_pon['width'] = self.ponto
                        self.mos_pon.place(x=self.pos_player_x, y=self.pos_player_y - 15)
                    if i == 'comida0':
                        self.comida0.place_forget()
                    elif i == 'comida1':
                        self.comida1.place_forget()
                    elif i == 'comida2':
                        self.comida2.place_forget()
                    elif i == 'comida3':
                        self.comida3.place_forget()
                    elif i == 'comida4':
                        self.comida4.place_forget()
                    elif i == 'comida5':
                        self.comida5.place_forget()
                    elif i == 'comida6':
                        self.comida6.place_forget()
                    elif i == 'comida7':
                        self.comida7.place_forget()
                    elif i == 'comida8':
                        self.comida8.place_forget()
                    elif i == 'comida9':
                        self.comida9.place_forget()


root = Tk()
Application()
root.configure(bg='green', border=10, relief=RIDGE)
root.state('zoomed')
root.title("Game")
root.mainloop()
