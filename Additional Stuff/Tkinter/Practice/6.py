"""
6. Joe’s Automotive
    Joe’s Automotive performs the following routine maintenance services:
        • Oil change          —   $26.00
        • Lube job            —   $18.00
        • Radiator flush      —   $30.00
        • Transmission flush  —   $80.00
        • Inspection          —   $15.00
        • Muffler replacement —   $100.00
        • Tire rotation       —   $20.00
    Write a GUI program with check buttons that allow the user to select any or all of these
    services. When the user clicks a button the total charges should be displayed.
"""
import tkinter as tk 
from tkinter import ttk
window = tk.Tk()
window.title('Auto Shop')
window.geometry('600x400')
# Functions



# Labels
label1 = tk.Label(text = 'Joes Automotive')
label1.grid(column = 0, row = 0)

label2 = tk.Label(text = 'Joe’s Automotive performs the following routine maintenance services:')
label2.grid(column = 0)

label3 = tk.Label(text = '• Oil change---------------------------------$26.00')
label3.grid(column = 0, row = 2, padx = (0,100))
button3 = ttk.Checkbutton(variable = 26).grid(column = 3, row = 2, padx = (20,0))

label4 = tk.Label(text = '• Lube job-----------------------------------$18.00')
label4.grid(column = 0, row = 3, padx = (0,100))
button4 = ttk.Checkbutton(variable = 18).grid(column = 3, row = 3, padx = (20,0))

label5 = tk.Label(text = '• Radiator flush-------------------------------$30.00')
label5.grid(column = 0, row = 4, padx = (0,100))
button5 = ttk.Checkbutton(variable = 30).grid(column = 3, row = 4, padx = (20,0))


label6 = tk.Label(text = '• Transmission flush--------------------------$80.00')
label6.grid(column = 0, row = 5, padx = (0,100))
button6 = ttk.Checkbutton(variable = 80).grid(column = 3, row = 5, padx = (20,0))


label7 = tk.Label(text = '• Inspection----------------------------------$15.00')
label7.grid(column = 0, row = 6, padx = (0,100))
button7 = ttk.Checkbutton(variable = 15).grid(column = 3, row = 6, padx = (20,0))


label8 = tk.Label(text = '• Muffler replacement-------------------------$100.00')
label8.grid(column = 0, row = 7, padx = (0,100))
button8 = ttk.Checkbutton(variable = 100).grid(column = 3, row = 7, padx = (20,0))


label9 = tk.Label(text = '• Tire rotation-----------------------------------$20.00')
label9.grid(column = 0, row = 8, padx = (0,100))
button9 = ttk.Checkbutton(variable = 20).grid(column = 3, row = 8, padx = (20,0))


# Button
button1 = tk.Button(text = 'Check Out')
button1.grid(column = 1, row = 9)
window.mainloop()





























