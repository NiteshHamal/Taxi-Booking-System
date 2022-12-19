import sys
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from backend.adminManagement import adminhistory, admin_change_password
from backend.analyticsbackend import totalbooking, totalcustomers, totaldrivers
from backend.bookingManagement import requestBooking1167, admin_update_booking
from backend.driverManagement import drivertablead, statusUpdate
from frontend import signin, customergui, drivergui
from middleware import Global
from middleware.admin import Admin
from middleware.booking import Booking
from middleware.driver import Driver


class AdminDashboard():
    def __init__(self, main):
        self.main=main
        self.main.title("Admin Dashboard")
        screenwidth=self.main.winfo_screenwidth()
        screenheight=self.main.winfo_screenheight()
        self.main.minsize(screenwidth,screenheight)
        self.main.state('zoomed')
        # self.root.iconbitmap("H:\\College\\Sem-2\\python assignment\\Taxi Booking System\\image\\Iconsmind-Outline-Taxi-2.ico")

        adminid=Entry(self.main)
        adminid.insert(0, Global.currentAdmin[0])

        # font
        sidefont=('Times New Roman', 15,'normal')

        # top frame
        upframe=Frame(self.main, height=100, bg="#4CD964")
        upframe.pack(side=TOP, fill=BOTH)

        titlelabel=Label(self.main, text="Welcome Nitesh Hamal",bg="#4CD964", font=('Times New Roman',25,'bold'))
        titlelabel.place(x=20, y=30)

        # side frame
        sideframe=Frame(self.main, width=350, bg='#e2f3f5')
        sideframe.pack(side=LEFT, fill=BOTH)

        # image
        image = Image.open("H:\\College\\Sem-2\\python assignment\\Taxi Booking System\\image\\Order ride-bro.png")
        image = image.resize((250, 250))
        image = ImageTk.PhotoImage(image)
        Image_Label = Label(sideframe, image=image, bg='#e2f3f5')
        Image_Label.image = image
        Image_Label.place(x=60, y=20)

        titlelbl=Label(sideframe, text="Taxi Booking System", bg='#e2f3f5', font=('Times New Roman', 16,'bold'))
        titlelbl.place(x=90, y=270)

        def assigndriver():
            root=tkinter.Toplevel()
            root.title("Assign Driver | Admin Dashboard")
            frame_width=1200
            frame_height=500
            root.resizable(0,0)
            screen_width=root.winfo_screenwidth()
            screen_height=root.winfo_screenheight()
            x_cordinate=int((screen_width/2)-(frame_width/2))
            y_cordinate=int((screen_height/2)-(frame_height/2))
            root.geometry("{}x{}+{}+{}".format(frame_width, frame_height, x_cordinate+120, y_cordinate))

            topframe=Frame(root, height=80, bg="#4CD964")
            topframe.pack(side=TOP, fill=BOTH)

            assgnlabel=Label(topframe, text="ASSIGN DRIVER FOR CUSTOMERS", font=('Times New Roman',18,'bold'))
            assgnlabel.place(relx=0.5, rely=0.5, anchor=CENTER)

            assigndriverframe=Frame(root, height=200)
            assigndriverframe.pack(side=TOP, fill=BOTH)

            bid_frame = LabelFrame(assigndriverframe, text="Booking ID", font=sidefont)
            bid_frame.place(x=10, y=10)

            bid_txt = Entry(bid_frame, text="", font=sidefont)
            bid_txt.pack()

            paddress_frame = LabelFrame(assigndriverframe, text='Pickup Address', font=sidefont)
            paddress_frame.place(x=310, y=10)

            paddress_txt = Entry(paddress_frame, text='', font=sidefont)
            paddress_txt.pack()

            daddress_label = LabelFrame(assigndriverframe, text="Drop Address", font=sidefont)
            daddress_label.place(x=610, y=10)

            daddress_txt1 = Entry(daddress_label, text='', font=sidefont)
            daddress_txt1.pack()

            date_label = LabelFrame(assigndriverframe, text="Pickup Date", font=sidefont)
            date_label.place(x=10, y=120)

            date_txt = Entry(date_label, text='', font=sidefont)
            date_txt.pack()

            time_label = LabelFrame(assigndriverframe, text="Pickup Time", font=sidefont)
            time_label.place(x=310, y=120)

            time_txt = Entry(time_label, text='', font=sidefont)
            time_txt.pack()

            driver_label = LabelFrame(
            assigndriverframe, text='Assign Driver', font=sidefont)
            driver_label.place(x=610, y=120)

            driver_txt = Entry(driver_label, text='', font=sidefont)
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
                    app.destroy()

                checktable.bind('<<TreeviewSelect>>', getselecteddriver)

            check_btn = Button(assigndriverframe, command=drivercheck,
                           text="Check Driver", font=sidefont, relief=RAISED, bd=5)
            check_btn.place(x=900, y=20)

            def confirm_booking():

                    if driver_txt.get() == '':
                                    messagebox.showwarning("TBS", "Please enter driver ID")
                                    root.destroy()

                    else:
                        booking = Booking(bookingid=bid_txt.get(),
                                  did=driver_txt.get(), status='Confirmed')
                        updateResult = admin_update_booking(booking)
                        driver = Driver(did=driver_txt.get(), status="Inactive")
                        result = statusUpdate(driver)
                        driver_txt.delete(0, END)
                    if updateResult == True:
                        messagebox.showinfo("TBS", "The driver is assigned successfully")
                        requestTable.delete(*requestTable.get_children())
                        requesttable()
                        historytable.delete(*historytable.get_children())
                        driverValue()
                        root.destroy()

                    else:
                            messagebox.showerror("TBS", "Error")

            confirm_btn = Button(assigndriverframe, text="Confirm Booking",command=confirm_booking, font=sidefont, relief=RAISED, bd=5)
            confirm_btn.place(x=900, y=100)



            assigndrivertable=ttk.Treeview(root)
            assigndrivertable.pack(side=BOTTOM, fill=BOTH, expand=TRUE, pady=(10,0))
            assigndrivertable['columns'] = (
            'bid', 'cid', 'fullname', 'paddress', 'daddress', 'pdate', 'ptime', 'status')
            assigndrivertable.column('#0', width=0, stretch=0)
            assigndrivertable.column('bid', width=0, stretch=0)
            assigndrivertable.column('cid', width=50, anchor=CENTER)
            assigndrivertable.column('fullname', width=100, anchor=CENTER)
            assigndrivertable.column('paddress', width=100, anchor=CENTER)
            assigndrivertable.column('daddress', width=100, anchor=CENTER)
            assigndrivertable.column('pdate', width=100, anchor=CENTER)
            assigndrivertable.column('ptime', width=100, anchor=CENTER)
            assigndrivertable.column('status', width=100, anchor=CENTER)

            assigndrivertable.heading('#0', text='', anchor=CENTER)
            assigndrivertable.heading('bid', text='', anchor=CENTER)
            assigndrivertable.heading('cid', text='Customer ID', anchor=CENTER)
            assigndrivertable.heading('fullname', text='Fullname', anchor=CENTER)
            assigndrivertable.heading('paddress', text='Pickup Address', anchor=CENTER)
            assigndrivertable.heading('daddress', text='Drop Address', anchor=CENTER)
            assigndrivertable.heading('pdate', text='Pickup Date', anchor=CENTER)
            assigndrivertable.heading('ptime', text='Pickup Time', anchor=CENTER)
            assigndrivertable.heading('status', text='Booking Status', anchor=CENTER)

            def assigndrivertable11():
                request = requestBooking1167()
                for row in request:
                    assigndrivertable.insert(parent='', index='end', values=(
                        row[1], row[0], row[2], row[3], row[4], row[5], row[6], row[7]))

            assigndrivertable11()

            def getbookingtabledata(a):
                bid_txt.delete(0, END)
                paddress_txt.delete(0, END)
                daddress_txt1.delete(0, END)
                date_txt.delete(0, END)
                time_txt.delete(0, END)

                itemselect11 = assigndrivertable.selection()[0]

                bid_txt.insert(0, assigndrivertable.item(itemselect11)['values'][0])
                paddress_txt.insert(0, assigndrivertable.item(itemselect11)['values'][3])
                daddress_txt1.insert(0, assigndrivertable.item(itemselect11)['values'][4])
                date_txt.insert(0, assigndrivertable.item(itemselect11)['values'][5])
                time_txt.insert(0, assigndrivertable.item(itemselect11)['values'][6])

            assigndrivertable.bind('<<TreeviewSelect>>', getbookingtabledata)


            root.mainloop()

        assignbtn=Button(sideframe, text="Assign Driver",command=assigndriver,font=sidefont,  bg='#e2f3f5', highlightthickness=0, borderwidth=0)
        assignbtn.place(x=100, y=350)

        # function to open customer management gui
        def customermanagementgui():
            root=tkinter.Toplevel()
            customergui.CustomerCRUD(root)
            root.mainloop()

        customerbtn=Button(sideframe, text="Customer Management",command=customermanagementgui, font=sidefont,  bg='#e2f3f5', highlightthickness=0, borderwidth=0)
        customerbtn.place(x=70, y=400)

        # function to open driver management gui
        def drivermanagementgui():
            root = tkinter.Toplevel()
            drivergui.DriverCRUD(root)
            root.mainloop()

        driverbtn=Button(sideframe, text="Driver Management", font=sidefont,  bg='#e2f3f5', highlightthickness=0, borderwidth=0, command=drivermanagementgui)
        driverbtn.place(x=80, y=450)

        def changepassword_gui():
            password=tkinter.Toplevel()
            password.title("Change Password")
            password.resizable(False, False)  # windows resizable false
            password.config(background="#4CD964")  # background color change
            width = 550
            height = 300
            screenwidth = password.winfo_screenwidth()
            screenheight = password.winfo_screenheight()
            xCordinate = int((screenwidth / 2) - (width / 2))
            yCordinate = int((screenheight / 2) - (height / 2))
            password.geometry('{}x{}+{}+{}'.format(width,height, xCordinate, yCordinate))

            labelframe=Frame(password,bg="#e2f3f5", width=500, height=250)
            labelframe.place(relx=0.5, rely=0.5, anchor=CENTER)

            newpasswordlbl=Label(labelframe, text="New Password: ",bg="#e2f3f5", font=('Times New Roman',14))
            newpasswordlbl.place(x=10, y=30)

            newpasswordtxt=Entry(labelframe, font=('Times New Roman',14), width=30)
            newpasswordtxt.place(x=180, y=30)

            confirmpasswordlbl = Label(labelframe, text="Confirm Password: ",bg="#e2f3f5", font=('Times New Roman', 14))
            confirmpasswordlbl.place(x=10, y=90)

            confirmpasswordtxt = Entry(labelframe, font=('Times New Roman', 14), width=30)
            confirmpasswordtxt.place(x=180, y=90)

            def changepassword():
                newpassword=newpasswordtxt.get()
                confirmpassword=confirmpasswordtxt.get()

                if newpassword==confirmpassword:
                    password=Admin(adminid=adminid.get(), password=confirmpassword)
                    result=admin_change_password(password)
                    if result==True:
                        messagebox.showinfo("TBS","The password is changed successfully")
                        self.main.destroy()
                        root=Tk()
                        signin.TaxiLogin(root)
                        root.mainloop()

                    else:
                        messagebox.showerror("TBS","Error Occurred!")

                else:
                    messagebox.showwarning("TBS","The new password and confirm password does not matched!")

            changepasswordbtn=Button(labelframe,command=changepassword, text="Change Password",font=('Times New Roman', 14) )
            changepasswordbtn.place(x=180, y=150)

            password.mainloop()

        passwordbtn=Button(sideframe,command=changepassword_gui, text="Change Password", font=sidefont,  bg='#e2f3f5', highlightthickness=0, borderwidth=0)
        passwordbtn.place(x=90, y=500)

        def logout720():
            self.main.destroy()
            root1 = Tk()
            obj = signin.TaxiLogin(root1)
            root1.mainloop()

        logoutbtn=Button(sideframe, text="Logout",command=logout720, font=sidefont,  bg='#e2f3f5', highlightthickness=0, borderwidth=0)
        logoutbtn.place(x=120, y=550)

        def exit():
            sys.exit()

        exitbtn=Button(sideframe, text="Exit", font=sidefont,command=exit,  bg='#e2f3f5', highlightthickness=0, borderwidth=0)
        exitbtn.place(x=130, y=600)

        centerframe=Frame(self.main,height=250, bg='#ffffff')
        centerframe.pack(side=TOP, fill=BOTH)

        analyticsframe1=Frame(centerframe,bg='#e2f3f5', width=250, height=200)
        analyticsframe1.place(x=40, y=20)

        customerresult=totalcustomers()
        customerresult1=customerresult[0]
        customerresult2=customerresult1[0]

        lbl1=Label(analyticsframe1, text="Total Customers \n\n {}".format(customerresult2), font=sidefont, bg='#e2f3f5')
        lbl1.place(relx=0.5, rely=0.5, anchor=CENTER)

        analyticsframe2 = Frame(centerframe, bg='#e2f3f5', width=250, height=200)
        analyticsframe2.place(x=320, y=20)

        bookingresult=totalbooking()
        bookingresult1=bookingresult[0]
        bookingresult2=bookingresult1[0]

        lbl2 = Label(analyticsframe2, text="Total Booking \n\n {}".format(bookingresult2), font=sidefont, bg='#e2f3f5')
        lbl2.place(relx=0.5, rely=0.5, anchor=CENTER)

        analyticsframe3 = Frame(centerframe, bg='#e2f3f5', width=250, height=200)
        analyticsframe3.place(x=600, y=20)

        driverresult=totaldrivers()
        driverresult1=driverresult[0]
        driverresult2=driverresult1[0]

        lbl3 = Label(analyticsframe3, text="Total Drivers \n\n {}".format(driverresult2), font=sidefont, bg='#e2f3f5')
        lbl3.place(relx=0.5, rely=0.5, anchor=CENTER)

        analyticsframe4 = Frame(centerframe, bg='#e2f3f5', width=250, height=200)
        analyticsframe4.place(x=880, y=20)

        lbl4 = Label(analyticsframe4, text="Last 15 days booking \n\n 200", font=sidefont, bg='#e2f3f5')
        lbl4.place(relx=0.5, rely=0.5, anchor=CENTER)

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

        maintab=ttk.Notebook(self.main)
        maintab.pack(side=BOTTOM, fill=BOTH, expand=TRUE, pady=(10,0))

        frame1=Frame(maintab)
        frame2=Frame(maintab)

        maintab.add(frame1, text="Booking")
        maintab.add(frame2,text="Booking History")

        requestTable=ttk.Treeview(frame1)
        requestTable.pack(side=BOTTOM, fill=BOTH, expand=TRUE, pady=(10,0))
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

        def requesttable():
            request = requestBooking1167()
            for row in request:
                requestTable.insert(parent='', index='end', values=(
                    row[1], row[0], row[2], row[3], row[4], row[5], row[6], row[7]))

        requesttable()


        historytable=ttk.Treeview(frame2)
        historytable.pack(side=BOTTOM, fill=BOTH, expand=TRUE, pady=(10,0))
        historytable['columns'] = ( 'bid', 'pickup', 'dropoff', 'date', 'time', 'status')
        historytable.column('#0', width=0, stretch=0)
        historytable.column('bid', width=100, anchor=CENTER)
        historytable.column('pickup', width=50, anchor=CENTER)
        historytable.column('dropoff', width=100, anchor=CENTER)
        historytable.column('date', width=100, anchor=CENTER)
        historytable.column('time', width=100, anchor=CENTER)
        historytable.column('status', width=100, anchor=CENTER)


        historytable.heading('#0', text='', anchor=CENTER)
        historytable.heading('bid', text='Booking ID', anchor=CENTER)
        historytable.heading('pickup', text='Pickup Address', anchor=CENTER)
        historytable.heading('dropoff', text='Dropoff Address', anchor=CENTER)
        historytable.heading('date', text='Date', anchor=CENTER)
        historytable.heading('time', text='Time', anchor=CENTER)
        historytable.heading('status', text='Status', anchor=CENTER)


        def driverValue():
            historyResult = adminhistory()
            for row in historyResult:
                historytable.insert(parent='', index='end', values=(
                    row[0], row[1], row[2], row[3], row[4], row[5]))
        driverValue()








if __name__=='__main__':
    main=Tk()
    AdminDashboard(main)
    main.mainloop()
