from tkinter import *
from GUI import Signin
from PIL import ImageTk, Image


class Registration:
    def __init__(self, root):
        self.root = root
        self.root.title("SignUp")
        self.root.geometry("550x500")  # size of the window
        self.root.state('zoomed')  # windows on zoomed / full-screen size
        self.root.resizable(False, False)  # windows resizable false
        self.root.config(background="#CECED2")  # background color change

        font1 = ('Cooper Black', 30, "bold")
        font2 = ('Cordia New', 14)

        # First frame
        frame1 = Frame(root, bg="#EFEFF4", height=650, width=600)
        frame1.place(x=175, y=100)

        signin_txt = Label(frame1, text=" Sign Up ", font=(
            'Cooper Black', 30, "bold", UNDERLINE))
        signin_txt.place(x=200, y=50)

        firstname_frame = LabelFrame(frame1, text="First Name")
        firstname_frame.place(x=175, y=150)

        firstname_txt = Entry(firstname_frame, text="",
                              font=font2, relief=RAISED)
        firstname_txt.pack()

        lastname_frame = LabelFrame(frame1, text="Last Name")
        lastname_frame.place(x=175, y=200)

        lastname_txt = Entry(lastname_frame, text="",
                             font=font2, relief=RAISED)
        lastname_txt.pack()

        address_frame = LabelFrame(frame1, text="Address")
        address_frame.place(x=175, y=250)

        address = Entry(address_frame, text="", font=font2, relief=RAISED)
        address.pack()

        email_frame = LabelFrame(frame1, text="Email")
        email_frame.place(x=175, y=300)

        email = Entry(email_frame, text="", font=font2, relief=RAISED)
        email.pack()

        phone_frame = LabelFrame(frame1, text="Phone Number")
        phone_frame.place(x=175, y=350)

        phone = Entry(phone_frame, text="", font=font2, relief=RAISED)
        phone.pack()

        password_frame = LabelFrame(frame1, text="Password")
        password_frame.place(x=175, y=400)

        password = Entry(password_frame, text="", font=font2, relief=RAISED)
        password.pack()

        btn_signin = Button(frame1, text="Submit", font=font3,
                            relief=GROOVE, command=input, bg="#4CD964", fg="#EFEFF4")
        btn_signin.place(x=220, y=470)

        # making function for command

        def signup():
            self.root.destroy()
            root = Tk()
            obj = Signin.Signin(root)
            root.mainloop()

        # making function for enter and leave event
        def on_enter(e):
            back_txt.config(fg="#4CD964")

        def on_leave(e):
            back_txt.config(fg="black")

        back_txt = Button(frame1, text="go back to Sign In page", font=(
            'Cordia New', 14, UNDERLINE), command=signup, bd=0, bg="#EFEFF4")
        back_txt.bind("<Enter>", on_enter)  # using enter event
        back_txt.bind("<Leave>", on_leave)  # using leave event
        back_txt.place(x=375, y=600)

        # Second Frame
        frame2 = Frame(self.root, bg="#4CD964", height=650, width=600)
        frame2.place(x=775, y=100)

        canvas = Canvas(frame2, height=646, width=600)
        canvas.pack()
        self.root.image = ImageTk.PhotoImage(Image.open(
            "H:\College\Sem-2\pictures\City driver-cuate11.png"))
        canvas.create_image(10, 10, anchor=NW, image=self.root.image)
