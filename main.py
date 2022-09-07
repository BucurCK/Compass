import tkinter as tk
import math
import time

WIDTH = 610
HEIGHT = 610

def get_test():
    global test 
    test = input("GET DATA: ")
    if(float(test) > in_degree_pas):
        my_pas_right()
    else:
        my_pas_left()
    print("TESTING: " + test)

def my_pas_right():
    global in_degree_pas,arrow_head
    in_radian = math.radians(in_degree_pas)
    canvas1.delete(arrow_head)
    x2 = x+rc*math.sin(in_radian)
    y2 = y-rc*math.cos(in_radian)
    arrow_head = canvas1.create_line(x,y,x2,y2,arrow='last',fill='red',width=5)
    if(in_degree_pas >= 360):
        in_degree_pas = 0
    
    in_degree_pas += 1
    
    if(in_degree_pas != float(test)):
        canvas1.after(10,my_pas_right)

def my_pas_left():
    global in_degree_pas,arrow_head
    in_radian = math.radians(in_degree_pas)
    canvas1.delete(arrow_head)
    x2 = x+rc*math.sin(in_radian)
    y2 = y-rc*math.cos(in_radian)
    arrow_head = canvas1.create_line(x,y,x2,y2,arrow='last',fill='red',width=5)
    if(in_degree_pas <= 0):
        in_degree_pas = 360
    
    in_degree_pas -= 1
    
    if(in_degree_pas != float(test)):
        canvas1.after(10,my_pas_left)

my_window = tk.Tk()

width = WIDTH
height = HEIGHT

c_width = width - 5
c_height = height - 5 #canvas width and height

display = "800x800"
my_window.geometry(display)

canvas1 = tk.Canvas(my_window, width=c_width, height=c_height, bg = 'BlueViolet')
canvas1.grid(row=0, column=0, padx=5, pady=5)

button_test = tk.Button(text = "TEST", command = get_test)
button_test.grid(row =1,column=0,padx=5,pady=5)

dial=canvas1.create_oval(10,10,WIDTH-10,HEIGHT-10,width=10,outline='black',fill='lightblue')

x,y = WIDTH/2, HEIGHT/2 #center coord 305
x1,y1,x2,y2 = x,y,x,10 #second needle

thick_center = 0.05*WIDTH
center = canvas1.create_oval(x-thick_center,y-thick_center,x+thick_center,y+thick_center,fill='lightgrey')

r1 = WIDTH/2*0.92 # dial lines for segment
r2 = WIDTH/2*0.7 # for coord before segments
rc = WIDTH/2*0.78 # compass arrow head
in_degree = 0
in_degree_pas =0
coord = iter(['N','E','S','W'])
arrow_head = canvas1.create_line(x,y,x2,y-rc,fill='red',width=5, arrow='last')

for i in range(0,60): #print all the lines and text around the compass
    in_radian = math.radians(in_degree)
    if(i%15==0):
        ratio = 0.85
        t1 = x+r2*math.sin(in_radian) #for adding text
        t2 = y-r2*math.cos(in_radian)
        canvas1.create_text(t1,t2,fill='black',font='Times 30 bold',text=next(coord))
    else:
        ratio = 0.9

    x1 = x+ratio*r1*math.sin(in_radian)
    y1 = y-ratio*r1*math.cos(in_radian)
    x2 = x+r1*math.sin(in_radian)
    y2 = y-r1*math.cos(in_radian)
    canvas1.create_line(x1,y1,x2,y2,width=1,fill='black') ##adds lines
    in_degree += 6



# my_pas()
my_window.mainloop()
