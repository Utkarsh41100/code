from  tkinter import *

root=Tk() # This line creates the main window of your application
root.geometry("1000x1000") # This sets the geometry of the application
photo=PhotoImage(file="Insert_Image_harry.png") # This line creates a PhotoImage object named photo
label=Label(image=photo) # This line creates a Label widget named label
label.pack() # This line places the label widget inside the root window
root.mainloop() # This line starts the Tkinter event loop