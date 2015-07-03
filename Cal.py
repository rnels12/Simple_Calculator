from __future__ import division
from Tkinter import *


def main():
    root = Tk()
    expl = []
    
    #Create number entry
    F1 = Frame(root,height=4, bd=1, relief=SUNKEN)
    F1.grid(columnspan=10)
    num_entry = Entry(F1)
    num_entry.grid(columnspan=4)

    #Create number & dot buttons
    F2 = Frame(); F2.grid()
    add_butt(F2,"0",4,0,num_entry,expl)
    dot = add_butt(F2,".",4,1,num_entry,expl)
    for i in range(3):
        for j in range(3) : add_butt(F2,str(i*3+j+1),i+1,j,num_entry,expl)

    #Create operation buttons    
    add_butt(F2,"=",4,2,num_entry,expl)
    add_butt(F2,"+",1,3,num_entry,expl)
    add_butt(F2,"-",2,3,num_entry,expl)
    add_butt(F2,"x",3,3,num_entry,expl)
    add_butt(F2,"/",4,3,num_entry,expl)
    add_butt(F2,"ESC",1,4,num_entry,expl)

    mainloop()


def add_butt(master,lab,r,c,ent,tmp):
    Button(master,text=lab,height=2, width=3, \
           command=lambda:callback( lab,ent,tmp ))\
        .grid(row=r,column=c,sticky=W)

#make buttons operating
def callback(name,ent,tmp):
    try:
        int(name)
        if len(tmp) != 0 and (tmp[-1] == '+' or tmp[-1] == '-' or\
                              tmp[-1] == '*' or tmp[-1] == '/') :
            ent.delete(0,END)
        ent.insert(END,name)
        tmp += [name]
    except ValueError:
        if name == "ESC" :
            Reset(ent,tmp)
            print tmp
        elif name == '.' and '.' not in ent.get() :
            if len(tmp) != 0 and (tmp[-1] == '+' or tmp[-1] == '-' or\
                                  tmp[-1] == '*' or tmp[-1] == '/') :
                ent.delete(0,END)
            ent.insert(END,name)
            tmp += [name]
        elif name == '+' : tmp += [name]
        elif name == '-' : tmp += [name]
        elif name == 'x' : tmp += ["*"]
        elif name == '/' : tmp += [name]
        else :
            ent.delete(0,END)
            result = eval( ''.join(tmp) )
            ent.insert(0,result)
            tmp[:] = [str(result)]
            
def Reset(ent,tmp):
    ent.delete(0,END)
    tmp[:] = []        
            
if __name__ == '__main__':
    main()
