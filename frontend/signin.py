from tkinter import *
import frontend.signup


class Signin:
    def __init__(self, root):
        self.root = root
        self.root.title("SignIn")
        self.root.geometry("550x500")  # size of the window
        self.root.state('zoomed')  # windows on zoomed / full-screen size
        self.root.resizable(False, False)  # windows resizable false
        self.root.config(background="#CECED2")  # background color change

        font1 = ('Cooper Black', 30, "bold")
        font2 = ('Cordia New', 14)
        font3 = ('Times New Roman', 25, "bold")

        # First frame
        frame1 = Frame(root, bg="#EFEFF4", height=650, width=600)
        frame1.place(x=175, y=100)

        signin_txt = Label(frame1, text="Sign in", font=font1)
        signin_txt.place(x=200, y=160)

        email_frame = LabelFrame(frame1, text="Email")
        email_frame.place(x=175, y=250)

        email_txt = Entry(email_frame, text="", font=font2, relief=RAISED)
        email_txt.pack()

        password_frame = LabelFrame(frame1, text="Password")
        password_frame.place(x=175, y=300)

        password = Entry(password_frame, text="", font=font2, relief=RAISED)
        password.pack()

        btn_signin = Button(frame1, text="Submit", font=font3,
                            relief=GROOVE, command=input, bg="#4CD964", fg="#EFEFF4")
        btn_signin.place(x=220, y=375)

        # Second Frame
        frame2 = Frame(self.root, bg="#4CD964", height=650, width=600)
        frame2.place(x=775, y=100)

        signup_lbl = Label(frame2, text="Sign UP", bg="#4CD964",
                           font=font1, fg="#EFEFF4")
        signup_lbl.place(x=200, y=200)

        signup_txt = Label(
            frame2, text="Sign up here if you don't have account", bg="#4CD964", font=font2)
        signup_txt.place(x=125, y=300)

        def signup():
            self.root.destroy()
            root = Tk()
            obj = frontend.signup.Registration(root)
            root.mainloop()

        btn_signup = Button(frame2, text="SIGN UP", font=font3,
                            relief=GROOVE, command=signup, bg="#EFEFF4")
        btn_signup.place(x=200, y=350)
