"""Order Panel Class.

Creates the side bar panel in our GUI.

Author: Mason Pride
Version: 0.1
"""
import tkinter as tk


class OrderPanel(tk.Frame):
    """Order Panel class."""
    def __init__(self, master) -> None:
        """Order Panel constructor."""
        self.__master = master
        tk.Frame.__init__(self, master=self.__master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        order_label = tk.Label(master=self, text="Order #")
        order_label.grid(row=0, column=0, padx=2, pady=2, sticky="E")

        self.__order_num = tk.Label(master=self, text="000")
        self.__order_num.grid(row=0, column=1, padx=2, pady=2, sticky="W")

        self.__order_list = tk.Listbox(master=self)
        self.__order_list.grid(row=1, column=0, columnspan=2,
                               padx=2, pady=2, sticky="NSEW")

        edit_button = tk.Button(master=self, text="Edit")
        edit_button.grid(row=2, column=0, columnspan=2,
                         padx=2, pady=2, sticky="NSEW")

        subtotal_label = tk.Label(master=self, text="Subtotal: $0.00")
        subtotal_label.grid(row=3, column=0, padx=2, pady=2, sticky="E")
        tax_label = tk.Label(master=self, text="Tax: $0.00")
        tax_label.grid(row=4, column=0, padx=2, pady=2, sticky="E")
        total_label = tk.Label(master=self, text="Total: $0.00")
        total_label.grid(row=5, column=0, padx=2, pady=2, sticky="E")
