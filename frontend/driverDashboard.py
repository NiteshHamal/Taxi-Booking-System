from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image
from frontend import signin
from middleware import Global
from middleware.driver import Driver
from backend.driverManagement import *


class DriverDashboard:

    def __init__(self, root):
        self.root = root
        self.root.title("Driver Dashboard")
        self.root.geometry("550x500")  # size of the window
        self.root.state('zoomed')  # windows on zoomed / full-screen size
        self.root.config(background="#CECED2")  # background color change

        # Keep track of button on/off
        global is_on
        is_on = True

        # font
        font1 = ('Cordia New', 14)

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
                        background="#4CD964",
                        foreground="black",
                        relief="flat",
                        font=('Times New Roman', 14))
        style.map("Treeview.Heading",
                  )

        # right frame
        right_bar = Frame(self.root, bg="#4CD964", width=350)
        right_bar.pack(side=LEFT, fill=BOTH)

        # image
        profile = ImageTk.PhotoImage(Image.open(
            "H:\\College\\Sem-2\\python assignment\\Taxi Booking System\\image\\profile.png"))
        profile_label = Label(right_bar, image=profile, bg="#4CD964")
        profile_label.image = profile
        profile_label.place(x=110, y=50)

        def changeStatus():
            global is_on
            # Check if it is on or off
            if is_on:
                active.config(image=off)
                # active_label.config(text="Inactive")
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
                        text="{}, You are Active". format(Global.currentDriver[1]))

        on = ImageTk.PhotoImage(Image.open(
            "H:\\College\\Sem-2\\python assignment\\Taxi Booking System\\image\\on.png"))
        off = ImageTk.PhotoImage(Image.open(
            "H:\\College\\Sem-2\\python assignment\\Taxi Booking System\\image\\off.png"))
        active = Button(right_bar, command=changeStatus, image=on,
                        relief=FLAT, bd=0, bg="#4CD964", activebackground="#4CD964")
        active.image = on
        active.place(x=130, y=200)

        active_label = Label(right_bar, text='{}, You are Active'.format(Global.currentDriver[1]),
                             font=font1, bg="#4CD964")
        active_label.place(x=55, y=290)

        # function for home_label to open home_frame
        def command_home(event):
            home_frame.pack(side=RIGHT, fill=BOTH, expand=TRUE)
            profile_frame.pack_forget()

        home_label = Label(right_bar, text="Home ", font=font1, bg="#4CD964",
                           highlightbackground='Black', highlightthickness='2')
        home_label.place(x=150, y=340)
        home_label.bind("<Button-1>", command_home)

        # function for profile_label top open profile_frame
        def command_profile(event):
            profile_frame.pack(side=RIGHT, fill=BOTH, expand=TRUE)
            home_frame.pack_forget()

        profile_label = Label(right_bar, text="Profile", font=font1,
                              bg="#4CD964", highlightbackground='Black', highlightthickness='2')
        profile_label.place(x=150, y=390)
        profile_label.bind("<Button-1>", command_profile)

        # function for logout
        def logout720():
            self.root.destroy()
            root = Tk()
            obj = signin.Signin(root)
            root.mainloop()

        # logout button with image
        logout = ImageTk.PhotoImage(Image.open(
            "H:\\College\\Sem-2\\python assignment\\Taxi Booking System\\image\\logout.png"))
        logout_btn = Button(right_bar, command=logout720, image=logout, bg="#4CD964",
                            relief=FLAT, activebackground="#4CD964")
        logout_btn.image = logout
        logout_btn.place(x=130, y=650)

        # home frame for driver
        home_frame = Frame(self.root)
        home_frame.pack(side=RIGHT, fill=BOTH, expand=TRUE)

        # adding widgets on home frame

        did_txt = Entry(home_frame)
        did_txt.insert(0, Global.currentDriver[0])

        bid_txt = Entry(home_frame)

        customer_name_label = LabelFrame(
            home_frame, text='Customer name', font=font1)
        customer_name_label.place(x=10, y=30)

        customr_name_txt = Entry(customer_name_label, text='', font=font1)
        customr_name_txt.pack()

        pickupadress_label = LabelFrame(
            home_frame, text='Pickup Address', font=font1)
        pickupadress_label.place(x=310, y=30)

        pickupaddress_txt = Entry(pickupadress_label, text='', font=font1)
        pickupaddress_txt.pack()

        dropadress_label = LabelFrame(
            home_frame, text='Drop Address', font=font1)
        dropadress_label.place(x=610, y=30)

        dropaddress_txt = Entry(dropadress_label, text='', font=font1)
        dropaddress_txt.pack()

        pickupdate_label = LabelFrame(
            home_frame, text="Pickup Date", font=font1)
        pickupdate_label.place(x=910, y=30)

        pickupdate_txt = Entry(pickupdate_label, text='', font=font1)
        pickupdate_txt.pack()

        pickuptime_label = LabelFrame(
            home_frame, text='Pickup Time', font=font1)
        pickuptime_label.place(x=10, y=150)

        pickuptime_txt = Entry(pickuptime_label, text='', font=font1)
        pickuptime_txt.pack()

        complete_booking_btn = Button(
            home_frame, text='Completed', font=font1, bd=4, relief=RAISED)
        complete_booking_btn.place(x=310, y=160)

        search_label = LabelFrame(home_frame, text='Search', font=font1)
        search_label.place(x=610, y=150)

        search_txt = Entry(search_label, text='', font=font1)
        search_txt.pack()

        serach_btn = Button(home_frame, text=' Search ',
                            font=font1, bd=4, relief=RAISED)
        serach_btn.place(x=910, y=160)

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

            result = driver_booking_table()
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

        # profile frame for driver
        profile_frame = Frame(self.root, bg="black")

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
