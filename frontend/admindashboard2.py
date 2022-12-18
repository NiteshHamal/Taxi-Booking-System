import sys
import tkinter
from tkinter import *
from sqlalchemy import create_engine
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pymysql
import mysql.connector
import pandas
from tkinter import ttk
from PIL import ImageTk, Image
from backend.adminManagement import adminhistory
from backend.bookingManagement import requestBooking1167
from backend.driverManagement import driverManage


class AdminDashboard():
    def __init__(self, root):
        self.root=root

        self.root.title("Admin Dashboard")

        screenwidth=self.root.winfo_screenwidth()
        screenheight=self.root.winfo_screenheight()
        self.root.minsize(screenwidth,screenheight)
        self.root.state('zoomed')
        # self.root.iconbitmap("H:\\College\\Sem-2\\python assignment\\Taxi Booking System\\image\\Iconsmind-Outline-Taxi-2.ico")


        sidefont=('Times New Roman', 18,'normal')

        sqlEngine=create_engine('mysql+pymysql://root:@localhost/taxi')
        db_connection=sqlEngine.connect()

        upframe=Frame(self.root, height=100, bg="#4CD964")
        upframe.pack(side=TOP, fill=BOTH)

        titlelabel=Label(self.root, text="Welcome Nitesh Hamal",bg="#4CD964", font=('Times New Roman',25,'bold'))
        titlelabel.place(x=20, y=30)

        sideframe=Frame(self.root, width=400, bg='#e2f3f5')
        sideframe.pack(side=LEFT, fill=BOTH)

        image = Image.open("H:\\College\\Sem-2\\python assignment\\Taxi Booking System\\image\\Order ride-bro.png")
        image = image.resize((300, 300))
        image = ImageTk.PhotoImage(image)
        Image_Label = Label(sideframe, image=image, bg='#e2f3f5')
        Image_Label.image = image
        Image_Label.place(x=30, y=20)

        titlelbl=Label(sideframe, text="Taxi Booking System", bg='#e2f3f5', font=('Times New Roman', 16,'bold'))
        titlelbl.place(x=80, y=320)

        def assigndriver():
            root=tkinter.Toplevel()
            root.title("Assign Driver | Admin Dashboard")
            frame_width=1000
            frame_height=500
            screen_width=root.winfo_screenwidth()
            screen_height=root.winfo_screenheight()
            x_cordinate=int((screen_width/2)-(frame_width/2))
            y_cordinate=int((screen_height/2)-(frame_height/2))
            root.geometry("{}x{}+{}+{}".format(frame_width, frame_height, x_cordinate+120, y_cordinate+70))
            root.mainloop()

        assignbtn=Button(sideframe, text="Assign Driver",command=assigndriver,font=sidefont,  bg='#e2f3f5', highlightthickness=0, borderwidth=0)
        assignbtn.place(x=100, y=400)

        customerbtn=Button(sideframe, text="Customer Management", font=sidefont,  bg='#e2f3f5', highlightthickness=0, borderwidth=0)
        customerbtn.place(x=55, y=450)

        driverbtn=Button(sideframe, text="Driver Management", font=sidefont,  bg='#e2f3f5', highlightthickness=0, borderwidth=0)
        driverbtn.place(x=70, y=500)

        passwordbtn=Button(sideframe, text="Change Password", font=sidefont,  bg='#e2f3f5', highlightthickness=0, borderwidth=0)
        passwordbtn.place(x=75, y=550)

        logoutbtn=Button(sideframe, text="Logout", font=sidefont,  bg='#e2f3f5', highlightthickness=0, borderwidth=0)
        logoutbtn.place(x=120, y=600)

        def exit():
            sys.exit()

        exitbtn=Button(sideframe, text="Exit", font=sidefont,command=exit,  bg='#e2f3f5', highlightthickness=0, borderwidth=0)
        exitbtn.place(x=130, y=650)

        graphframe=Frame(self.root,height=400, bg='#ffffff')
        graphframe.pack(side=TOP, fill=BOTH)




        query='SELECT *,count(bookingid) as ID FROM booking group by status limit 6'
        df=pandas.read_sql(query, db_connection, index_col="status")
        fig=df.plot.pie(title="Booking Report",y="ID",figsize=(4,4),legend=True, autopct='%1.0f%%').get_figure()

        plot=FigureCanvasTkAgg(fig, graphframe)
        plot.get_tk_widget().pack(side=LEFT, fill=BOTH, padx=(40,0))

        query2='SELECT *,count(bookingid) as ID FROM booking group by pickup_date limit 6'
        df2=pandas.read_sql(query2, db_connection, index_col="pickup_date")
        fig2=df2.plot.bar(title="Booking Report",y="ID",figsize=(5,4),).get_figure()
        plot=FigureCanvasTkAgg(fig2, graphframe)
        plot.get_tk_widget().place(relx=0.5, rely=0.5,anchor=CENTER )

        query3='SELECT *,count(bookingid) as ID FROM booking group by pickup_date limit 6'
        df3=pandas.read_sql(query3, db_connection, index_col="pickup_date")
        fig3=df3.plot.line(title="Booking Report",y="ID",figsize=(5,4),).get_figure()
        plot=FigureCanvasTkAgg(fig3, graphframe)
        plot.get_tk_widget().pack(side=RIGHT, fill=BOTH)


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

        maintab=ttk.Notebook(self.root)
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
    root=Tk()
    AdminDashboard(root)
    root.mainloop()
