import tkinter as tk
import datetime 
from csv import DictWriter
from tkinter import ttk
import cv2
#import subprocess
from PIL import ImageTk, Image
import pytesseract
import numpy as np
#from tkinter import *
#import time
import sys
#import PIL.Image
#import numpy as np
import pytesseract
from pytesseract import image_to_string
import os
#from tkinter import filedialog
#import tkFileDialog


WIDTH = 1500
HEIGHT =1800
root = tk.Tk()
root.title('TOLLNITIAN')
canvas = tk.Canvas(root , height= WIDTH,width=HEIGHT,bg='#ffffff')
canvas.pack()
#menu bar
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def load():   
    python = sys.executable
    os.execl(python, python, * sys.argv)
def abt_us():
    tk.messagebox.showinfo("Developed By","Sukhveer Singh")
def git_lnk():
    tk.messagebox.showinfo("GITHUB","github.com/veersingh give LIKE and SHARE")  
menubar = tk.Menu(root)
root.config(menu=menubar)
# create a pulldown menu, and add it to the menu bar
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New",command= load)
filemenu.add_separator()
filemenu.add_command(label="Restart",command=restart_program)
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

filemenu2 = tk.Menu(menubar, tearoff=0)
filemenu2.add_command(label="About Us",command=abt_us)
filemenu2.add_separator()
filemenu2.add_command(label="Git hub Link", command=git_lnk)
menubar.add_cascade(label="Help", menu=filemenu2)




#label for the app heading
labelfont=('times' ,45, 'bold')
frame_label = tk.Label(root ,text="ROAD AUTHORITY OF INDIA",font=labelfont,bg='#ffffff')
frame_label.place( rely=0.02 ,relwidth=1, relheight=0.05  ) 

frame_label2 = tk.Label(root ,text="HAVE A PLEASENT AND SAFE JOURNEY.....",font=labelfont,bg='#ffffff')
frame_label2.place( rely=0.92 ,relwidth=1, relheight=0.05  ) 

# frame for information 
frame= tk.Frame(root , bg='#ffffff',bd=5)
frame.place(relx=0.05,rely= 0.07,relwidth=0.39,relheight=0.82)

vehiclefont = ('times', 20 , 'bold')
vehicle_label = tk.Label(frame,text="VEHICLE NO...",font=vehiclefont ,bg='#d4fcdf')
vehicle_label.place( rely=0.02 ,relwidth=1, relheight=0.05  )      

entry_var = tk.StringVar()
vehicle_entry = tk.Entry(frame,text=entry_var, textvariable= entry_var, justify = 'center')
vehicle_entry.place(rely=0.075, relwidth=1 , relheight=0.05 , )    
vehicle_entry.focus()             

place_label = tk.Label(frame,text="ENTER PLACE",font=vehiclefont ,bg='#d4fcdf')
place_label.place( rely=0.180    ,relwidth=1, relheight=0.05  ) 

place_var = tk.StringVar()
place_combobox = ttk.Combobox(frame,text='PLACE',textvariable=place_var, state='readonly',justify='center')   
place_combobox['values']= ('PLACE 1','PLACE 2', 'PLACE 3 ')
place_combobox.current(0)
place_combobox.place(rely=0.235, relwidth= 1 , relheight=0.04)


side_label = tk.Label(frame,text="SELECT THE TYPE OF JOURNEY ",font=vehiclefont ,bg='#d4fcdf')
side_label.place( rely=0.340 ,relwidth=1, relheight=0.05  ) 

type_var = tk.StringVar()
journey_type = ttk.Radiobutton(frame, text='One Way', value= 'One Way', variable=type_var)
journey_type.place(relx=0,rely=0.40, relwidth= 0.49, relheight=0.05)

journey_type2 = ttk.Radiobutton(frame, text='Round Trip', value= 'Round Trip', variable=type_var)
journey_type2.place(relx=0.51,rely=0.40, relwidth= 0.49, relheight=0.05)

state_var = tk.StringVar()
state_type = ttk.Radiobutton(frame, text='STATE VEHICLE', value= 'STATE VEHICLE', variable=state_var)
state_type.place(relx=0,rely=0.47, relwidth= 0.49, relheight=0.05)

ostate_type = ttk.Radiobutton(frame, text='OUTER STATE VEHICLE', value= 'OUTER STATE VEHICLE', variable=state_var)
ostate_type.place(relx=0.51,rely=0.47, relwidth= 0.49, relheight=0.05)

vehicletyp_var = tk.StringVar()
vehicle_type = ttk.Radiobutton(frame, text='Light Vehicle', value= 'Light Vehicle', variable=vehicletyp_var)
vehicle_type.place(relx=0,rely=0.54, relwidth= 0.49, relheight=0.05)

vehicle_type2 = ttk.Radiobutton(frame, text='Heavy Vehicle', value= 'Heavy Vehicle', variable=vehicletyp_var)
vehicle_type2.place(relx=0.51,rely=0.54, relwidth= 0.49, relheight=0.05)

check_var = tk.IntVar()
state_check = ttk.Checkbutton(frame , text= "I agree to donate Rs 10 to the SWACHH BHARAT ABHIYAN CAMPAIGN ", variable=check_var)
state_check.place(rely= 0.6, relwidth= 1, relheight= 0.05 )


dnt_label = tk.Label(frame,text="DATE AND TIME ",font=50 ,bg='#d4fcdf')
dnt_label.place( rely=0.7 ,relwidth=1, relheight=0.05  ) 

dnt_var= tk.StringVar()
now = datetime.datetime.now()
dnt_msg = tk.Entry(frame,text=dnt_var,justify='center', state= 'readonly' )
dnt_var.set(now.strftime("%A-%d-%B-%Y %X"))
dnt_msg.place(rely= 0.76,relwidth= 1,relheight= 0.1)

#frame for camera FRAME 2
frame2= tk.Frame(root , bg='#80c1ff',bd=5)
frame2.place(relx=0.50,rely=0.07,relwidth=0.39,relheight=0.39)
#label for image 
cam_canvas= tk.Label(frame2 ,width=50,height=50 )
cam_canvas.place(relx=0, rely=0.070, relwidth=1,relheight=0.81)

#LABEL for the camera 
auto_take = tk.Label(frame2,text='AI CAMERA Demonstration')
auto_take.place(relx=0 ,rely= 0.015, relwidth= 1, relheight=0.05)
#camera code
def web():
   global background_image
   capture =cv2.VideoCapture(0)
   cv2.namedWindow("test")
   
   while True:
      ret,frame=capture.read()
      cv2.imshow('frame',frame)
      if not ret:
          break
      k = cv2.waitKey(1)
      if k%256 == 27:   
        # ESC pressed
        print("Escape hit, closing...")
        break
      elif k%256 == 32:
        # SPACE pressed
        #img_name = "opencv_frame_{}.png".format(img_counter)
        #image storing
        cv2.imwrite('img_name.png', frame)
      
   capture.release()
   cv2.destroyAllWindows()
   
background_image = tk.PhotoImage(file="img_name.png")   
tmi= background_image.subsample(1,2)
    
#thresholding function
def threshold():
    
    cam_canvas.config(image=tmi2)
    image1 = cv2.imread('img_name.png')
    img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY) 
    thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                          cv2.THRESH_BINARY, 199, 5) 
    #cv2.imshow('Adaptive Gaussian', thresh2) 
    cv2.imwrite('thres_img_name.png',thresh2)
    text = pytesseract.image_to_string('thres_img_name.png')
    pytext = ("hello")
    entry_var.set(text)
    print(pytext)
    

background_image2 = tk.PhotoImage(file="thres_img_name.png")
tmi2=background_image2.subsample(1,2)

    

#image view 
#image_list=[tmi,tmi2]
#image for the camera
def showImage():
    cam_canvas.config(image=tmi)
    

#button for TASKS
snap = tk.Button(frame2,text='CAMERA' , command=web)
snap.place(relx= 0.15, rely= 0.9,relheight=0.08 , relwidth=0.2 )

image_show = tk.Button(frame2,text='SHOW' ,command= showImage)
image_show.place(relx= 0.4, rely= 0.9,relheight=0.08 , relwidth=0.2 )
  
thres = tk.Button(frame2,text='image_correct', command =threshold )
thres.place(relx= 0.65, rely= 0.9,relheight=0.08 , relwidth=0.2 )
#frame for CURRENT image
frame3= tk.Frame(root , bg='#80c1ff',bd=5)
frame3.place(relx=0.50,rely=0.50,relwidth=0.39,relheight=0.39)

image2 = tk.PhotoImage(file="thres_img_name.png")
i2=image2.subsample(1,2)
image3 = tk.PhotoImage(file="img_name.png")
i3=image3.subsample(1,2)
#image functions
def cur_thres():
    
    cur_canvas.config(image=i2)
    
def cur_image():
    #image1 = ImageTk.PhotoImage(pil_image)
    cur_canvas.config(image=i3)

#label for image
cur_canvas= tk.Label(frame3 ,width=50,height=50 )
cur_canvas.place(relx=0, rely=0.070, relwidth=1,relheight=0.81)
#button for image SHOW 
cur_thres = tk.Button(frame3,text='Image_Correct' ,command= cur_thres)
cur_thres.place(relx= 0.65, rely= 0.9,relheight=0.08 , relwidth=0.2 )

image_show = tk.Button(frame3,text='Load the data ' ,command=load)
image_show.place(relx= 0.4, rely= 0.9,relheight=0.08 , relwidth=0.2 )

cur_snap = tk.Button(frame3,text='SHOW CURRENT VEHICLE', command= cur_image)
cur_snap.place(relx= 0.03, rely= 0.9,relheight=0.08 , relwidth=0.33 )

cur_auto_take = tk.Label(frame3,text='VEHICLE IMAGE DATA')
cur_auto_take.place(relx=0 ,rely= 0.015, relwidth= 1, relheight=0.05)
#submit button
def action():
    car_no = entry_var.get()
    place = place_var.get()
    entry = type_var.get()
    state = state_var.get()
    vehicle = vehicletyp_var.get()
    date_time = dnt_var.get()
    if check_var.get()== 1:
        check = 'YES'
    else:
        check = 'NO' 
        
    #print(f'{car_no}  {place}  {entry}  {state}  {vehicle}  {date_time}  {check}')
# write to csv file 
    with open('file.csv', 'a') as f:
            dict_writer = DictWriter(f,fieldnames=['VEHICLE NO','PLACE','ENTRY TYPE','STATE','VEHICLE TYPE','DONATION', 'DATE & TIME'])
            if os.stat('file.csv').st_size==0:
               dict_writer.writeheader()
            dict_writer.writerow({
                    'VEHICLE NO': car_no,
                    'PLACE': place,
                    'ENTRY TYPE': entry,
                    'STATE': state,
                    'VEHICLE TYPE': vehicle,
                    'DONATION': check,
                    'DATE & TIME': date_time
                    
                    })
    

    vehicle_entry.delete(0,tk.END)
           
submit_button = tk.Button(frame, text='SUBMIT', command =action)
submit_button.place(relx= 0.4, rely= 0.9,relheight=0.05 , relwidth=0.2 )


root.mainloop()


