import time
import tkinter as tk
from tkinter import ttk
from tkinter import Scale
import psutil
from tkcalendar import Calendar
from datetime import datetime
from tkinter import Text, Scrollbar
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math

# Function to get battery percentage
def get_battery_percentage():
    battery = psutil.sensors_battery()
    return str(battery.percent)

# Function to get and set volume
def set_volume(val):
    print(f'Setting volume to {val}')
    # Implement volume control here

# Function to get and set brightness
def set_brightness(val):
    print(f'Setting brightness to {val}')
    # Implement brightness control here

# Function to switch to the next page
def next_page():
    notebook.select(notebook.index("current") + 1)

# Function to switch to the previous page
def previous_page():
    notebook.select(notebook.index("current") - 1)

def tick(time1='', date1=''):
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # get the current date
    date2 = datetime.now().strftime('%Y-%m-%d')
    # if time string has changed, update it
    if time2 != time1 or date2 != date1:
        time1 = time2
        date1 = date2
        clock.config(text='Date: ' + date2 + '\nTime: ' + time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    clock.after(200, tick)

def plot_cosine():
    x = range(0, 360)
    y = [math.cos(math.radians(i)) for i in x]
    plot_graph(x, y, "Cosine Wave")

def plot_sine():
    x = range(0, 360)
    y = [math.sin(math.radians(i)) for i in x]
    plot_graph(x, y, "Sine Wave")

root = tk.Tk()
notebook = ttk.Notebook(root)

tab1 = ttk.Frame(notebook)
notebook.add(tab1, text='Tab 1')

tab2 = ttk.Frame(notebook)
notebook.add(tab2, text='Tab 2')

# Create another frame for the wave plot
wave_frame = ttk.Frame(root)

def plot_graph(x, y, title):
    fig = Figure(figsize=(5, 4), dpi=100)
    plot = fig.add_subplot(1, 1, 1)
    plot.plot(x, y)
    plot.set_title(title)
    
    canvas = FigureCanvasTkAgg(fig, master=wave_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


# Create the notebook with tabs
notebook = ttk.Notebook(root)
notebook.grid(row=3, column=0, columnspan=6, pady=10, padx=10, sticky="nsew")

# Add the wave plot to the notebook
notebook.add(wave_frame, text='Wave Plot')

root.title("General Purpose App")

# Create a frame for the heading and battery percentage
header_frame = tk.Frame(root)
header_frame.grid(row=0, column=0, columnspan=6, pady=10, padx=10, sticky="nsew")

# Create a label for the heading
heading = tk.Label(header_frame, text="App for general use \n made by Harshit Prashant Dhanwalkar", font=('times', 20, 'bold'))
heading.grid(row=0, column=0, columnspan=2)

# Battery percentage
battery_percentage = tk.Label(root, text="Battery: " + get_battery_percentage() + "%", font=('times', 15, 'bold'), bg='black', fg='white')
battery_percentage.grid(row=1, column=0, pady=10, padx=10, sticky="nsew")

# Clock
clock_frame = ttk.Frame(root)
clock = tk.Label(clock_frame, font=('times', 15, 'bold'), bg='black', fg='white')
clock.pack(fill='both', expand=0)
clock_frame.grid(row=1, column=1, columnspan=2, pady=10, padx=10, sticky="nsew")

# Calendar
calendar_frame = ttk.Frame(root)
cal = Calendar(calendar_frame, selectmode='none', font=('times', 10, 'bold'), bg='black', fg='white')
date = cal.datetime.today() + cal.timedelta(days=-2)
cal.calevent_create(date, 'Hello World', 'message')
cal.pack(fill="both", expand=True)
calendar_frame.grid(row=2, column=0, columnspan=1, pady=10, padx=10, sticky="nsew")

# Calculator
calculator_frame = ttk.Frame(root)
entry = ttk.Entry(calculator_frame, font=('times', 20, 'bold'))
entry.grid(row=2, column=1, columnspan=7, pady=10, padx=10, sticky="nsew")

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+', '='
]

def calculate():
    try:
        entry_string = entry.get()
        result = eval(entry_string)
        entry.delete(0, 'end')
        entry.insert('end', str(result))
    except Exception as e:
        entry.delete(0, 'end')
        entry.insert('end', 'Error')

row_val = 3
col_val = 3
for button in buttons:
    if button != '=':
        ttk.Button(calculator_frame, text=button, command=lambda button=button: entry.insert('end', button)).grid(row=row_val, column=col_val, pady=5, padx=5, sticky="nsew")
    else:
        ttk.Button(calculator_frame, text=button, command=calculate).grid(row=row_val, column=col_val, pady=5, padx=5, sticky="nsew")
    col_val += 1
    if col_val > 6:
        col_val = 3
        row_val += 1

calculator_frame.grid(row=2, column=1, rowspan=2, columnspan=2, pady=10, padx=10, sticky="nsew")

# Create an empty row between elements
tk.Label(root, text="").grid(row=2, column=0)

# Volume control
volume_frame = ttk.Frame(root)
volume_label = tk.Label(volume_frame, text="Volume", font=('times', 10, 'bold'), bg='black', fg='white')
volume = Scale(volume_frame, from_=0, to=100, orient=tk.VERTICAL, command=set_volume)
volume.set(50)  # Set initial volume
volume_label.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")
volume.grid(row=2, column=0, pady=10, padx=10, sticky="nsew")
volume_frame.grid(row=2, column=5, pady=10, padx=10, sticky="nsew")

# Create an empty row between elements
tk.Label(root, text="").grid(row=2, column=6)

# Brightness control
brightness_frame = ttk.Frame(root)
brightness_label = tk.Label(brightness_frame, text="Brightness", font=('times', 10, 'bold'), bg='black', fg='white')
brightness = Scale(brightness_frame, from_=0, to=100, orient=tk.VERTICAL, command=set_brightness)
brightness.set(50)  # Set initial brightness
brightness_label.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")
brightness.grid(row=2, column=0, pady=10, padx=10, sticky="nsew")
brightness_frame.grid(row=2, column=7, pady=10, padx=10, sticky="nsew")

# Notepad
notepad_frame = ttk.Frame(root)
notepad = Text(notepad_frame, font=('times', 10, 'bold'), bg='black', fg='white')
notepad.pack(fill='both', expand=2)
scrollbar = Scrollbar(notepad_frame, command=notepad.yview)
scrollbar.pack(side='right', fill='y')
notepad['yscrollcommand'] = scrollbar.set
notepad_frame.grid(row=4, column=0, columnspan=6, pady=10, padx=10, sticky="nsew")

'''
# Add buttons for next and previous page
prev_button = ttk.Button(root, text="Previous Page", command=previous_page)
prev_button.grid(row=5, column=4, pady=10, padx=10, sticky="nsew")

next_button = ttk.Button(root, text="Next Page", command=next_page)
next_button.grid(row=5, column=5, pady=10, padx=10, sticky="nsew")
'''

# Configure row and column weights
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Configure weights for specific frames
calculator_frame.grid_rowconfigure(0, weight=1)
calculator_frame.grid_columnconfigure(0, weight=1)
volume_frame.grid_rowconfigure(0, weight=1)
volume_frame.grid_columnconfigure(0, weight=1)
brightness_frame.grid_rowconfigure(0, weight=1)
brightness_frame.grid_columnconfigure(0, weight=1)
'''
wave_frame.grid_rowconfigure(0, weight=1)
wave_frame.grid_columnconfigure(0, weight=1)
'''

# Set the initial page to the first frame
notebook.select(0)

tick()
root.mainloop()
