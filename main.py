import tkinter as tk
from tkinter import ttk

def calculate_future_value():
    try:
        principal = float(principal_entry.get())
        inflation_rate = float(inflation_rate_entry.get()) / 100
        num_years = int(num_years_entry.get())

        future_value = principal / ((1 + inflation_rate) ** num_years)

        future_value_label.config(text="Future Value: Rs{:,.2f}".format(future_value))
    except ValueError:
        future_value_label.config(text="Invalid input")

root = tk.Tk()
root.title("Future Value Calculator")
root.configure(background="black")

style = ttk.Style(root)
style.configure('TLabel', background="black", foreground="white", font=('Arial', 20))
style.configure('TEntry', background="white", font=('Arial', 20),height=20,width=20)

principal_label = ttk.Label(root, text="Principal amount:")
principal_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

principal_entry = ttk.Entry(root)
principal_entry.grid(row=0, column=1, padx=10, pady=5)

inflation_rate_label = ttk.Label(root, text="Inflation rate (%):")
inflation_rate_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

inflation_rate_entry = ttk.Entry(root)
inflation_rate_entry.grid(row=1, column=1, padx=10, pady=5)

num_years_label = ttk.Label(root, text="Number of years:")
num_years_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

num_years_entry = ttk.Entry(root)
num_years_entry.grid(row=2, column=1, padx=10, pady=5)

future_value_label = ttk.Label(root, text="")
future_value_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

calculate_button = ttk.Button(root, text="Calculate", command=calculate_future_value)
calculate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()

