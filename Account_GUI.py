import customtkinter
from tkinter import *
from tkinter import ttk
import sqlite3
import os
import json
import webbrowser
from customtkinter import *
from customtkinter import CTkImage

#Importing the databases

database_switches = sqlite3.connect("database.db")
database_routers = sqlite3.connect("database.db")
database_users = sqlite3.connect("database_users.db")
database_keys = sqlite3.connect("database.db")


#Cursors for the databases  
cursor_switches = database_switches.cursor()
cursor_routers = database_routers.cursor()
cursor_users = database_users.cursor()
cursor_keys = database_keys.cursor()

#Defining the main GUI , Window 
app = customtkinter.CTk()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

path  = "../eTrafficApp/userinfo.json"
#Logging the user in json file userdetails.
with open(path,"r") as logging:
    #data = json.load(logging)
    data = logging.read()

#Main window 
app.title("eTraffic")
app.geometry("800x600")




#Main textbox

#Labels
def github():
    
    webbrowser.open(url="https://github.com/BeepBoopesMore/eTrafficApp")


github =  customtkinter.CTkButton(app,text="Github",command=github)
github.grid(row=0,column=1,pady=10)


                                         
# The auth enteries 

def login():
    username = username_entry.get()
    password = password_entry.get()
    if len(username) and len(password) > 0:
        #Check database
        cursor_users = database_users.cursor()
        #Checking if the username table exists 
        listOfTables = cursor_users.execute("SELECT name FROM sqlite_master WHERE type='table'AND name LIKE " + "'" + username + "';").fetchall()
        if listOfTables == []:
            error_label = customtkinter.CTkLabel(app,text="User does not exist")
            error_label.grid(row=4,column=12,pady=10)
            error_label.after(1000, error_label.destroy)
        else:
            #Log the user in 
            #TODO
            pass

    else:
        error_label = customtkinter.CTkLabel(app,text="Please enter username and password")
        error_label.grid(row=4,column=12,pady=10)
        error_label.after(1000, error_label.destroy)
username_entry = customtkinter.CTkEntry(app,placeholder_text="Username",text_color="white",font=("Roman", 20),width=200)
username_entry.grid(row=1,column=12,padx=10,pady=10)
password_entry = customtkinter.CTkEntry(app,placeholder_text="Password",text_color="white",font=("Roman", 20),width=200,show="*")
password_entry.grid(row=2,column=12,padx=10,pady=10)

login_button = customtkinter.CTkButton(app,text="Login",command=login)
login_button.grid(row=3,column=12,pady=10)

def callback(url):
    webbrowser.open_new(url)








#The loop that keeps the main window open
app.mainloop()  






