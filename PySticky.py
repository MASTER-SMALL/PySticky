import tkinter as tk
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.scrolledtext import ScrolledText


def window(FlengthUp, FlengthWide, BlengthUp, BlengthWide, frontColor, backColor):
    print('window() successfully started')
    root=tk.Tk()
    root.title("PySticky")
    root.geometry("500x500")

    frame = tk.Frame(root, width=FlengthWide, height=FlengthUp, background="bisque")
    frame.pack_propagate(0)
    frame.pack()

    textbox = ScrolledText(frame, width=BlengthWide, height=BlengthUp, fg=frontColor, bg=backColor)
    textbox.pack(fill=None, expand=False)

    def saveText():
        saveLocation = asksaveasfilename()
        stringSave = textbox.get("1.0",'end-1c')
        fileSave = open(saveLocation, "w")
        fileSave.write(stringSave)
        fileSave.close()
        showinfo(title="Alert!", message="File saved!")

    saveButton = tk.Button(root, text="Save", fill=None, height = 100, width = 50, bg="green", command=saveText)
    saveButton.pack(side="bottom")

    root.mainloop()
    print('window() successfully completed')

#Demo arguments
#window(450, 450, 50, 50, "Black", "White")
