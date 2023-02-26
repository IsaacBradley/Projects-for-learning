from tkinter import Tk, Label, X, Button
from tkinter import ttk
from tkinter import messagebox

class Einstein(Tk):
 def __init__(self):
  super(Einstein, self).__init__()
  self.title('Machiavelli')
  self.minsize(500, 500)
  self.resizable(0, 0)
  #self.overrideredirect(1)
  self.config(bg = 'steelblue')
  
def main():
 app = Einstein()

 lab = Label(text = 'TYPICAL CODE SNIPPET', fg = '#000', bg = 'powderblue').pack(fill = X)
 
 def disp():
  messagebox.showinfo(title = 'Einstein', message = 'You selected ' + com.get())
 
 courses = ["Medicine", "Engineering", "Education", "Nursing", "Computer Science"]
 com  = ttk.Combobox(font = ('Sans-serif', 20), value = courses)
 com.set("Kindly enter your choice")
 #com.bind("<<ComboboxSelected>>", disp)
 com.pack()
 
 button = Button(font = ("arial", 10),bg = '#000', fg = '#fff', text = "Submit", width = 20, height = 2, padx = 12, pady = 10, bd = 0)
 button.config(command = disp)
 button.pack()
 
 app.mainloop()
 
if __name__ == '__main__':
 main()