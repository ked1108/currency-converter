from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedTk as tk

import csv
import requests

root = tk()
root.set_theme('arc')
root.geometry("325x300")

def roe(code1, code2):
    result = requests.get('https://free.currconv.com/api/v7/convert?q={0}_{1}&compact=ultra&apiKey=504826555338a6696512'.format(code1, code2))

    if result.ok:
        data = result.json()
        rate = data[code1+"_"+code2]
        print(rate)
        return float(rate)

    else: return None



def convert():

    code1 = entry_currency1.get()
    code2 = entry_currency2.get()
    amt   = float(entry_amount.get())

    one_in_file = False
    two_in_file = False
    with open("codes.csv", 'r') as csvfile:
        data = csv.reader(csvfile, delimiter = ',')

        for row in data:
            if code1 in row:
                one_in_file = True
            if code2 in row:
                two_in_file = True

            if one_in_file and two_in_file:
                break

    if not (one_in_file and two_in_file):
        messagebox.showwarning(title = "Error!!!", message = "Wrong Input")
        root.destroy()

    rate = roe(code1, code2)

    value = rate * amt

    messagebox.showinfo(title = "Rate", message = ("The Value Is:\t"+str(value)))
            


curr1 = StringVar()
curr2 = StringVar()
amount = IntVar()

label = ttk.Label(root, text="Welcome To Currency")
label.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 10)

label_currency1 = ttk.Label(root, text="Enter The Currency Code:")
label_currency2 = ttk.Label(root, text="Enter The Currency Code:")
label_amount    = ttk.Label(root, text="Enter The Amount To Convert:")

label_currency1.grid(row = 1, column = 0, padx = 5, pady = 10)
label_currency2.grid(row = 2, column = 0, padx = 5, pady = 10)
label_amount.grid(row = 3, column = 0, padx = 5, pady = 10)

entry_currency1 = ttk.Entry(root, textvariable=curr1)
entry_currency2 = ttk.Entry(root, textvariable=curr2)
entry_amount    = ttk.Entry(root, textvariable=amount)

entry_currency1.grid(row = 1, column = 1, padx = 5, pady = 10)
entry_currency2.grid(row = 2, column = 1, padx = 5, pady = 10)
entry_amount.grid(row = 3, column = 1, padx = 5, pady = 10)



button_convert  = ttk.Button(root, text="Convert", command = convert)
button_convert.grid(row = 4, column = 0, columnspan = 2, padx = 5, pady = 10)





root['background'] = "#f5f6f7"
root.resizable(0, 0)
root.mainloop()


