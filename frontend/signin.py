from tkinter import *
from tkinter import messagebox
import frontend.signup
from frontend import admindashboard, customerdashboard, driverdashboard
from backend.loginManagement import *
from middleware.customer import Customer
from middleware.driver import Driver
from middleware.admin import Admin
from middleware import Global


class TaxiLogin:

    def __init__(self, root):
        self.root = root
        self.root.title("SignIn")
        self.root.state('zoomed')  # windows on zoomed / full-screen size
        # self.root.resizable(False, False)  # windows resizable false
        self.root.config(background="#CECED2")  # background color change

        def signup():
            self.root.destroy()
            root = Tk()
            obj = frontend.signup.Registration(root)
            root.mainloop()

        font1 = ('Cooper Black', 30, "bold")
        font2 = ('Cordia New', 14)
        font3 = ('Times New Roman', 25, "bold")

        def login720():
            cus_login = Customer(email=email_txt.get(),
                                 password=password11.get())
            user = login(cus_login)

            dri_login = Driver(email=email_txt.get(),
                               password=password11.get())
            duser = dlogin(dri_login)

            admin_login = Admin(email=email_txt.get(),
                                password=password11.get())
            auser = alogin(admin_login)

            if (email_txt.get() == '') or (password11.get() == ''):
                msg11 = messagebox.showwarning(
                    "Taxi Booking System", "Please Enter Email and Password")

            else:
                if user != None:
                    msg1 = messagebox.showinfo(
                        "Taxi Booking System", "Welcome {}".format(user[1]))
                    Global.currentUser = user
                    self.root.destroy()
                    root = Tk()
                    customerdashboard.CustomerDashboard(root)
                    root.mainloop()

                elif duser != None:
                    msg2 = messagebox.showinfo(
                        "Taxi Booking System", "Welcome {}".format(duser[1]))
                    Global.currentDriver = duser
                    self.root.destroy()
                    root = Tk()
                    driverdashboard.DriverDashboard(root)
                    root.mainloop()

                elif auser != None:
                    msg3 = messagebox.showinfo(
                        "Taxi Booking System", "Welcome {}".format(auser[1]))
                    Global.currentAdmin = auser
                    self.root.destroy()
                    root = Tk()
                    admindashboard.AdminDashboard(root)
                    root.mainloop()

                else:
                    msg4 = messagebox.showerror(
                        "Taxi Booking System", "Error: Wrong Email or Password")

        # First frame
        frame1 = Frame(root, bg="#EFEFF4", height=650, width=600)

        signin_txt = Label(frame1, text="Sign in", font=font1)
        signin_txt.place(x=200, y=160)

        email_frame = LabelFrame(frame1, text="Email")
        email_frame.place(x=175, y=250)

        email_txt = Entry(email_frame, font=font2, relief=RAISED)
        email_txt.pack()

        password_frame = LabelFrame(frame1, text="Password")
        password_frame.place(x=175, y=300)

        password11 = Entry(password_frame,
                           font=font2, relief=RAISED, show='*')
        password11.pack()

        btn_signin = Button(frame1, text="Submit", font=font3,
                            relief=GROOVE, command=login720, bg="#4CD964", fg="#EFEFF4")
        btn_signin.place(x=220, y=375)

        frame1.place(x=175, y=100)

        # Second Frame
        frame2 = Frame(self.root, bg="#4CD964", height=650, width=600)

        signup_lbl = Label(frame2, text="Sign UP", bg="#4CD964",
                           font=font1, fg="#EFEFF4")
        signup_lbl.place(x=200, y=200)

        signup_txt = Label(
            frame2, text="Sign up here if you don't have account", bg="#4CD964", font=font2)
        signup_txt.place(x=125, y=300)

        btn_signup = Button(frame2, text="SIGN UP", font=font3,
                            relief=GROOVE, command=signup, bg="#EFEFF4")
        btn_signup.place(x=200, y=350)

        frame2.place(x=775, y=100)


if __name__ == '__main__':
    root = Tk()
    TaxiLogin(root)
    root.mainloop()
