

import tkinter as tk


name = "amey"
username = input("enter your username :")
password = input("enter your password :")

if username == "amey01" and password == "amey123":
    print(f"login succesfully \n wellcome {name}")
     
elif username == "amey01" and password != "amey123" :
    print("you have enterd wrong password \n check your credentils")


elif username != "amey01" and password != "amey123" :
    print("you have enterd username and pasword wrong")


elif username != "amey01" and password == "amey123" :
    print("you have enterd wrong username")

else :
    print("something went wrong")

       #----GUI SETUP----

import tkinter as tk





# ---- GUI SETUP ----
import tkinter as tk

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "1234":
        print("Login successful")
    else:
        print("Wrong username or password")

app = tk.Tk()
app.title("Instagram Login Page")
app.geometry("400x300")

title_label = tk.Label(app, text="Instagram Login Page", font=("Lato", 19))
title_label.pack(pady=10)

username_label = tk.Label(app, text="Enter your username:", font=("Lato", 15))
username_label.pack(pady=5)

username_entry = tk.Entry(app, font=("Lato", 15))
username_entry.pack(pady=5)

password_label = tk.Label(app, text="Enter your password:", font=("Lato", 15))
password_label.pack(pady=5)

password_entry = tk.Entry(app, font=("Lato", 15), show="*")
password_entry.pack(pady=5)

login_btn = tk.Button(app, text="Login", font=("Lato", 15), command=login)
login_btn.pack(pady=10)

app.mainloop()
