from tkinter import *


class DriverDashboard:

    def __init__(self, root):
        self.root = root
        self.root.title("Driver Dashboard")
        self.root.geometry("550x500")  # size of the window
        self.root.state('zoomed')  # windows on zoomed / full-screen size


if __name__ == '__main__':
    root = Tk()
    DriverDashboard(root)
    root.mainloop()
