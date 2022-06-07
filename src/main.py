from tkinter import *
import random
import string
from haromszog_ablak import HaromszogAblak
from negyzet_ablak import NegyzetAblak
from teszt_ablak import TesztAblak
from trapez_ablak import TrapezAblak
from teglalap_ablak import TeglalapAblak
from paralelogramma_ablak import ParalelogrammaAblak
from mode import Mode

sikidomok = {
    # Key          Display
    "haromszog": "Háromszög",
    "negyzet": "Négyzet",
    "teglalap": "Téglalap",
    "rombusz": "Rombusz",
    "paralelogramma": "Paralelogramma",
    "trapez": "Trapéz",
    "deltoid": "Deltoid",
    "kor": "Kör"
}

def open_window(ablaknev, mode: Mode):
    if ablaknev == "teszt":
        TesztAblak(root, mode)
    if ablaknev == "trapez":
        TrapezAblak(root, mode)
    if ablaknev == "teglalap":
        TeglalapAblak(root, mode)
    if ablaknev == "paralelogramma":
        ParalelogrammaAblak(root, mode)
    if ablaknev == "haromszog":
        HaromszogAblak(root, mode)
    if ablaknev == "negyzet":
        NegyzetAblak(root, mode)


def rolunk():
    ablak2 = Toplevel(root)
    uzenet2 = Message(ablak2, text = 'Készítette: Császár András és Kulimák Máté\nBaja\n2022.04.27', width = 300)
    gomb2 = Button(ablak2, text = 'Kilép', command = ablak2.destroy)
    uzenet2.pack()
    gomb2.pack()
    ablak2.mainloop()

root = Tk() 
root.title('Főablak')
root.geometry("850x450")
root.resizable(False, False) 
menubar = Menu(root)
#első gomb a menüsávon
alakzatok_menu = Menu(menubar, tearoff=0)

# A gombokat sokkal konnyebben is meg lehetne oldani, majd dolgozunk rajta
# ez az a bizonyos "egyszerubb modszer":
for sikidom in sikidomok:
    a = ''.join(random.choice(string.ascii_letters) for i in range(10))
    exec(f"""
{a} = Menu(alakzatok_menu, tearoff=0)
{a}.add_command(label="Kerület", command = lambda: open_window(sikidom, Mode.KERULET) )
{a}.add_command(label="Terület", command = lambda: open_window(sikidom, Mode.TERULET) )
alakzatok_menu.add_cascade(label=sikidomok[sikidom].capitalize(), menu={a})
    """,
    {"alakzatok_menu": alakzatok_menu, "sikidom": sikidom, "Menu": Menu, "sikidomok": sikidomok, "open_window": open_window, "Mode": Mode}
)
# Soha ne csinalj ilyet kerlek soha de soha


alakzatok_menu.add_separator()  

menubar.add_cascade(label="Alakzatok", menu=alakzatok_menu)  
menubar.add_command(label="Névjegy", command = rolunk)
menubar.add_command(label="Kilépés", command=root.destroy)
root.config(menu=menubar)
 
#szöveg label 
l = Label(root, text="Rövid használati útmutató: \n A menüsávon található alakzatok gomb alatt kiválaszthatjuk a számítani kívánt alakzatot. Az alakzatra kattintva kiválaszthatjuk, hogy kerületet vagy területet szeretnénk számolni. A rólunk gombra nyomva a keszítőkről kaphat a felhasználó információkat.", wraplength=200, font = ('Arial', 13,))
l.grid(row = 2,column = 1, pady = 90)
#szöveg label vége 
 
#kép  
can1 = Canvas(root, width = 500, height = 400, bg = 'white')
photo = PhotoImage(file = './src/a.png')
item = can1.create_image(250, 200, image = photo)
can1.grid(row = 2,column = 2, pady = 0, padx =50)
#kép vége 


root.mainloop()