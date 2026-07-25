from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    uname = uname_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning",message="Please enter all details ")

    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered :\n Email: {uname} \n Password :  {password}\n is it okay to save")
        if is_ok:
            f = open("data.txt", "a")
            f.write(f"\n {website} | {uname} | {password}")
            f.close()

            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

#window Setup
window = Tk()
window.title("Password Manager")
window.config(pady=50 , padx= 50)

#Canvas Setup
canvas = Canvas(height=200, width=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

#Website display
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

#username Display
uname_label = Label(text="Username/Email:")
uname_label.grid(row=2, column=0)

#password Display
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1,columnspan=2 ,sticky="w")
website_entry.focus()
website_entry.get()

uname_entry = Entry(width=35)
uname_entry.grid(row=2, column=1,columnspan=2,sticky="w")
uname_entry.insert(0,"rathodsoham999@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1,sticky="w")

# Buttons


generate_password = Button(text="Generate Password")
generate_password.grid(row=3, column=2,sticky="w")

add = Button(text="Add",width=36 , command=save)
add.grid(row=4, column=1, columnspan=2,sticky="w")



window.mainloop()