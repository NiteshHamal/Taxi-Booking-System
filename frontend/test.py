from tkinter import *
from tkinter import ttk


class CustomerDashboard():
    def __init__(self, cusdash):
        self.cusdash = cusdash
        self.cusdash.title("Customer Dashboard")
        self.cusdash.resizable(False, False)
        self.cusdash.config(bg="")
        frame_width = 900
        frame_height = 600
        screen_width = self.cusdash.winfo_screenwidth()
        screen_height = self.cusdash.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (frame_width / 2))
        y_cordinate = int((screen_height / 2) - (frame_height / 2))
        self.cusdash.geometry(
            "{}x{}+{}+{}".format(frame_width, frame_height, x_cordinate, y_cordinate))

        myfont = ('Verdana', 10, 'bold')
        myfont2 = ('Verdana', 10)

        frame1 = LabelFrame(self.cusdash, bg="light yellow",
                            text="Customer Dashboard", height=250)
        frame1.pack(side=TOP, fill=BOTH)

        myprofile = Button(frame1, text="My Profile", font=myfont2, bg="white")
        myprofile.place(x=380, y=10, height=55, width=80)

        lblpickup = Label(frame1, text="Pick Up :",
                          font=myfont, bg="light yellow")
        lblpickup.place(x=10, y=80, width=100)

        pickuptxt = Entry(frame1, font=myfont2)
        pickuptxt.place(x=130, y=80)

        lbldrop = Label(frame1, text="Drop Off :",
                        font=myfont, bg="light yellow")
        lbldrop.place(x=487, y=80, width=100)

        droptxt = Entry(frame1, font=myfont2)
        droptxt.place(x=640, y=80)

        lbltime = Label(frame1, text="Pickup Time :",
                        font=myfont, bg="light yellow")
        lbltime.place(x=26, y=120, width=100)

        txttime = Entry(frame1, font=myfont2)
        txttime.place(x=130, y=120)

        lbldate = Label(frame1, text="Pickup Date :",
                        font=myfont, bg="light yellow")
        lbldate.place(x=500, y=120)

        txtdate = Entry(frame1, font=myfont2)
        txtdate.place(x=640, y=120)

        ridebtn = Button(frame1, text="Find a Ride", font=myfont2, bg="white")
        ridebtn.place(x=230, y=155)

        updatebtn = Button(frame1, text="Update", font=myfont2, bg="white")
        updatebtn.place(x=510, y=155)

        cancelbtn = Button(frame1, text="Cancel Ride",
                           font=myfont2, bg="white")
        cancelbtn.place(x=365, y=180)

        frame2 = Frame(self.cusdash, bg="light yellow", height=50)
        frame2.pack(side=BOTTOM, fill=BOTH)

        logout = Button(frame2, text="Log Out", font=myfont2, bg="white")
        logout.place(x=10, y=15, height=20, width=75)

        exitbtn = Button(frame2, text="Exit", font=myfont2, bg="white")
        exitbtn.place(x=800, y=15, height=20, width=75)

        table = ttk.Treeview(cusdash)
        table['columns'] = ('bid', 'pickup', 'dropoff',
                            'date', 'time', 'driverid', 'status')
        table.column('#0', width=0, stretch=0)
        table.column('bid', width=50)
        table.column('pickup', width=50)
        table.column('dropoff', width=50)
        table.column('date', width=50)
        table.column('time', width=50)
        table.column('driverid', width=50)
        table.column('status', width=50)

        table.heading('#0', text='', anchor=CENTER)
        table.heading('bid', text='Booking Id', anchor=CENTER)
        table.heading('pickup', text='Pick Up', anchor=CENTER)
        table.heading('dropoff', text='Drop Off', anchor=CENTER)
        table.heading('date', text='Pickup Date', anchor=CENTER)
        table.heading('time', text='Pickup Time', anchor=CENTER)
        table.heading('driverid', text='Driver Id', anchor=CENTER)
        table.heading('status', text='Booking Status', anchor=CENTER)

        table.pack(side=BOTTOM, fill=BOTH, expand=True)


if __name__ == '__main__':
    cusdash = Tk()
    CustomerDashboard(cusdash)
    cusdash.mainloop()
