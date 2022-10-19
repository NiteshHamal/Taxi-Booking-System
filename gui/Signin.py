from tkinter import *

signin = Tk()
signin.title("SignIn")
signin.geometry("550x500")  # size of the window
signin.state('zoomed')  # windows on zoomed / full-screen size
signin.resizable(False,False)  # windows resizable false
signin.config(background="#CECED2")  # background color change

font1=('Cooper Black',30,"bold")
font2=('Cordia New',14)
font3=('Times New Roman',25,"bold")

# First frame
frame1=Frame(signin, bg="#EFEFF4", height=650, width=600)
frame1.place(x=175, y=100)

signin_txt=Label(frame1, text="Sign in", font=font1)
signin_txt.place(x=200, y=160)

email_txt=Entry(frame1, text="",font=font2, relief=RAISED)
email_txt.place(x=175, y=250)

password=Entry(frame1, text="", font=font2, relief=RAISED)
password.place(x=175, y=300)

forget_txt=Label(frame1, text="Forget your password?", font=font2)
forget_txt.place(x=190, y=350)

btn_signin=Button(frame1, text="Submit",font=font3, relief=GROOVE, command=input, bg="#4CD964", fg="#EFEFF4")
btn_signin.place(x=220,y=400)

# Second Frame
frame2 = Frame(signin, bg="#4CD964", height=650,width=600)
frame2.place(x=775,y=100)

signup_lbl=Label(frame2, text="Sign UP",bg="#4CD964", font=font1, fg="#EFEFF4")
signup_lbl.place(x=200, y=200)

signup_txt=Label(frame2, text="Sign up here if you don't have account", bg="#4CD964", font=font2)
signup_txt.place(x=125, y=300)

btn_signup=Button(frame2, text="SIGN UP",font=font3, relief=GROOVE, command=input, bg="#EFEFF4")
btn_signup.place(x=200,y=350)


signin.mainloop()
