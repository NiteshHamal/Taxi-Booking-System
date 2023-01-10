import sys
import tkinter
from datetime import date
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
from backend.bookingManagement import insert, cusdastable, customerbookinghistory_table, cancelreqBooking, \
    customer_edit_booking
from backend.customerManagement import customer_change_password, editCus
from backend.validation import namevalidation, emailvalidation, numbervalidation, passwordvalidation, \
    timevalidation
from frontend import signin
from middleware import Global
from middleware.booking import Booking
from middleware.customer import Customer


class CustomerDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Dashboard")
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        self.root.minsize(screenwidth, screenheight)
        self.root.state('zoomed')

        # font
        sidefont = ('Times New Roman', 15, 'normal')

        bookingid = Entry(self.root, text="", font=sidefont)
        cid_txt = Entry(self.root)
        cid_txt.insert(0, Global.currentUser[0])

        # -----------------------------------Top Frame---------------------------------------------
        upframe = Frame(self.root, height=100, bg="#4CD964")
        upframe.pack(side=TOP, fill=BOTH)

        # -----------------------------------------Top frame title label----------------------------------------
        titlelabel = Label(self.root, text="Welcome {}".format(
            Global.currentUser[1]), bg="#4CD964", font=('Times New Roman', 25, 'bold'))
        titlelabel.place(x=20, y=30)

        # ----------------------------------Side Frame-------------------------------------------------
        sideframe = Frame(self.root, width=350, bg='#e2f3f5')
        sideframe.pack(side=LEFT, fill=BOTH)

        # --------------------------------------Side Frame Image--------------------------------------------
        image = Image.open(
            "H:\\College\\Sem-2\\python assignment\\Taxi Booking System\\image\\Order ride-bro.png")
        image = image.resize((250, 250))
        image = ImageTk.PhotoImage(image)
        Image_Label = Label(sideframe, image=image, bg='#e2f3f5')
        Image_Label.image = image
        Image_Label.place(x=60, y=20)

        # ---------------------------------Side Title Label--------------------------------------------
        titlelbl = Label(sideframe, text="Taxi Booking System",
                         bg='#e2f3f5', font=('Times New Roman', 16, 'bold'))
        titlelbl.place(x=90, y=270)

        def profile_gui():
            updateprofile = tkinter.Toplevel()
            updateprofile.title("Profile")
            updateprofile.resizable(False, False)
            updateprofile.config(background='#e2f3f5')
            width = 670
            height = 400
            screenwidth = updateprofile.winfo_screenwidth()
            screenheight = updateprofile.winfo_screenheight()
            xCordinate = int((screenwidth / 2) - (width / 2))
            yCordinate = int((screenheight / 2) - (height / 2))
            updateprofile.geometry('{}x{}+{}+{}'.format(width,
                                                        height, xCordinate, yCordinate))

            # image
            profile = ImageTk.PhotoImage(Image.open(
                "H:\\College\\Sem-2\\python assignment\\Taxi Booking System\\image\\profile.png"))
            profile_label = Label(updateprofile, image=profile, bg="#e2f3f5")
            profile_label.image = profile
            profile_label.place(x=270, y=20)

            # widgets on profile Top level

            # right column---------------------------------------------

            # label-------------

            profile_cid_lbl = Label(
                updateprofile, text='ID No: ', bg='#e2f3f5', font=('Times New Roman', 14))
            profile_cid_lbl.place(x=20, y=200)

            profile_address_lbl = Label(
                updateprofile, text='Address: ', bg='#e2f3f5', font=('Times New Roman', 14))
            profile_address_lbl.place(x=20, y=250)

            profile_number_lbl = Label(
                updateprofile, text='Number: ', bg='#e2f3f5', font=('Times New Roman', 14))
            profile_number_lbl.place(x=20, y=300)

            # entry--------------
            profile_cid_txt = Entry(
                updateprofile, font=('Times New Roman', 14))
            profile_cid_txt.insert(0, Global.currentUser[0])
            profile_cid_txt.bind("<Key>", lambda e: "break")
            profile_cid_txt.bind("<Button-1>", lambda e: "break")
            profile_cid_txt.place(x=100, y=200)

            profile_address_txt = Entry(
                updateprofile, font=('Times New Roman', 14))
            profile_address_txt.insert(0, Global.currentUser[2])
            profile_address_txt.bind("<Key>", lambda e: "break")
            profile_address_txt.bind("<Button-1>", lambda e: "break")
            profile_address_txt.place(x=100, y=250)

            profile_number_txt = Entry(
                updateprofile, font=('Times New Roman', 14))
            profile_number_txt.insert(0, Global.currentUser[4])
            profile_number_txt.bind("<Key>", lambda e: "break")
            profile_number_txt.bind("<Button-1>", lambda e: "break")
            profile_number_txt.place(x=100, y=300)

            # left column-------------------------------------------------------------

            # label--------------------------------
            profile_name_lbl = Label(
                updateprofile, text='Name: ', bg='#e2f3f5', font=('Times New Roman', 14))
            profile_name_lbl.place(x=380, y=200)

            profile_email_lbl = Label(
                updateprofile, text='Email: ', bg='#e2f3f5', font=('Times New Roman', 14))
            profile_email_lbl.place(x=380, y=250)

            profile_payment_lbl = Label(
                updateprofile, text='Payment: ', bg='#e2f3f5', font=('Times New Roman', 14))
            profile_payment_lbl.place(x=380, y=300)

            # entry------------------------------
            profile_name_txt = Entry(
                updateprofile, font=('Times New Roman', 14))
            profile_name_txt.insert(0, Global.currentUser[1])
            profile_name_txt.bind("<Key>", lambda e: "break")
            profile_name_txt.bind("<Button-1>", lambda e: "break")
            profile_name_txt.place(x=460, y=200)

            profile_email_txt = Entry(
                updateprofile, font=('Times New Roman', 14))
            profile_email_txt.insert(0, Global.currentUser[3])
            profile_email_txt.bind("<Key>", lambda e: "break")
            profile_email_txt.bind("<Button-1>", lambda e: "break")
            profile_email_txt.place(x=460, y=250)

            profile_payment_txt = Entry(
                updateprofile, font=('Times New Roman', 14))
            profile_payment_txt.insert(0, Global.currentUser[6])
            profile_payment_txt.bind("<Key>", lambda e: "break")
            profile_payment_txt.bind("<Button-1>", lambda e: "break")
            profile_payment_txt.place(x=460, y=300)

        profilebtn = Button(sideframe, text="My Profile", font=sidefont,
                            bg='#e2f3f5', highlightthickness=0, borderwidth=0, command=profile_gui)
        profilebtn.place(x=100, y=350)

        def updateprofile_gui():
            updateprofile = tkinter.Toplevel()
            updateprofile.title("Update Profile")
            updateprofile.resizable(False, False)
            updateprofile.config(background='#e2f3f5')
            width = 670
            height = 400
            screenwidth = updateprofile.winfo_screenwidth()
            screenheight = updateprofile.winfo_screenheight()
            xCordinate = int((screenwidth / 2) - (width / 2))
            yCordinate = int((screenheight / 2) - (height / 2))
            updateprofile.geometry('{}x{}+{}+{}'.format(width,
                                                        height, xCordinate, yCordinate))

            # image
            profile = ImageTk.PhotoImage(Image.open(
                "H:\\College\\Sem-2\\python assignment\\Taxi Booking System\\image\\profile.png"))
            profile_label = Label(updateprofile, image=profile, bg="#e2f3f5")
            profile_label.image = profile
            profile_label.place(x=270, y=20)

            # widgets on updateprofile Top level

            # right column---------------------------------------------

            # label-------------

            profile_cid_lbl = Label(
                updateprofile, text='ID No: ', bg='#e2f3f5', font=('Times New Roman', 14))
            profile_cid_lbl.place(x=20, y=200)

            profile_address_lbl = Label(
                updateprofile, text='Address: ', bg='#e2f3f5', font=('Times New Roman', 14))
            profile_address_lbl.place(x=20, y=250)

            profile_number_lbl = Label(
                updateprofile, text='Number: ', bg='#e2f3f5', font=('Times New Roman', 14))
            profile_number_lbl.place(x=20, y=300)

            # entry--------------
            profile_cid_txt = Entry(
                updateprofile, font=('Times New Roman', 14))
            profile_cid_txt.insert(0, Global.currentUser[0])
            profile_cid_txt.bind("<Key>", lambda e: "break")
            profile_cid_txt.bind("<Button-1>", lambda e: "break")
            profile_cid_txt.place(x=100, y=200)

            profile_address_txt = Entry(
                updateprofile, font=('Times New Roman', 14))
            profile_address_txt.insert(0, Global.currentUser[2])
            profile_address_txt.place(x=100, y=250)

            profile_number_txt = Entry(
                updateprofile, font=('Times New Roman', 14))
            profile_number_txt.insert(0, Global.currentUser[4])
            profile_number_txt.place(x=100, y=300)

            # left column-------------------------------------------------------------

            # label--------------------------------
            profile_name_lbl = Label(
                updateprofile, text='Name: ', bg='#e2f3f5', font=('Times New Roman', 14))
            profile_name_lbl.place(x=380, y=200)

            profile_email_lbl = Label(
                updateprofile, text='Email: ', bg='#e2f3f5', font=('Times New Roman', 14))
            profile_email_lbl.place(x=380, y=250)

            profile_payment_lbl = Label(
                updateprofile, text='Payment: ', bg='#e2f3f5', font=('Times New Roman', 14))
            profile_payment_lbl.place(x=380, y=300)

            # entry------------------------------
            profile_name_txt = Entry(
                updateprofile, font=('Times New Roman', 14))
            profile_name_txt.insert(0, Global.currentUser[1])
            profile_name_txt.place(x=460, y=200)

            profile_email_txt = Entry(
                updateprofile, font=('Times New Roman', 14))
            profile_email_txt.insert(0, Global.currentUser[3])
            profile_email_txt.place(x=460, y=250)

            profile_payment_txt = ttk.Combobox(
                updateprofile, font=('Times New Roman', 14))
            profile_payment_txt['values'] = ('Cash', 'Online')
            profile_payment_txt.insert(0, Global.currentUser[6])
            profile_payment_txt.place(x=460, y=300)

            def profile_updatebtnfunction():
                if (profile_name_txt.get() == '') or (profile_address_txt.get() == '') or (profile_email_txt == '') or (profile_email_txt == '') or (profile_number_txt == '') or (profile_payment_txt == ''):
                    messagebox.showerror("Error", 'Please Fill All The Fields')
                else:
                    nameResult = namevalidation(profile_name_txt.get())
                    if nameResult == True:
                        emailResult = emailvalidation(profile_email_txt.get())
                        if emailResult == True:
                            numberResult = numbervalidation(
                                profile_number_txt.get())
                            if numberResult == True:
                                profile_update1 = Customer(cid=Global.currentUser[0], fullname=profile_name_txt.get(),
                                                           address=profile_address_txt.get(),
                                                           email=profile_email_txt.get(),
                                                           number=profile_number_txt.get(),
                                                           payment=profile_payment_txt.get())
                                ecustomer = editCus(profile_update1)
                                if ecustomer == True:
                                    messagebox.showinfo(
                                        "Taxi Booking System", 'Profile Update Successfully!')
                                    updateprofile.destroy()
                                else:
                                    messagebox.showerror(
                                        'Taxi Booking System', 'Error Occurred!')
                            else:
                                messagebox.showerror(
                                    "Error ", 'Invalid Mobile Number(+977 is compulsary)')
                        else:
                            messagebox.showerror('Error ', 'Invalid Email')
                    else:
                        messagebox.showerror('Error', 'Invalid Name')

            profile_updatebtn = Button(
                updateprofile, text='Update', bg='#4CD964', font=sidefont, command=profile_updatebtnfunction)
            profile_updatebtn.place(x=290, y=350)

        profileupdatebtn = Button(sideframe, text="Update Profile", font=sidefont, bg='#e2f3f5',
                                  highlightthickness=0, borderwidth=0, command=updateprofile_gui)
        profileupdatebtn.place(x=90, y=400)

        def changepassword_gui():
            password = tkinter.Toplevel()
            password.title("Change Password")
            password.resizable(False, False)  # windows resizable false
            password.config(background="#4CD964")  # background color change
            width = 550
            height = 300
            screenwidth = password.winfo_screenwidth()
            screenheight = password.winfo_screenheight()
            xCordinate = int((screenwidth / 2) - (width / 2))
            yCordinate = int((screenheight / 2) - (height / 2))
            password.geometry('{}x{}+{}+{}'.format(width,
                                                   height, xCordinate, yCordinate))

            labelframe = Frame(password, bg="#e2f3f5", width=500, height=250)
            labelframe.place(relx=0.5, rely=0.5, anchor=CENTER)

            newpasswordlbl = Label(
                labelframe, text="New Password: ", bg="#e2f3f5", font=('Times New Roman', 14))
            newpasswordlbl.place(x=10, y=30)

            newpasswordtxt = Entry(labelframe, font=(
                'Times New Roman', 14), width=30)
            newpasswordtxt.place(x=180, y=30)

            confirmpasswordlbl = Label(
                labelframe, text="Confirm Password: ", bg="#e2f3f5", font=('Times New Roman', 14))
            confirmpasswordlbl.place(x=10, y=90)

            confirmpasswordtxt = Entry(
                labelframe, font=('Times New Roman', 14), width=30)
            confirmpasswordtxt.place(x=180, y=90)

            def changepassword():
                if (newpasswordtxt.get() == '') or (confirmpasswordtxt.get() == ''):
                    password.destroy()
                    messagebox.showerror('Error', 'Please Fill All the Fields')
                else:
                    passwordResult = passwordvalidation(newpasswordtxt.get())
                    if passwordResult == True:
                        passwordResult2 = passwordvalidation(
                            confirmpasswordtxt.get())
                        if passwordResult2 == True:
                            newpassword = newpasswordtxt.get()
                            confirmpassword = confirmpasswordtxt.get()
                            if newpassword == confirmpassword:
                                password720 = Customer(
                                    cid=cid_txt.get(), password=confirmpassword)
                                result = customer_change_password(password720)
                                if result == True:
                                    messagebox.showinfo(
                                        "TBS", "The password is changed successfully")
                                    self.root.destroy()
                                    root = Tk()
                                    signin.TaxiLogin(root)
                                    root.mainloop()
                                else:
                                    messagebox.showerror(
                                        "TBS", "Error Occurred!")
                            else:
                                password.destroy()
                                messagebox.showwarning(
                                    "TBS", "The new password and confirm password does not matched!")
                    else:
                        password.destroy()
                        messagebox.showerror(
                            'Error', 'Invalid password(Minimum eight characters-at least one uppercase,one lowercase, one number and one special character)')

            changepasswordbtn = Button(
                labelframe, command=changepassword, text="Change Password", font=('Times New Roman', 14))
            changepasswordbtn.place(x=180, y=150)

            password.mainloop()

        passwordbtn = Button(sideframe, command=changepassword_gui, text="Change Password",
                             font=sidefont, bg='#e2f3f5', highlightthickness=0, borderwidth=0)
        passwordbtn.place(x=80, y=450)

        def logout720():
            self.root.destroy()
            root1 = Tk()
            obj = signin.TaxiLogin(root1)
            root1.mainloop()

        logoutbtn = Button(sideframe, text="Logout", command=logout720,
                           font=sidefont,  bg='#e2f3f5', highlightthickness=0, borderwidth=0)
        logoutbtn.place(x=120, y=500)

        def exit():
            sys.exit()

        exitbtn = Button(sideframe, text="Exit", font=sidefont, command=exit,
                         bg='#e2f3f5', highlightthickness=0, borderwidth=0)
        exitbtn.place(x=130, y=550)

        # --------------------------------------Booking Form Frame-------------------------------------------
        formframe = Frame(self.root, height=250, bg='#ffffff')
        formframe.pack(side=TOP, fill=BOTH)

        paddress_frame = LabelFrame(
            formframe, text='Pickup Address', font=sidefont)
        paddress_frame.place(x=50, y=40)

        paddress_txt = Entry(paddress_frame, font=sidefont)
        paddress_txt.pack()

        daddress_label = LabelFrame(
            formframe, text="Drop Address", font=sidefont)
        daddress_label.place(x=350, y=40)

        daddress_txt1 = Entry(daddress_label, font=sidefont)
        daddress_txt1.pack()

        date_label = LabelFrame(formframe, text="Pickup Date", font=sidefont)
        date_label.place(x=50, y=150)

        dt = date.today()
        date_txt = DateEntry(date_label, font=sidefont, width=19, mindate=dt, date_pattern='yyyy-MM-dd')
        date_txt.pack()

        time_label = LabelFrame(formframe, text="Pickup Time", font=sidefont)
        time_label.place(x=350, y=150)

        time_txt = Entry(time_label, font=sidefont)
        time_txt.pack()

        bookingframe = LabelFrame(
            formframe, text="ACTION", bg='#e2f3f5', width=370, height=150)
        bookingframe.place(x=700, y=40)

        def requestbooking():
            if paddress_txt.get() == '' or daddress_txt1.get() == '' or date_txt.get() == '' or time_txt.get() == '':
                messagebox.showwarning(
                    "Taxi Booking System", "Please enter data in all the fields")
            else:
                timeResult = timevalidation(time_txt.get())
                if timeResult == True:
                    requestbooking = Booking(bookingid='', pickup_address=paddress_txt.get(),
                                             drop_address=daddress_txt1.get(
                    ), pickup_date=date_txt.get(), pickup_time=time_txt.get(),
                        status="Pending",
                        cid=cid_txt.get())
                    result = insert(requestbooking)
                    if result == True:
                        messagebox.showinfo(
                            "Taxi Booking System", "Booking Request Successful")
                        pendingbookingtable.delete(
                            *pendingbookingtable.get_children())
                        historybookingtable.delete(
                            *historybookingtable.get_children())
                        cusdas()
                        history()
                    else:
                        messagebox.showerror(
                            "Taxi Booking System", "Error Occurred!")
                else:
                    messagebox.showerror("Error", "Time is not Valid!")

        savebtn = Button(bookingframe, text="Request Ride", command=requestbooking,
                         bg="#4CD964", fg="white", font=sidefont, relief=RAISED, bd=5)
        savebtn.place(x=20, y=10)

        def updatebooking111():
            if paddress_txt.get() == '' or daddress_txt1.get() == '' or date_txt.get() == '' or time_txt.get() == '':
                messagebox.showwarning(
                    "Taxi Booking System", "Please enter data in all the fields")
            else:
                timeResult = timevalidation(time_txt.get())
                if timeResult == True:
                    booking = Booking(bookingid=bookingid.get(), pickup_address=paddress_txt.get(
                    ), drop_address=daddress_txt1.get(), pickup_date=date_txt.get(), pickup_time=time_txt.get())
                    updateResult = customer_edit_booking(booking)
                    if updateResult == True:
                        messagebox.showinfo("Taxi Booking System",
                                            "The booking request is updated")
                        pendingbookingtable.delete(
                            *pendingbookingtable.get_children())
                        historybookingtable.delete(
                            *historybookingtable.get_children())
                        cusdas()
                        history()
                    else:
                        messagebox.showerror("Taxi Booking System", "Error")
                else:
                    messagebox.showerror("Error", "Time is not Valid!")

        updatebtn = Button(bookingframe, command=updatebooking111, text="Update Booking",
                           bg="#4CD964", fg="white", font=sidefont, relief=RAISED, bd=5)
        updatebtn.place(x=170, y=10)

        def cancelrides():
            if paddress_txt.get() == '' or daddress_txt1.get() == '' or date_txt.get() == '' or time_txt.get() == '':
                messagebox.showwarning(
                    "Taxi Booking System", "Please enter data in all the fields")
            else:
                timeResult = timevalidation(time_txt.get())
                if timeResult == True:
                    cancelreq = cancelreqBooking(bookingid.get())
                    if cancelreq == True:
                        messagebox.showinfo(
                            "Taxi Booking System", "Booking Cancelled Successful")
                        pendingbookingtable.delete(
                            *pendingbookingtable.get_children())
                        historybookingtable.delete(
                            *historybookingtable.get_children())
                        cusdas()
                        history()
                    else:
                        messagebox.showerror(
                            "Taxi Booking System", "Error Occurred!")
                else:
                    messagebox.showerror("Error", "Time is not Valid!")

        deletebtn = Button(bookingframe, command=cancelrides, text="Cancel Booking",
                           bg="#4CD964", fg="white", font=sidefont, relief=RAISED, bd=5)
        deletebtn.place(x=20, y=70)

        def clear():
            paddress_txt.delete(0, END)
            daddress_txt1.delete(0, END)
            date_txt.delete(0, END)
            time_txt.delete(0, END)

        clearbtn = Button(bookingframe, command=clear, text="Clear",
                          bg="#4CD964", fg="white", font=sidefont, relief=RAISED, bd=5)
        clearbtn.place(x=190, y=70)

        maintab = ttk.Notebook(self.root)
        maintab.pack(side=BOTTOM, fill=BOTH, expand=TRUE, pady=(10, 0))

        frame1 = Frame(maintab)
        frame2 = Frame(maintab)

        maintab.add(frame1, text="Pending Booking")
        maintab.add(frame2, text="Booking History")

        pendingbookingtable = ttk.Treeview(frame1)
        pendingbookingtable.pack(
            side=BOTTOM, fill=BOTH, expand=TRUE, pady=(10, 0))
        pendingbookingtable['columns'] = (
            'bid', 'pickup', 'dropoff', 'date', 'time')
        pendingbookingtable.column('#0', width=0, stretch=0)
        pendingbookingtable.column('bid', width=100, anchor=CENTER)
        pendingbookingtable.column('pickup', width=50, anchor=CENTER)
        pendingbookingtable.column('dropoff', width=100, anchor=CENTER)
        pendingbookingtable.column('date', width=100, anchor=CENTER)
        pendingbookingtable.column('time', width=100, anchor=CENTER)

        pendingbookingtable.heading('#0', text='', anchor=CENTER)
        pendingbookingtable.heading('bid', text='Booking ID', anchor=CENTER)
        pendingbookingtable.heading(
            'pickup', text='Pickup Address', anchor=CENTER)
        pendingbookingtable.heading(
            'dropoff', text='Dropoff Address', anchor=CENTER)
        pendingbookingtable.heading('date', text='Date', anchor=CENTER)
        pendingbookingtable.heading('time', text='Time', anchor=CENTER)

        def cusdas():
            cusbook = Booking(cid=cid_txt.get(), status='Pending')
            cuspending = cusdastable(cusbook)
            for row in cuspending:
                pendingbookingtable.insert(parent='', index='end', values=(
                    row[0], row[1], row[2], row[3], row[4]))
        cusdas()

        def getbookingtabledata(a):
            bookingid.delete(0, END)
            paddress_txt.delete(0, END)
            daddress_txt1.delete(0, END)
            date_txt.delete(0, END)
            time_txt.delete(0, END)

            itemselect11 = pendingbookingtable.selection()[0]

            bookingid.insert(0, pendingbookingtable.item(
                itemselect11)['values'][0])
            paddress_txt.insert(0, pendingbookingtable.item(
                itemselect11)['values'][1])
            daddress_txt1.insert(
                0, pendingbookingtable.item(itemselect11)['values'][2])
            date_txt.insert(0, pendingbookingtable.item(
                itemselect11)['values'][3])
            time_txt.insert(0, pendingbookingtable.item(
                itemselect11)['values'][4])

        pendingbookingtable.bind('<<TreeviewSelect>>', getbookingtabledata)

        historybookingtable = ttk.Treeview(frame2)
        historybookingtable.pack(
            side=BOTTOM, fill=BOTH, expand=TRUE, pady=(10, 0))
        historybookingtable['columns'] = (
            'bid', 'pickup', 'dropoff', 'date', 'time')
        historybookingtable.column('#0', width=0, stretch=0)
        historybookingtable.column('bid', width=100, anchor=CENTER)
        historybookingtable.column('pickup', width=50, anchor=CENTER)
        historybookingtable.column('dropoff', width=100, anchor=CENTER)
        historybookingtable.column('date', width=100, anchor=CENTER)
        historybookingtable.column('time', width=100, anchor=CENTER)

        historybookingtable.heading('#0', text='', anchor=CENTER)
        historybookingtable.heading('bid', text='Booking ID', anchor=CENTER)
        historybookingtable.heading(
            'pickup', text='Pickup Address', anchor=CENTER)
        historybookingtable.heading(
            'dropoff', text='Dropoff Address', anchor=CENTER)
        historybookingtable.heading('date', text='Date', anchor=CENTER)
        historybookingtable.heading('time', text='Time', anchor=CENTER)

        def history():

            historyResult = customerbookinghistory_table(cid_txt.get())
            for row in historyResult:
                historybookingtable.insert(parent='', index='end', values=(
                    row[0], row[1], row[2], row[3], row[4]))
        history()

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
                        font=('Times New Roman', 16))
        style.map("Treeview.Heading",
                  )

