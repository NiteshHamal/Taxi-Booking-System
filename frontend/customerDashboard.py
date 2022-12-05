from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from frontend import signin
from middleware.booking import Booking
from middleware import Global
from backend.bookingManagement import insert
from PIL import ImageTk, Image


class CusDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Dashboard")
        self.root.geometry("550x500")  # size of the window
        self.root.state('zoomed')  # windows on zoomed / full-screen size
        self.root.config(background="#CECED2")  # background color change

        def change_home():  # function for home button
            home_frame.pack(side=RIGHT, fill=BOTH, expand=TRUE)
            history.pack_forget()
            profile.pack_forget()

        def change_history():  # function for history button
            history.pack(side=RIGHT, fill=BOTH, expand=TRUE)
            home_frame.pack_forget()
            profile.pack_forget()

        def change_profile():  # function for profile button
            profile.pack(side=RIGHT, fill=BOTH, expand=TRUE)
            history.pack_forget()
            home_frame.pack_forget()

        heading_font = ('Cooper Black', 30, "bold", UNDERLINE)
        text_font = ('Cordia New', 14)
        nav_font = ('Times New Roman', 25, "bold")

        # first frame / navbar
        navbar = Frame(self.root, bg="#4CD964", width=350)
        navbar.pack(side=LEFT, fill=BOTH)

        # image
        profile = ImageTk.PhotoImage(Image.open(
            "H:\\College\\Sem-2\\python assignment\\Taxi Booking System\\image\\profile.png"))
        profile_label = Label(navbar, image=profile, bg="#4CD964")
        profile_label.image = profile
        profile_label.place(x=90, y=50)

        # home button
        home_btn = Button(navbar, text=" Home  ", command=change_home,
                          font=nav_font, bg="#4CD964", relief=RIDGE)
        home_btn.place(x=90, y=210)

        # history button
        history_button = Button(navbar, text="History",
                                command=change_history, font=nav_font, bg="#4CD964", relief=RIDGE)
        history_button.place(x=90, y=300)

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

        pickupdate = DateEntry(date_frame, width=18, font=text_font)
        pickupdate.pack()

        time_frame = LabelFrame(home_frame, text="Pickup Time")
        time_frame.place(x=50, y=370)

        pickuptime = Entry(time_frame, text="", font=text_font, relief=RAISED)
        pickuptime.pack()

        cid_txt = Entry(home_frame)
        # cid_txt.insert(0, Global.currentUser[0])

        # function for request booking by customer
        def requestbooking():
            requestbooking = Booking(bookingid='', pickup_address=pickaddress.get(), drop_address=dropaddress.get(
            ), pickup_date=pickupdate.get(), pickup_time=pickuptime.get(), status="Pending", cid=cid_txt.get())
            result = insert(requestbooking)
            if result == True:
                msg1 = messagebox.showinfo(
                    "Taxi Booking System", "Booking Request Successful")

            else:
                msg2 = messagebox.showerror(
                    "Taxi Booking System", "Error Occurred!")

        request = Button(home_frame, text='Request',
                         font=text_font, relief=RAISED, command=requestbooking)
        request.place(x=60, y=430)

        clear = Button(home_frame, text='  Clear  ',
                       font=text_font, relief=RAISED)
        clear.place(x=180, y=430)

        cancel = Button(home_frame, text=' Cancel ',
                        font=text_font, relief=RAISED)
        cancel.place(x=120, y=480)

        # # frame for table
        # table_frame = Frame(home_frame)
        # table_frame.pack()
        #
        # requested_table = ttk.Treeview(table_frame)
        # requested_table['columns'] = ('bid', 'p_address','d_address','p_date','p_time','status')
        # requested_table.column('#0', width=0, stretch=NO)
        # requested_table.column('bid', width = 50, anchor=CENTER)
        # requested_table.column('p_address', width = 100, anchor=CENTER)
        # requested_table.column('d_address', width = 100, anchor=CENTER)
        # requested_table.column('p_date', width = 100, anchor=CENTER)
        # requested_table.column('p_time', width = 100, anchor=CENTER)
        # requested_table.column('status', width = 100, anchor=CENTER)
        #
        # requested_table.heading('#0', text = '', anchor= CENTER)
        # requested_table.heading('bid', text = 'Booking ID', anchor= CENTER)
        # requested_table.heading('p_address', text = 'Pickup Address', anchor= CENTER)
        # requested_table.heading('d_address', text = 'Drop Address', anchor= CENTER)
        # requested_table.heading('p_date', text = 'Pickup Date', anchor= CENTER)
        # requested_table.heading('p_time', text = 'Pickup Time', anchor= CENTER)
        # requested_table.heading('status', text = 'Booking Status', anchor= CENTER)

        # driver management frame
        history = Frame(self.root, bg="black")

        # customer management frame
        profile = Frame(self.root, bg="blue")


if __name__ == '__main__':
    root = Tk()
    CusDashboard(root)
    root.mainloop()
