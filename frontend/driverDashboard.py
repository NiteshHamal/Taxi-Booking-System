from tkinter import *
from PIL import ImageTk, Image
from frontend import signin
from middleware import Global


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

        # right frame
        right_bar = Frame(self.root, bg="#4CD964", width=350)
        right_bar.pack(side=LEFT, fill=BOTH)

        # image
        profile = ImageTk.PhotoImage(Image.open(
            "H:\\College\\Sem-2\\python assignment\\Taxi Booking System\\image\\profile.png"))
        profile_label = Label(right_bar, image=profile, bg="#4CD964")
        profile_label.image = profile
        profile_label.place(x=90, y=50)

        def changeStatus():
            global is_on
            # Check if it is on or off
            if is_on:
                active.config(image=off)
                active_label.config(text="Inactive")
                is_on = FALSE
            else:
                active.config(image=on)
                active_label.config(text="Active")
                is_on = TRUE

        on = ImageTk.PhotoImage(Image.open(
            "H:\\College\\Sem-2\\python assignment\\Taxi Booking System\\image\\on.png"))
        off = ImageTk.PhotoImage(Image.open(
            "H:\\College\\Sem-2\\python assignment\\Taxi Booking System\\image\\off.png"))
        active = Button(right_bar, command=changeStatus, image=on,
                        relief=FLAT, bd=0, bg="#4CD964", activebackground="#4CD964")
        active.image = on
        active.place(x=110, y=300)

        active_label = Label(right_bar, text=" Active ",
                             font=font1, bg="#4CD964")
        active_label.place(x=125, y=390)

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
        logout_btn.place(x=110, y=650)

        home_frame = Frame(self.root)
        home_frame.pack(side=RIGHT, fill=BOTH, expand=TRUE)

        did_txt = Entry(home_frame)
        # did_txt.insert(0, Global.currentUser[0])


if __name__ == '__main__':
    root = Tk()
    DriverDashboard(root)
    root.mainloop()
