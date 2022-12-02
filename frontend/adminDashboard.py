from tkinter import *
from PIL import ImageTk, Image


class AdminDashboard:

    def __init__(self, root):
        self.root = root
        self.root.title("Admin Dashboard")
        self.root.geometry("550x500")  # size of the window
        self.root.state('zoomed')  # windows on zoomed / full-screen size
        self.root.config(background="#CECED2")  # background color change

        def change_home():  # function for home button
            home_frame.pack(side=RIGHT, fill=BOTH, expand=TRUE)
            driver.pack_forget()
            customer.pack_forget()

        def change_driver():  # function for driver management button
            driver.pack(side=RIGHT, fill=BOTH, expand=TRUE)
            home_frame.pack_forget()
            customer.pack_forget()

        def change_customer():  # function for customer management button
            customer.pack(side=RIGHT, fill=BOTH, expand=TRUE)
            driver.pack_forget()
            home_frame.pack_forget()

        # font used in the button in navbar
        nav_font = ('Times New Roman', 25, "bold")

        # first frame / navbar
        navbar = Frame(self.root, bg="#4CD964", width=350)
        navbar.pack(side=LEFT, fill=BOTH)

        # image
        profile = ImageTk.PhotoImage(Image.open(
            "H:\\College\\Sem-2\\python assignment\\Taxi Booking System\\image\\profile.png"))
        profile_label = Label(navbar, image=profile, bg="#4CD964")
        profile_label.image = profile
        profile_label.place(x=100, y=50)

        # home button
        home_btn = Button(navbar, text="Home", command=change_home,
                          font=nav_font, bg="#4CD964", relief=RIDGE)
        home_btn.place(x=110, y=210)

        # driver manage button
        driver_button = Button(navbar, text="Manage Driver",
                               command=change_driver, font=nav_font, bg="#4CD964", relief=RIDGE)
        driver_button.place(x=50, y=300)

        # customer manage button
        customer_button = Button(navbar, text="Manage Customer",
                                 command=change_customer, font=nav_font, bg="#4CD964", relief=RIDGE)
        customer_button.place(x=30, y=390)

        # logout button with image
        logout = ImageTk.PhotoImage(Image.open(
            "H:\\College\\Sem-2\\python assignment\\Taxi Booking System\\image\\logout.png"))
        logout_btn = Button(navbar, image=logout, bg="#4CD964",
                            relief=FLAT, activebackground="#4CD964")
        logout_btn.image = logout
        logout_btn.place(x=110, y=650)

        # second frame
        # home frame of admin
        home_frame = Frame(self.root, bg="red")
        home_frame.pack(side=RIGHT, fill=BOTH, expand=TRUE)

        # driver management frame
        driver = Frame(self.root, bg="black")

        # customer management frame
        customer = Frame(self.root, bg="blue")


if __name__ == '__main__':
    root = Tk()
    AdminDashboard(root)
    root.mainloop()
