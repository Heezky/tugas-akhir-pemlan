# GABRIEL HIZKIA MARHATA SIMBOLON       205150301111027
# AHMAD MUNIF CLEVERIANDY               205150307111020

import tkinter as tk
import random
from secrets import choice 

gui = tk.Tk()
gui.title("Party Pahlawan VS Raja Iblis")
gui.geometry('530x250')

class Karakter:
    def __init__(self, name, hp, attack, skill, skill2):
        self._name = name
        self._hp = hp
        self._attack = attack
        self._skill = skill
        self._skill2 = skill2
    
    #method memukul
    def memukul(self, musuh):
        musuh.setHp(musuh.getHp() - self._attack)
        print(self._name + " memukul " + musuh.getName() + ". HP " + musuh.getName() + ": " + str(musuh.getHp()))
        if musuh.getHp() <= 0:
            print(musuh.getName() + " sudah kalah")
    
    #method skill healing
    def healing(self, musuh):
        musuh.setHp(musuh.getHp() + self._skill)
        print(self._name + " telah memulihkan " + musuh.getName() + ". HP " + musuh.getName() + ": " + str(musuh.getHp()))

    #method skill healing Raja Iblis
    def healing2(self, musuh):
        musuh.setHp(musuh.getHp() + self._skill2)
        print(self._name + " telah memulihkan diri sendiri. HP " + self.getName() + ": " + str(self.getHp()))

    #method ultimate skill
    def ultimate(self, musuh):
        musuh.setHp(musuh.getHp() - self._skill)
        print(self._name + " menggunakan ultimate skill ke " + musuh.getName() + ". HP " + musuh.getName() + ": " + str(musuh.getHp()))

    def getName(self):
        return self._name

    def getHp(self):
        return self._hp

    def setHp(self, hp):
        self._hp = hp

#atribut karakter
Pahlawan = Karakter("Pahlawan", 300, 50, 120, 0)
Healer = Karakter("Healer", 200, 15, 75, 0)
Tank = Karakter("Tank", 600, 25, 75, 0)
RajaIblis = Karakter("Raja Iblis", 800, 50, 55, 45)

def randomChoice():
    global list
    list = random.choice([1,2,3,4,5,6,7])

#fungsi attack Raja Iblis
d = 0
e = 0
def AttackRajaIblis():
    global d
    hp1 = Pahlawan.getHp()
    hp2 = Healer.getHp()
    hp3 = Tank.getHp()
    # print(hp1)
    # print(hp2)
    # print(hp3)
    randomChoice()
    if list == 1:
        if hp1 <= 0:
            AttackRajaIblis()
        else:
            RajaIblis.memukul(Pahlawan)
            lbl1.config(text="Pahlawan  HP : " + str(Pahlawan.getHp()))
    elif list == 2:
        if hp2 <= 0:
            AttackRajaIblis()
        else :
            RajaIblis.memukul(Healer)
            lbl2.config(text="Healer    HP : " + str(Healer.getHp()))
    elif list == 3:
        if hp3 <= 0:
            AttackRajaIblis()
        else:
            RajaIblis.memukul(Tank)
            lbl3.config(text="Tank     HP : " + str(Tank.getHp()))
    elif list == 4:
        if d < 1:
            RajaIblis.ultimate(Pahlawan)
            lbl1.config(text="Pahlawan  HP : " + str(Pahlawan.getHp()))
            d += 1
        elif d == 1:
            AttackRajaIblis()
    elif list == 5:
        if d < 1:
            RajaIblis.ultimate(Healer)
            lbl2.config(text="Healer    HP : " + str(Healer.getHp()))
            d += 1
        elif d == 1:
            AttackRajaIblis()
    elif list == 6:
        if d < 1:
            RajaIblis.ultimate(Tank)
            lbl3.config(text="Tank     HP : " + str(Tank.getHp()))
            d += 1
        elif d == 1:
            AttackRajaIblis()
        global e
    elif list == 7:
        if e < 1:
            RajaIblis.healing2(RajaIblis)
        elif e == 1:
            AttackRajaIblis()

#fungsi attack party pahlawan
def serang1():
    Pahlawan.memukul(RajaIblis)
    lbl4.config(text="Raja Iblis    HP : " + str(RajaIblis.getHp()))
    AttackRajaIblis()
def serang2():
    Healer.memukul(RajaIblis)
    lbl4.config(text="Raja Iblis    HP : " + str(RajaIblis.getHp()))
    AttackRajaIblis()
def serang3():
    Tank.memukul(RajaIblis)
    lbl4.config(text="Raja Iblis    HP : " + str(RajaIblis.getHp()))
    AttackRajaIblis()

#fungsi skill heal
a = 0
def heal1():
    global a
    if a < 2:
        Healer.healing(Pahlawan)
        lbl1.config(text="Pahlawan  HP : " + str(Pahlawan.getHp()))
        a += 1
    elif a == 2:
        print("Skill habis")

def heal2():
    global a
    if a < 2:
        Healer.healing(Tank)
        lbl3.config(text="Tank     HP : " + str(Tank.getHp()))
        a += 1
    elif a == 2:
        print("Skill habis")

#fungsi skill ultimate
b = 0
c = 0
def ultimate1():
    global b
    if b < 1:
        Pahlawan.ultimate(RajaIblis)
        lbl4.config(text="Raja Iblis    HP : " + str(RajaIblis.getHp()))
        b += 1
    elif b == 1:
        print("Skill habis")
    AttackRajaIblis()
def ultimate2():
    global c
    if c < 1:
        Tank.ultimate(RajaIblis)
        lbl4.config(text="Raja Iblis    HP : " + str(RajaIblis.getHp()))
        c += 1
    elif c == 1:
        print("Skill habis")
    AttackRajaIblis()

#tampilan GUI
lbl0 = tk.Label(gui, text="Pilih action yang diinginkan. Healing max 2 kali dan Ultimate max 1")
lbl0.grid(row=0, column=0, sticky='w')

# hp1 = Pahlawan.getHp()
lbl1 = tk.Label(gui, text="Pahlawan     HP : " + str(Pahlawan.getHp()))
lbl1.grid(row=1, column=0, sticky='w')
printButton = tk.Button(gui, text = "Serang", command = serang1)
printButton.grid(row=2, sticky='ew')
printButton = tk.Button(gui, text = "Ultimate", command = ultimate1)
printButton.grid(row=2, column=3, sticky='ew')

lbl2 = tk.Label(gui, text="Healer   HP : " + str(Healer.getHp()))
lbl2.grid(row=3, column=0, sticky='w')
printButton = tk.Button(gui, text = "Serang", command = serang2)
printButton.grid(row=4, sticky='ew')
printButton = tk.Button(gui, text = "Heal Pahlawan", command = heal1)
printButton.grid(row=4, column=3, sticky='ew')
printButton = tk.Button(gui, text = "Heal Tank", command = heal2)
printButton.grid(row=4, column=4, sticky='ew')

lbl3 = tk.Label(gui, text="Tank     HP : " + str(Tank.getHp()))
lbl3.grid(row=6, column=0, sticky='w')
printButton = tk.Button(gui, text = "Serang", command = serang3)
printButton.grid(row=7, sticky='ew')
printButton = tk.Button(gui, text = "Ultimate", command = ultimate2)
printButton.grid(row=7, column=3, sticky='ew')

lbl4= tk.Label(gui, text="Raja Iblis    HP : " + str(RajaIblis.getHp()))
lbl4.grid(row=8, column=0, sticky='w')

lb4 = tk.Label(gui, text = "")
lb4.grid(row=15, sticky='ew')
gui.mainloop()
