import tkinter
from tkinter import *
from tkinter import messagebox, ttk

from PIL import ImageTk, Image

from middleware.booking import Booking
from middleware.driver import Driver
from backend.driverManagement import *
from backend.customerManagement import *
from backend.bookingManagement import *
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

        # font used in the button in navbar
        nav_font = ('Times New Roman', 25, "bold")
        reg_font = ('Cordia New', 14)

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

        # first frame / navbar
        navbar = Frame(self.root, bg="#4CD964", width=350)
        navbar.pack(side=LEFT, fill=BOTH)

        # image
        profile = ImageTk.PhotoImage(Image.open(
            "H:\\College\\Sem-2\\python assignment\\Taxi Booking System\\image\\profile.png"))
        profile_label = Label(navbar, image=profile, bg="#4CD964")
        profile_label.image = profile
        profile_label.place(x=100, y=50)

        def change_home():  # function for home button
            home_frame.pack(side=RIGHT, fill=BOTH, expand=TRUE)
            driver.pack_forget()
            customer.pack_forget()

        # home button
        home_btn = Button(navbar, text="Home", command=change_home,
                          font=nav_font, bg="#4CD964", relief=RIDGE)
        home_btn.place(x=110, y=210)

        def change_driver():  # function for driver management button
            driver.pack(side=RIGHT, fill=BOTH, expand=TRUE)
            home_frame.pack_forget()
            customer.pack_forget()

        # driver manage button
        driver_button = Button(navbar, text="Manage Driver",
                               command=change_driver, font=nav_font, bg="#4CD964", relief=RIDGE)
        driver_button.place(x=50, y=300)

        def change_customer():  # function for customer management button
            customer.pack(side=RIGHT, fill=BOTH, expand=TRUE)
            driver.pack_forget()
            home_frame.pack_forget()

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

        daddress_txt1 = Entry(daddress_label, text='', font=reg_font)
        daddress_txt1.pack()

        date_label = LabelFrame(home_frame, text="Pickup Date", font=reg_font)
        date_label.place(x=10, y=120)

        date_txt = Entry(date_label, text='', font=reg_font)
        date_txt.pack()

        time_label = LabelFrame(home_frame, text="Pickup Time", font=reg_font)
        time_label.place(x=310, y=120)

        time_txt = Entry(time_label, text='', font=reg_font)
        time_txt.pack()

        driver_label = LabelFrame(
            home_frame, text='Assign Driver', font=reg_font)
        driver_label.place(x=610, y=120)

        driver_txt = Entry(driver_label, text='', font=reg_font)
        driver_txt.pack()

        def drivercheck():
            app = tkinter.Toplevel()
            app.title("Check Driver")
            app.resizable(False, False)  # windows resizable false
            app.config(background="#CECED2")  # background color change
            width = 550
            height = 500
            screenwidth = app.winfo_screenwidth()
            screenheight = app.winfo_screenheight()

            xCordinate = int((screenwidth/2)-(width/2))
            yCordinate = int((screenheight/2)-(height/2))

            app.geometry('{}x{}+{}+{}'.format(width,
                         height, xCordinate, yCordinate))

            checktable = ttk.Treeview(app, height=25)
            checktable['columns'] = ('did', 'fullname', 'address')
            checktable.column('#0', width=0, stretch=0)
            checktable.column('did', width=100, anchor=CENTER)
            checktable.column('fullname', width=100, anchor=CENTER)
            checktable.column('address', width=100, anchor=CENTER)

            checktable.heading('#0', text='', anchor=CENTER)
            checktable.heading('did', text='Driver ID', anchor=CENTER)
            checktable.heading('fullname', text='Full Name', anchor=CENTER)
            checktable.heading('address', text='Address', anchor=CENTER)
            checktable.pack(fill=BOTH)

            def checkdriver():
                driverad = drivertablead()
                for row1 in driverad:
                    checktable.insert(parent='', index='end',
                                      values=(row1[0], row1[1], row1[2]))
            checkdriver()

            def getselecteddriver(nitesh):
                driver_txt.delete(0, END)
                itemselect720 = checktable.selection()[0]
                driver_txt.insert(0, checktable.item(
                    itemselect720)['values'][0])

            checktable.bind('<<TreeviewSelect>>', getselecteddriver)

        check_btn = Button(home_frame, command=drivercheck,
                           text="Check Driver", font=reg_font, relief=RAISED, bd=5)
        check_btn.place(x=800, y=250)

        def confirm_booking():

            if driver_txt.get() == '':
                messagebox.showwarning("TBS", "Please enter driver ID")

            else:
                booking = Booking(bookingid=bid_txt.get(),
                                  did=driver_txt.get(), status='Confirmed')
                updateResult = admin_update_booking(booking)
                driver = Driver(did=driver_txt.get(), status="Inactive")
                result = statusUpdate(driver)
                driver_txt.delete(0, END)
            if updateResult == True:
                messagebox.showinfo("TBS", "The booking is confirmed")
                requestTable.delete(*requestTable.get_children())
                requesttable()

            else:
                messagebox.showerror("TBS", "Error")

        confirm_btn = Button(home_frame, text="Confirm Booking",
                             command=confirm_booking, font=reg_font, relief=RAISED, bd=5)
        confirm_btn.place(x=980, y=250)

        aid_txt = Entry(home_frame)
        # aid_txt.insert(0, Global.currentUser[0])------------------------------------------------------------------------------------------------------------------------------------------------------

        #  adding request table in home_frame ----------------------------------------------------
        requestTable = ttk.Treeview(home_frame, height=18)
        requestTable['columns'] = (
            'bid', 'cid', 'fullname', 'paddress', 'daddress', 'pdate', 'ptime', 'status')
        requestTable.column('#0', width=0, stretch=0)
        requestTable.column('bid', width=0, stretch=0)
        requestTable.column('cid', width=50, anchor=CENTER)
        requestTable.column('fullname', width=100, anchor=CENTER)
        requestTable.column('paddress', width=100, anchor=CENTER)
        requestTable.column('daddress', width=100, anchor=CENTER)
        requestTable.column('pdate', width=100, anchor=CENTER)
        requestTable.column('ptime', width=100, anchor=CENTER)
        requestTable.column('status', width=100, anchor=CENTER)

        requestTable.heading('#0', text='', anchor=CENTER)
        requestTable.heading('bid', text='', anchor=CENTER)
        requestTable.heading('cid', text='Customer ID', anchor=CENTER)
        requestTable.heading('fullname', text='Fullname', anchor=CENTER)
        requestTable.heading('paddress', text='Pickup Address', anchor=CENTER)
        requestTable.heading('daddress', text='Drop Address', anchor=CENTER)
        requestTable.heading('pdate', text='Pickup Date', anchor=CENTER)
        requestTable.heading('ptime', text='Pickup Time', anchor=CENTER)
        requestTable.heading('status', text='Booking Status', anchor=CENTER)

        requestTable.pack(side=BOTTOM, fill=BOTH)

        # function to show values in request table ------------------------------------------------
        def requesttable():
            request = requestBooking1167()
            for row in request:
                requestTable.insert(parent='', index='end', values=(
                    row[1], row[0], row[2], row[3], row[4], row[5], row[6], row[7]))

        requesttable()

        def getbookingtabledata(a):
            bid_txt.delete(0, END)
            name_txt.delete(0, END)
            paddress_txt.delete(0, END)
            daddress_txt1.delete(0, END)
            date_txt.delete(0, END)
            time_txt.delete(0, END)

            itemselect11 = requestTable.selection()[0]

            bid_txt.insert(0, requestTable.item(itemselect11)['values'][0])
            name_txt.insert(0, requestTable.item(itemselect11)['values'][2])
            paddress_txt.insert(0, requestTable.item(
                itemselect11)['values'][3])
            daddress_txt1.insert(
                0, requestTable.item(itemselect11)['values'][4])
            date_txt.insert(0, requestTable.item(itemselect11)['values'][5])
            time_txt.insert(0, requestTable.item(itemselect11)['values'][6])

        requestTable.bind('<<TreeviewSelect>>', getbookingtabledata)

        # driver management frame --------------------------------------------------------------------
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

        dsearch_frame = LabelFrame(driver, text='Search Driver', font=reg_font)
        dsearch_frame.place(x=10, y=240)

        dsearch_txt = Entry(dsearch_frame, text='', font=reg_font)
        dsearch_txt.pack()

        did_txt = Entry(driver)

        # function for add button to add driver ----------------------------------------------------

        def addDriver():
            driver = Driver(did='', fullname=dname_txt.get(), address=daddress_txt.get(
            ), email=demail_txt.get(), licenseno=dlicenseno_txt.get(), password=dpassword_txt.get(), status="Active")
            result = add(driver)
            if result == True:
                msg1 = messagebox.showinfo(
                    "Taxi Booking System", "Driver Added Successfully!")
                driverTable.delete(*driverTable.get_children())
                searchDri()
            else:
                msg2 = messagebox.showinfo(
                    "Taxi Booking System", "Error Occurred!")

        dadd_btn = Button(driver, text='    ADD   ', font=reg_font,
                          relief=RAISED, bd=5, command=addDriver)
        dadd_btn.place(x=310, y=125)

        def editDriver():
            driver1 = Driver(fullname=dname_txt.get(), address=daddress_txt.get(), email=demail_txt.get(),
                             licenseno=dlicenseno_txt.get(),  did=did_txt.get())
            edriver = editDri(driver1)
            if edriver == True:
                msg1 = messagebox.showinfo(
                    "Taxi Booking System", "Driver Edit Successful")
                driverTable.delete(*driverTable.get_children())
                searchDri()
            else:
                msg2 = messagebox.showerror(
                    "Taxi Booking System", "Error Occurred!")

        dupdate_btn = Button(driver, text='UPDATE',
                             font=reg_font, relief=RAISED, bd=5, command=editDriver)
        dupdate_btn.place(x=470, y=125)

        def deleteDriver():
            driver2 = Driver(did=did_txt.get())
            ddriver = deleteDri(driver2)
            if ddriver == True:
                msg1 = messagebox.showinfo(
                    "Taxi Booking System", "Driver Delete Successful")
                driverTable.delete(*driverTable.get_children())
                searchDri()
            else:
                msg2 = messagebox.showerror(
                    "Taxi Booking System", "Error Occurred!")

        ddelete_btn = Button(driver, text='DELETE',
                             font=reg_font, relief=RAISED, bd=5, command=deleteDriver)
        ddelete_btn.place(x=630, y=125)

        def searchDri():
            driverTable.delete(*driverTable.get_children())
            drivertest = dsearch_txt.get()
            sdriver = driverSearch(drivertest)
            for row in sdriver:
                driverTable.insert(parent='', index='end', values=(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

        dsearch_btn = Button(driver, text='SEARCH',
                             font=reg_font, relief=RAISED, bd=5, command=searchDri)
        dsearch_btn.place(x=310, y=250)

        def clearDri():
            did_txt.delete(0, END)
            dname_txt.delete(0, END)
            daddress_txt.delete(0, END)
            demail_txt.delete(0, END)
            dlicenseno_txt.delete(0, END)
            dpassword_txt.delete(0, END)

        dclear_btn = Button(driver, text='CLEAR',
                            font=reg_font, relief=RAISED, bd=5, command=clearDri)
        dclear_btn.place(x=470, y=250)

        # adding driver Info table in driver frame ------------------------------------------------
        driverTable = ttk.Treeview(driver, height=18)
        driverTable['columns'] = (
            'did', 'fullname', 'address', 'email', 'licenseno', 'status')
        driverTable.column('#0', width=0, stretch=0)
        driverTable.column('did', width=50, anchor=CENTER)
        driverTable.column('fullname', width=100, anchor=CENTER)
        driverTable.column('address', width=100, anchor=CENTER)
        driverTable.column('email', width=100, anchor=CENTER)
        driverTable.column('licenseno', width=100, anchor=CENTER)
        driverTable.column('status', width=100, anchor=CENTER)

        driverTable.heading('#0', text='', anchor=CENTER)
        driverTable.heading('did', text='Driver ID', anchor=CENTER)
        driverTable.heading('fullname', text='Fullname', anchor=CENTER)
        driverTable.heading('address', text='Address', anchor=CENTER)
        driverTable.heading('email', text='Email', anchor=CENTER)
        driverTable.heading('licenseno', text='License No', anchor=CENTER)
        driverTable.heading('status', text='Status', anchor=CENTER)

        driverTable.pack(side=BOTTOM, fill=BOTH)

        # function to show values in driver Table -------------------------------------------------
        def driverValue():
            drivertable = driverManage()
            for row in drivertable:
                driverTable.insert(parent='', index='end', values=(
                    row[0], row[1], row[2], row[3], row[4], row[5]))
        driverValue()

        def selectdriverTable(a):
            did_txt.delete(0, END)
            dname_txt.delete(0, END)
            daddress_txt.delete(0, END)
            demail_txt.delete(0, END)
            dlicenseno_txt.delete(0, END)

            selectitem1 = driverTable.selection()[0]
            did_txt.insert(0, driverTable.item(selectitem1)['values'][0])
            dname_txt.insert(0, driverTable.item(selectitem1)['values'][1])
            daddress_txt.insert(0, driverTable.item(selectitem1)['values'][2])
            demail_txt.insert(0, driverTable.item(selectitem1)['values'][3])
            dlicenseno_txt.insert(
                0, driverTable.item(selectitem1)['values'][4])

        driverTable.bind('<<TreeviewSelect>>', selectdriverTable)

        # customer management frame---------------------------------------------------------------------------------------------------------
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

        searchcuslbl = LabelFrame(
            customer, text='Search Customer', font=reg_font)
        searchcuslbl.place(x=10, y=240)

        searchcustxt = Entry(searchcuslbl, text='', font=reg_font)
        searchcustxt.pack()

        cid_txt = Entry(customer, text='')

        def addCustomer():
            customer = Customer(fullname=cname_txt.get(), address=caddress_txt.get(), email=cemail_txt.get(),
                                number=cphoneno_txt.get(), password=cpassword_txt.get(), payment=cpayment.get())
            result = register(customer)
            if result == True:
                msg1 = messagebox.showinfo(
                    "Taxi Booking System", "Customer Registration Successful")
                customerTable.delete(*customerTable.get_children())
                customerValue()

            else:
                msg2 = messagebox.showerror(
                    "Taxi Booking System", "Error Occurred!")

        cadd_btn = Button(customer, text='    ADD   ', font=reg_font,
                          relief=RAISED, bd=5, command=addCustomer)
        cadd_btn.place(x=590, y=125)

        def editCustomer():
            customer1 = Customer(fullname=cname_txt.get(), address=caddress_txt.get(), email=cemail_txt.get(),
                                 number=cphoneno_txt.get(), payment=cpayment.get(), cid=cid_txt.get())
            ecustomer = editCus(customer1)
            if ecustomer == True:
                msg1 = messagebox.showinfo(
                    "Taxi Booking System", "Customer Edit Successful")
                customerTable.delete(*customerTable.get_children())
                customerValue()
            else:
                msg2 = messagebox.showerror(
                    "Taxi Booking System", "Error Occurred!")

        cupdate_btn = Button(customer, text='UPDATE',
                             font=reg_font, relief=RAISED, bd=5, command=editCustomer)
        cupdate_btn.place(x=750, y=125)

        def deleteCustomer():
            customer2 = Customer(cid=cid_txt.get())
            dcustomer = deleteCus(customer2)
            if dcustomer == True:
                msg1 = messagebox.showinfo(
                    "Taxi Booking System", "Customer Delete Successful")
                customerTable.delete(*customerTable.get_children())
                customerValue()
            else:
                msg2 = messagebox.showerror(
                    "Taxi Booking System", "Error Occurred!")

        cdelete_btn = Button(customer, text='DELETE',
                             font=reg_font, relief=RAISED, bd=5, command=deleteCustomer)
        cdelete_btn.place(x=910, y=125)

        def searchCus():
            customerTable.delete(*customerTable.get_children())
            customertest = searchcustxt.get()
            testname = customerSearch(customertest)
            for row in testname:
                customerTable.insert(parent='', index='end', values=(
                    row[0], row[1], row[2], row[3], row[4], row[5]))

        csearch_btn = Button(customer, text='SEARCH',
                             font=reg_font, relief=RAISED, bd=5, command=searchCus)
        csearch_btn.place(x=310, y=245)

        customerTable = ttk.Treeview(customer, height=18)
        customerTable['columns'] = (
            'cid', 'fullname', 'address', 'email', 'number', 'payment')
        customerTable.column('#0', width=0, stretch=0)
        customerTable.column('cid', width=50, anchor=CENTER)
        customerTable.column('fullname', width=100, anchor=CENTER)
        customerTable.column('address', width=100, anchor=CENTER)
        customerTable.column('email', width=100, anchor=CENTER)
        customerTable.column('number', width=100, anchor=CENTER)
        customerTable.column('payment', width=100, anchor=CENTER)

        customerTable.heading('#0', text='', anchor=CENTER)
        customerTable.heading('cid', text='Customer ID', anchor=CENTER)
        customerTable.heading('fullname', text='Fullname', anchor=CENTER)
        customerTable.heading('address', text='Address', anchor=CENTER)
        customerTable.heading('email', text='Email', anchor=CENTER)
        customerTable.heading('number', text='Phone No', anchor=CENTER)
        customerTable.heading('payment', text='Payment', anchor=CENTER)

        customerTable.pack(side=BOTTOM, fill=BOTH)

        # function to show values in customer Table -------------------------------------------------
        def customerValue():
            customertable = customerManage()
            for row in customertable:
                customerTable.insert(parent='', index='end', values=(
                    row[0], row[1], row[2], row[3], row[4], row[5]))
        customerValue()

        def selectcustomertable(a):
            cid_txt.delete(0, END)
            cname_txt.delete(0, END)
            caddress_txt.delete(0, END)
            cemail_txt.delete(0, END)
            cphoneno_txt.delete(0, END)
            cpassword_txt.delete(0, END)
            cpayment.delete(0, END)

            selectitem = customerTable.selection()[0]
            cid_txt.insert(0, customerTable.item(selectitem)['values'][0])
            cname_txt.insert(0, customerTable.item(selectitem)['values'][1])
            caddress_txt.insert(0, customerTable.item(selectitem)['values'][2])
            cemail_txt.insert(0, customerTable.item(selectitem)['values'][3])
            cphoneno_txt.insert(0, customerTable.item(selectitem)['values'][4])
            cpayment.insert(0, customerTable.item(selectitem)['values'][5])

        customerTable.bind('<<TreeviewSelect>>', selectcustomertable)


if __name__ == '__main__':
    root = Tk()
    AdminDashboard(root)
    root.mainloop()
