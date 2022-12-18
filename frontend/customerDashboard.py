from datetime import date
from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

from backend.customerManagement import editCus
from frontend import signin
from middleware.booking import Booking
from backend.bookingManagement import cusdastable, cancelreqBooking
from middleware import Global
from backend.bookingManagement import insert
from PIL import ImageTk, Image

from middleware.customer import Customer


class CusDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Dashboard")
        self.root.geometry("550x500")  # size of the window
        self.root.state('zoomed')  # windows on zoomed / full-screen size
        self.root.config(background="#CECED2")  # background color change

        heading_font = ('Cooper Black', 30, "bold", UNDERLINE)
        text_font = ('Cordia New', 14)
        nav_font = ('Times New Roman', 25, "bold")

        # first frame / navbar
        navbar = Frame(self.root, bg="#4CD964", width=350)
        navbar.pack(side=LEFT, fill=BOTH)

        # style of table
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        rowheight=25,
                        background="#f0f0f0",
                        fieldbackground="#f0f0f0",
                        bordercolor="#343638",
                        borderwidth=2,
                        font=('Times New Roman', 14))

        style.configure("Treeview.Heading",
                        background="#565b5e",
                        foreground="white",
                        relief="flat",
                        font=('Times New Roman', 14))
        style.map("Treeview.Heading",
                  )

        # image
        profile = ImageTk.PhotoImage(Image.open(
            "H:\\College\\Sem-2\\python assignment\\Taxi Booking System\\image\\profile.png"))

        profile_label = Label(navbar, image=profile, bg="#4CD964")
        profile_label.image = profile
        profile_label.place(x=90, y=50)

        def change_home():  # function for home button
            home_frame.pack(side=RIGHT, fill=BOTH, expand=TRUE)
            history_frame.pack_forget()
            profile_frame.pack_forget()

        # home button
        home_btn = Button(navbar, text=" Home  ", command=change_home,
                          font=nav_font, bg="#4CD964", relief=RIDGE)
        home_btn.place(x=90, y=210)

        def change_history():  # function for history button
            history_frame.pack(side=RIGHT, fill=BOTH, expand=TRUE)
            home_frame.pack_forget()
            profile_frame.pack_forget()

        # history button
        history_button = Button(navbar, text="History",
                                command=change_history, font=nav_font, bg="#4CD964", relief=RIDGE)
        history_button.place(x=90, y=300)

        def change_profile():  # function for profile button
            profile_frame.pack(side=RIGHT, fill=BOTH, expand=TRUE)
            history_frame.pack_forget()
            home_frame.pack_forget()

        # profile button
        profile_button = Button(navbar, text=" Profile ",
                                command=change_profile, font=nav_font, bg="#4CD964", relief=RIDGE)
        profile_button.place(x=90, y=390)

        # function for logout
        def logout720():
            self.root.destroy()
            root = Tk()
            obj = signin.Signin(root)
            root.mainloop()

        # logout button with image
        logout = ImageTk.PhotoImage(Image.open(
            "H:\\College\\Sem-2\\python assignment\\Taxi Booking System\\image\\logout.png"))
        logout_btn = Button(navbar, command=logout720, image=logout, bg="#4CD964",
                            relief=FLAT, activebackground="#4CD964")
        logout_btn.image = logout
        logout_btn.place(x=110, y=650)

        # second frame
        # home frame of admin
        home_frame = Frame(self.root)
        home_frame.pack(side=RIGHT, fill=BOTH, expand=TRUE)

        # driver management frame
        history_frame = Frame(self.root, bg="black")

        # customer management frame
        profile_frame = Frame(self.root)

        # adding widgets in home frame
        booking_txt = Label(home_frame, text="Booking", font=heading_font)
        booking_txt.place(x=70, y=120)

        pickaddress_frame = LabelFrame(home_frame, text="PickUp Address")
        pickaddress_frame.place(x=50, y=220)

        pickaddress = Entry(pickaddress_frame, text="",
                            font=text_font, relief=RAISED)
        pickaddress.pack()

        dropaddress_frame = LabelFrame(home_frame, text="Drop Address")
        dropaddress_frame.place(x=50, y=270)

        dropaddress = Entry(dropaddress_frame, text="",
                            font=text_font, relief=RAISED)
        dropaddress.pack()

        date_frame = LabelFrame(home_frame, text="Pickup Date")
        date_frame.place(x=50, y=320)

        todaydate = date.today()
        pickupdate = DateEntry(date_frame, width=18,
                               font=text_font, mindate=todaydate)
        pickupdate.pack()

        time_frame = LabelFrame(home_frame, text="Pickup Time")
        time_frame.place(x=50, y=370)

        pickuptime = Entry(time_frame, text="", font=text_font, relief=RAISED)
        pickuptime.pack()

        cid_txt = Entry(home_frame)
        # ----------------------------------------------------------------------------------------------
        cid_txt.insert(0, Global.currentUser[0])

        bid_txt = Entry(home_frame)

        # function for request booking by customer
        def requestbooking():
            requestbooking = Booking(bookingid='', pickup_address=pickaddress.get(), drop_address=dropaddress.get(
            ), pickup_date=pickupdate.get(), pickup_time=pickuptime.get(), status="Pending", cid=cid_txt.get())
            result = insert(requestbooking)
            if result == True:
                msg1 = messagebox.showinfo(
                    "Taxi Booking System", "Booking Request Successful")
                requested_table.delete(*requested_table.get_children())
                cusdas()

            else:
                msg2 = messagebox.showerror(
                    "Taxi Booking System", "Error Occurred!")

        request = Button(home_frame, text='Request',
                         font=text_font, relief=RAISED, command=requestbooking)
        request.place(x=60, y=430)

        def clearfun():
            pickaddress.delete(0, END)
            dropaddress.delete(0, END)
            pickupdate.delete(0, END)
            pickuptime.delete(0, END)
            bid_txt.delete(0, END)

        clear = Button(home_frame, text='  Clear  ',
                       font=text_font, relief=RAISED, command=clearfun)
        clear.place(x=180, y=430)

        def cancelfun():
            cancelreq = cancelreqBooking(bid_txt.get())
            if cancelreq == True:
                msg1 = messagebox.showinfo(
                    "Taxi Booking System", "Booking Cancelled Successful")
                requested_table.delete(*requested_table.get_children())
                cusdas()
            else:
                msg2 = messagebox.showerror(
                    "Taxi Booking System", "Error Occurred!")

        cancel = Button(home_frame, text=' Cancel ',
                        font=text_font, relief=RAISED, command=cancelfun)
        cancel.place(x=120, y=480)

        requested_table = ttk.Treeview(home_frame)
        requested_table['columns'] = (
            'bid', 'p_address', 'd_address', 'p_date', 'p_time')
        requested_table.column('#0', width=0, stretch=NO)
        requested_table.column('bid', width=0, stretch=NO)
        requested_table.column('p_address', width=200, anchor=CENTER)
        requested_table.column('d_address', width=200, anchor=CENTER)
        requested_table.column('p_date', width=200, anchor=CENTER)
        requested_table.column('p_time', width=200, anchor=CENTER)

        requested_table.heading('#0', text='', anchor=CENTER)
        requested_table.heading('bid', text='', anchor=CENTER)
        requested_table.heading(
            'p_address', text='Pickup Address', anchor=CENTER)
        requested_table.heading(
            'd_address', text='Drop Address', anchor=CENTER)
        requested_table.heading('p_date', text='Pickup Date', anchor=CENTER)
        requested_table.heading('p_time', text='Pickup Time', anchor=CENTER)
        requested_table.pack(side=RIGHT, fill=BOTH)

        def cusdas():
            cusbook = Booking(cid=cid_txt.get(), status='Pending')
            cuspending = cusdastable(cusbook)
            for row in cuspending:
                requested_table.insert(parent='', index='end', values=(
                    row[0], row[1], row[2], row[3], row[4]))
        cusdas()

       # function to get selected item values from table
        def selectrequested_table(a):
            bid_txt.delete(0, END)
            pickaddress.delete(0, END)
            dropaddress.delete(0, END)
            pickupdate.delete(0, END)
            pickuptime.delete(0, END)

            selectitem = requested_table.selection()[0]
            bid_txt.insert(0, requested_table.item(selectitem)['values'][0])
            pickaddress.insert(
                0, requested_table.item(selectitem)['values'][1])
            dropaddress.insert(
                0, requested_table.item(selectitem)['values'][2])
            pickupdate.insert(0, requested_table.item(selectitem)['values'][3])
            pickuptime.insert(0, requested_table.item(selectitem)['values'][4])

        requested_table.bind('<<TreeviewSelect>>', selectrequested_table)

        # widgets on profile frame ----------------------------------------------------------------------

        cus_fullname = LabelFrame(profile_frame, text= 'Fullname', font=text_font)
        cus_fullname.place(x=300, y=100)

        cus_fullname_txt = Entry(cus_fullname, font=text_font)
        cus_fullname_txt.insert(0, Global.currentUser[1])
        cus_fullname_txt.pack()

        cus_address = LabelFrame(profile_frame, text='Address', font=text_font)
        cus_address.place(x=300, y=190)

        cus_address_txt= Entry(cus_address, font=text_font)
        cus_address_txt.insert(0, Global.currentUser[2])
        cus_address_txt.pack()

        cus_email = LabelFrame(profile_frame, text="Email", font=text_font)
        cus_email.place(x=300, y=280)

        cus_email_txt = Entry(cus_email, font=text_font)
        cus_email_txt.insert(0, Global.currentUser[3])
        cus_email_txt.pack()

        cus_number = LabelFrame(profile_frame, text="Phone Number", font=text_font)
        cus_number.place(x=300, y=370)

        cus_number_txt = Entry(cus_number, font=text_font)
        cus_number_txt.insert(0, Global.currentUser[4])
        cus_number_txt.pack()

        cus_password = LabelFrame(profile_frame, text="Password", font=text_font)
        cus_password.place(x=300, y=460)

        cus_password_txt = Entry(cus_password, font=text_font)
        cus_password_txt.insert(0, Global.currentUser[5])
        cus_password_txt.pack()

        cus_payment = LabelFrame(profile_frame, text='Payment Method', font=text_font)
        cus_payment.place(x=300, y=550)

        cus_payment_combo = ttk.Combobox(cus_payment, font=text_font, width=18)
        cus_payment_combo['values'] = ('Cash', 'Online')
        cus_payment_combo.insert(0, Global.currentUser[6])
        cus_payment_combo.pack()

        def editCustomer():
            customer1 = Customer(fullname=cus_fullname_txt.get(), address=cus_address_txt.get(), email=cus_email_txt.get(),
                                 number=cus_number_txt.get(), payment=cus_payment_combo.get(), cid=Global.currentUser[0])
            ecustomer = editCus(customer1)
            if ecustomer == True:
                msg1 = messagebox.showinfo(
                    "Taxi Booking System", "Customer Edit Successful")
            else:
                msg2 = messagebox.showerror(
                    "Taxi Booking System", "Error Occurred!")

        update_btn = Button(profile_frame, text='UPDATE', relief=RAISED, bd=4, font=text_font, bg='#4CD964', command=editCustomer)
        update_btn.place(x=800, y=370)






if __name__ == '__main__':
    root = Tk()
    CusDashboard(root)
    root.mainloop()
