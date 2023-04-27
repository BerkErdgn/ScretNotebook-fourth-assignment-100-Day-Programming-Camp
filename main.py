import tkinter
from cryptography.fernet import Fernet
from tkinter import messagebox
import base64, hashlib


def errorMessage(error_message):
    messagebox.showinfo("Information", error_message)


def gen_fernet_key(passcode:bytes) -> bytes:
    assert isinstance(passcode, bytes)
    hlib = hashlib.md5()
    hlib.update(passcode)
    return base64.urlsafe_b64encode(hlib.hexdigest().encode('latin-1'))


def encryption():
    secret_title = title_entry.get()
    secret_text = secret_not_text.get("1.0", tkinter.END)
    secret_key = mater_key_entry.get()

    print(secret_title)
    print(secret_text)
    print(secret_key)

    if secret_title == "" or secret_text == "\n" or secret_key == "":
        error_message = "Please fill in all the blanks"
        errorMessage(error_message=error_message)

    else:
        key = gen_fernet_key(secret_key.encode('utf-8'))
        fernet = Fernet(key)
        cypher_text = fernet.encrypt(secret_text.encode('utf-8'))
        cypher_text_string = cypher_text.decode("utf-8")
        with open("secretnot.txt", mode="a") as secretFile:
            secretFile.write(f"\n{secret_title}\n{cypher_text_string}\n")
        secret_not_text.delete(1.0, tkinter.END)
        title_entry.delete(0,tkinter.END)
        mater_key_entry.delete(0,tkinter.END)
        error_message = "Successfully saved"
        errorMessage(error_message)


def decryption():
    try:
        cypher_text = secret_not_text.get("1.0", tkinter.END)
        secret_key = mater_key_entry.get()
        key = gen_fernet_key(secret_key.encode('utf-8'))
        fernet = Fernet(key)
        decr_data = fernet.decrypt(cypher_text).decode('utf-8')
        secret_not_text.delete(1.0, tkinter.END)
        secret_not_text.insert(1.0, decr_data)

    except:
        error_message = "Wrong password, please try again"
        errorMessage(error_message)


window = tkinter.Tk()
window.title("Secret Notebook")
window.config(padx=50, pady=50)

FONT_ONE = ("Arial", 10)
WIDTH_ENTRY = 35

top_secret_pic = tkinter.PhotoImage(file="topsecret.png")
pic_label = tkinter.Label(image=top_secret_pic, bg="#f0f0f0")
pic_label.pack()

title_label = tkinter.Label(text="Enter your title", font=FONT_ONE, pady=5)
title_label.pack()

title_entry = tkinter.Entry(width=WIDTH_ENTRY)
title_entry.focus()
title_entry.pack()

secret_not_label = tkinter.Label(text="Enter your secret", font=FONT_ONE, pady=5)
secret_not_label.pack()

secret_not_text = tkinter.Text(width=45)
secret_not_text.pack()

mater_key_label = tkinter.Label(text="Enter master key", font=FONT_ONE, pady=5)
mater_key_label.pack()

mater_key_entry = tkinter.Entry(width=WIDTH_ENTRY)
mater_key_entry.pack()

save_button = tkinter.Button(text="Save & Encrypt", command=encryption)
save_button.config(pady=5)
save_button.pack()

decrypt_button = tkinter.Button(text="Decrypt", command=decryption)
decrypt_button.config(pady=5)
decrypt_button.pack()

window.mainloop()
