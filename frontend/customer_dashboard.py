from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry


class Cus_Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Dashboard")
        self.root.geometry("550x500")  # size of the window
        self.root.state('zoomed')  # windows on zoomed / full-screen size
        self.root.config(background="#CECED2")  # background color change

        font1 = ('Cooper Black', 30, "bold")
        font2 = ('Cordia New', 14)


        # First frame
        frame1 = Frame(root, bg="#4CD964", height=100)
        frame1.pack(side=TOP, fill=BOTH)

        title_txt = Label(frame1, text="Taxi Booking", font=(
            'Cooper Black', 30, "bold", UNDERLINE), bg="#4CD964")
        title_txt.pack(anchor=CENTER, expand = 'yes', pady=15)




        # Second Frame
        frame2 = Frame(root, height=760)
        frame2.pack(fill=BOTH, expand='yes')

        style = ttk.Style()
        style.theme_create( "MyStyle", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
        "TNotebook.Tab": {"configure": {"padding": [20, 5] },}})

        style.theme_use("MyStyle")

         # tab
        main_tab = ttk.Notebook(frame2)
        home = ttk.Frame(main_tab)
        history = ttk.Frame(main_tab)
        profile = ttk.Frame(main_tab)

        # adding tab to main_tab
        main_tab.add(home, text='Home')
        main_tab.add(history, text='History')
        main_tab.add(profile, text='Profile')

        # main tab pack
        main_tab.pack(side=TOP, fill=BOTH, expand=TRUE)

        # home tab
        home_frame = Frame(home)
        home_frame.pack(fill=BOTH, expand=TRUE)

        # adding widgets in home tab
        booking_txt = Label(home_frame, text="Booking", font=font1)
        booking_txt.place(x=170, y=50)

        pickaddress_frame = LabelFrame(home_frame, text="PickUp Address")
        pickaddress_frame.place(x=150, y=150)

        pickaddress = Entry (pickaddress_frame, text="", font=font2, relief=RAISED)
        pickaddress.pack()

        dropaddress_frame = LabelFrame(home_frame, text="Drop Address")
        dropaddress_frame.place(x=150, y=200)

        dropaddress = Entry(dropaddress_frame, text="", font=font2, relief=RAISED)
        dropaddress.pack()

        date_frame = LabelFrame(home_frame, text="Pickup Date")
        date_frame.place(x=150,y=250)

        pickupdate = DateEntry(date_frame, width=18, font=font2)
        pickupdate.pack()





if __name__ == '__main__':
    root = Tk()
    Cus_Dashboard(root)
    root.mainloop()
