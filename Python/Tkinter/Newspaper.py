from tkinter import *
import os
from PIL import Image,ImageTk
root = Tk()
root.geometry("1500x800")
Current_dir=os.getcwd()
Image_path=os.path.join(Current_dir,"Images","code - Shortcut.png")# To add image from other directory
img1 = PhotoImage(file=Image_path)
label1 = Label(root, image=img1, width=100, height=50)
label1.pack(anchor="nw",side="left")
label2=Label(text="This is a miecraft background")
label2.pack(side="left",anchor="nw")
Image_Path2=os.path.join(Current_dir,"Images","pexels-eberhard-grossgasteiger-1612371.png")
img2=PhotoImage(file=Image_Path2)
label3=Label(image=img2,width=100,height=50)
label3.pack(anchor="nw")
root.mainloop()
# from tkinter import *
# from PIL import Image, ImageTk
# import os
# root = Tk()
# root.geometry("1500x800")
# Current_dir = os.getcwd()
# # First Image
# Image_path = os.path.join(Current_dir, "Images", "pexels-tuấn-kiệt-jr-1391498.jpg")
# img1 = Image.open(Image_path)
# img1 = img1.resize((300, 300))  # Resize image to fit label
# img1 = ImageTk.PhotoImage(img1)
# label1 = Label(root, image=img1)
# label1.pack(anchor="nw", side="left")
# label2 = Label(text="This is a minecraft background")
# label2.pack(side="left", anchor="nw")
# # Second Image
# Image_Path2 = os.path.join(Current_dir, "Images", "pexels-eberhard-grossgasteiger-1612371.jpg")
# img2 = Image.open(Image_Path2)
# img2 = img2.resize((300, 300))  # Resize image to fit label
# img2 = ImageTk.PhotoImage(img2)
# label3 = Label(image=img2)
# label3.pack(anchor="nw")
# root.mainloop()


