from tkinter import Tk, StringVar, Entry, Label, Button


class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.title('Einstein')
        self.config(bg='#000')
        self.geometry('500x500+0+0')


def main():
    app = Window()

    entry = StringVar()
    Entry(font=('calibri', 16), textvariable=entry).pack()
    entry.set('Enter name here')

    label = Label(font=('Helvetica', 16))
    label.config(bg='#000', fg='#fff')
    label.pack()

    def submit():
        label.config(text='Hello ' + entry.get())

    Button(font=('Helvetica', 16), text='Submit', command=submit).pack()

    app.mainloop()


if __name__ == '__main__':
    main()
