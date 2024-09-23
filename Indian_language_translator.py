from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from googletrans import Translator
import webbrowser

window = Tk()
window.title("ಕ क  ক ક ਕ INDIAN LANGUAGE TRANSLATOR  க క ക କ क")
window.geometry("1080x600")
window.config(background="#FCF2FF")

def change_label():
    c1 = one_combo.get()
    c2 = two_combo.get()
    label_1.configure(text=c1.upper())
    label_2.configure(text=c2.upper())

def current_trans():
    text_ = text_1.get(1.0, END).strip()
    if text_:
        t1 = Translator()
        src_lang = lang_map[one_combo.get()]
        dest_lang = lang_map[two_combo.get()]
        trans_text = t1.translate(text_, src=src_lang, dest=dest_lang)
        trans_text = trans_text.text

        text_2.delete(1.0, END)
        text_2.insert(END, trans_text)
    else:
        messagebox.showwarning("Input Error", "Please enter text to translate.")

def translate_url():
    url = url_entry.get().strip()
    if url:
        dest_lang = lang_map[two_combo.get()]
        translated_url = f"https://translate.google.com/translate?hl={dest_lang}&sl=en&u={url}"
        webbrowser.open(translated_url)
    else:
        messagebox.showwarning("Input Error", "Please enter a URL to translate.")

trans_language = googletrans.LANGUAGES
lang_map = {value: key for key, value in trans_language.items()}
lang_a = list(trans_language.values())

one_combo = ttk.Combobox(window, values=lang_a, font="Arial 15 bold", state="readonly")
one_combo.place(x=110, y=20)
one_combo.set("english")

label_1 = Label(window, text="ENGLISH", font="Arial 31 bold", bg="#AC4AE6", width=17, bd=4, relief=GROOVE)
label_1.place(x=10, y=50)

f_1 = Frame(window, bg="white", bd="5")
f_1.place(x=10, y=118, width=440, height=210)

text_1 = Text(f_1, font="Arial 21", bg="white", relief=GROOVE, wrap=WORD)
text_1.place(x=0, y=0, width=430, height=200)

scrollbar_one = Scrollbar(f_1)
scrollbar_one.pack(side="right", fill="y")

text_1.config(yscrollcommand=scrollbar_one.set)
scrollbar_one.config(command=text_1.yview)

two_combo = ttk.Combobox(window, values=lang_a, font="Arial 15 bold", state="readonly")
two_combo.place(x=730, y=20)
two_combo.set("Select Language")

label_2 = Label(window, text="LANGUAGE", font="Arial 31 bold", bg="#AC4AE6", width=17, bd=4, relief=GROOVE)
label_2.place(x=600, y=50)

f_2 = Frame(window, bg="white", bd="5")
f_2.place(x=595, y=118, width=440, height=210)

text_2 = Text(f_2, font="Arial 21", bg="white", relief=GROOVE, wrap=WORD)
text_2.place(x=0, y=0, width=430, height=200)

scrollbar_two = Scrollbar(f_2)
scrollbar_two.pack(side="right", fill="y")

text_2.config(yscrollcommand=scrollbar_two.set)
scrollbar_two.config(command=text_2.yview)

button_translate = Button(window, text="TRANSLATE", font="Arial 16 bold italic", activebackground="blue",
                          cursor="hand2", bd=4, fg="white", bg="#53079D", command=current_trans)
button_translate.place(x=450, y=350)

url_entry = Entry(window, font="Arial 15 bold", width=40)
url_entry.place(x=300, y=400)

button_translate_url = Button(window, text="TRANSLATE URL", font="Arial 16 bold italic", activebackground="blue",
                              cursor="hand2", bd=4, fg="white", bg="#53079D", command=translate_url)
button_translate_url.place(x=450, y=440)

change_label()

window.mainloop()