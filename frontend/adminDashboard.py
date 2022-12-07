from tkinter import *
from tkinter import messagebox, ttk

from PIL import ImageTk, Image
from middleware.driver import Driver
from backend.driverManagement import *
from backend.customerManagement import *
from middleware.customer import Customer
from middleware import Global
from frontend import signin


class AdminDashboard:

    def __init__(self, root):
        self.root = root
        self.root.title("Admin Dashboard")
        self.root.geometry("550x500")  # size of the window
        self.root.state('zoomed')  # windows on zoomed / full-screen size
        self.root.config(background="#CECED2")  # background color change

        def change_home():  # function for home button
            home_frame.pack(side=RIGHT, fill=BOTH, expand=TRUE)
            driver.pack_forget()
            customer.pack_forget()

        def change_driver():  # function for driver management button
            driver.pack(side=RIGHT, fill=BOTH, expand=TRUE)
            home_frame.pack_forget()
            customer.pack_forget()

        def change_customer():  # function for customer management button
            customer.pack(side=RIGHT, fill=BOTH, expand=TRUE)
            driver.pack_forget()
            home_frame.pack_forget()

        # font used in the button in navbar
        nav_font = ('Times New Roman', 25, "bold")
        reg_font = ('Cordia New', 14)

        # first frame / navbar
        navbar = Frame(self.root, bg="#4CD964", width=350)
        navbar.pack(side=LEFT, fill=BOTH)

        # image
        profile = ImageTk.PhotoImage(Image.open(
            "H:\\College\\Sem-2\\python assignment\\Taxi Booking System\\image\\profile.png"))
        profile_label = Label(navbar, image=profile, bg="#4CD964")
        profile_label.image = profile
        profile_label.place(x=100, y=50)

        # home button
        home_btn = Button(navbar, text="Home", command=change_home,
                          font=nav_font, bg="#4CD964", relief=RIDGE)
        home_btn.place(x=110, y=210)

        # driver manage button
        driver_button = Button(navbar, text="Manage Driver",
                               command=change_driver, font=nav_font, bg="#4CD964", relief=RIDGE)
        driver_button.place(x=50, y=300)

        # customer manage button
        customer_button = Button(navbar, text="Manage Customer",
                                 command=change_customer, font=nav_font, bg="#4CD964", relief=RIDGE)
        customer_button.place(x=30, y=390)

        # function for logout
        def logout720():
            self.root.destroy()
            root = Tk()
            obj = signin.Signin(root)
            root.mainloop()

        # logout button with image
        logout = ImageTk.PhotoImage(Image.open(
            "H:\\College\\Sem-2\\python assignment\\Taxi Booking System\\image\\logout.png"))
        logout_btn = Button(navbar, image=logout, bg="#4CD964",
                            relief=FLAT, activebackground="#4CD964", command=logout720)
        logout_btn.image = logout
        logout_btn.place(x=110, y=650)

        # second frame
        # home frame of admin
        home_frame = Frame(self.root)
        home_frame.pack(side=RIGHT, fill=BOTH, expand=TRUE)

        # adding widgets on home frame

        bid_frame = LabelFrame(home_frame, text="Booking ID", font=reg_font)
        bid_frame.place(x=10, y=10)

        bid_txt = Entry(bid_frame, text="", font=reg_font)
        bid_txt.pack()

        name_frame = LabelFrame(home_frame, text='Full Name', font=reg_font)
        name_frame.place(x=310, y=10)

        name_txt = Entry(name_frame, text='', font=reg_font)
        name_txt.pack()

        paddress_frame = LabelFrame(
            home_frame, text='Pickup Address', font=reg_font)
        paddress_frame.place(x=610, y=10)

        paddress_txt = Entry(paddress_frame, text='', font=reg_font)
        paddress_txt.pack()

        daddress_label = LabelFrame(
            home_frame, text="Drop Address", font=reg_font)
        daddress_label.place(x=910, y=10)

        daddress_txt = Entry(daddress_label, text='', font=reg_font)
        daddress_txt.pack()

        date_label = LabelFrame(home_frame, text="Pickup Date", font=reg_font)
        date_label.place(x=10, y=120)

        date_txt = Entry(date_label, text='', font=reg_font)
        date_txt.pack()

        time_label = LabelFrame(home_frame, text="Pickup Time", font=reg_font)
        time_label.place(x=310, y=120)

        time_txt = Entry(time_label, text='', font=reg_font)
        time_txt.pack()

        status_label = LabelFrame(
            home_frame, text='Booking Status', font=reg_font)
        status_label.place(x=610, y=120)

        status_txt = Entry(status_label, text='', font=reg_font)
        status_txt.pack()

        driver_label = LabelFrame(
            home_frame, text='Assign Driver', font=reg_font)
        driver_label.place(x=910, y=120)

        driver_txt = Entry(driver_label, text='', font=reg_font)
        driver_txt.pack()

        check_btn = Button(home_frame, text="Check Driver",
                           font=reg_font, relief=RAISED, bd=5)
        check_btn.place(x=800, y=240)

        confirm_btn = Button(home_frame, text="Confirm Booking",
                             font=reg_font, relief=RAISED, bd=5)
        confirm_btn.place(x=980, y=240)

        aid_txt = Entry(home_frame)
        # aid_txt.insert(0, Global.currentUser[0])

        # driver management frame
        driver = Frame(self.root)

        #  adding widget on driver management frame or driver frame

        dname_frame = LabelFrame(driver, text='Full Name', font=reg_font)
        dname_frame.place(x=10, y=10)

        dname_txt = Entry(dname_frame, text='', font=reg_font)
        dname_txt.pack()

        daddress_frame = LabelFrame(driver, text='Address', font=reg_font)
        daddress_frame.place(x=310, y=10)

        daddress_txt = Entry(daddress_frame, text='', font=reg_font)
        daddress_txt.pack()

        demail_frame = LabelFrame(driver, text='Email', font=reg_font)
        demail_frame.place(x=610, y=10)

        demail_txt = Entry(demail_frame, text='', font=reg_font)
        demail_txt.pack()

        dlicenseno_frame = LabelFrame(driver, text='License No', font=reg_font)
        dlicenseno_frame.place(x=910, y=10)

        dlicenseno_txt = Entry(dlicenseno_frame, text='', font=reg_font)
        dlicenseno_txt.pack()

        dpassword_frame = LabelFrame(driver, text='Password', font=reg_font)
        dpassword_frame.place(x=10, y=120)

        dpassword_txt = Entry(dpassword_frame, text='', font=reg_font)
        dpassword_txt.pack()

        # function for add button to add driver
        def addDriver():
            driver = Driver(did='', fullname=dname_txt.get(), address=daddress_txt.get(
            ), email=demail_txt.get(), licenseno=dlicenseno_txt.get(), password=dpassword_txt.get(), status="Active")
            result = add(driver)
            if result == True:
                msg1 = messagebox.showinfo(
                    "Taxi Booking System", "Driver Added Successfully!")
            else:
                msg2 = messagebox.showinfo(
                    "Taxi Booking System", "Error Occurred!")

        add_btn = Button(driver, text='    ADD   ', font=reg_font,
                         relief=RAISED, bd=5, command=addDriver)
        add_btn.place(x=310, y=125)

        update_btn = Button(driver, text='UPDATE',
                            font=reg_font, relief=RAISED, bd=5)
        update_btn.place(x=460, y=125)

        delete_btn = Button(driver, text='DELETE',
                            font=reg_font, relief=RAISED, bd=5)
        delete_btn.place(x=620, y=125)

        # customer management frame
        customer = Frame(self.root)

        #  adding widget on driver management frame or driver frame

        cname_frame = LabelFrame(customer, text='Full Name', font=reg_font)
        cname_frame.place(x=10, y=10)

        cname_txt = Entry(cname_frame, text='', font=reg_font)
        cname_txt.pack()

        caddress_frame = LabelFrame(customer, text='Address', font=reg_font)
        caddress_frame.place(x=310, y=10)

        caddress_txt = Entry(caddress_frame, text='', font=reg_font)
        caddress_txt.pack()

        cemail_frame = LabelFrame(customer, text='Email', font=reg_font)
        cemail_frame.place(x=610, y=10)

        cemail_txt = Entry(cemail_frame, text='', font=reg_font)
        cemail_txt.pack()

        cphoneno_frame = LabelFrame(customer, text='Phone No', font=reg_font)
        cphoneno_frame.place(x=910, y=10)

        cphoneno_txt = Entry(cphoneno_frame, text='', font=reg_font)
        cphoneno_txt.pack()

        cpassword_frame = LabelFrame(customer, text='Password', font=reg_font)
        cpassword_frame.place(x=10, y=120)

        cpassword_txt = Entry(cpassword_frame, text='', font=reg_font)
        cpassword_txt.pack()

        cpayment_frame = LabelFrame(customer, text='Payment', font=reg_font)
        cpayment_frame.place(x=310, y=120)

        cpayment = ttk.Combobox(cpayment_frame, font=reg_font, width=18)
        cpayment['values'] = ('Cash', 'Online')
        cpayment.pack()

        def addCustomer():
            customer = Customer(fullname=cname_txt.get(), address=caddress_txt.get(), email=cemail_txt.get(),
                                number=cphoneno_txt.get(), password=cpassword_txt.get(), payment=cpayment.get())
            result = register(customer)
            if result == True:
                msg1 = messagebox.showinfo(
                    "Taxi Booking System", "Customer Registration Successful")

            else:
                msg2 = messagebox.showerror(
                    "Taxi Booking System", "Error Occurred!")

        cadd_btn = Button(customer, text='    ADD   ', font=reg_font,
                          relief=RAISED, bd=5, command=addCustomer)
        cadd_btn.place(x=610, y=125)

        cupdate_btn = Button(customer, text='UPDATE',
                             font=reg_font, relief=RAISED, bd=5)
        cupdate_btn.place(x=770, y=125)

        cdelete_btn = Button(customer, text='DELETE',
                             font=reg_font, relief=RAISED, bd=5)
        cdelete_btn.place(x=930, y=125)


if __name__ == '__main__':
    root = Tk()
    AdminDashboard(root)
    root.mainloop()
