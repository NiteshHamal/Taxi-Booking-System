from tkinter import *
from tkinter import ttk, messagebox

from backend.customerManagement import customerManage, customerSearch, editCus
from middleware.customer import Customer
from backend.customerManagement import register


class CustomerCRUD:

    def __init__(self, root):
        self.root = root
        self.root.title("Customer Management")
        frame_width = 1000
        frame_height = 550
        root.resizable(0, 0)
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (frame_width / 2))
        y_cordinate = int((screen_height / 2) - (frame_height / 2))
        root.geometry("{}x{}+{}+{}".format(frame_width,
                      frame_height, x_cordinate + 120, y_cordinate))

        font = ('Times New Roman', 16, 'normal')

        upframe = Frame(self.root, height=70, bg="#4CD964")
        upframe.pack(side=TOP, fill=BOTH)

        searchlbl = Label(upframe, text="Search: ", bg="#4CD964", font=font)
        searchlbl.place(x=20, y=25)

        searchtxt = Entry(upframe, bg="#4CD964", font=font)
        searchtxt.place(x=100, y=25)

        # function to search customer -----------------------------------------------------------------
        def searchCus():
            treeview.delete(*treeview.get_children())
            customertest = searchtxt.get()
            testname = customerSearch(customertest)
            for row in testname:
                treeview.insert(parent='', index='end', values=(
                    row[0], row[1], row[2], row[3], row[4], row[5]))

        searchbtn = Button(upframe, text=" Search ",
                           font=font, width=10, command=searchCus)
        searchbtn.place(x=340, y=18)

        formframe = Frame(self.root, height=180)
        formframe.pack(side=TOP, fill=BOTH)

        cidtxt = Entry()

        namelabel = Label(formframe, text="Name: ", font=font)
        namelabel.place(x=20, y=20)

        nametxt = Entry(formframe, font=font)
        nametxt.place(x=120, y=20)

        emaillbl = Label(formframe, text="Email: ", font=font)
        emaillbl.place(x=20, y=70)

        emailtxt = Entry(formframe, font=font)
        emailtxt.place(x=120, y=70)

        mobilelbl = Label(formframe, text="Mobile: ", font=font)
        mobilelbl.place(x=20, y=120)

        mobiletxt = Entry(formframe, font=font)
        mobiletxt.place(x=120, y=120)

        # ------------------------------------Second Column------------------------------------

        addresslbl = Label(formframe, text="Address: ", font=font)
        addresslbl.place(x=370, y=20)

        addresstxt = Entry(formframe, font=font)
        addresstxt.place(x=470, y=20)

        passwordlbl = Label(formframe, text="Password: ", font=font)
        passwordlbl.place(x=370, y=70)

        passwordtxt = Entry(formframe, font=font)
        passwordtxt.place(x=470, y=70)

        paymentlabel = Label(formframe, text="Payment: ", font=font)
        paymentlabel.place(x=370, y=120)

        data = ['Cash', 'Online']

        paymentcombo = ttk.Combobox(formframe, values=data, font=font)
        paymentcombo.place(x=470, y=120)

        # function to add new customers ------------------------------------------------------------------
        def addCustomer():
            if (nametxt.get() == '') or (addresstxt.get() == '') or (emailtxt.get() == '') or (passwordtxt.get() == '') or (mobiletxt.get() == '') or (paymentcombo.get() == ''):
                messagebox.showerror("Error", "Please Fill All The Fields")
            else:
                customer = Customer(fullname=nametxt.get(), address=addresstxt.get(), email=emailtxt.get(),
                                    number=mobiletxt.get(), password=passwordtxt.get(), payment=paymentcombo.get())
                result = register(customer)
                if result == True:
                    msg1 = messagebox.showinfo(
                        "Taxi Booking System", "Customer Registration Successful")
                    treeview.delete(*treeview.get_children())
                    customerValue()
                else:
                    msg2 = messagebox.showerror(
                        "Taxi Booking System", "Error Occurred!")

        savebtn = Button(formframe, text="  Save Record  ",
                         bg="#4CD964", font=font, command=addCustomer)
        savebtn.place(x=780, y=20)

        # function to edit or to update customer--------------------------------------------------------
        def editCustomer():
            if (nametxt.get() == '') or (addresstxt.get() == '') or (emailtxt.get() == '') or (mobiletxt.get() == '') or (paymentcombo.get() == ''):
                messagebox.showerror(
                    "Error", "Please Fill All The Fields Execpt Password Field")
            else:
                customer1 = Customer(fullname=nametxt.get(), address=addresstxt.get(), email=emailtxt.get(),
                                     number=mobiletxt.get(), payment=paymentcombo.get(), cid=cidtxt.get())
                ecustomer = editCus(customer1)
                if ecustomer == True:
                    msg1 = messagebox.showinfo(
                        "Taxi Booking System", "Customer Edit Successful")
                    treeview.delete(*treeview.get_children())
                    customerValue()
                else:
                    msg2 = messagebox.showerror(
                        "Taxi Booking System", "Error Occurred!")

        updatebtn = Button(formframe, text="Update Record",
                           bg="#4CD964", font=font, command=editCustomer)
        updatebtn.place(x=780, y=70)

        # function to clear all field -----------------------------------------------------------------
        def clearallfield():
            cidtxt.delete(0, END)
            nametxt.delete(0, END)
            addresstxt.delete(0, END)
            emailtxt.delete(0, END)
            mobiletxt.delete(0, END)
            passwordtxt.delete(0, END)
            paymentcombo.delete(0, END)
            searchtxt.delete(0, END)
            treeview.delete(*treeview.get_children())
            customerValue()

        clearbtn = Button(formframe, text="   Clear Field   ",
                          bg="#4CD964", font=font, command=clearallfield)
        clearbtn.place(x=780, y=120)

        # table ------------------------------------------------------------------------------

        treeview = ttk.Treeview(self.root)
        treeview.pack(side=BOTTOM, fill=BOTH, expand=TRUE)

        treeview['columns'] = ('cid', 'name', 'address',
                               'email', 'number', 'payment')
        treeview.column('#0', width=0, stretch=0)
        treeview.column('cid', width=100, anchor=CENTER)
        treeview.column('name', width=100, anchor=CENTER)
        treeview.column('address', width=100, anchor=CENTER)
        treeview.column('email', width=100, anchor=CENTER)
        treeview.column('number', width=100, anchor=CENTER)
        treeview.column('payment', width=100, anchor=CENTER)

        treeview.heading('#0', text='', anchor=CENTER)
        treeview.heading('cid', text='Customer ID', anchor=CENTER)
        treeview.heading('name', text='Name', anchor=CENTER)
        treeview.heading('address', text='Address', anchor=CENTER)
        treeview.heading('email', text='Email', anchor=CENTER)
        treeview.heading('number', text='Mobile No', anchor=CENTER)
        treeview.heading('payment', text='Payment', anchor=CENTER)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="white",
                        bordercolor="#343638",
                        borderwidth=0,
                        font=('Times New Roman', 14))
        style.map('Treeview', background=[('selected', '#22559b')])

        style.configure("Treeview.Heading",
                        background="#565b5e",
                        foreground="white",
                        relief="flat",
                        font=('Times New Roman', 14))
        style.map("Treeview.Heading",
                  background=[('active', '#3484F0')], )

        # function to show values in customer Table -------------------------------------------------
        def customerValue():
            customertable = customerManage()
            for row in customertable:
                treeview.insert(parent='', index='end', values=(
                    row[0], row[1], row[2], row[3], row[4], row[5]))

        customerValue()

        def selectcustomertable(a):
            cidtxt.delete(0, END)
            nametxt.delete(0, END)
            addresstxt.delete(0, END)
            emailtxt.delete(0, END)
            mobiletxt.delete(0, END)
            passwordtxt.delete(0, END)
            paymentcombo.delete(0, END)

            selectitem = treeview.selection()[0]
            cidtxt.insert(0, treeview.item(selectitem)['values'][0])
            nametxt.insert(0, treeview.item(selectitem)['values'][1])
            addresstxt.insert(0, treeview.item(selectitem)['values'][2])
            emailtxt.insert(0, treeview.item(selectitem)['values'][3])
            mobiletxt.insert(0, treeview.item(selectitem)['values'][4])
            paymentcombo.insert(0, treeview.item(selectitem)['values'][5])

        treeview.bind('<<TreeviewSelect>>', selectcustomertable)


