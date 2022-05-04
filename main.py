import tkinter as tk


# Function mile to km
def mile_to_km(miles):
    return miles * 1.60934


# Function button click
def click():
    # Get input
    miles = float(input_text.get())
    # Call function
    km = mile_to_km(miles)
    # Display result
    label3.config(text=km)


# Window
window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=200)
window.config(padx=50, pady=200)

# Input
input_text = tk.Entry(width=10)
input_text.grid(row=0, column=1)

# Label1
label1 = tk.Label(text="Miles", font=("Arial", 12))
label1.grid(row=0, column=2)

# Label2
label2 = tk.Label(text="is equivalent to")
label2.grid(row=1, column=0)

# Label3
label3 = tk.Label(text="0", font=("Arial", 12))
label3.grid(row=1, column=1)

# Label4
label4 = tk.Label(text="Kilometers")
label4.grid(row=1, column=2)

# Button
button = tk.Button(text="Calculate", command=click)
button.grid(row=2, column=1)

window.mainloop()
