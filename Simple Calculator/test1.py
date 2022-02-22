# import module
# crete main application window
# widgets
# hold main window
from cProfile import label
from tkinter import *
root=Tk()
root.title("my GUI appilcation")
root.geometry("400x300") 
root.resizable(False,False)                    # properties changing method
root.attributes('-alpha',1)                  # window light  adjusting mode
#root.config(bg='red')                        # window color change or # (root[bg='yellow])

l1=Label(root, text ="username :")#bg="blue"
l2=Label(root , text="password :")#bg='yellow'
e1=Entry(root,textvariable='a')
e2=Entry(root,textvariable='*')
#def fun():
#print ('button click')
#b1.Button(root,text="click")
#l4=label(image=legal1.jpg,_Compound,right)
e1=Entry(root)
e2=Entry(root)
l1.grid(row=1,column=4)
l2.grid(row=2,column=4)
root.mainloop()
#constructor
