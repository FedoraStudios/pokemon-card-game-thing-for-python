from tkinter import *

from PIL import ImageTk, Image

root = Tk()
root.title("Pokemon card game")
root.geometry("600x400")
root.configure(bg="royal blue")

abra = ImageTk.PhotoImage(Image.open("abra.jpg"))
bulbasour = ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
button = ImageTk.PhotoImage(Image.open("button.jpg"))
charmander = ImageTk.PhotoImage(Image.open("charmender.jpg"))
iyvesuor = ImageTk.PhotoImage(Image.open("iyvasour.jpg"))
jigglypugg = ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
kadabra = ImageTk.PhotoImage(Image.open("kadabra.jpg"))
meowth = ImageTk.PhotoImage(Image.open("meowth.jpg"))
nidoking = ImageTk.PhotoImage(Image.open("nidoking.jpg"))
paras = ImageTk.PhotoImage(Image.open("paras.jpg"))
persion = ImageTk.PhotoImage(Image.open("persion.jpg"))
pikachu = ImageTk.PhotoImage(Image.open("pikachu.jpg"))
Ratata = ImageTk.PhotoImage(Image.open("ratata.jpg"))
Squirtle = ImageTk.PhotoImage(Image.open("squirtle.jpg"))


PlayerOne = Label(root, text = "Player 1", bg = "red", fg = "royal blue")
PlayerOne.place(relx = 0.1, rely = 0.3, anchor=CENTER)

PlayerOneScore = Label(root, bg = "red", fg = "royal blue")
PlayerOneScore.place(relx = 0.1, rely = 0.4, anchor=CENTER)

PlayerTwo = Label(root, text = "Player 2", bg = "red", fg = "royal blue")
PlayerTwo.place(relx = 0.9, rely = 0.3, anchor=CENTER)

PlayerTwoScore = Label(root, bg = "red", fg = "royal blue")
PlayerTwoScore.place(relx = 0.9, rely = 0.4, anchor=CENTER)


RandomPokemonLabel = Label(root, bg = "yellow2", fg = "royal blue")
RandomPokemonLabel.place(relx = 0.5, rely = 0.5, anchor=CENTER)

root.mainloop()