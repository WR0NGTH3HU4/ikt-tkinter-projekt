from tkinter import *
from teszt_ablak import teszt_ablak
from mode import Mode

def open_window(ablaknev, mode: Mode):
    if ablaknev == "teszt":
        teszt_ablak(ablak1, mode, ablaknev)


def rolunk():
    ablak2 = Toplevel(ablak1)
    uzenet2 = Message(ablak2, text = 'Készítette: Császár András és Kulimák Máté\nBaja\n2022.04.27', width = 300)
    gomb2 = Button(ablak2, text = 'Kilép', command = ablak2.destroy)
    uzenet2.pack()
    gomb2.pack()
    ablak2.mainloop()

ablak1 = Tk() 
ablak1.title('Főablak')
ablak1.geometry("850x450")
ablak1.resizable(False, False) 
menubar = Menu(ablak1)
#első gomb a menüsávon
file = Menu(menubar, tearoff=0)

#teszt gomb
teszt = Menu(file, tearoff=0)
teszt.add_command(label="Kerület", command = lambda: open_window("teszt", Mode.KERULET) )
teszt.add_command(label="Terület")
file.add_cascade(label='Teszt', menu=teszt)
#teszt gomb

#háromszög menü gomb kezdete
haromszög = Menu(file, tearoff=0)
haromszög.add_command(label="Kerület")
haromszög.add_command(label="Terület")
file.add_cascade(label='Háromszög', menu=haromszög)
#háromszög menü gomb vége
 
#trapéz menü gomb kezdete
trapéz = Menu(file, tearoff=0)
trapéz.add_command(label="Kerület")
trapéz.add_command(label="Terület")
file.add_cascade(label='Trapéz', menu=trapéz)
#trapéz menü gomb vége

#paralelogramma menü gomb kezdete
Paralelogramma = Menu(file, tearoff=0)
Paralelogramma.add_command(label="Kerület")
Paralelogramma.add_command(label="Terület")
file.add_cascade(label='Paralelogramma', menu=Paralelogramma)
#paralelogramma menü gomb vége

#téglalap menü gomb kezdete
teglalap = Menu(file, tearoff=0)
teglalap.add_command(label="Kerület")
teglalap.add_command(label="Terület")
file.add_cascade(label='Téglalap', menu=teglalap)
#téglalap menü gomb vége

#deltoid menü gomb kezdete
deltoid = Menu(file, tearoff=0)
deltoid.add_command(label="Kerület")
deltoid.add_command(label="Terület")
file.add_cascade(label='Deltoid', menu=deltoid)
#deltoid menü gomb vége

#rombusz menü gomb kezdete
rombusz = Menu(file, tearoff=0)
rombusz.add_command(label="Kerület")
rombusz.add_command(label="Terület")
file.add_cascade(label='Rombusz', menu=rombusz)
#rombusz menü gomb vége

#négyzet menü gomb kezdete
negyzet = Menu(file, tearoff=0)
negyzet.add_command(label="Kerület")
negyzet.add_command(label="Terület")
file.add_cascade(label='Négyzet', menu=negyzet)
#négyzet menü gomb vége

#kör menü gomb kezdete
kor = Menu(file, tearoff=0)
kor.add_command(label="Kerület")
kor.add_command(label="Terület")
file.add_cascade(label='Kör', menu=kor)
#kör menü gomb vége


file.add_separator()  
file.add_command(label="Exit", command=ablak1.destroy)  
menubar.add_cascade(label="Alakzatok", menu=file)  
#első gomb a menüsávon vége

#második gomb a menüsávon
menubar.add_cascade(label="Névjegy", command = rolunk)
ablak1.config(menu=menubar) 
#második gomb a menüsávon vége
 
#szöveg label 
l = Label(ablak1, text="Rövid használati útmutató: \n A menüsávon található alakzatok gomb alatt kiválaszthatjuk a számítani kívánt alakzatot. Az alakzatra kattintva kiválaszthatjuk, hogy kerületet vagy területet szeretnénk számolni. A rólunk gombra nyomva a keszítőkről kaphat a felhasználó információkat.", wraplength=200, font = ('Arial', 13,))
l.grid(row = 2,column = 1, pady = 90)
#szöveg label vége 
 
#kép  
can1 = Canvas(ablak1, width = 500, height = 400, bg = 'white')
photo = PhotoImage(file = './src/a.png')
item = can1.create_image(250, 200, image = photo)
can1.grid(row = 2,column = 2, pady = 0, padx =50)
#kép vége 
    
 
#kilépés gomb
kilep  = Button(ablak1, text='Kilépés', command = ablak1.destroy)
kilep.grid(row = 3, column = 4)
#kilépés gomb vége


ablak1.mainloop()