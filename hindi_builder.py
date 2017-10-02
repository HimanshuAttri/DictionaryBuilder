 # -*- coding: utf-8 -*-
import sys  
from Tkinter import *
import numpy as np
root = Tk()
reload(sys)  
sys.setdefaultencoding('utf-8')
sz=13

def add():
    if len(e.get())==0 or len(f.get())==0:
     err=Tk()
     Label(err, text="Error: Invalid Entry",font=(None, sz)).grid(row=0,column=0)
     Button(err, text='Ok',command=err.destroy,font=(None, sz)).grid(row=1,column=0)
     print "Error himanshu"
     return 0
    F = open(e.get(),'w') 
    F.write(f.get())
    f.delete(0,'end')
    e.delete(0,'end')
   

def read():
    T.delete('1.0', END)
    if len(e.get())==0:
     err=Tk()
     Label(err, text="Error: Invalid Entry",font=(None, sz)).grid(row=0,column=0)
     Button(err, text='Ok',command=err.destroy,font=(None, sz)).grid(row=1,column=0)
     print "Error himanshu"
     return 0
    F = open(e.get(),'r') 
    st=F.read()
    f.insert(0,st)
    T.insert(END, e.get()+": "+st+"\n")
    

def printall():
    F = open(e.get(),'r') 
    print e.get(),": ",F.read()


def listall():
    ms=''
    T.delete('1.0', END)
    import glob, os
#    os.chdir("/home/himanshu/dm")
    for f in glob.glob("*"):
      if f=="h1.py":
        continue  
      if f=="final.txt":
        continue 
      print(f)
      ms=ms+f+' '

       
      
      
    w=ms.split()  
    w.sort()
    
    for word in w:
      print(word)
      F = open(word,'r')
      T.insert(END, word+": "+F.read()+"\n")
      G = open('final.txt','a')
      G.write(word+": "+F.read()+"\n")

Label(root, text="शब्द",font=(None, sz)).grid(row=0)
Label(root, text="अर्थ",font=(None, sz)).grid(row=1)
e = Entry(root,font=(None, sz))
f = Entry(root,font=(None, sz))

e.grid(row=0, column=1)

f.grid(row=1, column=1)
status=Label(root, text="",font=(None, sz)).grid(row=0,column=2)


kl=Tk()


Button(root, text='Save', command=add)

T = Text(kl, height=20, width=30,font=(None, sz))
T.pack()
Button(root, text='खोज',command=read,font=(None, sz)).grid(row=2,column=0)
Button(root, text='सभी देखें',command=listall,font=(None, sz)).grid(row=2,column=1)
Button(root, text='रक्षित करें',command=add,font=(None, sz)).grid(row=2,column=2)
#r=Tk()
#app = App(master = r)
mainloop()














