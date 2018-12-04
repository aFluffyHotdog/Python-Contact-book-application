import tkinter as tk
from tkinter import *
import contactlist_func


def load_gui(app, window):

    tk.Label(window, text="First Name")\
        .grid(row=0, column=0, sticky=W)

    # create a hidden entry field to keep the ID of each contactlist entry
    tk.Entry(window, text=app.text_id, width=0) \
        .grid(row=1, column=0)
    # put the First name entry field on top of the ID field
    tk.Entry(window, text=app.text_first_name, width=30)\
        .grid(row=1, column=0)

    tk.Label(window, text="Last Name") \
        .grid(row=2, column=0, sticky=W)

    tk.Entry(window, text=app.text_last_name, width=30) \
        .grid(row=3, column=0)

    tk.Label(window, text="Email")\
        .grid(row=4, column=0, sticky=W)

    tk.Entry(window, text=app.text_email, width=30)\
        .grid(row=5, column=0)

    tk.Label(window, text="Phone Number") \
        .grid(row=6, column=0, sticky=W)

    tk.Entry(window, text=app.text_phone_number, width=30) \
        .grid(row=7, column=0)

    tk.Label(window, text="Address") \
        .grid(row=8, column=0, sticky=W)

    tk.Entry(window, text=app.text_address, width=30) \
        .grid(row=9, column=0)

    # establish and grid a frame for action buttons NEW, EDIT, DELETE, CLEAR
    app.action_frame = tk.Frame(window)
    app.action_frame.grid(row=10, column=0, sticky=EW)

    # button for ADD contact and grid it to the action_frame
    app.btn_add_person = tk.Button(app.action_frame, text="ADD", command=lambda: contactlist_func.add_person(app),
              relief=GROOVE, bg='#dcdcdc')
    app.btn_add_person.grid(row=0, column=0, pady=10)

    # buttons for EDIT, DELETE, CLEAR person and grid it to action_frame
    # then grid_remove to hide from view
    # EDIT button
    app.btn_edit_person = tk.Button(app.action_frame, text="EDIT", command=lambda: contactlist_func.edit_person(app),
                                   relief=GROOVE, bg='#dcdcdc')
    app.btn_edit_person.grid(row=0, column=0, pady=10, padx=5)
    app.btn_edit_person.grid_remove()
    # DELETE button
    app.btn_delete_person = tk.Button(app.action_frame, text="DELETE", command=lambda: contactlist_func.delete_person(app),
                                   relief=GROOVE, bg='#dcdcdc')
    app.btn_delete_person.grid(row=0, column=1, pady=10, padx=5)
    app.btn_delete_person.grid_remove()
    # CLEAR button
    app.btn_clear_form = tk.Button(app.action_frame, text="CLEAR", command=lambda: contactlist_func.clear_form(app),
              relief=GROOVE, bg='#dcdcdc')
    app.btn_clear_form.grid(row=0, column=2, pady=10, padx=5)
    app.btn_clear_form.grid_remove()

    tk.Label(window, text="Contact List").grid(row=0, column=1, sticky=W, padx=(25, 0))

    # add contactlist Listbox with scroll bar
    sb = Scrollbar(window, orient=VERTICAL)
    app.contactlist_box = tk.Listbox(window, exportselection=0, yscrollcommand=sb.set, width=28)
    app.contactlist_box.bind('<<ListboxSelect>>', lambda event: contactlist_func.select_entry(app))
    sb.config(command=app.contactlist_box.yview)
    app.contactlist_box.grid(row=1, column=1, rowspan=9, padx=(25, 0), sticky=NSEW)
    sb.grid(row=1, column=2, rowspan=9, sticky=N+S+E)