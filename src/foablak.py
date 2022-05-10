from tkinter import *

def rolunk():
    ablak2 = Toplevel(ablak1)
    uzenet2 = Message(ablak2, text = 'Készítette: Császár András és Kulimák Máté\nBaja\n2022.04.27', width = 300)
    gomb2 = Button(ablak2, text = 'Kilép', command = ablak2.destroy)
    uzenet2.pack()
    gomb2.pack()
    ablak2.mainloop()


ablak1 = Tk()
ablak1.geometry("400x200")
menubar = Menu(ablak1)
#első gomb a menüsávon
file = Menu(menubar, tearoff=0)  
file.add_command(label="Háromszög")  
file.add_command(label="Trapéz")  
file.add_command(label="Paralelogramma")  
file.add_command(label="Téglalap")  
file.add_command(label="Deltoid")
file.add_command(label="Rombusz") 
file.add_command(label="Négyzet")
file.add_command(label="Kör")      
file.add_separator()  
file.add_command(label="Exit", command=ablak1.quit)  
menubar.add_cascade(label="Alakzatok", menu=file)  
#első gomb a menüsávon vége

#második gomb a menüsávon
menubar.add_cascade(label="Névjegy", command = rolunk)
ablak1.config(menu=menubar) 
#második gomb a menüsávon vége

#szöveg label 
l = Label(ablak1, text="Rövid használati útmutató: \n A menüsávon található alakzatok gomb alatt kiválaszthatjuk a számítani kívánt alakzatot. Az alakzatra kattintva kiválaszthatjuk, hogy kerületet vagy területet szeretnénk számolni. A rólunk gombra nyomva a keszítőkről kaphat a felhasználó információkat.", wraplength=200)
l.grid(row = 2,column = 0, pady = 20)
#szöveg label vége

#kép 
can1 = Canvas(ablak1, width = 400, height = 100, bg = 'white')
photo = PhotoImage(file = './a.png')
item = can1.create_image(80, 80, image = photo)
can1.grid()
#kép vége

'''
#kilépés gomb
kilep  = Button(ablak1, text='Kilépés')
kilep.grid(sticky = 's')
#kilépés gomb vége
'''

ablak1.mainloop()