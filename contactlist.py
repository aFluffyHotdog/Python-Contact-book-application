from tkinter import *
import contactlist_gui
import contactlist_func


class AppWindow(Frame):
    def __init__(self, app, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.app = app

     
        self.app.option_add("*font", "ComicSansMS 10")
        self.app.resizable(width=False, height=False)
        # TODO: add center_window function
        # contactlist_func.center_window(app, 500, 340)
        self.app.geometry('{}x{}'.format(500, 340))

        self.app.title('Python Contact Book')
        #self.app.iconbitmap(self.app, default="assets/contactlist.ico")
        #chaning background color to red
        self.app.configure(bg='turquoise')
        # create an outer frame with padding around window to put all other content
        self.container = Frame(self.app)
        self.container.grid(row=0, column=0, padx=25, pady=10)
        self.container.configure(bg='turquoise')
        # define tkinter string vars for form fields
        self.text_id = StringVar()
        self.text_first_name = StringVar()
        self.text_last_name = StringVar()
        self.text_email = StringVar()
        self.text_phone_number = StringVar()
        self.text_address = StringVar()
        self.text_favorite = StringVar()

        # create list for form fields and put variables in list
        self.contactlist_fields = []
        self.contactlist_fields.append(self.text_id)
        self.contactlist_fields.append(self.text_first_name)
        self.contactlist_fields.append(self.text_last_name)
        self.contactlist_fields.append(self.text_email)
        self.contactlist_fields.append(self.text_phone_number)
        self.contactlist_fields.append(self.text_address)
        self.contactlist_fields.append(self.text_favorite)

        # set contactlist list for displaying contacts
        self.contactlist_list = []
        # set active index to -1
        self.active_contactbox_index = -1

        # load GUI into container Frame
        contactlist_gui.load_gui(self)

        # load database and populate contact list
        contactlist_func.create_db()
        contactlist_func.load_contactlist(self)


if __name__ == "__main__":
    root = Tk()
    App = AppWindow(root)
    root.mainloop()
