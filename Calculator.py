# © vanrobo 2024
# basically my first project 
# imports the Python Modules
import tkinter as tk # https://docs.python.org/3/library/tkinter.html
import ttkbootstrap as ttk # https://ttkbootstrap.readthedocs.io/en/latest/gettingstarted/installation/

# theme of the window ; can be customized
theme = 'darkly' # Try (light themes) cosmo, flatly, journal and (dark themes) solar, superhero, darkly, vapor
window = ttk.Window(themename=theme)

# Gets the X and Y location of the cursor and moves the window along with the cursor on holding down M1 
def movewin(event):
    window.geometry('+{0}+{1}'.format(event.x_root,event.y_root))

# updates the entry widget
def update_entry(entry,value):
    # get current text / value in the widget
    current_text = entry.get()
    clear_entry(entry)
    entry.insert(0 ,current_text + value)
    # inserts the current text followed by the new value into the entry widget

# evaluate the expression in the entry

def evaluate_entry(entry):
    try:
        # Takes the text in the entry widget and evaluates it as a python expression , and stores the result as a variable
        result=eval(entry.get())
        clear_entry(entry)
        entry.insert(0,str(result))
    except Exception as e:
        clear_entry(entry)
        entry.insert(0,"Error")

# clears the entry widget
def clear_entry(entry):
    entry.delete(0,tk.END)

# title of the Window (does not show up)
window.title(
    "Calculator"
)

# sets the window geometry
window.geometry(
    "435x700+500+500"
)

# disables the default window given by TKINTER
window.overrideredirect(1)

# makes a Close Button
text = ttk.Button(bootstyle='danger',text='X',command=lambda: window.destroy()).place(x=400,y=0,height=35,width=35)

# defines the rest of the title bar + credits
frame = ttk.Frame(window,bootstyle='dark')
label = ttk.Label(text='Calculator',bootstyle='inverse-dark')
credits = ttk.Label(text='© Vanrobo 2024',bootstyle='success')


# places the rest of the title bar + credits onto the window
label.place(x=10,y=0,height=35)
frame.place(x=0,y=0,width=400,height=35)
credits.place(x=10,y=675) 

# binds the titlebar to the movewin function which helps move the entire window
frame.bind('<B1-Motion>',movewin)

# places the entry widget 
entry = ttk.Entry(window,width=16,font=('Arial',24),bootstyle="info")
entry.place(x=35,y=50)

# A table for all the buttons 
buttons = [('7',20,150), ('8',120,150), ('9',220,150),('/',320,150),
           ('4',20,250), ('5',120,250), ('6',220,250),('*',320,250),
           ('1',20,350), ('2',120,350), ('3',220,350),('-',320,350),
           ('0',20,450), ('.',120,450), ('=',220,450),('+',320,450),
           ('C',20,550)
    ]

# places all the buttons depending on their use case
# the text refers to the text on the actual widget, and the X and Y represent their coordinates
for (text,x,y) in buttons:
    # checks if the button is supposed to evaluate, clear or update the entry.

    # evaluates the entry
    if text == '=':
        button = tk.Button(window,text=text,width=10,height=3, command=lambda e=entry:evaluate_entry(e))
    
    # these buttons clear the entry widget
    elif text == 'C':
        button = tk.Button(window,text=text,width=10,height=3, command=lambda e=entry:clear_entry(e))
    
    # these buttons update the entry widget
    else:
        button = tk.Button(window,text=text,width=10,height=3, command=lambda e=entry,val=text:update_entry(e,val))
    button.place(x=x,y=y)

# completes the window
window.mainloop()
