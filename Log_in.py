from tkinter import *
import tkinter.messagebox
import os
import hashlib
import json


def main():
    root = Tk()
    app = Window_1(root)
    root.mainloop()


class Window_1:
    def __init__(self, master):
        self.master = master
        self.master.title("Login Window")
        self.master.geometry('1350x750')
        self.master.config(bg='lightskyblue')
        self.Frame = Frame(self.master, bg='lightskyblue')
        self.Frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.Lbl_Title = Label(self.Frame, text='Login Menu', font=('arial', 55, 'bold'), bg='lightskyblue',
                               fg='Black')
        self.Lbl_Title.grid(row=0, column=0, columnspan=3, pady=40)

        self.Login_Frame_1 = LabelFrame(self.Frame, width=1350, height=600, relief='ridge', bg='lightskyblue', bd=15,
                                        font=('arial', 20, 'bold'))
        self.Login_Frame_1.grid(row=1, column=0)
        self.Login_Frame_2 = LabelFrame(self.Frame, width=1000, height=600, relief='ridge', bg='lightskyblue', bd=15,
                                        font=('arial', 20, 'bold'))
        self.Login_Frame_2.grid(row=2, column=0)

        self.Label_Username = Label(self.Login_Frame_1, text='Username', font=('arial', 20, 'bold'),
                                    bg='lightskyblue', bd=20)
        self.Label_Username.grid(row=0, column=0)
        self.text_Username = Entry(self.Login_Frame_1, font=('arial', 20, 'bold'), textvariable=self.Username)
        self.text_Username.grid(row=0, column=1, padx=50)

        self.Label_Password = Label(self.Login_Frame_1, text='Password', font=('arial', 20, 'bold'),
                                    bg='lightskyblue', bd=20)
        self.Label_Password.grid(row=1, column=0)
        self.text_Password = Entry(self.Login_Frame_1, font=('arial', 20, 'bold'), show='*', textvariable=self.Password)
        self.text_Password.grid(row=1, column=1)

        self.btnLogin = Button(self.Login_Frame_2, text='Login', width=10, font=('airia', 15, 'bold'),
                               command=self.Login)
        self.btnLogin.grid(row=3, column=0, padx=8, pady=20)

       

        self.btnExit = Button(self.Login_Frame_2, text='Exit', width=10, font=('airia', 15, 'bold'), command=self.Exit)
        self.btnExit.grid(row=3, column=2, padx=8, pady=20)

        self.btnRegister = Button(self.Login_Frame_2, text='Register', width=10, font=('airia', 15, 'bold'),
                                  command=self.Register)
        self.btnRegister.grid(row=3, column=1, padx=8, pady=20)

        self.load_user_data()  # Load registered users from file

    def Login(self):
        u = self.Username.get()
        p = self.Password.get()

        if u in self.passwords:
            hashed_password = hashlib.md5(p.encode()).hexdigest()
            if self.passwords[u] == hashed_password:
                self.__menu__()
                return
        tkinter.messagebox.askyesno("Login", "Error: Invalid username or password")
        self.Username.set("")
        self.Password.set("")

    def Reset(self):
        self.Username.set("")
        self.Password.set("")

    def Exit(self):
        self.Exit = tkinter.messagebox.askokcancel("Login System", "Confirm if you want to Exit")
        if self.Exit > 0:
            self.master.destroy()
            return

    def __menu__(self):
        filename = 'Menu.py'
        os.system(filename)
        os.system('notepad ' + filename)

    def Register(self):
        u = self.Username.get()
        p = self.Password.get()

        if u in self.passwords:
            tkinter.messagebox.askyesno("Register", "Username already exists!")
        else:
            self.passwords[u] = hashlib.md5(p.encode()).hexdigest()
            self.save_user_data()  # Save registered users to file
            tkinter.messagebox.askyesno("Register", "Registration successful!")

            self.Username.set("")
            self.Password.set("")

    def load_user_data(self):
        try:
            with open("user_data.json", "r") as file:
                self.passwords = json.load(file)
        except FileNotFoundError:
            self.passwords = {}

    def save_user_data(self):
        with open("user_data.json", "w") as file:
            json.dump(self.passwords, file)


if __name__ == '__main__':
    main()
