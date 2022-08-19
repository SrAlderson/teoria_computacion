from tkinter import Place, Tk , Label, Button,Entry , StringVar
import tkinter as tk
from tkinter.constants import CENTER
from tkinter import *
from functools import partial
from tkinter import ttk
import turtle

from Negocio import validacion_correo
from Negocio import validacion_entero
from Negocio import validacion_decimal
from Negocio import validacion_cientifico


class Application(tk.Frame):

        def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            self.pack()

            self.create_widgets()

        def tiene_exactamente_un_exp(self,numero):
            nume = str(numero)
            primer_indice = nume.find("E")
            if primer_indice == -1:
                return False
            else:
                return True

        def tiene_exactamente_un_punto(self,numero):
            nume = str(numero)
            primer_indice = nume.find(".")
            if primer_indice == -1:
                return False
            else:
                return True

        def tiene_exactamente_un_signo(self,numero):
            nume = str(numero)
            primer_indice = nume.find("+")
            segundo_indice = nume.find("-")
            if primer_indice == -1 and segundo_indice == -1:
                return False
            else:
                return True

        def validate_entry3(self,text):
            return text.isdigit() or self.tiene_exactamente_un_exp(text) or self.tiene_exactamente_un_signo(text) or self.tiene_exactamente_un_punto(text)

        def validate_entry(self,text):
            return text.isdigit() or self.tiene_exactamente_un_punto(text) or self.tiene_exactamente_un_signo(text)

        def validate_entry2(self,text):
            return text.isdigit()

        def create_widgets(self):

            cad1 = StringVar()
            cad2 = StringVar()
            cad3 = StringVar()
            cad4 = StringVar()      

            Interfaz.configure(background='#00995F')
            Interfaz.title("Menu de la interacción de las cadenas")
            Interfaz.geometry("1000x500")

            header = tk.Frame(Interfaz,bg='#00995F')
            header.place(x=400,y=0,width=1000,height=100)

            lblheader=Label(header, text="Menu de la interacción de las cadenas con ER", bg='#00995F')
            lblheader.place(x=0, y=0)

            body = tk.Frame(Interfaz,bg='#E5EAE8')
            body.place(x=0,y=100,width=1000,height=380)

            lbl1=Label(body,text="Numero Cientifico", bg='#E5EAE8')
            lbl1.place(x= 100, y=70)
            txt1 = ttk.Entry(body, justify=CENTER, textvariable= cad1,state=tk.DISABLED,validate="key",validatecommand=(self.master.register(self.validate_entry3), "%S"))
            txt1.place(x=100, y= 100)
            lbl2 = Label(body,text="Numero Real", bg='#E5EAE8')
            lbl2.place(x= 300, y=70)
            txt2 = ttk.Entry(body, justify=CENTER, textvariable= cad2,state=tk.DISABLED,validate="key",validatecommand=(self.master.register(self.validate_entry), "%S"))
            txt2.place(x=300, y= 100)
            lbl3=Label(body,text="Numero Entero", bg='#E5EAE8')
            lbl3.place(x= 500, y=70)
            txt3 = ttk.Entry(body, justify=CENTER, textvariable= cad3, state=tk.DISABLED,validate="key",validatecommand=(self.master.register(self.validate_entry2), "%S"))
            txt3.place(x=500, y= 100)
            lbl4=Label(body,text="Correo", bg='#E5EAE8')
            lbl4.place(x= 700, y=70)
            txt4  = ttk.Entry(body, justify=CENTER, textvariable= cad4,state=tk.DISABLED)
            txt4.place(x=700, y= 100)

            #validacion de botones
            
            btn1= ttk.Button(body,text="Validar", command=partial(validacion_decimal,txt2))
            btn1.place(x=300,y=140,width=120, height=30)

            btn6 = ttk.Button(body,text="Validar",command=partial(validacion_cientifico,txt1))
            btn6.place(x=100,y=140,width=120, height=30)

            def habilitar_camptext():
                txt1.config(state= tk.NORMAL)
                txt2.config(state= tk.NORMAL)
                txt3.config(state= tk.NORMAL)
                txt4.config(state= tk.NORMAL)
        
            btn3= ttk.Button(body,text="Habilitar",command= habilitar_camptext)
            btn3.place(x=800,y=250,width=80, height=30) 

            btn4 = ttk.Button(body,text="Validar",command=partial(validacion_correo,txt4))
            btn4.place(x=700,y=140,width=120, height=30) 

            btn5= ttk.Button(body,text="Validar",command=partial(validacion_entero,txt3))
            btn5.place(x=500,y=140,width=120, height=30)


            subfooter = tk.Frame(Interfaz,bg='#E5EAE8')
            subfooter.place(x=0,y=430,width=1000,height=20)
            lbfooter = tk.Label(subfooter,text="Jessica Cedeño | Giovanni Gonzalez | Andres Castro",bg='#E5EAE8')
            lbfooter.place(x=350,y=0)

            footer = tk.Frame(Interfaz,bg='#00995F')
            footer.place(x=0,y=480,width=1000,height=20)

            lbfooter = tk.Label(footer,text="Universidad Central - 2022",bg='#00995F',fg='white')
            lbfooter.place(x=400,y=0)
    
        
        

Interfaz = Tk()
eject = Application(master=Interfaz)
eject.mainloop()
