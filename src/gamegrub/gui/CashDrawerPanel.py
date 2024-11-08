"""Cash Drawer Panel class.

Author: Mason Pride
Version: 0.1
"""
import tkinter as tk


class CashDrawerPanel(tk.Frame):
    """Cash Drawer Panel class."""
    def __init__(self, master) -> None:
        """Cash panel class constructor."""
        self.__master = master
        tk.Frame.__init__(self, master=self.__master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        cash_label = tk.Label(master=self, text="Cash Transaction")
        cash_label.grid(row=0, column=1, padx=2, pady=2, sticky="NSEW")

        cash_total_label = tk.Label(master=self, text="Total $ 0.00")
        cash_total_label.grid(row=2, column=1, padx=2, pady=2, sticky="NSEW")

        hundred_label = tk.Label(master=self, text="$100")
        hundred_label.grid(row=3, column=0, padx=2, pady=2, sticky="NSEW")
        hundred_spinbox = tk.Spinbox(master=self, from_=0, to=1, width=5)
        hundred_spinbox.grid(row=3, column=1, padx=2, pady=2, sticky="W")

        fifty_label = tk.Label(master=self, text="$50")
        fifty_label.grid(row=4, column=0, padx=2, pady=2, sticky="NSEW")
        fifty_spinbox = tk.Spinbox(master=self, from_=0, to=1, width=5)
        fifty_spinbox.grid(row=4, column=1, padx=2, pady=2, sticky="W")

        twenty_label = tk.Label(master=self, text="$20")
        twenty_label.grid(row=5, column=0, padx=2, pady=2, sticky="NSEW")
        twenty_spinbox = tk.Spinbox(master=self, from_=0, to=1, width=5)
        twenty_spinbox.grid(row=5, column=1, padx=2, pady=2, sticky="W")

        ten_label = tk.Label(master=self, text="$10")
        ten_label.grid(row=6, column=0, padx=2, pady=2, sticky="NSEW")
        ten_spinbox = tk.Spinbox(master=self, from_=0, to=1, width=5)
        ten_spinbox.grid(row=6, column=1, padx=2, pady=2, sticky="W")

        five_label = tk.Label(master=self, text="$5")
        five_label.grid(row=7, column=0, padx=2, pady=2, sticky="NSEW")
        five_spinbox = tk.Spinbox(master=self, from_=0, to=1, width=5)
        five_spinbox.grid(row=7, column=1, padx=2, pady=2, sticky="W")

        one_label = tk.Label(master=self, text="$1")
        one_label.grid(row=7, column=0, padx=2, pady=2, sticky="NSEW")
        one_spinbox = tk.Spinbox(master=self, from_=0, to=1, width=5)
        one_spinbox.grid(row=7, column=1, padx=2, pady=2, sticky="W")

        dollar_coin_label = tk.Label(master=self, text="$1.00")
        dollar_coin_label.grid(row=3, column=2, padx=2, pady=2, sticky="NSEW")
        dollar_coin_spinbox = tk.Spinbox(master=self, from_=0, to=1, width=5)
        dollar_coin_spinbox.grid(row=3, column=3, padx=2, pady=2, sticky="W")

        half_dollar_label = tk.Label(master=self, text="$0.50")
        half_dollar_label.grid(row=4, column=2, padx=2, pady=2, sticky="NSEW")
        half_dollar_spinbox = tk.Spinbox(master=self, from_=0, to=1, width=5)
        half_dollar_spinbox.grid(row=4, column=3, padx=2, pady=2, sticky="W")

        quarter_label = tk.Label(master=self, text="$0.25")
        quarter_label.grid(row=5, column=2, padx=2, pady=2, sticky="NSEW")
        quarter_spinbox = tk.Spinbox(master=self, from_=0, to=1, width=5)
        quarter_spinbox.grid(row=5, column=3, padx=2, pady=2, sticky="W")

        dime_label = tk.Label(master=self, text="$0.10")
        dime_label.grid(row=6, column=2, padx=2, pady=2, sticky="NSEW")
        dime_spinbox = tk.Spinbox(master=self, from_=0, to=1, width=5)
        dime_spinbox.grid(row=6, column=3, padx=2, pady=2, sticky="W")

        nickle_label = tk.Label(master=self, text="$0.05")
        nickle_label.grid(row=7, column=2, padx=2, pady=2, sticky="NSEW")
        nickle_spinbox = tk.Spinbox(master=self, from_=0, to=1, width=5)
        nickle_spinbox.grid(row=7, column=3, padx=2, pady=2, sticky="W")

        penny_label = tk.Label(master=self, text="$0.01")
        penny_label.grid(row=7, column=2, padx=2, pady=2, sticky="NSEW")
        penny_spinbox = tk.Spinbox(master=self, from_=0, to=1, width=5)
        penny_spinbox.grid(row=7, column=3, padx=2, pady=2, sticky="W")

        finalize = tk.Button(master=self, text="Finalize",
                             command=lambda: self.action_performed("finalize"))
        finalize.grid(row=8, column=0, columnspan=2, sticky="EW")

        cancel = tk.Button(master=self, text="Cancel",
                           command=lambda:
                           self.action_performed("cancel"))
        cancel.grid(row=8, column=2, columnspan=2, sticky="EW")
