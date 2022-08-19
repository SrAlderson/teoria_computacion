from tkinter import *
from tkinter import messagebox as MessageBox
import re 





def validacion_correo(txt4):

        n=txt4.get()

        if n!='':
        
            va = re.compile(r'^(\w|\.|\_|\-)+[@](\w|\.|\_|\-)+[.]\w{1,3}(?:[.]?)$')

            m = va.search(n)


            print(m)


            if m == None :

                    MessageBox.showwarning('Advertencia','Incorrecto el correo')

            else:

                    MessageBox.showinfo('Informacion','Correo Correcto')



def validacion_entero(txt3):

    num = txt3.get()

    validacion = re.compile(r'^(?:\+|\-?)[\d]')

    validacion_decimal = re.compile(r'^[\d]+[.][\d]')

    numero = validacion.search(num)

    nume = validacion_decimal.search(num)

    print(numero)

    print(nume)

    if nume == None :

        if numero == None:

            MessageBox.showwarning('Advertencia','Numero Incorrecto')

        else:

            MessageBox.showinfo('Informacion','Numero Correcto')

    else:

        MessageBox.showwarning('Advertencia','Numero Incorrecto')



def validacion_decimal(txt2):

    num = txt2.get()
    
    validacion = re.compile(r'^(?:\+|\-?)[\d]+[.][\d]')

    numero = validacion.search(num)

    print(numero)

    if numero == None:

        MessageBox.showwarning('Advertencia','Numero Incorrecto')

    else:

        MessageBox.showinfo('Informacion','Numero Correcto')



def validacion_cientifico(txt1):

    num = txt1.get()
    
    validacion = re.compile(r'^(?:\+|\-?)[\d]+(?:.?)[\d]+[E](?:\+|\-?)[\d]+')

    numero = validacion.search(num)

    print(numero)

    if numero == None:

        MessageBox.showwarning('Advertencia','Numero Incorrecto')

    else:

        MessageBox.showinfo('Informacion','Numero Correcto')


