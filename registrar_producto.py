import tkinter as tk 
from tkinter import *

#tamaños de la pantalla en general. 

screen = tk.Tk()
screen.title("Sistema de inventario.")
screen.geometry("800x600")
screen.resizable(True, True)

#Labels. 

label_principal = tk.Label(screen, text= "INVENTARIO", font= ("Helvetica", 25, "bold"), bg= "White")
label_principal.pack(pady= 30) 

screen.config(bg = "White") 

#Botones 

boton_1= tk.Button(screen, text = "Ingresar Producto", width=15, height=2, font= ("Times New Roman", 15), bg= "LightBlue", fg= "Black")
boton_1.pack(pady=20) 

boton_2= tk.Button(screen, text = "Mostrar Inventario", width=15, height=2, font= ("Times New Roman", 15), bg= "LightBlue", fg= "Black")
boton_2.pack(pady=20)  



screen.mainloop()
