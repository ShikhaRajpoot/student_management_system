from tkinter import *
from tkinter import messagebox
import mysql.connector

con = mysql.connector.Connect(host='localhost', user='root', password='root', database='shikha')
cursor = con.cursor()


def insert_data(r, n, m):
    if r.get() == '' or n.get() == '' or m.get() == '':
        messagebox.showerror('ALERT', 'please insert all the field')
    else:
        query = 'insert into studentdata values (%s, %s, %s)'
        values = (r.get(), n.get(), m.get())
        cursor.execute(query, values)
        con.commit()
        messagebox.showinfo('insert', 'Data inserted successfully')

    r.delete(0, 'end')
    n.delete(0, 'end')
    m.delete(0, 'end')


def search_data(rno_entry, name_entry, mark_entry):
    query = 'select * from studentdata where rno=%s'
    values = (rno_entry.get(),)
    cursor.execute(query, values)
    row = cursor.fetchone()

    name_entry.delete(0, 'end')
    mark_entry.delete(0, 'end')

    name_entry.insert(0, row[1])
    mark_entry.insert(0, row[2])


def update_data(n, m, r):
    query = 'update studentdata set name=%s, marks = %s where rno= %s'
    values = (n.get(), m.get(), r.get())
    cursor.execute(query, values)
    con.commit()
    messagebox.showinfo('Update', 'Data Updated Successfully...')

    n.delete(0, 'end')
    m.delete(0, 'end')
    r.delete(0, 'end')


def delete_data(rno_entry, student_entry, student_marks):
    query = 'delete from studentdata where rno=%s'
    value = (rno_entry.get(),)
    cursor.execute(query, value)
    con.commit()
    messagebox.showinfo('Delete', 'Data Deleted successfully....')

    rno_entry.delete(0, 'end')
    student_entry.delete(0, 'end')
    student_marks.delete(0, 'end')


def student_data_table():
    student_frame = Frame()
    student_frame.pack(fill=BOTH, expand=True)

    student_rno_label = Label(student_frame, text='Enter Rno', font=('cambria', 18))
    student_rno_label.pack()
    student_rno_label.place(x=5, y=20)

    student_rno = Entry(student_frame, font=('cambria', 18))
    student_rno.pack()
    student_rno.place(x=140, y=20)

    student_name_label = Label(student_frame, text='Enter Name', font=('cambria', 18))
    student_name_label.pack()
    student_name_label.place(x=5, y=70)

    student_name = Entry(student_frame, font=('cambria', 18))
    student_name.pack()
    student_name.place(x=140, y=70)

    student_marks_label = Label(student_frame, text='Enter Marks', font=('cambria', 18))
    student_marks_label.pack()
    student_marks_label.place(x=5, y=120)

    student_marks = Entry(student_frame, font=('cambria', 18))
    student_marks.pack()
    student_marks.place(x=140, y=120)

    insert_button = Button(student_frame, text='Insert', font=('cambria', 18),
                           command=lambda: insert_data(student_rno, student_name, student_marks))
    insert_button.pack()
    insert_button.place(x=10, y=180)

    search_button = Button(student_frame, text='Search', font=('cambria', 18),
                           command=lambda: search_data(student_rno, student_name, student_marks))
    search_button.pack()
    search_button.place(x=150, y=180)

    update_button = Button(student_frame, text='Update', font=('cambria', 18),
                           command=lambda: update_data(student_name, student_marks, student_rno))
    update_button.pack()
    update_button.place(x=280, y=180)

    delete_button = Button(student_frame, text='Delete', font=('cambria', 18),
                           command=lambda: delete_data(student_rno, student_name, student_marks))
    delete_button.pack()
    delete_button.place(x=150, y=240)


def validate_signin_data(u, p, d):
    query = 'select * from userdata where name=%s and password=%s'
    values = (u.get(), p.get())
    cursor.execute(query, values)
    data = cursor.fetchall()
    if len(data) > 0:
        messagebox.showinfo('signin', 'signin successful....')
        d.destroy()
        student_data_table()
    else:
        messagebox.showerror('signin', 'signin failed....')
        d.destroy()
        home()


def sign_in():
    sign_in_frame = Frame()
    sign_in_frame.pack()

    user_label = Label(sign_in_frame, text='User Name', font=('cambria', 18))
    user_label.pack()

    user = Entry(sign_in_frame, font=('cambria', 18))
    user.pack()

    password_label = Label(sign_in_frame, text='Password', font=('cambria', 18))
    password_label.pack()

    password = Entry(sign_in_frame, show='*', font=('cambria', 18))
    password.pack()

    signin_button = Button(sign_in_frame, text='signin', font=('cambria', 18),
                           command=lambda: validate_signin_data(user,
                                                                password, sign_in_frame))
    signin_button.pack()


def insert_signup_data(n, p, e, f):
    if n.get() == '' or e.get() == '' or p.get() == '':
        messagebox.showerror('error', 'please enter all the fields')
    else:
        query = "insert into userdata values (%s, %s, %s)"
        values = (n.get(), e.get(), p.get())
        cursor.execute(query, values)
        con.commit()
        messagebox.showinfo('inserted', 'data inserted successfully..')
        f.destroy()
        home()


def sign_up():
    signup_frame = Frame()
    signup_frame.pack()

    user_label = Label(signup_frame, text='User Name', font=('cambria', 18))
    user_label.pack()

    user = Entry(signup_frame, font=('cambria', 18))
    user.pack()

    email_label = Label(signup_frame, text='Email', font=('cambria', 18))
    email_label.pack()

    email = Entry(signup_frame, font=('cambria', 18))
    email.pack()

    password_label = Label(signup_frame, text='password', font=('cambria', 18))
    password_label.pack()

    password = Entry(signup_frame, show='*', font=('cambria', 18))
    password.pack()

    sign_up_button = Button(signup_frame, text='Sign Up', font=('cambria', 18),
                            command=lambda: insert_signup_data(user, password, email, signup_frame))

    sign_up_button.pack()


def home():
    home_frame = Frame()
    home_frame.pack(fill=BOTH, expand=True)
    home_frame.place(x=150, y=50)

    button_sign_in = Button(home_frame, text='Sign in', font=('cambria', 18), command=sign_in)
    button_sign_in.pack()

    button_sign_up = Button(home_frame, text='Sign up', font=('cambria', 18), command=sign_up)
    button_sign_up.pack()


root = Tk()
root.geometry('400x300')
root.resizable(0, 0)
home()
root.mainloop()
