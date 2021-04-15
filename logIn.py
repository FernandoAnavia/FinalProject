from tkinter import *
from tkinter import messagebox
from db import *
from admin_Dashboard import OpenNewWindowAdmnDash
from logInSession import *

app = Tk()
app.title('LogIn')
app.geometry('400x250')

def NewLoginWindow():
    def Log_In():
        
        valName = userName_text.get()
        valPass = password_text.get()

        cursor = mydb.cursor()

        sql = "SELECT loginPassword, firstName, uTypeId FROM UserSystem where UserId = %s"

        try:

            cursor.execute(sql, (valName,))
            tablePass = cursor.fetchone()
            print(tablePass)


            try:
                for row in tablePass:

                    if (tablePass[0] == valPass):
                        UserDetails.UserID = valName
                        UserDetails.UserName = tablePass[1]                   
                        messagebox.showinfo('Success', 'Welcome ' + tablePass[1])
                        app.destroy()
                        OpenNewWindowAdmnDash()
                        break
                        

                    else:
                        messagebox.showerror('Error','Password not valid')
            
                        break
            except:
                messagebox.showerror('Error', 'User does not exist')

            
        except mysql.connector.Error as e:
            messagebox.showerror('Error',e)

        

    userName_text = StringVar()
    userName_label = Label(app, text='User ID', font=(12))
    userName_label.place(x = 30, y = 40)
    userName_entry = Entry(app, textvariable = userName_text)
    userName_entry.place(x = 180, y = 45)


    password_text = StringVar()
    password_label = Label(app, text='Password', font=(12))
    password_label.place(x = 30, y = 90)
    password_entry = Entry(app, show = "*", textvariable = password_text)
    password_entry.place(x = 180, y = 95)


    logIn_btn = Button(app, text='LogIn', width=12, command= Log_In)
    logIn_btn.place(x=200, y=160, anchor = "center")

    app.mainloop()

if __name__ == "__main__":
    NewLoginWindow()