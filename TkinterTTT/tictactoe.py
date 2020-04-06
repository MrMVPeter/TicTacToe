from tkinter import *
from tttLogic import *


root = Tk()
root.geometry('600x650')
root.title('TicTacToe')
buttons = []
score_labels = []


def make_board():
    frames = []
    bottum_io = []
    indx = 0
    for rw in range(1, 4):
        for col in range(1, 4):
            frames.append(Frame(root, width=200, height=200))
            frames[indx].propagate(FALSE)
            buttons.append(Button(frames[indx],
                                  font=('Helvetica', '100'),
                                  bg='#b0b0b0'))
            frames[indx].grid(row=rw, column=col)
            buttons[indx].pack(expand=TRUE, fill=BOTH)
            buttons[indx].config(command=lambda button_out=indx: callback(button_out))
            indx += 1
    for i in range(3):
        bottum_io.append(Frame(root, width=200, height=50))
        bottum_io[i].propagate(FALSE)
        bottum_io[i].grid(row=4, column=i + 1)
    for i in [1, 3]:
        score_labels.append(Label(bottum_io[i - 1]))
    score_labels[0].config(text='Player {} : {}'.format('X', ttt.score['X']))
    score_labels[1].config(text='Player {} : {}'.format('O', ttt.score['O']))
    qb = Button(bottum_io[1], text='Quit', bg='Red', command=quit)
    qb.pack(expand=TRUE, fill=BOTH)
    score_labels[0].pack(expand=TRUE, fill=BOTH)
    score_labels[1].pack(expand=TRUE, fill=BOTH)


def callback(button_out):
    # If Move is Valid
    if ttt.player_move(button_out):
        ttt.change_turn()
        ttt.check_board(ttt.state)
        draw_board()
    buttons[button_out].config(text='{}'.format(ttt.state[button_out]))


def draw_board():
    for i in range(9):
        buttons[i].config(text='{}'.format(ttt.state[i]))
    score_labels[0].config(text='Player {} : {}'.format('X', ttt.score['X']))
    score_labels[1].config(text='Player {} : {}'.format('O', ttt.score['O']))


ttt = Game()
make_board()
root.mainloop()
