from tkinter import *
from cryptography.fernet import Fernet
root = Tk()
root.title("Encryptor by sudo-nick")
root.geometry("400x300")
root.config(bg='black')
def en(l):
    l = int(l)
    s = str(e.get())
    key = Fernet.generate_key()
    f = Fernet(key)
    encpass = f.encrypt(s.encode())
    decpass = f.decrypt(encpass)
    show = encpass[20:20+l]
    ne = StringVar()
    ans = Entry(root, textvariable=ne, bg='black',
                fg='white', font=11, border=0, justify='center')
    ne.set(show) #used entry so you can copy enc pass
    ans.pack()
    # ans.configure(state='disabled')
    print("For cross-checking, original password : ", decpass)

l = Label(root, text="Enter the password : ", bg="black", border=0, font=("Jokerman", 11), fg="green2")
l.pack(pady=8)

e = Entry(root, fg='gray7', bg='white', border=0, font=("Comic Sans MS", 13), justify="center")
e.pack(pady=10)

l = Label(root, text="How long do you want your enc. pass to be : ", bg="black", border=0, font=("Jokerman", 11), fg="green2")
l.pack(pady=10)

lng = Entry(root, width='5', fg="gray7", bg="white", border=0, font=("Comic Sans MS", 13), justify="center")
lng.pack(pady=5)

btn = Button(root, text="Encrypt", width=10, height=2, command=lambda: en(lng.get()), fg='cyan', bg='black', activeforeground='yellow', activebackground='black')
btn.pack(pady=8)

root.mainloop()
