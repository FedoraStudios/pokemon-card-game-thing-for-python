from tkinter import *

import random

from PIL import ImageTk, Image

root = Tk()
root.title("Pokemon card game")
root.geometry("800x600")
root.configure(bg="royal blue")

abra = ImageTk.PhotoImage(Image.open("abra.jpg"))
bulbasour = ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
button = ImageTk.PhotoImage(Image.open("button.jpg"))
charmander = ImageTk.PhotoImage(Image.open("charmender.jpg"))
iyvesuor = ImageTk.PhotoImage(Image.open("iyvasour.jpg"))
jigglypuff = ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
kadabra = ImageTk.PhotoImage(Image.open("kadabra.jpg"))
meowth = ImageTk.PhotoImage(Image.open("meowth.jpg"))
nidoking = ImageTk.PhotoImage(Image.open("nidoking.jpg"))
paras = ImageTk.PhotoImage(Image.open("paras.jpg"))
persian = ImageTk.PhotoImage(Image.open("persion.jpg"))
pikachu = ImageTk.PhotoImage(Image.open("pikachu.jpg"))
Ratata = ImageTk.PhotoImage(Image.open("ratata.jpg"))
Squirtle = ImageTk.PhotoImage(Image.open("squirtle.jpg"))

PokemonList = [abra, bulbasour, charmander, iyvesuor, jigglypuff, kadabra, meowth, nidoking, paras, persian, pikachu, Ratata, Squirtle]
PokemonHpList = [30, 60, 50, 100, 70, 70, 60, 90, 40, 70, 200, 40, 50]

PlayerOne = Label(root, text = "Player 1", bg = "red", fg = "royal blue")
PlayerOne.place(relx = 0.1, rely = 0.3, anchor=CENTER)

PlayerOneScoreLabel = Label(root, bg = "red", fg = "royal blue")
PlayerOneScoreLabel.place(relx = 0.1, rely = 0.4, anchor=CENTER)

PlayerTwo = Label(root, text = "Player 2", bg = "red", fg = "royal blue")
PlayerTwo.place(relx = 0.9, rely = 0.3, anchor=CENTER)

PlayerTwoScoreLabel = Label(root, bg = "red", fg = "royal blue")
PlayerTwoScoreLabel.place(relx = 0.9, rely = 0.4, anchor=CENTER)


RandomPokemonLabel = Label(root, bg = "yellow2", fg = "royal blue")
RandomPokemonLabel.place(relx = 0.5, rely = 0.5, anchor=CENTER)


PlayerOneScore = 0
PlayerTwoScore = 0

CopyRightFooterThing = Label(root, text="Made By Emir R. Frias Suzuki")
CopyRightFooterThing.place(relx = 0.4, rely = 0.97)


def PlayerOneDef():
    global PlayerOneScore 
    RandomNumber = random.randint(0,12)
    RandomPokemonLabel["image"] = PokemonList[RandomNumber]
    PlayerOneScore = PlayerOneScore + PokemonHpList[RandomNumber]
    PlayerOneScoreLabel["text"] = str(PlayerOneScore)
    
PlayerOneBtn = Button(root, image=button,  command=PlayerOneDef)
PlayerOneBtn.place(relx = 0.1, rely = 0.6, anchor=CENTER)


def PlayerTwoDef():
    global PlayerTwoScore 
    RandomNumber = random.randint(0,12)
    RandomPokemonLabel["image"] = PokemonList[RandomNumber]
    PlayerTwoScore = PlayerTwoScore + PokemonHpList[RandomNumber]
    PlayerTwoScoreLabel["text"] = str(PlayerTwoScore)
    
PlayerTwoBtn = Button(root, image=button,  command=PlayerTwoDef)
PlayerTwoBtn.place(relx = 0.9, rely = 0.6, anchor=CENTER)
 
root.mainloop()