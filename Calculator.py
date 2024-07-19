import tkinter as tk
import ttkbootstrap as ttk
window = ttk.Window(themename='darkly')

def movewin(event):
    window.geometry('+{0}+{1}'.format(event.x_root,event.y_root))

def update_entry(entry,value):
    current_text = entry.get()
    clear_entry(entry)
    entry.insert(0 ,current_text + value)

def evaluate_entry(entry):
    try:
        result=eval(entry.get())
        clear_entry(entry)
        entry.insert(0,str(result))
    except Exception as e:
        clear_entry(entry)
        entry.insert(0,"Error")

def clear_entry(entry):
    entry.delete(0,tk.END)


window.title(
    "Testing!"
)

window.geometry(
    "435x700+500+500"
)

window.overrideredirect(1)

text = ttk.Button(bootstyle='danger',text='X',command=lambda: window.destroy()).place(x=400,y=0,height=35,width=35)

frame = ttk.Frame(window,bootstyle='dark')

frame.place(x=0,y=0,width=400,height=35)

label = ttk.Label(text='Calculator',bootstyle='inverse-dark')

label.place(x=10,y=0,height=35)

credits = ttk.Label(text='Made by Vanrobo',bootstyle='success')

credits.place(x=10,y=675) 

frame.bind('<B1-Motion>',movewin)

entry = ttk.Entry(window,width=16,font=('Arial',24),bootstyle="info")
entry.place(x=35,y=50)

buttons = [('7',20,150), ('8',120,150), ('9',220,150),('/',320,150),
           ('4',20,250), ('5',120,250), ('6',220,250),('*',320,250),
           ('1',20,350), ('2',120,350), ('3',220,350),('-',320,350),
           ('0',20,450), ('.',120,450), ('=',220,450),('+',320,450),
           ('C',20,550)
    ]

for (text,x,y) in buttons:
    if text == '=':
        button = tk.Button(window,text=text,width=10,height=3, command=lambda e=entry:evaluate_entry(e))

    elif text == 'C':
        button = tk.Button(window,text=text,width=10,height=3, command=lambda e=entry:clear_entry(e))
    
    else:
        button = tk.Button(window,text=text,width=10,height=3, command=lambda e=entry,val=text:update_entry(e,val))
    button.place(x=x,y=y)



# buttontest=ttk.Button(text="1")

# buttontest.place(x=20,y=150,width=75,height=75)

# buttontest2=ttk.Button(text="2")

# buttontest2.place(x=20,y=250,width=75,height=75)

window.mainloop()

