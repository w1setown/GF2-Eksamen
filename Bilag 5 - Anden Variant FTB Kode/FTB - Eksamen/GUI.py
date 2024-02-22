import tkinter as tk
from app import OrderManager

class OrderManagerGUI:

    def __init__(self, master):
        self.master = master
        self.order_manager = OrderManager()

        self.text_box = self.Text_box("", 5, 0)
        self.create_button("Add Order", self.add_order, 6, 0    )

        self.ordered_listbox = self.create_listbox("Ordered", 0)
        self.prep_listbox = self.create_listbox("Prep", 1)
        self.ready_listbox = self.create_listbox("Ready", 2)
        
        self.create_button("Move to Prep", self.move_to_prep, 1, 3)
        self.create_button("Move All to Prep", self.move_all_to_prep, 2, 3)
        self.create_button("Move to Ready", self.move_to_ready, 3, 3)
        self.create_button("Move All to Ready", self.move_all_to_ready, 4, 3)
        

    def create_listbox(self, title, column):
        frame = tk.Frame(self.master)
        frame.grid(row=0, column=column, rowspan=5, padx=5)

        label = tk.Label(frame, text=title)
        label.pack()

        listbox = tk.Listbox(frame, height=20, width=40, borderwidth=2, relief="groove")
        listbox.pack()

        return listbox

    def create_button(self, text, command, row, column):
        button = tk.Button(self.master, text=text, command=command, borderwidth=2, relief="groove")
        button.grid(row=row, column=column)

    def Text_box(self, title, row, column):
        frame = tk.Frame(self.master)
        frame.grid(row=row, column=column)

        label = tk.Label(frame, text=title)
        label.pack()
        

        text_box = tk.Text(frame, height=2, width=20, borderwidth=2, relief="groove")
        text_box.pack()

        return text_box

    
    def add_order(self):
        order = self.text_box.get("1.0", tk.END).strip()
        if order:
            self.order_manager.add_order(order)
            self.text_box.delete("1.0", tk.END)
            self.update_listboxes()

    def move_to_prep(self):
        selected = self.ordered_listbox.curselection()
        if selected:
            item = self.ordered_listbox.get(selected)
            self.order_manager.move_to_prep(item)
            self.update_listboxes()

    def move_to_ready(self):
        selected = self.prep_listbox.curselection()
        if selected:
            item = self.prep_listbox.get(selected)
            self.order_manager.move_to_ready(item)
            self.update_listboxes()

    def move_all_to_prep(self):
        self.order_manager.move_all_to_prep()
        self.update_listboxes()

    def move_all_to_ready(self):
        self.order_manager.move_all_to_ready()
        self.update_listboxes()

    def update_listboxes(self):
        self.ordered_listbox.delete(0, tk.END)
        for item in self.order_manager.ordered:
            self.ordered_listbox.insert(tk.END, item)

        self.prep_listbox.delete(0, tk.END)
        for item in self.order_manager.prep:
            self.prep_listbox.insert(tk.END, item)

        self.ready_listbox.delete(0, tk.END)
        for item in self.order_manager.ready:
            self.ready_listbox.insert(tk.END, item)

if __name__ == "__main__":
    root = tk.Tk()
    gui = OrderManagerGUI(root)
    root.mainloop()