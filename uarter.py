from tkinter import *
from serial import Serial

root = Tk()
root.title("UARTer")
print ("Вкажіть COM-порт")


def comprint():
    global COM
    COM = comy.get()
    print ("Вибраний порт: COM" + COM)


def potsprint():
    ser = Serial()
    ser.baudrate = 9600
    ser.port = COM
    print ("COM-порт: COM" + ser.port + ", бодрейт: 9600")

    print("Вміст команд:")
    cmd1 = ("s2c01" + c01.get())
    print (cmd1)
    cmd2 = ("s2c03" + c03.get())
    print (cmd2)
    cmd3 = ("s2d01" + d01.get())
    print (cmd3)
    cmd4 = ("s2d03" + d03.get())
    print (cmd4)
    cmd5 = ("s2e01" + e01.get())
    print (cmd5)
    cmd6 = ("s2e03" + e03.get())
    print (cmd6)
    cmd7 = ("s2f01" + f01.get())
    print (cmd7)
    cmd8 = ("s2f03" + f03.get())
    print (cmd8)

    ser.write(cmd1)
    ser.write(cmd2)
    ser.write(cmd3)
    ser.write(cmd4)
    ser.write(cmd5)
    ser.write(cmd6)
    ser.write(cmd7)
    ser.write(cmd8)


comlf = LabelFrame(text="COM")
cbl = Label(comlf, text="COM-порт:")
cbl.pack()
comy = Entry(comlf)
comy.insert(0, "1")
comy.pack(padx=10)
combtn = Button(comlf, text="Вибрати", width=10, command=comprint)
combtn.pack(padx=10, pady=10)
comlf.pack(padx=10, pady=10)

clf = LabelFrame(text="C")
clf.pack(pady=10, padx=10)

cbl1 = Label(clf, text="01")
cbl1.pack(side=LEFT, pady=10, padx=10)
c01 = Entry(clf)
c01.insert(0, "ff")
c01.pack(side=LEFT, pady=10, padx=10)

cbl3 = Label(clf, text="03")
cbl3.pack(side=LEFT, pady=10, padx=10)
c03 = Entry(clf)
c03.insert(0, "00")
c03.pack(side=LEFT, pady=10, padx=10)

dlf = LabelFrame(text="D")
dlf.pack(pady=10, padx=10)

dbl1 = Label(dlf, text="01")
dbl1.pack(side=LEFT, pady=10, padx=10)
d01 = Entry(dlf)
d01.insert(0, "ff")
d01.pack(side=LEFT, pady=10, padx=10)

dbl3 = Label(dlf, text="03")
dbl3.pack(side=LEFT, pady=10, padx=10)
d03 = Entry(dlf)
d03.insert(0, "00")
d03.pack(side=LEFT, pady=10, padx=10)

elf = LabelFrame(text="E")
elf.pack(pady=10, padx=10)

ebl1 = Label(elf, text="01")
ebl1.pack(side=LEFT, pady=10, padx=10)
e01 = Entry(elf)
e01.insert(0, "ff")
e01.pack(side=LEFT, pady=10, padx=10)

ebl3 = Label(elf, text="03")
ebl3.pack(side=LEFT, pady=10, padx=10)
e03 = Entry(elf)
e03.insert(0, "00")
e03.pack(side=LEFT, pady=10, padx=10)

flf = LabelFrame(text="F")
flf.pack(pady=10, padx=10)

fbl1 = Label(flf, text="01")
fbl1.pack(side=LEFT, pady=10, padx=10)
f01 = Entry(flf)
f01.insert(0, "ff")
f01.pack(side=LEFT, pady=10, padx=10)

fbl3 = Label(flf, text="03")
fbl3.pack(side=LEFT, pady=10, padx=10)
f03 = Entry(flf)
f03.insert(0, "00")
f03.pack(side=LEFT, pady=10, padx=10)

sndbtn = Button(text="Застосувати", width=10, command=potsprint)
sndbtn.pack(padx=10, pady=10)

mainloop()
