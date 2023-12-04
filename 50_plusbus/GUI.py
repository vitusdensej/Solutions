import tkinter as tk
from tkinter import ttk

main_window = tk.Tk()
main_window.title("my first GUI")
main_window.geometry("1500x700")

padx = 0
pady = 0

dataframe = tk.Frame(main_window)
dataframe.grid(row=0, column=0)

def create_tree_view(col, fields, select_command):
    tree_view_scroll_bar = tk.Scrollbar(dataframe)
    tree_view_scroll_bar.grid(row=5, column=col, padx=0, pady=pady, sticky='ns')
    tree_view = ttk.Treeview(dataframe, yscrollcommand=tree_view_scroll_bar.set, selectmode="browse")
    tree_view.grid(row=5, column=col, padx=padx, pady=pady)
    tree_view.bind("<<TreeviewSelect>>", select_command)
    tree_view_scroll_bar.config(command=tree_view.yview)

    tree_view["columns"] = fields
    tree_view.column("#0", width=0, stretch=tk.NO)
    tree_view.heading("#0", text="", anchor=tk.W)

    for f in fields:
        tree_view.column(f, anchor=tk.E, width=12 * len(f))
        tree_view.heading(f, text=f, anchor=tk.CENTER)

    return tree_view

# placeholder function for commands
def _pass():
    pass

customer_view = create_tree_view(1, ("id", "last name", "contact"), _pass)
route_view = create_tree_view(2, ("id", "start/end", "date", "seats"), _pass)
reservation_view = create_tree_view(3, ("id", "customer id", "route id", "seats"), _pass)

button_frame = tk.LabelFrame(main_window)
button_frame.grid(row=1, column=0)

create_button = tk.Button(button_frame, text="Create")
create_button.grid(row=0, column=0)

update_button = tk.Button(button_frame, text="Update")
update_button.grid(row=0, column=1)

delete_button = tk.Button(button_frame, text="Delete")
delete_button.grid(row=0, column=2)

if __name__ == "__main__":
    main_window.mainloop()
