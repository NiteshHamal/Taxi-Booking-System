from tkinter import *
from backend.customerManagement import test
from tkinter.ttk import Treeview

app = Tk()
app.geometry("1000x1000")

search = Entry(app)
search.pack()


# adding driver Info table in driver frame ------------------------------------------------
customerTable = Treeview(app, height=25)
customerTable['columns'] = (
    'cid', 'fullname', 'address', 'email', 'phone', 'password', 'payment')
customerTable.column('#0', width=0, stretch=0)
customerTable.column('cid', width=50, anchor=CENTER)
customerTable.column('fullname', width=100, anchor=CENTER)
customerTable.column('address', width=100, anchor=CENTER)
customerTable.column('email', width=100, anchor=CENTER)
customerTable.column('phone', width=100, anchor=CENTER)
customerTable.column('password', width=100, anchor=CENTER)
customerTable.column('payment', width=100, anchor=CENTER)

customerTable.heading('#0', text='', anchor=CENTER)
customerTable.heading('cid', text='Driver ID', anchor=CENTER)
customerTable.heading('fullname', text='Fullname', anchor=CENTER)
customerTable.heading('address', text='Address', anchor=CENTER)
customerTable.heading('email', text='Email', anchor=CENTER)
customerTable.heading('phone', text='License No', anchor=CENTER)
customerTable.heading('password', text='Status', anchor=CENTER)
customerTable.heading('payment', text='Password', anchor=CENTER)

customerTable.pack(side=BOTTOM, fill=BOTH)


def nametest():
    customertest = search.get()
    testname = test(customertest)
    print(testname)
    for row in testname:
        customerTable.insert(parent='', index='end', values=(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6]))


btn = Button(app, text='search', command=nametest)
btn.pack()


app.mainloop()
