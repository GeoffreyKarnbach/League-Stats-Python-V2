# FETCHER Modules
from FETCHER.data_fetcher import*
from FETCHER.html_downloader import*

# Custom UI Module
from GUI.windows import*

# Built-in
from tkinter import*
from tkinter.messagebox import*


root = Tk()
root.title("Test")
root.withdraw()

refresh = askyesno("Refetch League Stats","Do you want to refetch all your data (May take some time)?")
if refresh:
    download_html("GoyoteGoyote")
    fecth_data_from_html("DATA/match_history.html")

main_frame = Frame(root)
main_frame.grid(column=0, row = 0, padx = 10, pady = 10)

Index(root, main_frame)

root.deiconify()
root.mainloop()

