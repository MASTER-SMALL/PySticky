import tkinter as tk
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.scrolledtext import ScrolledText


backgroundColorPicked="bisque3"
def window(FlengthUp, FlengthWide, BlengthUp, BlengthWide, frontColor, backColor, saveToggle, configToggle, textInsert):
    print('window() successfully started')
    root=tk.Tk()
    root.title("PySticky")
    root.geometry("500x500")
    root.configure(background=backgroundColorPicked)

    frame = tk.Frame(root, width=FlengthWide, height=FlengthUp, background="bisque")
    frame.pack_propagate(0)
    frame.pack()

    textbox = ScrolledText(frame, width=BlengthWide, height=BlengthUp, fg=frontColor, bg=backColor)
    #sets the default text to value textInsert
    textbox.insert(END, textInsert)
    textbox.pack(fill=None, expand=False)

    def saveText():
        saveLocation = asksaveasfilename(defaultextension=".txt", filetypes=(("Plain text file", "*.txt"),("Rich text file", "*.rtf"),("All Files", "*.*") ))
        stringSave = textbox.get("1.0",'end-1c')
        fileSave = open(saveLocation, "w")
        fileSave.write(stringSave)
        fileSave.close()
        showinfo(title="Alert!", message="File saved!")

    def configBox():
        def saveSettings():
            global backgroundColorPicked
            backgroundColorPicked = backgroundColorPickedBox.get()
            frontColorPicked = frontColorPickedBox.get()
            #carry any written text
            textCarry = textbox.get("1.0",'end-1c')
            backColorPicked = backColorPickedBox.get()
            window(450, 450, 50, 50, frontColorPicked, backColorPicked, True, True, textCarry)
        
        config=tk.Tk()
        config.title("Config")
        config.geometry("200x250")
        config.configure(background="bisque3")

        backgroundColorPickedPrompt = Label(config, text="Background Color:")
        backgroundColorPickedPrompt.pack()
        
        backgroundColorPickedBox = Entry(config)
        backgroundColorPickedBox.insert(END, "bisque3")
        backgroundColorPickedBox.pack()
        
        frontColorPickedPrompt = Label(config, text="Text Color:")
        frontColorPickedPrompt.pack()
        
        frontColorPickedBox = Entry(config)
        frontColorPickedBox.insert(END, "Black")
        frontColorPickedBox.pack()

        backColorPickedPrompt = Label(config, text="TextBox Color:")
        backColorPickedPrompt.pack()
        
        backColorPickedBox = Entry(config)
        backColorPickedBox.insert(END, "White")
        backColorPickedBox.pack()
        
        submitConfigButton = tk.Button(config, text="Save Settings", fill=None, height = 1, width = 50, command=saveSettings)
        submitConfigButton.pack()

        config.mainloop()
    
    if saveToggle == True:
        saveButton = tk.Button(root, text="Save", fill=None, height = 1, width = 25, bg="cyan", command=saveText)
        saveButton.pack()
        
    if configToggle == True:
        configButton = tk.Button(root, text="Config", fill=None, height = 1, width = 25, bg="cyan", command=configBox)
        configButton.pack()

    root.mainloop()
    print('window() successfully completed')
