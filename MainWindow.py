from tkinter import *

def paginaInvatare():
    pagInv = Tk()

    def exitPage():
        mainWindow.deiconify()
        pagInv.quit()

    pagInv.geometry("400x400")
    pagInv.title("Invatare")
    label = Label(pagInv, text="SA INVATAM IMPREUNA")
    label.pack()
    button1 = Button(pagInv, text="Igiena", command=pagInvIgiena)
    button2 = Button(pagInv, text="Alimentatie", command=pagInvAlimentatie)
    button3 = Button(pagInv, text="Sport", command=pagInvSport)
    button4 = Button(pagInv, text="Exit", command=exitPage)
    button1.place(x=170 , y=80)
    button2.place(x=170, y=120)
    button3.place(x=170, y=160)
    button4.place(x=170, y=200)
    pagInv.mainloop()

def pagInvIgiena():
    pagIg = Tk()
    pagIg.geometry("400x400")
    pagIg.title("Invatare - Igiena")
    label = Label(pagIg, text="IGIENA")
    label.pack()
    pagIg.mainloop()


def pagInvAlimentatie():
    pagAlim = Tk()
    pagAlim.geometry("400x400")
    pagAlim.title("Invatare - Alimentatie")
    label = Label(pagIg, text="ALIMENTATIE")
    label.pack()
    pagAlim.mainloop()

def pagInvSport():
    pagSport = Tk()
    pagSport.geometry("400x400")
    pagSport.title("Invatare - Sport")
    label = Label(pagIg, text="SPORT")
    label.pack()
    pagSport.mainloop()

def openPagInv():
    mainWindow.withdraw()
    paginaInvatare()

def pagJoacaIgiena():
    pagJoacaIg = Tk()
    pagJoacaIg.geometry("400x400")
    pagIg.title("Joaca - Igiena")
    label = Label(pagIg, text="IGIENA")
    label.pack()
    pagJoacaIg.mainloop()


def pagJoacaAlimentatie():
    pagJoacaAlim = Tk()
    pagJoacaAlim.geometry("400x400")
    pagJoacaAlim.title("Joaca - Alimentatie")
    label = Label(pagIg, text="ALIMENTATIE")
    label.pack()
    pagJoacaAlim.mainloop()

def pagJoacaSport():
    pagJoacaSport = Tk()
    pagJoacaSport.geometry("400x400")
    pagJoacaSport.title("Joaca - Sport")
    label = Label(pagIg, text="SPORT")
    label.pack()
    pagJoacaSport.mainloop()


#Deschidere pagina principala
mainWindow = Tk()
mainWindow.geometry("800x800")
mainWindow.title("Cum sa iti pastrezi sanatatea")

startButton = Button(mainWindow, text="Start", fg="green" , command= openPagInv)
quitButton = Button(mainWindow, text="Exit", fg="green" , command=quit)
startButton.pack()
quitButton.pack()
mainWindow.mainloop()