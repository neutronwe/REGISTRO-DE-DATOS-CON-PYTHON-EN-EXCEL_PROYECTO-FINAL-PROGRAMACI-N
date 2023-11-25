from tkinter import Tk, Label, Button,Entry, Frame, END
import pandas as pd

ventana = Tk()
ventana.config(bg='black')
ventana.geometry('560x388')
ventana.resizable(0,0)
ventana.title('Formulario Personal')
nombre1,cedula1,edad1,correo1,telefono1 = [],[],[],[],[]

def agregar_datos():
  global nombre1, cedula1, dni1, correo1, celular1

  nombre1.append(ingresa_nombre.get())
  cedula1.append(ingresa_cedula.get())
  edad1.append(ingresa_edad.get())
  correo1.append(ingresa_correo.get())
  celular1.append(ingresa_celular.get())

  ingresa_nombre.delete(0,END)
  ingresa_cedula.delete(0,END)
  ingresa_edad.delete(0,END)
  ingresa_correo.delete(0,END)
  ingresa_celular.delete(0,END)

def guardar_datos():	
  global nombre1,cedula1,edad1,correo1,celular1
  datos = {'Nombres':nombre1,'Cedula':cedula1, 'Edad':edad1, 'Correo':correo1, 'Celular':celular1 } 
  nom_excel  = str(nombre_archivo.get() + ".xlsx")	
  df = pd.DataFrame(datos,columns =  ['Nombres', 'Cedula', 'Edad', 'Correo', 'Celular']) 
  df.to_excel(nom_excel)
  nombre_archivo.delete(0,END)

frame1 = Frame(ventana, bg='gray15')
frame1.grid(column=0, row=0, sticky='nsew')
frame2 = Frame(ventana, bg='gray16')
frame2.grid(column=1, row=0, sticky='nsew')

nombre = Label(frame1, text ='N Y A', width=10).grid(column=0, row=0, pady=20, padx= 10)
ingresa_nombre = Entry(frame1,  width=20, font = ('Berlin Sans FB',12))
ingresa_nombre.grid(column=1, row=0)

cedula = Label(frame1, text ='Cedula', width=10).grid(column=0, row=1, pady=20, padx= 10)
ingresa_cedula = Entry(frame1, width=20, font = ('Berlin Sans FB',12))
ingresa_cedula.grid(column=1, row=1)

edad = Label(frame1, text ='Edad', width=10).grid(column=0, row=2, pady=20, padx= 10)
ingresa_edad = Entry(frame1,  width=20, font = ('Berlin Sans FB',12))
ingresa_edad.grid(column=1, row=2)

correo = Label(frame1, text ='Correo', width=10).grid(column=0, row=3, pady=20, padx= 10)
ingresa_correo = Entry(frame1,  width=20, font = ('Berlin Sans FB',12))
ingresa_correo.grid(column=1, row=3)

telefono = Label(frame1, text ='N. Celular', width=10).grid(column=0, row=4, pady=20, padx= 10)
ingresa_celular = Entry(frame1, width=20, font = ('Berlin Sans FB',12))
ingresa_celular.grid(column=1, row=4)

agregar = Button(frame1, width=20, font = ('Arial',12, 'bold'), text='Agregar', bg='blue',bd=5, command =agregar_datos)
agregar.grid(columnspan=2, row=5, pady=20, padx= 10)

archivo = Label(frame2, text ='Nombre del Archivo : ', width=25, bg='gray16',font = ('Calibri Light',12, 'bold'), fg='white')
archivo.grid(column=0, row=0, pady=10, padx= 10)

nombre_archivo = Entry(frame2, width=23, font = ('Calibri Lignt',12),highlightbackground = "green", highlightthickness=4)
nombre_archivo.grid(column=0, row=1, pady=1, padx= 10)

guardar = Button(frame2, width=20, font = ('Arial',12, 'bold'), text='Guardar', bg='green2',bd=5, command =guardar_datos)
guardar.grid(column=0, row=2, pady=20, padx= 10)
ventana.mainloop()