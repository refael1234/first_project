import tkinter

files = tkinter.Tk()
text_widget = tkinter.Text(files)
text_widget.pack()

# Open the result file and insert its contents into the Text widget
with open("result.txt", "r") as file:
    contents = file.read()
    text_widget.insert(tkinter.END, contents)

# Run the Tkinter event loop
files.mainloop()