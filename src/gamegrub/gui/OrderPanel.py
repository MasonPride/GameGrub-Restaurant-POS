"""Order Panel Class.

Creates the side bar panel in our GUI.

Author: Mason Pride
Version: 0.1
"""
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Treeview, Scrollbar
from typing import Dict
from src.gamegrub.data.Item import Item
from src.gamegrub.gui.PanelFactory import PanelFactory
from src.gamegrub.gui.SelectionDialog import SelectionDialog
from cc410.register.CardReader import CardReader
from cc410.register.CardTransactionResult import CardTransactionResult
from src.gamegrub.gui.CashDrawerPanel import CashDrawerPanel
from cc410.register.ReceiptPrinter import ReceiptPrinter


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

        """
        self.__order_list = tk.Listbox(master=self)
        self.__order_list.grid(row=1, column=0, columnspan=2,
                               padx=2, pady=2, sticky="NSEW")
        """
        self.__items: Dict[str, Item] = dict()
        list_frame = tk.Frame(master=self)
        list_frame.grid_columnconfigure(0, weight=1)
        list_frame.grid_rowconfigure(0, weight=1)
        self.__order_list = Treeview(master=list_frame,
                                     show="tree", selectmode="browse")
        order_list_scrollbar = Scrollbar(master=list_frame, orient="vertical",
                                         command=self.__order_list.yview)
        self.__order_list.configure(yscroll=order_list_scrollbar.set)
        self.__order_list.grid(row=0, column=0, sticky="NSEW")
        order_list_scrollbar.grid(row=0, column=1, sticky="NSE")
        list_frame.grid(row=1, column=0, columnspan=2, sticky="NSEW")

        edit_button = tk.Button(master=self, text="Edit",
                                command=lambda:
                                self.action_performed("edit"))
        edit_button.grid(row=2, column=0, sticky="NSEW")

        delete_button = tk.Button(master=self, text="Delete",
                                  command=lambda:
                                  self.action_performed("delete"))
        delete_button.grid(row=2, column=1, sticky="NSEW")

        subtotal_label = tk.Label(master=self, text="Subtotal: $0.00")
        subtotal_label.grid(row=3, column=0, padx=2, pady=2, sticky="E")
        tax_label = tk.Label(master=self, text="Tax: $0.00")
        tax_label.grid(row=4, column=0, padx=2, pady=2, sticky="E")
        total_label = tk.Label(master=self, text="Total: $0.00")
        total_label.grid(row=5, column=0, padx=2, pady=2, sticky="E")

        new_button = tk.Button(master=self, text="New Order",
                            command=lambda:
                            self.action_performed("new"))
        new_button.grid(row=6, column=0, sticky="NSEW")

        checkout_button = tk.Button(master=self, text="Checkout",
                                 command=lambda:
                                 self.action_performed("checkout"))
        checkout_button.grid(row=6, column=1, sticky="NSEW")

    def action_performed(self, text: str) -> None:
        """Handle button actions."""
        print(text)
        if text == "edit":
            node = self.__order_list.focus()
            if node:
                while node not in self.__items:
                    node = self.__order_list.parent(node)
                item: Item = self.__items[node]
                panel = PanelFactory.get_panel_by_item(self.__master, item)
                self.__master.load_panel(panel)
        elif text == "delete":
            node = self.__order_list.focus()
            if node:
                while node not in self.__items:
                    node = self.__order_list.parent(node)
                del self.__items[node]
                self.__order_list.delete(node)
        elif text == "new":
            pass
        elif text == "checkout":
            dialog = SelectionDialog(self.__master,
                                     title="Checkout",
                                     message="Cash or Credit/Debit?",
                                     options=["Cash",
                                     "Credit/Debit",
                                     "Cancel"])
            if dialog.result == "Credit/Debit":
                reader: CardReader = CardReader()
                result: CardTransactionResult = reader.run_card()
                if result == CardTransactionResult.APPROVED:
                    messagebox.showinfo("Success", str(result))
                    receipt = ReceiptPrinter()
                    receipt.start_receipt()
                    receipt.print_line("Order#: " +
                                       str(self.__order_num.cget("text")))
                    for item_id, value in self.__items.items():
                        receipt.print_line(str(value) +
                        " $" + str(value.price))
                else:
                    messagebox.showinfo("Error", str(result))
            elif dialog.result == "Cash":
                self.__master.load_panel(CashDrawerPanel(self.__master))

    def save_item(self, item: Item) -> None:
        """Save item method.

        Saves an instance of an item to our sidebar.

        Args:
            item: Instance of an item.
        """
        for item_id, value in self.__items.items():
            if item is value:
                self.__update_tree(item, item_id)
                return
        self.__items[self.__update_tree(item)] = item

    def __update_tree(self, item: Item, index: str = "end") -> str:
        """Update tree method.

        Updates the sidebar tree.

        Args:
            item: Instance of an item.
            index: index of node.

        Returns:
            str representing an index.
        """
        if index == "end":
            index = self.__order_list.insert(parent="",
                                             index="end",
                                             text=str(item))
        else:
            self.__order_list.item(index, text=str(item))
            for child in self.__order_list.get_children(index):
                self.__order_list.delete(child)
        self.__order_list.item(index, open=True)

        for line in item.instructions:
            self.__order_list.insert(parent=index, index="end", text=line)
        return index
