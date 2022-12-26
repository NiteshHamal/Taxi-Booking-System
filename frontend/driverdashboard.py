import sys
import tkinter
from tkinter import *
from tkinter import messagebox, ttk
from PIL import ImageTk, Image
from backend.bookingManagement import completetripbydriver
from backend.driverManagement import statusUpdate, driver_change_password, driver_booking_table, \
    driver_search_booking_table, searchDriver
from frontend import signin
from middleware import Global
from middleware.driver import Driver
from middleware.booking import Booking


class DriverDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Dashboard")
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        self.root.minsize(screenwidth, screenheight)
        self.root.state('zoomed')

        # Keep track of button on/off
        global is_on
        is_on = True

        # font
        sidefont = ('Times New Roman', 15, 'normal')

        did_txt = Entry(self.root)
        did_txt.insert(0, Global.currentDriver[0])

        # -----------------------------------Top Frame---------------------------------------------
        upframe = Frame(self.root, height=100, bg="#4CD964")
        upframe.pack(side=TOP, fill=BOTH)

        # -----------------------------------------Top frame title label----------------------------------------
        titlelabel = Label(self.root, text="Welcome {}".format(
            Global.currentDriver[1]), bg="#4CD964", font=('Times New Roman', 25, 'bold'))
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

        titlelbl = Label(sideframe, text="Taxi Booking System",
                         bg='#e2f3f5', font=('Times New Roman', 16, 'bold'))
        titlelbl.place(x=90, y=270)

        # function to change the status of the driver
        def changeStatus():
            global is_on
            # Check if it is on or off
            if is_on:
                active.config(image=off)
                is_on = FALSE
                driver = Driver(did=did_txt.get(), status="Inactive")
                result = statusUpdate(driver)
                if result == True:
                    active_label.config(
                        text="{}, You are Inactive".format(Global.currentDriver[1]))
            else:
                active.config(image=on)
                # active_label.config(text="Active")
                is_on = TRUE
                driver1 = Driver(did=did_txt.get(), status="Active")
                result = statusUpdate(driver1)
                if result == True:
                    active_label.config(
                        text="{}, You are Active".format(Global.currentDriver[1]))

        on = ImageTk.PhotoImage(Image.open(
            "H:\\College\\Sem-2\\python assignment\\Taxi Booking System\\image\\on.png"))
        off = ImageTk.PhotoImage(Image.open(
            "H:\\College\\Sem-2\\python assignment\\Taxi Booking System\\image\\off.png"))
        active = Button(sideframe, command=changeStatus, image=on,
                        relief=FLAT, bd=0, bg="#e2f3f5", activebackground="#e2f3f5")
        active.image = on
        active.place(x=130, y=300)

        active_label = Label(sideframe, text='{}, You are Active'.format(Global.currentDriver[1]),
                             font=sidefont, bg="#e2f3f5")
        active_label.place(x=55, y=390)

        # toplevel frame to open when clicked the change password button
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
                newpassword = newpasswordtxt.get()
                confirmpassword = confirmpasswordtxt.get()

                if newpassword == confirmpassword:
                    password = Driver(did=did_txt.get(),
                                      password=confirmpassword)
                    result = driver_change_password(password)
                    if result == True:
                        messagebox.showinfo(
                            "TBS", "The password is changed successfully")
                        self.root.destroy()
                        root = Tk()
                        signin.TaxiLogin(root)
                        root.mainloop()

                    else:
                        messagebox.showerror("TBS", "Error Occurred!")

                else:
                    messagebox.showwarning(
                        "TBS", "The new password and confirm password does not matched!")

            changepasswordbtn = Button(
                labelframe, command=changepassword, text="Change Password", font=('Times New Roman', 14))
            changepasswordbtn.place(x=180, y=150)

            password.mainloop()

        changepasswordbtn = Button(sideframe, text='Change Password', font=sidefont, bg='#e2f3f5',
                                   highlightthickness=0, borderwidth=0, command=changepassword_gui)
        changepasswordbtn.place(x=90, y=440)

        # function to log out the driver dashboard
        def logout720():
            self.root.destroy()
            root1 = Tk()
            obj = signin.TaxiLogin(root1)
            root1.mainloop()

        logoutbtn = Button(sideframe, text='Logout', font=sidefont, bg='#e2f3f5',
                           highlightthickness=0, borderwidth=0, command=logout720)
        logoutbtn.place(x=120, y=490)

        # function to exit the program
        def exit():
            sys.exit()

        exitbtn = Button(sideframe, text='Exit', font=sidefont, bg='#e2f3f5',
                         highlightthickness=0, borderwidth=0, command=exit)
        exitbtn.place(x=130, y=540)

        # frame for driver to complete the booking and view all booking
        home_frame = Frame(self.root, bg='#ffffff')
        home_frame.pack(side=RIGHT, fill=BOTH, expand=TRUE)

        bid_txt = Entry(home_frame)

        customer_name_label = LabelFrame(
            home_frame, text='Customer name', font=sidefont)
        customer_name_label.place(x=10, y=30)

        customr_name_txt = Entry(customer_name_label, font=sidefont)
        customr_name_txt.pack()

        pickupadress_label = LabelFrame(
            home_frame, text='Pickup Address', font=sidefont)
        pickupadress_label.place(x=310, y=30)

        pickupaddress_txt = Entry(pickupadress_label, font=sidefont)
        pickupaddress_txt.pack()

        dropadress_label = LabelFrame(
            home_frame, text='Drop Address', font=sidefont)
        dropadress_label.place(x=610, y=30)

        dropaddress_txt = Entry(dropadress_label, font=sidefont)
        dropaddress_txt.pack()

        pickupdate_label = LabelFrame(
            home_frame, text="Pickup Date", font=sidefont)
        pickupdate_label.place(x=910, y=30)

        pickupdate_txt = Entry(pickupdate_label, font=sidefont)
        pickupdate_txt.pack()

        pickuptime_label = LabelFrame(
            home_frame, text='Pickup Time', font=sidefont)
        pickuptime_label.place(x=10, y=150)

        pickuptime_txt = Entry(pickuptime_label, font=sidefont)
        pickuptime_txt.pack()

        def completefunction():
            complete1 = Booking(bookingid=bid_txt.get(), status='Completed')
            completetripbydriverresult = completetripbydriver(complete1)
            driver = Driver(did=did_txt.get(), status="Active")
            result = statusUpdate(driver)
            if completetripbydriverresult == True:
                messagebox.showinfo('Taxi Booking System', 'Trip is Complete')
                upcoming_trip_table.delete(*upcoming_trip_table.get_children())
                bookingtable()
                switch()
                bid_txt.delete(0, END)
                customr_name_txt.delete(0, END)
                pickupaddress_txt.delete(0, END)
                pickuptime_txt.delete(0, END)
                dropaddress_txt.delete(0, END)
                pickupdate_txt.delete(0, END)
            else:
                messagebox.showerror('Taxi Booking System', 'Error Occurred!')

        complete_booking_btn = Button(
            home_frame, text='Completed', font=sidefont, bd=4, relief=RAISED, command=completefunction)
        complete_booking_btn.place(x=310, y=160)

        def clearfunction():
            bid_txt.delete(0, END)
            customr_name_txt.delete(0, END)
            pickupaddress_txt.delete(0, END)
            pickuptime_txt.delete(0, END)
            dropaddress_txt.delete(0, END)
            pickupdate_txt.delete(0, END)
            search_txt.delete(0, END)
            upcoming_trip_table.delete(*upcoming_trip_table.get_children())
            bookingtable()

        clear_btn = Button(home_frame, text=' Clear ', font=sidefont,
                           bd=4, relief=RAISED, command=clearfunction)
        clear_btn.place(x=470, y=160)

        search_label = LabelFrame(home_frame, text='Search', font=sidefont)
        search_label.place(x=610, y=150)

        search_txt = Entry(search_label, font=sidefont)
        search_txt.pack()

        # function to search in the table
        def searchfromtable():
            upcoming_trip_table.delete(*upcoming_trip_table.get_children())
            result = driver_search_booking_table(search_txt.get())
            for row in result:
                upcoming_trip_table.insert(parent='', index='end', values=(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

        search_btn = Button(home_frame, text=' Search ',
                            font=sidefont, bd=4, relief=RAISED, command=searchfromtable)
        search_btn.place(x=910, y=160)

        # style of table
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        rowheight=20,
                        background="#f0f0f0",
                        fieldbackground="#f0f0f0",
                        bordercolor="#343638",
                        borderwidth=2,
                        font=('Times New Roman', 14))
        style.configure("Treeview.Heading",
                        background="#4CD964",
                        foreground="black",
                        relief="flat",
                        font=('Times New Roman', 14))
        style.map("Treeview.Heading",
                  )

        # adding table on home frame
        upcoming_trip_table = ttk.Treeview(home_frame, height=20)
        upcoming_trip_table['columns'] = (
            'bid', 'name', 'number', 'paddress', 'daddress', 'pdate', 'ptime', 'status')
        upcoming_trip_table.column('#0', width=0, stretch=0)
        upcoming_trip_table.column('bid', width=0, stretch=0)
        upcoming_trip_table.column('name', width=100, anchor=CENTER)
        upcoming_trip_table.column('number', width=100, anchor=CENTER)
        upcoming_trip_table.column('paddress', width=100, anchor=CENTER)
        upcoming_trip_table.column('daddress', width=100, anchor=CENTER)
        upcoming_trip_table.column('pdate', width=100, anchor=CENTER)
        upcoming_trip_table.column('ptime', width=100, anchor=CENTER)
        upcoming_trip_table.column('status', width=100, anchor=CENTER)
        upcoming_trip_table.heading('#0', text='', anchor=CENTER)
        upcoming_trip_table.heading('bid', text='', anchor=CENTER)
        upcoming_trip_table.heading(
            'name', text='Customer Name', anchor=CENTER)
        upcoming_trip_table.heading(
            'number', text='Phone Number', anchor=CENTER)
        upcoming_trip_table.heading(
            'paddress', text='Pickup Address', anchor=CENTER)
        upcoming_trip_table.heading(
            'daddress', text='Drop Address', anchor=CENTER)
        upcoming_trip_table.heading('pdate', text='Pickup Date', anchor=CENTER)
        upcoming_trip_table.heading('ptime', text='Pickup Time', anchor=CENTER)
        upcoming_trip_table.heading('status', text='Status', anchor=CENTER)
        upcoming_trip_table.pack(side=BOTTOM, fill=BOTH)

        def bookingtable():
            result = driver_booking_table(did_txt.get())
            for x in result:
                upcoming_trip_table.insert(parent='', index='end', values=(
                    x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7]))
        bookingtable()

        def getData(a):
            # did_txt
            bid_txt.delete(0, END)
            customr_name_txt.delete(0, END)
            pickupaddress_txt.delete(0, END)
            pickuptime_txt.delete(0, END)
            dropaddress_txt.delete(0, END)
            pickupdate_txt.delete(0, END)
            selectitem = upcoming_trip_table.selection()[0]
            bid_txt.insert(0, upcoming_trip_table.item(
                selectitem)['values'][0])
            customr_name_txt.insert(
                0, upcoming_trip_table.item(selectitem)['values'][1])
            pickupaddress_txt.insert(
                0, upcoming_trip_table.item(selectitem)['values'][3])
            pickuptime_txt.insert(
                0, upcoming_trip_table.item(selectitem)['values'][4])
            dropaddress_txt.insert(
                0, upcoming_trip_table.item(selectitem)['values'][4])
            pickupdate_txt.insert(
                0, upcoming_trip_table.item(selectitem)['values'][5])
        upcoming_trip_table.bind('<<TreeviewSelect>>', getData)

        def switch():
            driverid = did_txt.get()
            driverInfo = searchDriver(driverid)
            if driverInfo != None:
                if driverInfo[5] == 'Active':
                    active.config(image=on)
                    active_label.config(
                        text='{}, You are Active'.format(Global.currentDriver[1]))
                else:
                    active.config(image=off)
                    active_label.config(
                        text='{}, You are Inactive'.format(Global.currentDriver[1]))
        switch()


if __name__ == '__main__':
    root = Tk()
    DriverDashboard(root)
    root.mainloop()
