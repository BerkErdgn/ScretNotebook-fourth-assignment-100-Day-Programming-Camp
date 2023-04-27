import tkinter

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

secret_not_entry = tkinter.Text(width=45)
secret_not_entry.pack()

mater_key_label = tkinter.Label(text="Enter master key", font=FONT_ONE, pady=5)
mater_key_label.pack()

mater_key_entry = tkinter.Entry(width=WIDTH_ENTRY)
mater_key_entry.pack()

save_button = tkinter.Button(text="Save & Encrypt")
save_button.config(pady=5)
save_button.pack()

decrypt_button = tkinter.Button(text="Decrypt")
decrypt_button.config(pady=5)
decrypt_button.pack()

window.mainloop()
