
import tkinter as  tk
import datetime
from tkinter import ttk
import cv2
import pytesseract
import sys
import os
import sqlite3
#from PIL import Image
from csv import DictWriter
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
#from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
#from pandas import DataFrame
import numpy as np
#import search
WIDTH = 1500
HEIGHT =1500
root = tk.Tk()
root.title('TOLLNITIAN')
root.iconbitmap('car_13260.ico')
canvas = tk.Canvas(root , height= WIDTH,width=HEIGHT,bg='#ffffff')
canvas.pack()
#menu bar
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def load():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    showImage()

def abt_us():
    tk.messagebox.showinfo("Developed By","Sukhveer Singh")
def git_lnk():
    tk.messagebox.showinfo("GITHUB","github.com/veersingh9540 give LIKE and SHARE")
#open a new window on click  search
def Search():
    newWin = tk.Toplevel(root)
    canvas = tk.Canvas(newWin , height= 1000,width=1000,bg='#ffffff')
    canvas.pack()
    #search frame
    search_frame= tk.Frame(newWin , bg='#b8f5ca',bd=5)
    search_frame.place(relx=0.05,rely= 0.07,relwidth=0.5,relheight=0.90)
    #UI making
    vehiclefont = ('times', 20 , 'bold')
    vehicle_label = tk.Label(search_frame,text="VEHICLE NO...",font=vehiclefont ,bg='#d4fcdf')
    vehicle_label.place( rely=0.02 ,relwidth=1, relheight=0.05  )
    entryN_var = tk.StringVar()
    vehicle_entry = tk.Entry(search_frame,text=entryN_var, textvariable= entryN_var, justify = 'center')
    vehicle_entry.place(rely=0.075, relwidth=1 , relheight=0.05 , )
    vehicle_entry.focus()

    place_label = tk.Label(search_frame,text="PLACE",font=vehiclefont ,bg='#d4fcdf')
    place_label.place( rely=0.150 ,relwidth=1, relheight=0.05  )
    place_var = tk.StringVar()
    place_entry = tk.Entry(search_frame,text=place_var, textvariable= place_var, justify = 'center')
    place_entry.place(rely=0.205, relwidth=1 , relheight=0.05 , )


    type_label = tk.Label(search_frame,text="TYPE OF TRAVEL",font=vehiclefont ,bg='#d4fcdf')
    type_label.place( rely=0.280 ,relwidth=1, relheight=0.05  )
    type_var = tk.StringVar()
    type_entry = tk.Entry(search_frame,text=type_var, textvariable= type_var, justify = 'center')
    type_entry.place(rely=0.335, relwidth=1 , relheight=0.05 , )


    vehiclehl_label = tk.Label(search_frame,text="TYPE OF VEHICLE",font=vehiclefont ,bg='#d4fcdf')
    vehiclehl_label.place( rely=0.41 ,relwidth=1, relheight=0.05  )
    entryhl_var = tk.StringVar()
    vehiclehl_entry = tk.Entry(search_frame,text=entryhl_var, textvariable= entryhl_var, justify = 'center')
    vehiclehl_entry.place(rely=0.465, relwidth=1 , relheight=0.05 , )


    vehicleso_label = tk.Label(search_frame,text="VEHICLE REGISTRATION",font=vehiclefont ,bg='#d4fcdf')
    vehicleso_label.place( rely=0.54 ,relwidth=1, relheight=0.05  )
    entryso_var = tk.StringVar()
    vehicleso_entry = tk.Entry(search_frame,text=entryso_var, textvariable= entryso_var, justify = 'center')
    vehicleso_entry.place(rely=0.595, relwidth=1 , relheight=0.05 , )


    donation_label = tk.Label(search_frame,text="DONATED ??",font=vehiclefont ,bg='#d4fcdf')
    donation_label.place( rely=0.67 ,relwidth=1, relheight=0.05  )
    donation_var = tk.StringVar()
    donation_entry = tk.Entry(search_frame,text=donation_var, textvariable= donation_var, justify = 'center')
    donation_entry.place(rely=0.725, relwidth=1 , relheight=0.05 , )


    dnt_label = tk.Label(search_frame,text="DATE AND TIME",font=vehiclefont ,bg='#d4fcdf')
    dnt_label.place( rely=0.8 ,relwidth=1, relheight=0.05  )
    dnt_var = tk.StringVar()
    dnt_entry = tk.Entry(search_frame,text=dnt_var, textvariable= dnt_var, justify = 'center')
    dnt_entry.place(rely=0.855, relwidth=1 , relheight=0.05 , )

    #frame for image
    frameS= tk.Frame(newWin , bg='#000000',bd=5)
    frameS.place(relx=0.57,rely=0.30,relwidth=0.39,relheight=0.39)
    #label for image
    cam_canvasSL= tk.Canvas(frameS ,width=50,height=50)
    cam_canvasSL.place( relwidth=1,relheight=1)

    fig = Figure(figsize=(5, 4), dpi=100)
    t = np.arange(0, 3, .01)
    fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

    canvas = FigureCanvasTkAgg(fig, master=cam_canvasSL)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, cam_canvasSL)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    #database search
    def database_search():
        global SLi
        Connect = sqlite3.connect('Toll_data.db')
        c = Connect.cursor()
        c.execute("SELECT * FROM Toll WHERE Vehicle_No='%s'"%entryN_var.get())
        data=c.fetchone()
        place_var.set(data[1])
        type_var.set(data[2])
        entryhl_var.set(data[3])
        entryso_var.set(data[4])
        donation_var.set(data[5])
        dnt_var.set(data[6])
        #imageSL = tk.PhotoImage(Image.open(data[7]))
        #SLi= imageSL.subsample(1,2)
        Connect.commit()
        Connect.close()

    submit_button = tk.Button(search_frame, text='SEARCH', command =database_search)
    submit_button.place(relx= 0.4, rely= 0.95,relheight=0.05 , relwidth=0.2 )

def data_analysis1():
    os.system('python data.py')


def data_analysis2():
    os.system('python vehicle.py')

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
filemenu2.add_command(label="About Us",command =abt_us )
filemenu2.add_command(label="SEARCH VEHICLE DATA",command= Search)
filemenu2.add_separator()
filemenu2.add_command(label="Git hub Link", command=git_lnk)
menubar.add_cascade(label="Help", menu=filemenu2)

filemenu3 = tk.Menu(menubar, tearoff=0)
filemenu3.add_command(label="Heavy Load Analysis",command= data_analysis1)
filemenu3.add_separator()
filemenu3.add_command(label="ALL Analysis",command= data_analysis2)

menubar.add_cascade(label="Data Analysis", menu=filemenu3)



#label for the app heading
labelfont=('times' ,45, 'bold')
frame_label = tk.Label(root ,text="ROAD AUTHORITY OF INDIA",font=labelfont,bg='#ffffff')
frame_label.place( rely=0.02 ,relwidth=1, relheight=0.05  )

frame_label2 = tk.Label(root ,text="HAVE A PLEASENT AND SAFE JOURNEY.....",font=labelfont,bg='#ffffff')
frame_label2.place( rely=0.92 ,relwidth=1, relheight=0.05  )

# frame for information
frame= tk.Frame(root , bg='#ffffff', borderwidth=2 , relief="groove")
frame.place(relx=0.05,rely= 0.09,relwidth=0.39,relheight=0.82)

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
frame2= tk.Frame(root , bg='#000000', borderwidth=2 , relief="groove")
frame2.place(relx=0.50,rely=0.09,relwidth=0.39,relheight=0.39)
#label for image
cam_canvas= tk.Label(frame2 ,width=50,height=50, borderwidth=5 , relief="groove")
cam_canvas.place(relx=0, rely=0.070, relwidth=1,relheight=0.81)

#LABEL for the camera
auto_take = tk.Label(frame2,text='AI CAMERA ')
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
        threshold()
        load()
   capture.release()
   cv2.destroyAllWindows()


background_image = tk.PhotoImage(file="img_name.png")
tmi= background_image.subsample(1,2)
#thresholding function
def threshold():

    image1 = cv2.imread('img_name.png')
    img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)    
    
                                          

    cv2.imwrite('thres_img_name.png',img)
    text = pytesseract.image_to_string('thres_img_name.png')
    pytext = ("hello")
    entry_var.set(text)
    print(pytext)


background_image2 = tk.PhotoImage(file="thres_img_name.png")
tmi2=background_image2.subsample(1,2)


#image for the camera
def showImage():
    cam_canvas.config(image=tmi)
#button for TASKS frame2
image_show = tk.Button(frame2,text='SHOW THIS IMAGE' ,command= showImage)
image_show.place(relx= 0.3, rely= 0.9,relheight=0.08 , relwidth=0.4 )

#frame for CURRENT image
frame3= tk.Frame(root , bg='#000000', borderwidth=2 , relief="groove")
frame3.place(relx=0.50,rely=0.50,relwidth=0.39,relheight=0.39)

image2 = tk.PhotoImage(file="thres_img_name.png")
i2=image2.subsample(1,2)
image3 = tk.PhotoImage(file="img_name.png")
i3=image3.subsample(1,2)
#image functions
def cur_thres():

    cur_canvas.config(image=i2)

def hello():
    threshold()
    cur_thres()
#label for image
cur_canvas= tk.Label(frame3 ,width=50,height=50 ,borderwidth=5 , relief="groove")
cur_canvas.place(relx=0, rely=0.070, relwidth=1,relheight=0.81)
#button for image SHOW
cur_thres_button = tk.Button(frame3,text='PROCESS THIS IMAGE' ,command= hello)
cur_thres_button.place(relx= 0.55, rely= 0.9,relheight=0.08 , relwidth=0.4 )

image_show = tk.Button(frame3,text='Load the data ' ,command=load)
image_show.place(relx= 0.2, rely= 0.9,relheight=0.08 , relwidth=0.2 )


cur_auto_take = tk.Label(frame3,text='VEHICLE IMAGE DATA')
cur_auto_take.place(relx=0 ,rely= 0.015, relwidth= 1, relheight=0.05)
#submit button
def database_action():
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
    with open('img_name.png','rb') as f:
        image_data = f.read()
    conn = sqlite3.connect('Toll_data.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Toll(Vehicle_No TEXT,Place TEXT,Entry TEXT,State TEXT,Vehicle_Type TEXT,Date_and_Time TEXT,Donation TEXT,IMAGE)')
    cursor.execute('INSERT INTO Toll(Vehicle_No,Place,Entry,State,Vehicle_Type,Date_and_Time,Donation,IMAGE) VALUES(?,?,?,?,?,?,?,?)',(car_no,place,entry,state,vehicle,date_time,check,image_data))
    conn.commit()
    conn.close()
    #print(f'{car_no}  {place}  {entry}  {state}  {vehicle}  {date_time}  {check}')

    # write to csv file
    with open('file.csv','a') as f:
        dict_writer = DictWriter(f,fieldnames=['Sno','Car Number','Place','Entry','State','Vehicle','Date and Time','Donation'])
        if  os.stat('file.csv').st_size==0:
             dict_writer.writeheader()

        dict_writer.writerow({
            'Car Number': car_no,
            'Place': place,
            'Entry':entry,
            'State': state,
            'Vehicle': vehicle ,
            'Date and Time': date_time,
            'Donation': check

        }
        )

    vehicle_entry.delete(0,tk.END)

submit_button = tk.Button(frame, text='SUBMIT', command =database_action)
submit_button.place(relx= 0.2, rely= 0.9,relheight=0.05 , relwidth=0.2 )
root.bind("<Return>",database_action)
snap = tk.Button(frame,text='CAMERA' , command=web)
snap.place(relx= 0.6, rely= 0.9,relheight=0.05 , relwidth=0.2 )


root.mainloop()
