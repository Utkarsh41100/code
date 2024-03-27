from tkinter import *
root=Tk()
root.geometry("500x600")
root.title("Utkarsh")
# Important label options
# text - adds text
# bd - background
# fg - foreground
# font- change font
#font=("Times",14,"bold"))
# font="Times 14 bold"
# padx - x padding
# pady - y padding
# relief - border styling -SUNKEN,RISED,GROOVE,RIDGE
abhishek_label=Label(text='''Interstellar is a 2014 epic science fiction film co-written, directed, and produced by Christopher Nolan. \nIt stars Matthew McConaughey, Anne Ha\nthaway, Jessica Chastain, Bill Irwin, Ellen Burstyn, Michael Caine, and Matt Damon. \nSet in a dystopian future where humanity is embroiled in a catast\nrophic blight and famine, the film follows a group of astronauts who travel through a wormhole near Saturn in search of a new  \n''',bg="black",fg="white",padx=9,pady=1,relief=SUNKEN)
# Important pack options
#abhishek_label.pack(anchor="nw")
#abhishek_label.pack(side=BOTTOM,anchor="se")
# side=top,bottom,left,right
# by default side is top
abhishek_label.pack(side=BOTTOM,fill="x")
root.mainloop()