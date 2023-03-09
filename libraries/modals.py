from tkinter import *
from datetime import datetime as dt
from . import myquery

#-----------------------------------------------current queries
qa1 = myquery.A1_query()
qa2 = myquery.A2_query()
qa3 = myquery.A3_query()
qa4 = myquery.A4_query()
#print(qa1[0])


#-------------------------------------------------windows
def emptywindow():
    q0= Label(entlab,text='Empty',bg='white')
    q0.grid(row=0, column=0,sticky=W,pady=4,padx=4)

    q1= Label(entlab,text='Empty',bg='white')
    q1.grid(row=1, column=0,sticky=W,pady=4,padx=4)
    
    q2= Label(entlab,text='Not specified',bg='white')
    q2.grid(row=2, column=0,sticky=W,pady=4,padx=4)
        
    q3= Label(entlab,text='Not specified',bg='white')
    q3.grid(row=3, column=0,sticky=W,pady=4,padx=4)

    q4= Label(entlab,text='Not specified',bg='white')
    q4.grid(row=4, column=0,sticky=W,pady=4,padx=4)
        
    q5= Label(entlab,text='Empty',bg='white')
    q5.grid(row=5, column=0,sticky=W,pady=4,padx=4)
        
    q6= Label(entlab,text='Empty',bg='white')
    q6.grid(row=6, column=0,sticky=W,pady=4,padx=4)
        
    q7= Label(entlab,text='Empty',bg='white')
    q7.grid(row=7, column=0,sticky=W,pady=4,padx=4)
        
    q8= Label(entlab,text='Available',bg='white')
    q8.grid(row=8, column=0,sticky=W,pady=4,padx=4)
        
    q9= Label(entlab,text='Empty',bg='white')
    q9.grid(row=9, column=0,sticky=W,pady=4,padx=4)
        
    q10= Label(entlab,text='Empty',bg='white')
    q10.grid(row=10, column=0,sticky=W,pady=4,padx=4)

def emptywindow2():
    q0= Label(entlab2,text='No info',bg='white',fg='#545454')
    q0.grid(row=0, column=0,sticky=W,pady=4,padx=4)

    q1= Label(entlab2,text='No info',bg='white',fg='#545454')
    q1.grid(row=1, column=0,sticky=W,pady=4,padx=4)
    
    q2= Label(entlab2,text='No info',bg='white',fg='#545454')
    q2.grid(row=2, column=0,sticky=W,pady=4,padx=4)
        
    q3= Label(entlab2,text='No info',bg='white',fg='#545454')
    q3.grid(row=3, column=0,sticky=W,pady=4,padx=4)

    q4= Label(entlab2,text='No info',bg='white',fg='#545454')
    q4.grid(row=4, column=0,sticky=W,pady=4,padx=4)
        
    q5= Label(entlab2,text='No info',bg='white',fg='#545454')
    q5.grid(row=5, column=0,sticky=W,pady=4,padx=4)
        
    q6= Label(entlab2,text='No info',bg='white',fg='#545454')
    q6.grid(row=6, column=0,sticky=W,pady=4,padx=4)
        
    q7= Label(entlab2,text='No info',bg='white',fg='#545454')
    q7.grid(row=7, column=0,sticky=W,pady=4,padx=4)
        
    q8= Label(entlab2,text='No info',bg='white',fg='#545454')
    q8.grid(row=8, column=0,sticky=W,pady=4,padx=4)
        
    q9= Label(entlab2,text='No info',bg='white',fg='#545454')
    q9.grid(row=9, column=0,sticky=W,pady=4,padx=4)
        
    q10= Label(entlab2,text='No info',bg='white',fg='#545454')
    q10.grid(row=10, column=0,sticky=W,pady=4,padx=4)

def a1_a1data():
    #function A1 apartment one data, queried from myquery
    q0= Label(entlab,text=qa1[0][0],bg='white')
    q0.grid(row=0, column=0,sticky=W,pady=4,padx=4)
            
    q1= Label(entlab,text=qa1[0][1],bg='white')
    q1.grid(row=1, column=0,sticky=W,pady=4,padx=4)
        
    q2= Label(entlab,text=qa1[0][10],bg='white')
    q2.grid(row=2, column=0,sticky=W,pady=4,padx=4)
            
    q3= Label(entlab,text=qa1[0][2],bg='white')
    q3.grid(row=3, column=0,sticky=W,pady=4,padx=4)

    q4= Label(entlab,text=qa1[0][3],bg='white')
    q4.grid(row=4, column=0,sticky=W,pady=4,padx=4)
            
    q5= Label(entlab,text=qa1[0][4],bg='white')
    q5.grid(row=5, column=0,sticky=W,pady=4,padx=4)
            
    q6= Label(entlab,text=qa1[0][5],bg='white')
    q6.grid(row=6, column=0,sticky=W,pady=4,padx=4)
            
    q7= Label(entlab,text=qa1[0][6],bg='white')
    q7.grid(row=7, column=0,sticky=W,pady=4,padx=4)
            
    q8= Label(entlab,text=qa1[0][7],bg='white')
    q8.grid(row=8, column=0,sticky=W,pady=4,padx=4)
            
    q9= Label(entlab,text=qa1[0][8],bg='white')
    q9.grid(row=9, column=0,sticky=W,pady=4,padx=4)
            
    q10= Label(entlab,text=qa1[0][9],bg='white')
    q10.grid(row=10, column=0,sticky=W,pady=4,padx=4)

def a1_a2data():
    q0= Label(entlab,text=qa1[1][0],bg='white')
    q0.grid(row=0, column=0,sticky=W,pady=4,padx=4)
            
    q1= Label(entlab,text=qa1[1][1],bg='white')
    q1.grid(row=1, column=0,sticky=W,pady=4,padx=4)
        
    q2= Label(entlab,text=qa1[1][10],bg='white')
    q2.grid(row=2, column=0,sticky=W,pady=4,padx=4)
            
    q3= Label(entlab,text=qa1[1][2],bg='white')
    q3.grid(row=3, column=0,sticky=W,pady=4,padx=4)

    q4= Label(entlab,text=qa1[1][3],bg='white')
    q4.grid(row=4, column=0,sticky=W,pady=4,padx=4)
            
    q5= Label(entlab,text=qa1[1][4],bg='white')
    q5.grid(row=5, column=0,sticky=W,pady=4,padx=4)
            
    q6= Label(entlab,text=qa1[1][5],bg='white')
    q6.grid(row=6, column=0,sticky=W,pady=4,padx=4)
            
    q7= Label(entlab,text=qa1[1][6],bg='white')
    q7.grid(row=7, column=0,sticky=W,pady=4,padx=4)
            
    q8= Label(entlab,text=qa1[1][7],bg='white')
    q8.grid(row=8, column=0,sticky=W,pady=4,padx=4)
            
    q9= Label(entlab,text=qa1[1][8],bg='white')
    q9.grid(row=9, column=0,sticky=W,pady=4,padx=4)
            
    q10= Label(entlab,text=qa1[1][9],bg='white')
    q10.grid(row=10, column=0,sticky=W,pady=4,padx=4)


def a1a1():
    global window
    window = Toplevel()
    window.title('A1 Apartment(1) Tenant Information')
    window.geometry('352x410+450+167')
    window.attributes('-toolwindow',1)
    window.attributes('-topmost', True) #inplace of true, 1 also works
    window.focus_force()
    
    global entlab
    global entlab2
    
    #create frame
    master = LabelFrame(window,height=400,width=270,pady=5,padx=5)
    master.grid(row=0,column=0,columnspan=2,sticky=W+E+N+S)
    
    topiclab = LabelFrame(master,relief='flat',bg='#e8e8e8',text='Tenant Information')
    topiclab.grid(row=0,column=0,sticky=S)
    
    entlab = LabelFrame(master,height=341,width=200,bg='#ffffff',relief='sunken',text='Current Tenant Info View')
    entlab.grid(row=0,column=1,sticky=W+E)
    
    entlab2 = LabelFrame(master,height=341,width=200,bg='#ffffff',relief='sunken',text='Previous Tenant Info View')
    entlab2.grid(row=0,column=1,sticky=W+E)
    
    spc = Frame(entlab,width=213,bg='#ffffff')
    spc.grid(row=0,column=0,columnspan=2)
 
    foot = Frame(window,width=100)
    foot.grid(row=1,column=0,rowspan=2,columnspan=2,sticky=W+E+N+S)

    f1 = Frame(foot,width=130)
    f1.grid(row=1,column=2,sticky=W+E)    
    
    #labelsTopics
    l0= Label(topiclab,text='Name :')
    l0.grid(row=0, column=0,sticky=W,pady=4)

    l1= Label(topiclab,text='Nationality :')
    l1.grid(row=1, column=0,sticky=W,pady=4)
    
    l2= Label(topiclab,text='Room Number :')
    l2.grid(row=2, column=0,sticky=W,pady=4)
    
    l3= Label(topiclab,text='Apartment Type :')
    l3.grid(row=3, column=0,sticky=W,pady=4)

    l4= Label(topiclab,text='Apartment Number :')
    l4.grid(row=4, column=0,sticky=W,pady=4)
    
    l5= Label(topiclab,text='Contact :')
    l5.grid(row=5, column=0,sticky=W,pady=4)
    
    l6= Label(topiclab,text='Email :')
    l6.grid(row=6, column=0,sticky=W,pady=4)
    
    l7= Label(topiclab,text='Emergency Contact :')
    l7.grid(row=7, column=0,sticky=W,pady=4)
    
    l8= Label(topiclab,text='Room Status :')
    l8.grid(row=8, column=0,sticky=W,pady=4)
    
    l9= Label(topiclab,text='CheckIn Date :')
    l9.grid(row=9, column=0,sticky=W,pady=4)
    
    l10= Label(topiclab,text='Next Vacancy :')
    l10.grid(row=10, column=0,sticky=W,pady=4)
    
    #labelQueries
    try:
        if 'A1' and '1' in qa1[0]: 
            entlab.lift()         
            a1_a1data()
        else:
            emptywindow()
    except IndexError:
        emptywindow()
    
    chk = IntVar()
    def cal_cb():
        pt=chk.get()
    
        d = dt.strptime(qa1[0][9],'%Y-%m-%d').date()
        ans = myquery.a1a1Query(d)
        print(ans)
        if pt == 1 and ans == []:
            entlab2.lift()
            emptywindow2()
        elif pt == 0:
            entlab.lift()
            a1_a1data()
        else:
            entlab2.lift()

            q0= Label(entlab2,text=ans[0][1],bg='white')
            q0.grid(row=0, column=0,sticky=W,pady=4,padx=4)
                    
            q1= Label(entlab2,text=ans[0][2],bg='white')
            q1.grid(row=1, column=0,sticky=W,pady=4,padx=4)
                
            q2= Label(entlab2,text=ans[0][8],bg='white')
            q2.grid(row=2, column=0,sticky=W,pady=4,padx=4)
                    
            q3= Label(entlab2,text=ans[0][9],bg='white')
            q3.grid(row=3, column=0,sticky=W,pady=4,padx=4)

            q4= Label(entlab2,text=ans[0][10],bg='white')
            q4.grid(row=4, column=0,sticky=W,pady=4,padx=4)
                    
            q5= Label(entlab2,text=ans[0][4],bg='white')
            q5.grid(row=5, column=0,sticky=W,pady=4,padx=4)
                    
            q6= Label(entlab2,text=ans[0][6],bg='white')
            q6.grid(row=6, column=0,sticky=W,pady=4,padx=4)
                    
            q7= Label(entlab2,text=ans[0][7],bg='white')
            q7.grid(row=7, column=0,sticky=W,pady=4,padx=4)
                    
            q8= Label(entlab2,text='_____________',bg='white')
            q8.grid(row=8, column=0,sticky=W,pady=4,padx=4)
                    
            q9= Label(entlab2,text=ans[0][11],bg='white')
            q9.grid(row=9, column=0,sticky=W,pady=4,padx=4)
                    
            q10= Label(entlab2,text=ans[0][12],bg='white')
            q10.grid(row=10, column=0,sticky=W,pady=4,padx=4)
        

    #checkbox
    cb = Checkbutton(foot,text='View previous tenant',variable=chk,command=cal_cb)
    cb.grid(row=0,column=0)
    cb.deselect()
        
    #create buttons
    b1 = Button(foot,text='Ok',width='10',bd=1,command=window.destroy)
    b1.grid(row=0,column=3,sticky=E+S,pady=8)
    

#a1a1()

def a1a2():
    try:
        window.destroy()
    except:
        pass
   
#a1a2()


def closing():
    try:
        window.destroy()
    except TclError:
        pass
    try:
        window1.destroy()
    except TclError:
        pass
