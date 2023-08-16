import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter asśk
from tkinter import messagebox
import database

app = customtkinter.CTk()
app.little('Employee Management System')
app.geometry('900x420')
app.config(bg='#161C25')
app.resizable(False,False)

font1 = ('Arial',20, 'bold')
font2 = ('Arial',12, 'bold')

id_label = customtkinter.CTkLabel(app,font=font1,text='ID:',text_color='#fff',bg_color='#161C25')
id_label.place(x=20,y=20)

id_entry = customtkinter.CTkLabel(app,font=font1,text_color='#000',fg_color='#fff',border_color='#0C9295',border_width=2,width=180)
id_entry.place(x=100,y=20)

name_label = customtkinter.CTkLabel(app,font=font1,text='Name:',text_color='#fff',bg_color='#161C25')
name_label.place(x=20,y=80)

name_entry = customtkinter.CTkEntry(app,font=font1,text='Name:',text_color='#000',bg_color='#161C25')
name_entry.place(x=100,y=80)

role_label = customtkinter.CTkLabel(app,font=font1,text='Name:',text_color='#fff',bg_color='#161C25')
role_label.place(x=20,y=140)