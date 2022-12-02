from tkinter import *
from frontend import signin
from PIL import ImageTk, Image
from middleware.customer import Customer
from backend.customerManagement import register
from tkinter import messagebox


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
        font3 = ('Times New Roman', 25, "bold")

        # First frame
        frame1 = Frame(root, bg="#EFEFF4", height=650, width=600)
        frame1.place(x=175, y=100)

        signin_txt = Label(frame1, text=" Sign Up ", font=(
            'Cooper Black', 30, "bold", UNDERLINE))
        signin_txt.place(x=200, y=50)

        fullname_frame = LabelFrame(frame1, text="Full Name")
        fullname_frame.place(x=175, y=150)

        fullname_txt = Entry(fullname_frame, text="",
                             font=font2, relief=RAISED)
        fullname_txt.pack()

        address_frame = LabelFrame(frame1, text="Address")
        address_frame.place(x=175, y=200)

        address = Entry(address_frame, text="", font=font2, relief=RAISED)
        address.pack()

        email_frame = LabelFrame(frame1, text="Email")
        email_frame.place(x=175, y=250)

        email = Entry(email_frame, text="", font=font2, relief=RAISED)
        email.pack()

        number_frame = LabelFrame(frame1, text="Phone Number")
        number_frame.place(x=175, y=300)

        number = Entry(number_frame, text="", font=font2, relief=RAISED)
        number.pack()

        password_frame = LabelFrame(frame1, text="Password")
        password_frame.place(x=175, y=350)

        password = Entry(password_frame, text="", font=font2, relief=RAISED)
        password.pack()

        payment_frame = LabelFrame(frame1, text="Payment Method")
        payment_frame.place(x=175, y=400)

        payment = Entry(payment_frame, text='', font=font2, relief=RAISED)
        payment.pack()

        def saveInfo():
            customer = Customer(fullname=fullname_txt.get(), address=address.get(), email=email.get(),
                                number=number.get(), password=password.get(), payment=payment.get())
            result = register(customer)
            if result == True:
                msg1 = messagebox.showinfo(
                    "Taxi Booking System", "Customer Registration Successful")

            else:
                msg2 = messagebox.showerror(
                    "Taxi Booking System", "Error Occurred!")

        btn_signin = Button(frame1, text="Submit", font=font3,
                            relief=GROOVE, command=saveInfo, bg="#4CD964", fg="#EFEFF4")
        btn_signin.place(x=220, y=470)

        # making function for command

        def signup():
            self.root.destroy()
            root = Tk()
            obj = signin.Signin(root)
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

        taxi_image = Canvas(frame2, height=646, width=600)
        taxi_image.pack()
        self.root.image = ImageTk.PhotoImage(Image.open(
            "H:\College\Sem-2\python assignment\Taxi Booking System\image\signup.png"))
        taxi_image.create_image(10, 10, anchor=NW, image=self.root.image)
