from tkinter import *
from tkinter import ttk, messagebox

from backend.driverManagement import driverManage, editDri, add, driverSearch
from middleware.driver import Driver


class DriverCRUD:

    def __init__(self, root):
        self.root = root
        self.root.title("Driver Management")
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
        def searchDri():
            treeview.delete(*treeview.get_children())
            drivertest = searchtxt.get()
            sdriver = driverSearch(drivertest)
            for row in sdriver:
                treeview.insert(parent='', index='end', values=(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

        searchbtn = Button(upframe, text=" Search ",
                           font=font, width=10, command=searchDri)
        searchbtn.place(x=340, y=18)

        formframe = Frame(self.root, height=180)
        formframe.pack(side=TOP, fill=BOTH)

        didtxt = Entry()

        namelabel = Label(formframe, text="Name: ", font=font)
        namelabel.place(x=20, y=20)

        nametxt = Entry(formframe, font=font)
        nametxt.place(x=120, y=20)

        emaillbl = Label(formframe, text="Email: ", font=font)
        emaillbl.place(x=20, y=70)

        emailtxt = Entry(formframe, font=font)
        emailtxt.place(x=120, y=70)

        licenselbl = Label(formframe, text="License.no: ", font=font)
        licenselbl.place(x=20, y=120)

        licensetxt = Entry(formframe, font=font)
        licensetxt.place(x=120, y=120)

        # ------------------------------------Second Column------------------------------------

        addresslbl = Label(formframe, text="Address: ", font=font)
        addresslbl.place(x=370, y=20)

        addresstxt = Entry(formframe, font=font)
        addresstxt.place(x=470, y=20)

        passwordlbl = Label(formframe, text="Password: ", font=font)
        passwordlbl.place(x=370, y=70)

        passwordtxt = Entry(formframe, font=font)
        passwordtxt.place(x=470, y=70)

        # function to add new driver ------------------------------------------------------------------
        def addDriver():
            if (nametxt.get() == '') or (emailtxt.get() == '') or (addresstxt.get() == '') or (licensetxt.get() == '') or (passwordtxt.get() == ''):
                messagebox.showerror("Error", 'Please Fill All The Fields')
            else:
                driver = Driver(did='', fullname=nametxt.get(), address=addresstxt.get(
                ), email=emailtxt.get(), licenseno=licensetxt.get(), password=passwordtxt.get(), status="Active")
                result = add(driver)
                if result == True:
                    msg1 = messagebox.showinfo(
                        "Taxi Booking System", "Driver Added Successfully!")
                    treeview.delete(*treeview.get_children())
                    driverValue()
                else:
                    msg2 = messagebox.showinfo(
                        "Taxi Booking System", "Error Occurred!")

        savebtn = Button(formframe, text="  Save Record  ",
                         bg="#4CD964", font=font, command=addDriver)
        savebtn.place(x=780, y=20)

        # function to edit or to update driver--------------------------------------------------------
        def editDriver():
            if (nametxt.get() == '') or (addresstxt.get() == '') or (emailtxt.get() == '') or (licensetxt.get() == ''):
                messagebox.showerror(
                    "Error", "Please Fill All The Fields Execpt Password Field")
            else:
                driver1 = Driver(fullname=nametxt.get(), address=addresstxt.get(), email=emailtxt.get(),
                                 licenseno=licensetxt.get(),  did=didtxt.get())
            edriver = editDri(driver1)
            if edriver == True:
                msg1 = messagebox.showinfo(
                    "Taxi Booking System", "Driver Edit Successful")
                treeview.delete(*treeview.get_children())
                driverValue()
            else:
                msg2 = messagebox.showerror(
                    "Taxi Booking System", "Error Occurred!")

        updatebtn = Button(formframe, text="Update Record",
                           bg="#4CD964", font=font, command=editDriver)
        updatebtn.place(x=780, y=70)

        # function to clear all field -----------------------------------------------------------------
        def clearallfield():
            didtxt.delete(0, END)
            nametxt.delete(0, END)
            addresstxt.delete(0, END)
            emailtxt.delete(0, END)
            licensetxt.delete(0, END)
            passwordtxt.delete(0, END)
            searchtxt.delete(0, END)
            treeview.delete(*treeview.get_children())
            driverValue()

        clearbtn = Button(formframe, text="   Clear Field   ",
                          bg="#4CD964", font=font, command=clearallfield)
        clearbtn.place(x=780, y=120)

        # table ------------------------------------------------------------------------------

        treeview = ttk.Treeview(self.root)
        treeview.pack(side=BOTTOM, fill=BOTH, expand=TRUE)

        treeview['columns'] = ('did', 'fullname', 'address',
                               'email', 'licenseno', 'status')
        treeview.column('#0', width=0, stretch=0)
        treeview.column('did', width=100, anchor=CENTER)
        treeview.column('fullname', width=100, anchor=CENTER)
        treeview.column('address', width=100, anchor=CENTER)
        treeview.column('email', width=100, anchor=CENTER)
        treeview.column('licenseno', width=100, anchor=CENTER)
        treeview.column('status', width=100, anchor=CENTER)

        treeview.heading('#0', text='', anchor=CENTER)
        treeview.heading('did', text='Customer ID', anchor=CENTER)
        treeview.heading('fullname', text='Name', anchor=CENTER)
        treeview.heading('address', text='Address', anchor=CENTER)
        treeview.heading('email', text='Email', anchor=CENTER)
        treeview.heading('licenseno', text='License No', anchor=CENTER)
        treeview.heading('status', text='Payment', anchor=CENTER)

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

        # function to show values in driver Table -------------------------------------------------
        def driverValue():
            drivertable = driverManage()
            for row in drivertable:
                treeview.insert(parent='', index='end', values=(
                    row[0], row[1], row[2], row[3], row[4], row[5]))

        driverValue()

        def selectdriverTable(a):
            didtxt.delete(0, END)
            nametxt.delete(0, END)
            addresstxt.delete(0, END)
            emailtxt.delete(0, END)
            licensetxt.delete(0, END)
            passwordtxt.delete(0, END)
            searchtxt.delete(0, END)

            selectitem1 = treeview.selection()[0]
            didtxt.insert(0, treeview.item(selectitem1)['values'][0])
            nametxt.insert(0, treeview.item(selectitem1)['values'][1])
            addresstxt.insert(0, treeview.item(selectitem1)['values'][2])
            emailtxt.insert(0, treeview.item(selectitem1)['values'][3])
            licensetxt.insert(
                0, treeview.item(selectitem1)['values'][4])

        treeview.bind('<<TreeviewSelect>>', selectdriverTable)


