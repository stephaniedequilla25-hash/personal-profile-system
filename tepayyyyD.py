import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

root = tk.Tk()
root.title(": Person Profile Management System")
root.geometry("700x500")

title_label = tk.Label(root, text=": Person Profile Management System")
title_label.pack(pady=10)

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

root.mainloop()

# Full Name
ttk.Label(
 parent,
 text="Full Name:",
 style="Heading.TLabel"
 ).grid(row=0, column=0, sticky="w", pady=7)

 ttk.Entry(
  parent,
 textvariable=self.full_name_var,
 width=32
  ).grid(row=0, column=1, pady=7, padx=(10, 0))

  # Email
 ttk.Label(
  parent,
  text="Email Address:",
  style="Heading.TLabel"
  ).grid(row=1, column=0, sticky="w", pady=7)

 ttk.Entry(
  parent,
  textvariable=self.email_var,
  width=32
 ).grid(row=1, column=1, pady=7, padx=(10, 0))

 # Phone
ttk.Label(
  parent,
  text="Phone Number:",
  style="Heading.TLabel"
 ).grid(row=2, column=0, sticky="w", pady=7)

  ttk.Entry(
  parent,
  textvariable=self.phone_var,
  width=32
 ).grid(row=2, column=1, pady=7, padx=(10, 0))

 # City
   ttk.Label(
   parent,
   text="City:",
   style="Heading.TLabel"
).grid(row=3, column=0, sticky="w", pady=7)

  ttk.Entry(
    parent,
    textvariable=self.city_var,
     width=32
 ).grid(row=3, column=1, pady=7, padx=(10, 0))

  # Age
  ttk.Label(
    parent,
    text="Age:",
    style="Heading.TLabel"
 ).grid(row=4, column=0, sticky="w", pady=7)

  ttk.Entry(
   parent,
  textvariable=self.age_var,
   width=32
 ).grid(row=4, column=1, pady=7, padx=(10, 0))

 
