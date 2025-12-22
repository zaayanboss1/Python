import tkinter as tk
from tkinter import ttk,messagebox

class Restaurant Order Management:
    def __init__(self,root):
        self.root=root
        self.root.title(
            "Restaurant Management App")


        self.menu_items={
            "FRIES MEAL": 2,
            "LUNCH MEAL": 2,
            "BURGER MEAL": 4,
            "PIZAA MEAL": 4,
            "CHEESE BURGER": 2.5,
            "DRINKS": 1
        }
        self.exchange_rate=82
        self.setup_background(root)

        ttk.Label(frame,
            text="Restaurant Order Management",
            font=("Arial",20,"bold")).grid(row=0,
                                        colimnspan=3,
                                        padx=10,
                                        pady=10)
        self.menu_labels={}
        self.menu_quantities={}

        for i,(item,price)in enumerate(self.menu_items.items(),start=1):
            label = ttk.Label(frame,
                            text="f{item}($[price])):"
                            font=("Arial",12))
            label.grid(row=i,column=0,padx=10,pady=5)
            self.menuu_quantities[item]=quantity_entry
        self.currency_var=tk.StringVar()
        tyk.label(frame,text="Currency:",
                    font=("Arial",12)).grid(row=len(self.menu_items)+1,
                    column=0,
                    padx=10,
                    pady=5)
    currency_dropdown=ttk.Combobox(frame,
                                    textvariable=self.currency_var,
                                    state="readonly",width=18,
                                    values=('USD','INR'))
    currency_dropdown.grid(row=len(self.menu ))