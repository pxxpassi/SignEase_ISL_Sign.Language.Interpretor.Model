# Importing Required Modules & libraries
from tkinter import *
import pygame
import os
import cv2
import mediapipe as mp
import numpy as np
import tensorflow as tf
from tkinter import PhotoImage
from PIL import Image, ImageTk

class Sign:
  
  def __init__(self,root):
    self.root = root
    # Title of the window
    self.root.title("Sign LAnguage Interpretation Model")
    # Window Geometry
    self.root.geometry("900x500")
    
    # Declaring track Variable
    self.track = StringVar()
    # Declaring Status Variable
    self.status = StringVar()

    def destroy():
      root.destroy()
    
    # Creating Track Frame for Song label & status label
    signframe = LabelFrame(self.root,text="Sign Language Interpretation",font=("times new roman",16,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
    signframe.place(x=0,y=0,width=400,height=500)
    label1 = Label(signframe,text="Interpreted:",font=("calibri",14,"bold"),fg="white", bg="grey").grid(row=0, column=0, columnspan=2, padx=10,pady=10)
    label2 = Label(signframe,text="Correction:",font=("calibri",14,"bold"),fg="white", bg="grey").grid(row=1, column=0, columnspan=2, pady=10)
    label2 = Label(signframe,text="Sentence:",font=("calibri",14,"bold"),fg="white", bg="grey").grid(row=2, column=0,padx=10,pady=10,columnspan=2)
    entry1 = Entry(signframe).grid(row=0, column=2, columnspan=1, pady = 10)
    entry1 = Entry(signframe).grid(row=1, column=2, columnspan=1, pady = 10)
    entry1 = Entry(signframe).grid(row=2, column=2, columnspan=1, pady = 10)
    button1 = Button(signframe, text="Reset", font = ("calibri",14,"bold"), fg="white", bg="black").grid(row=3,column=0,padx=10, pady=10)
    button2 = Button(signframe, text="Exit", font = ("calibri",14,"bold"), fg="white", bg="black",command=destroy).grid(row=3,column=1,padx=10, pady=10)
    
    camframe = LabelFrame(self.root,text="Camera",font=("times new roman",16,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
    camframe.place(x=400,y=0,width=500,height=500)
    label = Label(camframe)
    label.pack()

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    cap = cv2.VideoCapture(0)

    # Function to update the camera frame
    def update_frame():
        ret, frame = cap.read()
        if ret:
            # Convert the OpenCV frame to a PhotoImage
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = Image.fromarray(frame)
            photo = ImageTk.PhotoImage(image=frame)

            # Update the label with the new frame
            label.config(image=photo)
            label.photo = photo
            label.after(10, update_frame)
            # Update the frame every 10 milliseconds
      

    update_frame()  # Start updating the frame

    
    
    # Start the Tkinter main loop
    root.mainloop()

    # Release the camera and destroy the OpenCV window when the GUI is closed
    cap.release()
    cv2.destroyAllWindows()

# Creating TK Container
root = Tk()
# Passing Root to MusicPlayer Class
Sign(root)
# Root Window Looping
root.mainloop()
