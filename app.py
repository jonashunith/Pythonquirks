from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import TkTreectrl 
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta as rd
import time
from libraries import backend,myquery,modals


win=Tk()
win.title('Administrator interface')
win.geometry('')


def abt():
    about=Toplevel()
    about.title('')
    about.geometry('400x400+200+100')
    about.resizable(0,0)
    about.attributes('-toolwindow',1)
    about.attributes('-topmost',True)
    about.focus_force()
    
    fr1 = Frame(about)
    fr1.grid(row=0,column=0,sticky=W+E)
    fr2 = Frame(about)
    fr2.grid(row=2,column=0,pady=10,sticky=W+E)
    
    txt0 = Label(fr1,text='Administrator',font=('Helvetica','30','bold'),fg='teal',width='16')
    txt0.grid(row=0,column=0,pady=5)
    ttk.Separator(about).grid(row=1,column=0,columnspan=1,padx=2,sticky=W+E)
    
    txt1 = Label(fr2,justify='left',text='\tAdministrator Software \n\tVersion 1000 \n\t©2020.All rights reserved \n\tDesigned by IADS gh')
    txt1.grid(row=0,column=0)
    




#create a menu
menubar = Menu(win)

#add first menu dropdown called File
menu = Menu(menubar, tearoff=0)
menu.add_command(label='Registration')
menu.add_command(label='Admin')
menu.add_separator()
menu.add_command(label='Exit',command=win.destroy)
menubar.add_cascade(label='File', menu=menu)

#add another menu dropdown
menuedit = Menu(menubar, tearoff=0)
menuedit.add_command(label='Refresh')
menuedit.add_separator()
menuedit.add_command(label='Preferences')
menubar.add_cascade(label='Edit', menu=menuedit)

#add another menu dropdown
m_help = Menu(menubar, tearoff=0)
m_help.add_command(label='About Aprt Manager',command=abt)
m_help.add_separator()
m_help.add_command(label='FAQ')
menubar.add_cascade(label='Help', menu=m_help)

win.config(menu = menubar)

#create a function that generates another window 
    
def second():
    window=Tk()
    window.geometry('400x200')
    
    menubar = Menu(window)
    menu = Menu(menubar, tearoff=0)
    menu.add_command(label='Open')
    menubar.add_cascade(label='File', menu=menu)
    window.config(menu = menubar)
   
    window.mainloop()
    
def third():
    window=Tk()
    window.geometry('400x200')
    menubar = Menu(window)
    menu = Menu(menubar, tearoff=0)
    menu.add_command(label='Open')
    menubar.add_cascade(label='File', menu=menu)
    window.config(menu = menubar)

    window.mainloop()


#---------DECLARE VARIABLES---------#
#Tenant variables
t_name_text = StringVar()
gender_text = StringVar()
mob_num_text = StringVar()
address_text = StringVar()
email_text = StringVar()
nation_text = StringVar()
emg_num_text = StringVar()
ct_name_text = StringVar()
chk_in_text = StringVar()
duration_text = IntVar()
chk_out_text = StringVar()

#Room variables
block_text = StringVar()
aptype_text = StringVar()    
apnum_text = StringVar()
status_text = StringVar()
search_text = StringVar()


def reset_tenant_entries():
    e1.delete(0,END)
    e2.current(0)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    e10.current(0)
    
def reset_room_entries():
    eb1.current(0)
    eb2.current(0)
    eb3.current(0)
    eb4.current(0)
    
def add_tenant_query():
    '''(This function collects the inputted data 
    from the tenant fields and feeds them into the 
    backend function t_insert)'''
    backend.t_insert(t_name_text.get().title(),
                gender_text.get(),
                mob_num_text.get(),
                address_text.get().title(),
                email_text.get(),
                nation_text.get().title(),
                emg_num_text.get(),
                ct_name_text.get().title(),
                chk_in_text.get(),
                chk_out_text.get())
                
def add_room_query():
    '''(This function collects the inputted data 
    from the room fields and feeds them into the 
    backend function r_insert)'''
    backend.r_insert(block_text.get(),
                    aptype_text.get(),
                    apnum_text.get(),
                    status_text.get())
    
#---------CREATE FUNCTIONALITY---------#
def t_add():
    if apnum_text.get() != '--Select--' and len(mob_num_text.get()) !=0  and len(t_name_text.get()) !=0 and aptype_text.get() != '--Select--':
        #MERGING R-INSERT WITH T-INSERT TO PRODUCE EQUAL IDS       
        aq1 = myquery.A1_query()  #aq1 for A query 1
        aq2 = myquery.A2_query()
        aq3 = myquery.A3_query()
        aq4 = myquery.A4_query()
        bq1 = myquery.B1_query()
        bq2 = myquery.B2_query()
        bq3 = myquery.B3_query()
        bq4 = myquery.B4_query()
        cq1 = myquery.C1_query()
        cq2 = myquery.C2_query()
        cq3 = myquery.C3_query()
        cq4 = myquery.C4_query()
        dq1 = myquery.D1_query()
        dq2 = myquery.D2_query()
        dq3 = myquery.D3_query()
        dq4 = myquery.D4_query()
        eq1 = myquery.E1_query()
        eq2 = myquery.E2_query()
        eq3 = myquery.E3_query()
        eq4 = myquery.E4_query() 
                          
        #BLOCK A APARTMENT A1
        while block_text.get() == 'A' and aptype_text.get() == 'A1':
            if apnum_text.get() == '1':
                try:
                    if 'A1' and '1' in aq1[0]:
                        tkinter.messagebox.showerror('Entry Manager','A1 apartment 1 is occupied')
                        eb2.focus_set() #send the highlight to the apartment type field
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        #RESET T ENTRIES
                        reset_tenant_entries()
                        #RESET R ENTRIES 
                        reset_room_entries()
                        
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '2':
                try:
                    if 'A1' and '2' in aq1[0] or 'A1' and '2' in aq1[1]:
                        tkinter.messagebox.showerror('Entry Manager','A1 apartment 2 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '3':
                try:
                    if 'A1' and '3' in aq1[0] or 'A1' and '3' in aq1[1] \
                    or 'A1' and '3' in aq1[2]:
                        tkinter.messagebox.showerror('Entry Manager','A1 apartment 3 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
            
            elif apnum_text.get() == '4':
                try:
                    if 'A1' and '4' in aq1[0] or 'A1' and '4' in aq1[1] \
                    or 'A1' and '4' in aq1[2] or 'A1' and '4' in aq1[3]:
                        tkinter.messagebox.showerror('Entry Manager','A1 apartment 4 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
            
        #BLOCK A APARTMENT A2
        while block_text.get() == 'A' and aptype_text.get() == 'A2':
            if apnum_text.get() == '1':
                try:
                    if 'A2' and '1' in aq2[0]:
                        tkinter.messagebox.showerror('Entry Manager','A2 apartment 1 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '2':
                try:
                    if 'A2' and '2' in aq2[0] or 'A2' and '2' in aq2[1]:
                        tkinter.messagebox.showerror('Entry Manager','A2 apartment 2 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '3':
                try:
                    if 'A2' and '3' in aq2[0] or 'A2' and '3' in aq2[1] \
                    or 'A2' and '3' in aq2[2]:
                        tkinter.messagebox.showerror('Entry Manager','A2 apartment 3 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()

                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
            
            elif apnum_text.get() == '4':
                try:
                    if 'A2' and '4' in aq2[0] or 'A2' and '4' in aq2[1] \
                    or 'A2' and '4' in aq2[2] or 'A2' and '4' in aq2[3]:
                        tkinter.messagebox.showerror('Entry Manager','A2 apartment 4 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
            
        #BLOCK A APARTMENT A3
        while block_text.get() == 'A' and aptype_text.get() == 'A3':
            if apnum_text.get() == '1':
                try:
                    if 'A3' and '1' in aq3[0]:
                        tkinter.messagebox.showerror('Entry Manager','A3 apartment 1 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '2':
                try:
                    if 'A3' and '2' in aq3[0] or 'A3' and '2' in aq3[1]:
                        tkinter.messagebox.showerror('Entry Manager','A3 apartment 2 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '3':
                try:
                    if 'A3' and '3' in aq3[0] or 'A3' and '3' in aq3[1] \
                    or 'A3' and '3' in aq3[2]:
                        tkinter.messagebox.showerror('Entry Manager','A3 apartment 3 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()

                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
            
            elif apnum_text.get() == '4':
                try:
                    if 'A3' and '4' in aq3[0] or 'A3' and '4' in aq3[1] \
                    or 'A3' and '4' in aq3[2] or 'A3' and '4' in aq3[3]:
                        tkinter.messagebox.showerror('Entry Manager','A3 apartment 4 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                        
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
        #BLOCK A APARTMENT A4
        while block_text.get() == 'A' and aptype_text.get() == 'A4':
            if apnum_text.get() == '1':
                try:
                    if 'A4' and '1' in aq4[0]:
                        tkinter.messagebox.showerror('Entry Manager','A4 apartment 1 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '2':
                try:
                    if 'A4' and '2' in aq4[0] or 'A4' and '2' in aq4[1]:
                        tkinter.messagebox.showerror('Entry Manager','A4 apartment 2 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '3':
                try:
                    if 'A4' and '3' in aq4[0] or 'A4' and '3' in aq4[1] \
                    or 'A4' and '3' in aq4[2]:
                        tkinter.messagebox.showerror('Entry Manager','A4 apartment 3 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()

                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
            
            elif apnum_text.get() == '4':
                try:
                    if 'A4' and '4' in aq4[0] or 'A4' and '4' in aq4[1] \
                    or 'A4' and '4' in aq4[2] or 'A4' and '4' in aq4[3]:
                        tkinter.messagebox.showerror('Entry Manager','A4 apartment 4 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                        
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
        #BLOCK B APARTMENT B1
        while block_text.get() == 'B' and aptype_text.get() == 'B1':
            if apnum_text.get() == '1':
                try:
                    if 'B1' and '1' in bq1[0]:
                        tkinter.messagebox.showerror('Entry Manager','B1 apartment 1 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '2':
                try:
                    if 'B1' and '2' in bq1[0] or 'B1' and '2' in bq1[1]:
                        tkinter.messagebox.showerror('Entry Manager','B1 apartment 2 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '3':
                try:
                    if 'B1' and '3' in bq1[0] or 'B1' and '3' in bq1[1] \
                    or 'B1' and '3' in bq1[2]:
                        tkinter.messagebox.showerror('Entry Manager','B1 apartment 3 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
            
            elif apnum_text.get() == '4':
                try:
                    if 'B1' and '4' in bq1[0] or 'B1' and '4' in bq1[1] \
                    or 'B1' and '4' in bq1[2] or 'B1' and '4' in bq1[3]:
                        tkinter.messagebox.showerror('Entry Manager','B1 apartment 4 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()

        #BLOCK B APARTMENT B2
        while block_text.get() == 'B' and aptype_text.get() == 'B2':
            if apnum_text.get() == '1':
                try:
                    if 'B2' and '1' in bq2[0]:
                        tkinter.messagebox.showerror('Entry Manager','B2 apartment 1 is occupied')
                        break
                    else:
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        add_tenant_query()
                        add_room_query()
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '2':
                try:
                    if 'B2' and '2' in bq2[0] or 'B2' and '2' in bq2[1]:
                        tkinter.messagebox.showerror('Entry Manager','B2 apartment 2 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '3':
                try:
                    if 'B2' and '3' in bq2[0] or 'B2' and '3' in bq2[1] \
                    or 'B2' and '3' in bq2[2]:
                        tkinter.messagebox.showerror('Entry Manager','B2 apartment 3 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
            
            elif apnum_text.get() == '4':
                try:
                    if 'B2' and '4' in bq2[0] or 'B2' and '4' in bq2[1] \
                    or 'B2' and '4' in bq2[2] or 'B2' and '4' in bq2[3]:
                        tkinter.messagebox.showerror('Entry Manager','B2 apartment 4 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()

        #BLOCK B APARTMENT B3
        while block_text.get() == 'B' and aptype_text.get() == 'B3':
            if apnum_text.get() == '1':
                try:
                    if 'B3' and '1' in bq3[0]:
                        tkinter.messagebox.showerror('Entry Manager','B3 apartment 1 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '2':
                try:
                    if 'B3' and '2' in bq3[0] or 'B3' and '2' in bq3[1]:
                        tkinter.messagebox.showerror('Entry Manager','B3 apartment 2 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '3':
                try:
                    if 'B3' and '3' in bq3[0] or 'B3' and '3' in bq3[1] \
                    or 'B3' and '3' in bq3[2]:
                        tkinter.messagebox.showerror('Entry Manager','B3 apartment 3 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
            
            elif apnum_text.get() == '4':
                try:
                    if 'B3' and '4' in bq3[0] or 'B3' and '4' in bq3[1] \
                    or 'B3' and '4' in bq3[2] or 'B3' and '4' in bq3[3]:
                        tkinter.messagebox.showerror('Entry Manager','B3 apartment 4 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()

        #BLOCK B APARTMENT B4
        while block_text.get() == 'B' and aptype_text.get() == 'B4':
            if apnum_text.get() == '1':
                try:
                    if 'B4' and '1' in bq4[0]:
                        tkinter.messagebox.showerror('Entry Manager','B4 apartment 1 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '2':
                try:
                    if 'B4' and '2' in bq4[0] or 'B4' and '2' in bq4[1]:
                        tkinter.messagebox.showerror('Entry Manager','B4 apartment 2 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '3':
                try:
                    if 'B4' and '3' in bq4[0] or 'B4' and '3' in bq4[1] \
                    or 'B4' and '3' in bq4[2]:
                        tkinter.messagebox.showerror('Entry Manager','B4 apartment 3 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
            
            elif apnum_text.get() == '4':
                try:
                    if 'B4' and '4' in bq4[0] or 'B4' and '4' in bq4[1] \
                    or 'B4' and '4' in bq4[2] or 'B4' and '4' in bq4[3]:
                        tkinter.messagebox.showerror('Entry Manager','B4 apartment 4 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()

        #BLOCK C APARTMENT C1
        while block_text.get() == 'C' and aptype_text.get() == 'C1':
            if apnum_text.get() == '1':
                try:
                    if 'C1' and '1' in cq1[0]:
                        tkinter.messagebox.showerror('Entry Manager','C1 apartment 1 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '2':
                try:
                    if 'C1' and '2' in cq1[0] or 'C1' and '2' in cq1[1]:
                        tkinter.messagebox.showerror('Entry Manager','C1 apartment 2 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '3':
                try:
                    if 'C1' and '3' in cq1[0] or 'C1' and '3' in cq1[1] \
                    or 'C1' and '3' in cq1[2]:
                        tkinter.messagebox.showerror('Entry Manager','C1 apartment 3 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
            
            elif apnum_text.get() == '4':
                try:
                    if 'C1' and '4' in cq1[0] or 'C1' and '4' in cq1[1] \
                    or 'C1' and '4' in cq1[2] or 'C1' and '4' in cq1[3]:
                        tkinter.messagebox.showerror('Entry Manager','C1 apartment 4 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()

        #BLOCK C APARTMENT C2
        while block_text.get() == 'C' and aptype_text.get() == 'C2':
            if apnum_text.get() == '1':
                try:
                    if 'C2' and '1' in cq2[0]:
                        tkinter.messagebox.showerror('Entry Manager','C2 apartment 1 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '2':
                try:
                    if 'C2' and '2' in cq2[0] or 'C2' and '2' in cq2[1]:
                        tkinter.messagebox.showerror('Entry Manager','C2 apartment 2 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '3':
                try:
                    if 'C2' and '3' in cq2[0] or 'C2' and '3' in cq2[1] \
                    or 'C2' and '3' in cq2[2]:
                        tkinter.messagebox.showerror('Entry Manager','C2 apartment 3 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()

                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
            
            elif apnum_text.get() == '4':
                try:
                    if 'C2' and '4' in cq2[0] or 'C2' and '4' in cq2[1] \
                    or 'C2' and '4' in cq2[2] or 'C2' and '4' in cq2[3]:
                        tkinter.messagebox.showerror('Entry Manager','C2 apartment 4 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                        
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()

        #BLOCK C APARTMENT C3
        while block_text.get() == 'C' and aptype_text.get() == 'C3':
            if apnum_text.get() == '1':
                try:
                    if 'C3' and '1' in cq3[0]:
                        tkinter.messagebox.showerror('Entry Manager','C3 apartment 1 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '2':
                try:
                    if 'C3' and '2' in cq3[0] or 'C3' and '2' in cq3[1]:
                        tkinter.messagebox.showerror('Entry Manager','C3 apartment 2 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '3':
                try:
                    if 'C3' and '3' in cq3[0] or 'C3' and '3' in cq3[1] \
                    or 'C3' and '3' in cq3[2]:
                        tkinter.messagebox.showerror('Entry Manager','C3 apartment 3 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()

                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
            
            elif apnum_text.get() == '4':
                try:
                    if 'C3' and '4' in cq3[0] or 'C3' and '4' in cq3[1] \
                    or 'C3' and '4' in cq3[2] or 'C3' and '4' in cq3[3]:
                        tkinter.messagebox.showerror('Entry Manager','C3 apartment 4 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                        
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()

        #BLOCK C APARTMENT C4
        while block_text.get() == 'C' and aptype_text.get() == 'C4':
            if apnum_text.get() == '1':
                try:
                    if 'C4' and '1' in cq4[0]:
                        tkinter.messagebox.showerror('Entry Manager','C4 apartment 1 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '2':
                try:
                    if 'C4' and '2' in cq4[0] or 'C4' and '2' in cq4[1]:
                        tkinter.messagebox.showerror('Entry Manager','C4 apartment 2 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '3':
                try:
                    if 'C4' and '3' in cq4[0] or 'C4' and '3' in cq4[1] \
                    or 'C4' and '3' in cq4[2]:
                        tkinter.messagebox.showerror('Entry Manager','C4 apartment 3 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()

                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
            
            elif apnum_text.get() == '4':
                try:
                    if 'C4' and '4' in cq4[0] or 'C4' and '4' in cq4[1] \
                    or 'C4' and '4' in cq4[2] or 'C4' and '4' in cq4[3]:
                        tkinter.messagebox.showerror('Entry Manager','C4 apartment 4 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                        
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()

        #BLOCK D APARTMENT D1
        while block_text.get() == 'D' and aptype_text.get() == 'D1':
            if apnum_text.get() == '1':
                try:
                    if 'D1' and '1' in dq1[0]:
                        tkinter.messagebox.showerror('Entry Manager','D1 apartment 1 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '2':
                try:
                    if 'D1' and '2' in dq1[0] or 'D1' and '2' in dq1[1]:
                        tkinter.messagebox.showerror('Entry Manager','D1 apartment 2 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '3':
                try:
                    if 'D1' and '3' in dq1[0] or 'D1' and '3' in dq1[1] \
                    or 'D1' and '3' in dq1[2]:
                        tkinter.messagebox.showerror('Entry Manager','D1 apartment 3 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()

                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
            
            elif apnum_text.get() == '4':
                try:
                    if 'D1' and '4' in dq1[0] or 'D1' and '4' in dq1[1] \
                    or 'D1' and '4' in dq1[2] or 'D1' and '4' in dq1[3]:
                        tkinter.messagebox.showerror('Entry Manager','D1 apartment 4 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                        
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()

        #BLOCK D APARTMENT D2
        while block_text.get() == 'D' and aptype_text.get() == 'D2':
            if apnum_text.get() == '1':
                try:
                    if 'D2' and '1' in dq2[0]:
                        tkinter.messagebox.showerror('Entry Manager','D2 apartment 1 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '2':
                try:
                    if 'D2' and '2' in dq2[0] or 'D2' and '2' in dq2[1]:
                        tkinter.messagebox.showerror('Entry Manager','D2 apartment 2 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '3':
                try:
                    if 'D2' and '3' in dq2[0] or 'D2' and '3' in dq2[1] \
                    or 'D2' and '3' in dq2[2]:
                        tkinter.messagebox.showerror('Entry Manager','D2 apartment 3 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()

                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
            
            elif apnum_text.get() == '4':
                try:
                    if 'D2' and '4' in dq2[0] or 'D2' and '4' in dq2[1] \
                    or 'D2' and '4' in dq2[2] or 'D2' and '4' in dq2[3]:
                        tkinter.messagebox.showerror('Entry Manager','D2 apartment 4 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                        
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()

        #BLOCK D APARTMENT D3
        while block_text.get() == 'D' and aptype_text.get() == 'D3':
            if apnum_text.get() == '1':
                try:
                    if 'D3' and '1' in dq3[0]:
                        tkinter.messagebox.showerror('Entry Manager','D3 apartment 1 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '2':
                try:
                    if 'D3' and '2' in dq3[0] or 'D3' and '2' in dq3[1]:
                        tkinter.messagebox.showerror('Entry Manager','D3 apartment 2 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '3':
                try:
                    if 'D3' and '3' in dq3[0] or 'D3' and '3' in dq3[1] \
                    or 'D3' and '3' in dq3[2]:
                        tkinter.messagebox.showerror('Entry Manager','D3 apartment 3 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()

                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
            
            elif apnum_text.get() == '4':
                try:
                    if 'D3' and '4' in dq3[0] or 'D3' and '4' in dq3[1] \
                    or 'D3' and '4' in dq3[2] or 'D3' and '4' in dq3[3]:
                        tkinter.messagebox.showerror('Entry Manager','D3 apartment 4 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                        
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()

        #BLOCK D APARTMENT D4
        while block_text.get() == 'D' and aptype_text.get() == 'D4':
            if apnum_text.get() == '1':
                try:
                    if 'D4' and '1' in dq4[0]:
                        tkinter.messagebox.showerror('Entry Manager','D4 apartment 1 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '2':
                try:
                    if 'D4' and '2' in dq4[0] or 'D4' and '2' in dq4[1]:
                        tkinter.messagebox.showerror('Entry Manager','D4 apartment 2 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '3':
                try:
                    if 'D4' and '3' in dq4[0] or 'D4' and '3' in dq4[1] \
                    or 'D4' and '3' in dq4[2]:
                        tkinter.messagebox.showerror('Entry Manager','D4 apartment 3 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()

                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
            
            elif apnum_text.get() == '4':
                try:
                    if 'D4' and '4' in dq4[0] or 'D4' and '4' in dq4[1] \
                    or 'D4' and '4' in dq4[2] or 'D4' and '4' in dq4[3]:
                        tkinter.messagebox.showerror('Entry Manager','D4 apartment 4 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                        
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()

        #BLOCK E APARTMENT E1
        while block_text.get() == 'E' and aptype_text.get() == 'E1':
            if apnum_text.get() == '1':
                try:
                    if 'E1' and '1' in eq1[0]:
                        tkinter.messagebox.showerror('Entry Manager','E1 apartment 1 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '2':
                try:
                    if 'E1' and '2' in eq1[0] or 'E1' and '2' in eq1[1]:
                        tkinter.messagebox.showerror('Entry Manager','E1 apartment 2 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '3':
                try:
                    if 'E1' and '3' in eq1[0] or 'E1' and '3' in eq1[1] \
                    or 'E1' and '3' in eq1[2]:
                        tkinter.messagebox.showerror('Entry Manager','E1 apartment 3 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()

                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
            
            elif apnum_text.get() == '4':
                try:
                    if 'E1' and '4' in eq1[0] or 'E1' and '4' in eq1[1] \
                    or 'E1' and '4' in eq1[2] or 'E1' and '4' in eq1[3]:
                        tkinter.messagebox.showerror('Entry Manager','E1 apartment 4 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                        
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()

        #BLOCK E APARTMENT E2
        while block_text.get() == 'E' and aptype_text.get() == 'E2':
            if apnum_text.get() == '1':
                try:
                    if 'E2' and '1' in eq2[0]:
                        tkinter.messagebox.showerror('Entry Manager','E2 apartment 1 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '2':
                try:
                    if 'E2' and '2' in eq2[0] or 'E2' and '2' in eq2[1]:
                        tkinter.messagebox.showerror('Entry Manager','E2 apartment 2 is occupied')
                        eb2.focus_set() #send the highlight to the apartment type field
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '3':
                try:
                    if 'E2' and '3' in eq2[0] or 'E2' and '3' in eq2[1] \
                    or 'E2' and '3' in eq2[2]:
                        tkinter.messagebox.showerror('Entry Manager','E2 apartment 3 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()

                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
            
            elif apnum_text.get() == '4':
                try:
                    if 'E2' and '4' in eq2[0] or 'E2' and '4' in eq2[1] \
                    or 'E2' and '4' in eq2[2] or 'E2' and '4' in eq2[3]:
                        tkinter.messagebox.showerror('Entry Manager','E2 apartment 4 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                        
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()

        #BLOCK E APARTMENT E3
        while block_text.get() == 'E' and aptype_text.get() == 'E3':
            if apnum_text.get() == '1':
                try:
                    if 'E3' and '1' in eq3[0]:
                        tkinter.messagebox.showerror('Entry Manager','E3 apartment 1 is occupied')
                        eb2.focus_set() #send the highlight to the apartment type field
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '2':
                try:
                    if 'E3' and '2' in eq3[0] or 'E3' and '2' in eq3[1]:
                        tkinter.messagebox.showerror('Entry Manager','E3 apartment 2 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '3':
                try:
                    if 'E3' and '3' in eq3[0] or 'E3' and '3' in eq3[1] \
                    or 'E3' and '3' in eq3[2]:
                        tkinter.messagebox.showerror('Entry Manager','E3 apartment 3 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()

                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
            
            elif apnum_text.get() == '4':
                try:
                    if 'E3' and '4' in eq3[0] or 'E3' and '4' in eq3[1] \
                    or 'E3' and '4' in eq3[2] or 'E3' and '4' in eq3[3]:
                        tkinter.messagebox.showerror('Entry Manager','E3 apartment 4 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                        
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()

        #BLOCK E APARTMENT E4
        while block_text.get() == 'E' and aptype_text.get() == 'E4':
            if apnum_text.get() == '1':
                try:
                    if 'E4' and '1' in eq4[0]:
                        tkinter.messagebox.showerror('Entry Manager','E4 apartment 1 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '2':
                try:
                    if 'E4' and '2' in eq4[0] or 'E4' and '2' in eq4[1]:
                        tkinter.messagebox.showerror('Entry Manager','E4 apartment 2 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
        
            elif apnum_text.get() == '3':
                try:
                    if 'E4' and '3' in eq4[0] or 'E4' and '3' in eq4[1] \
                    or 'E4' and '3' in eq4[2]:
                        tkinter.messagebox.showerror('Entry Manager','E4 apartment 3 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()

                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()
            
            elif apnum_text.get() == '4':
                try:
                    if 'E4' and '4' in eq4[0] or 'E4' and '4' in eq4[1] \
                    or 'E4' and '4' in eq4[2] or 'E4' and '4' in eq4[3]:
                        tkinter.messagebox.showerror('Entry Manager','E4 apartment 4 is occupied')
                        break
                    else:
                        add_tenant_query()
                        add_room_query()
                        tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                        reset_tenant_entries()
                        reset_room_entries()
                        
                except IndexError:
                    add_tenant_query()
                    add_room_query()
                    tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
                    reset_tenant_entries()
                    reset_room_entries()

        
    else:
        tkinter.messagebox.showerror('Entry Manager', 'your entries are missing key values')
        e1.focus_set()

def t_display():
    '''
    view_area.delete(0,END)
    for row in myquery.t_rview():
        view_area.insert(END,str(''),row)
        '''
    view_area.delete(0,END)
    for row in myquery.t_rview():
        view_area.insert(END,*row)
    #view_area.delete(0,END)
    #for row in myquery.t_rview():
    #    view_area.insert('',END,values=row)
    
    #print(b4['text'])
    
def grab_selection(event):
    try:
        global line
        index = view_area.curselection()[0]
        line = view_area.get(index)[0]
        #print(line[0]) #the multlistbox adds another tuple to the query so hence two sq brackets to access the query data

        if line != '':
            e1.delete(0,END)
            e1.insert(END,line[1])
            e2.current(0)
            if line[2] == 'MALE':
                e2['value']=('--Select--',line[2],'FEMALE')
                e2.current(1)
            elif line[2] == 'FEMALE':
                e2['value']=('--Select--','MALE',line[2])
                e2.current(2)
            e3.delete(0,END)
            e3.insert(END,line[3])
            e4.delete(0,END)
            e4.insert(END,line[4])
            e5.delete(0,END)
            e5.insert(END,line[5])
            e6.delete(0,END)
            e6.insert(END,line[6])
            e7.delete(0,END)
            e7.insert(END,line[7])
            e8.delete(0,END)
            e8.insert(END,line[8])
            e9.delete(0,END)
            if e9['state']=='readonly':
                e9.configure(state='normal')
                e9.delete(0,END)
            e9.insert(END,line[9])
            dur = time_convert(line[9]) - time_convert(line[10])
            diff = int(abs(dur.days)/30).__round__()
            duration_text.set(diff)
            e11.delete(0,END)
            if e11['state']=='readonly':
                e11.configure(state='normal')
                e11.delete(0,END)
            e11.insert(END,line[10])
            e11.configure(state='readonly')
            
            #R VALUES
            eb1.current(0)
            if line[11] == 'A':
                eb1['value']=('--Select--',line[11],'B','C','D','E')
                eb1.current(1)
            elif line[11] == 'B':
                eb1['value']=('--Select--','A',line[11],'C','D','E')
                eb1.current(2)
            elif line[11] == 'C':
                eb1['value']=('--Select--','A','B',line[11],'D','E')
                eb1.current(3)
            elif line[11] == 'D':
                eb1['value']=('--Select--','A','B','C',line[11],'E')
                eb1.current(4)
            elif line[11] == 'E':
                eb1['value']=('--Select--','A','B','C','D',line[11])
                eb1.current(5)
            eb2.current(0)
            if line[12] == 'A1': #------A
                eb2['value']=('--Select--',line[12],'A2','A3','A4','B1',
                        'B2','B3','B4','C1','C2','C3','C4',
                        'D1','D2','D3','D4','E1','E2','E3','E4')
                eb2.current(1)
            elif line[12] == 'A2':
                eb2['value']=('--Select--','A1',line[12],'A3','A4','B1',
                        'B2','B3','B4','C1','C2','C3','C4',
                        'D1','D2','D3','D4','E1','E2','E3','E4')
                eb2.current(2)
            elif line[12] == 'A3':
                eb2['value']=('--Select--','A1','A2',line[12],'A4','B1',
                        'B2','B3','B4','C1','C2','C3','C4',
                        'D1','D2','D3','D4','E1','E2','E3','E4')
                eb2.current(3)
            elif line[12] == 'A4':
                eb2['value']=('--Select--','A1','A2','A3',line[12],'B1',
                        'B2','B3','B4','C1','C2','C3','C4',
                        'D1','D2','D3','D4','E1','E2','E3','E4')
                eb2.current(4)
            elif line[12] == 'B1': #------B
                eb2['value']=('--Select--','A1','A2','A3','A4',line[12],
                        'B2','B3','B4','C1','C2','C3','C4',
                        'D1','D2','D3','D4','E1','E2','E3','E4')
                eb2.current(5)
            elif line[12] == 'B2':
                eb2['value']=('--Select--','A1','A2','A3','A4','B1',line[12],
                        'B3','B4','C1','C2','C3','C4',
                        'D1','D2','D3','D4','E1','E2','E3','E4')
                eb2.current(6)
            elif line[12] == 'B3':
                eb2['value']=('--Select--','A1','A2','A3','A4','B1',
                        'B2',line[12],'B4','C1','C2','C3','C4',
                        'D1','D2','D3','D4','E1','E2','E3','E4')
                eb2.current(7)
            elif line[12] == 'B4':
                eb2['value']=('--Select--','A1','A2','A3','A4','B1',
                        'B2','B3',line[12],'C1','C2','C3','C4',
                        'D1','D2','D3','D4','E1','E2','E3','E4')
                eb2.current(8)
            elif line[12] == 'C1': #------C
                eb2['value']=('--Select--','A1','A2','A3','A4','B1',
                        'B2','B3','B4',line[12],'C2','C3','C4',
                        'D1','D2','D3','D4','E1','E2','E3','E4')
                eb2.current(9)
            elif line[12] == 'C2':
                eb2['value']=('--Select--','A1','A2','A3','A4','B1',
                        'B2','B3','B4','C1',line[12],'C3','C4',
                        'D1','D2','D3','D4','E1','E2','E3','E4')
                eb2.current(10)
            elif line[12] == 'C3':
                eb2['value']=('--Select--','A1','A2','A3','A4','B1',
                        'B2','B3','B4','C1','C2',line[12],'C4',
                        'D1','D2','D3','D4','E1','E2','E3','E4')
                eb2.current(11)
            elif line[12] == 'C4':
                eb2['value']=('--Select--','A1','A2','A3','A4','B1',
                        'B2','B3','B4','C1','C2','C3',line[12],
                        'D1','D2','D3','D4','E1','E2','E3','E4')
                eb2.current(12)
            elif line[12] == 'D1': #------D
                eb2['value']=('--Select--','A1','A2','A3','A4','B1',
                        'B2','B3','B4','C1','C2','C3','C4',
                        line[12],'D2','D3','D4','E1','E2','E3','E4')
                eb2.current(13)
            elif line[12] == 'D2':
                eb2['value']=('--Select--','A1','A2','A3','A4','B1',
                        'B2','B3','B4','C1','C2','C3','C4',
                        'D1',line[12],'D3','D4','E1','E2','E3','E4')
                eb2.current(14)
            elif line[12] == 'D3':
                eb2['value']=('--Select--','A1','A2','A3','A4','B1',
                        'B2','B3','B4','C1','C2','C3','C4',
                        'D1','D2',line[12],'D4','E1','E2','E3','E4')
                eb2.current(15)
            elif line[12] == 'D4':
                eb2['value']=('--Select--','A1','A2','A3','A4','B1',
                        'B2','B3','B4','C1','C2','C3','C4',
                        'D1','D2','D3',line[12],'E1','E2','E3','E4')
                eb2.current(16)
            elif line[12] == 'E1': #------E
                eb2['value']=('--Select--','A1','A2','A3','A4','B1',
                        'B2','B3','B4','C1','C2','C3','C4',
                        'D1','D2','D3','D4',line[12],'E2','E3','E4')
                eb2.current(17)
            elif line[12] == 'E2':
                eb2['value']=('--Select--','A1','A2','A3','A4','B1',
                        'B2','B3','B4','C1','C2','C3','C4',
                        'D1','D2','D3','D4','E1',line[12],'E3','E4')
                eb2.current(18)
            elif line[12] == 'E3':
                eb2['value']=('--Select--','A1','A2','A3','A4','B1',
                        'B2','B3','B4','C1','C2','C3','C4',
                        'D1','D2','D3','D4','E1','E2',line[12],'E4')
                eb2.current(19)
            elif line[12] == 'E4':
                eb2['value']=('--Select--','A1','A2','A3','A4','B1',
                        'B2','B3','B4','C1','C2','C3','C4',
                        'D1','D2','D3','D4','E1','E2','E3',line[12])
                eb2.current(20)
            eb3.current(0)
            if line[13] == '1':
                eb3['value']=('--Select--',line[13],'2','3','4')
                eb3.current(1)
            elif line[13] == '2':
                eb3['value']=('--Select--','1',line[13],'3','4')
                eb3.current(2)
            elif line[13] == '3':
                eb3['value']=('--Select--','1','2',line[13],'4')
                eb3.current(3)
            elif line[13] == '4':
                eb3['value']=('--Select--','1','2','3',line[13])
                eb3.current(4)
            eb4.current(0)
            if line[14] == 'Occupied':
                eb4['value']=('--Select--',line[14],'Available','Unavailable','Vacant')
                eb4.current(1)
            elif line[14] == 'Available':
                eb4['value']=('--Select--','Occupied',line[14],'Unavailable','Vacant')
                eb4.current(2)
            elif line[14] == 'Unavailable':
                eb4['value']=('--Select--','Occupied','Available',line[14],'Vacant')
                eb4.current(3)
            elif line[14] == 'Vacant':
                eb4['value']=('--Select--','Occupied','Available','Unavailable',line[14])
                eb4.current(4)

        else:
            e1.delete(0,END),
            e2.current(0),
            e3.delete(0,END),
            e4.delete(0,END),
            e5.delete(0,END),
            e6.delete(0,END),
            e7.delete(0,END),
            e8.delete(0,END),
            e9.configure(state='readonly')
            chk_in_text.set(time.strftime('%Y-%m-%d'))
            e11.configure(state='readonly')
            chk_out_text.set(evac)
            
            #R-VALUES
            eb1.current(0)
            eb2.current(0)
            eb3.current(0)
            eb4.current(0)
            
    except IndexError:
        pass

def t_remove():
    if apnum_text.get() != '--Select--' and len(mob_num_text.get()) !=0  \
    and len(t_name_text.get()) !=0 and aptype_text.get() != '--Select--':
        rem = tkinter.messagebox.askyesno('Delete Manager', 'Are you sure you want to delete?')
        if rem > 0:
            try:
                backend.t_delete(line[0])
                e1.delete(0,END),
                e2.current(0),
                e3.delete(0,END),
                e4.delete(0,END),
                e5.delete(0,END),
                e6.delete(0,END),
                e7.delete(0,END),
                e8.delete(0,END),
                e10.current(0)
                #R-ENTRIES
                eb1.current(0),
                eb2.current(0),
                eb3.current(0),
                eb4.current(0)
            except:
                pass
            return
    else:
        tkinter.messagebox.showinfo('Delete Manager', 'Select an entry to delete?')
    
def t_update():
    if apnum_text.get() != '--Select--' and len(mob_num_text.get()) !=0  and len(t_name_text.get()) !=0 and aptype_text.get() != '--Select--':
        aq1 = myquery.A1_query() 
        aq2 = myquery.A2_query()
        aq3 = myquery.A3_query()
        aq4 = myquery.A4_query()
        bq1 = myquery.B1_query()
        bq2 = myquery.B2_query()
        bq3 = myquery.B3_query()
        bq4 = myquery.B4_query()
        cq1 = myquery.C1_query()
        cq2 = myquery.C2_query()
        cq3 = myquery.C3_query()
        cq4 = myquery.C4_query()
        dq1 = myquery.D1_query()
        dq2 = myquery.D2_query()
        dq3 = myquery.D3_query()
        dq4 = myquery.D4_query()
        eq1 = myquery.E1_query()
        eq2 = myquery.E2_query()
        eq3 = myquery.E3_query()
        eq4 = myquery.E4_query() 

        #BLOCK A APARTMENT A1
        while block_text.get() == 'A' and aptype_text.get() == 'A1':
            if apnum_text.get() == '1':
                try:
                    if 'A1' and '1' in aq1[0]:
                        if t_name_text.get() in aq1[0]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            #RESET T-ENTRIES
                            reset_tenant_entries()
                            #RESET R-ENTRIES
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','A1 apartment 1 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries()  
        
            elif apnum_text.get() == '2':
                try:
                    if 'A1' and '2' in aq1[0] or 'A1' and '2' in aq1[1]:
                        if t_name_text.get() in aq1[0] or t_name_text.get() in aq1[1]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','A1 apartment 2 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 

            elif apnum_text.get() == '3':
                try:
                    if 'A1' and '3' in aq1[0] or 'A1' and '3' in aq1[1] \
                    or 'A1' and '3' in aq1[2]:
                        if t_name_text.get() in aq1[0] or t_name_text.get() in aq1[1] \
                        or t_name_text.get() in aq1[2]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','A1 apartment 3 is occupied')
                        break                        
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries()    
            
            elif apnum_text.get() == '4':
                try:
                    if 'A1' and '4' in aq1[0] or 'A1' and '4' in aq1[1] \
                    or 'A1' and '4' in aq1[2] or 'A1' and '4' in aq1[3]:
                        if t_name_text.get() in aq1[0] or t_name_text.get() in aq1[1] \
                        or t_name_text.get() in aq1[2] or t_name_text.get() in aq1[3]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','A1 apartment 4 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries()   
            
        #BLOCK A APARTMENT A2
        while block_text.get() == 'A' and aptype_text.get() == 'A2':
            if apnum_text.get() == '1':
                try:
                    if 'A2' and '1' in aq2[0]:
                        if t_name_text.get() in aq2[0]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','A2 apartment 1 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries()  
        
            elif apnum_text.get() == '2':
                try:
                    if 'A2' and '2' in aq2[0] or 'A2' and '2' in aq2[1]:
                        if t_name_text.get() in aq2[0] or t_name_text.get() in aq2[1]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','A2 apartment 2 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 

            elif apnum_text.get() == '3':
                try:
                    if 'A2' and '3' in aq2[0] or 'A2' and '3' in aq2[1] \
                    or 'A2' and '3' in aq2[2]:
                        if t_name_text.get() in aq2[0] or t_name_text.get() in aq2[1] \
                        or t_name_text.get() in aq2[2]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','A2 apartment 3 is occupied')
                        break                        
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
            
            elif apnum_text.get() == '4':
                try:
                    if 'A2' and '4' in aq2[0] or 'A2' and '4' in aq2[1] \
                    or 'A2' and '4' in aq2[2] or 'A2' and '4' in aq2[3]:
                        if t_name_text.get() in aq2[0] or t_name_text.get() in aq2[1] \
                        or t_name_text.get() in aq2[2] or t_name_text.get() in aq2[3]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','A2 apartment 4 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
                        
        #BLOCK A APARTMENT A3
        while block_text.get() == 'A' and aptype_text.get() == 'A3':
            if apnum_text.get() == '1':
                try:
                    if 'A3' and '1' in aq3[0]:
                        if t_name_text.get() in aq3[0]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','A3 apartment 1 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 

            elif apnum_text.get() == '2':
                try:
                    if 'A3' and '2' in aq3[0] or 'A3' and '2' in aq3[1]:
                        if t_name_text.get() in aq3[0] or t_name_text.get() in aq3[1]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','A3 apartment 2 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 

            elif apnum_text.get() == '3':
                try:
                    if 'A3' and '3' in aq3[0] or 'A3' and '3' in aq3[1] \
                    or 'A3' and '3' in aq3[2]:
                        if t_name_text.get() in aq3[0] or t_name_text.get() in aq3[1] \
                        or t_name_text.get() in aq3[2]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','A3 apartment 3 is occupied')
                        break                        
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
            
            elif apnum_text.get() == '4':
                try:
                    if 'A3' and '4' in aq3[0] or 'A3' and '4' in aq3[1] \
                    or 'A3' and '4' in aq3[2] or 'A3' and '4' in aq3[3]:
                        if t_name_text.get() in aq3[0] or t_name_text.get() in aq3[1] \
                        or t_name_text.get() in aq3[2] or t_name_text.get() in aq3[3]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','A3 apartment 4 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
                                                
        #BLOCK A APARTMENT A4
        while block_text.get() == 'A' and aptype_text.get() == 'A4':
            if apnum_text.get() == '1':
                try:
                    if 'A4' and '1' in aq4[0]:
                        if t_name_text.get() in aq4[0]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','A4 apartment 1 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
        
            elif apnum_text.get() == '2':
                try:
                    if 'A4' and '2' in aq4[0] or 'A4' and '2' in aq4[1]:
                        if t_name_text.get() in aq4[0] or t_name_text.get() in aq2[1]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','A4 apartment 2 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 

            elif apnum_text.get() == '3':
                try:
                    if 'A4' and '3' in aq4[0] or 'A4' and '3' in aq4[1] \
                    or 'A4' and '3' in aq4[2]:
                        if t_name_text.get() in aq4[0] or t_name_text.get() in aq4[1] \
                        or t_name_text.get() in aq4[2]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','A4 apartment 3 is occupied')
                        break                        
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
            
            elif apnum_text.get() == '4':
                try:
                    if 'A4' and '4' in aq4[0] or 'A4' and '4' in aq4[1] \
                    or 'A4' and '4' in aq4[2] or 'A4' and '4' in aq4[3]:
                        if t_name_text.get() in aq4[0] or t_name_text.get() in aq4[1] \
                        or t_name_text.get() in aq4[2] or t_name_text.get() in aq4[3]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','A4 apartment 4 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
                        
        #BLOCK B APARTMENT B1
        while block_text.get() == 'B' and aptype_text.get() == 'B1':
            if apnum_text.get() == '1':
                try:
                    if 'B1' and '1' in bq1[0]:
                        if t_name_text.get() in bq1[0]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','B1 apartment 1 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 

            elif apnum_text.get() == '2':
                try:
                    if 'B1' and '2' in bq1[0] or 'B1' and '2' in bq1[1]:
                        if t_name_text.get() in bq1[0] or t_name_text.get() in bq1[1]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','B1 apartment 2 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 

            elif apnum_text.get() == '3':
                try:
                    if 'B1' and '3' in bq1[0] or 'B1' and '3' in bq1[1] \
                    or 'B1' and '3' in bq1[2]:
                        if t_name_text.get() in bq1[0] or t_name_text.get() in bq1[1] \
                        or t_name_text.get() in bq1[2]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','B1 apartment 3 is occupied')
                        break                        
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries()  
            
            elif apnum_text.get() == '4':
                try:
                    if 'B1' and '4' in bq1[0] or 'B1' and '4' in bq1[1] \
                    or 'B1' and '4' in bq1[2] or 'B1' and '4' in bq1[3]:
                        if t_name_text.get() in bq1[0] or t_name_text.get() in bq1[1] \
                        or t_name_text.get() in bq1[2] or t_name_text.get() in bq1[3]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','B1 apartment 4 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 

        #BLOCK B APARTMENT B2
        while block_text.get() == 'B' and aptype_text.get() == 'B2':
            if apnum_text.get() == '1':
                try:
                    if 'B2' and '1' in bq2[0]:
                        if t_name_text.get() in bq2[0]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','B2 apartment 1 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 

            elif apnum_text.get() == '2':
                try:
                    if 'B2' and '2' in bq2[0] or 'B2' and '2' in bq2[1]:
                        if t_name_text.get() in bq2[0] or t_name_text.get() in bq2[1]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','B2 apartment 2 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 

            elif apnum_text.get() == '3':
                try:
                    if 'B2' and '3' in bq2[0] or 'B2' and '3' in bq2[1] \
                    or 'B2' and '3' in bq2[2]:
                        if t_name_text.get() in bq2[0] or t_name_text.get() in bq2[1] \
                        or t_name_text.get() in bq2[2]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','B2 apartment 3 is occupied')
                        break                        
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 

            elif apnum_text.get() == '4':
                try:
                    if 'B2' and '4' in bq2[0] or 'B2' and '4' in bq2[1] \
                    or 'B2' and '4' in bq2[2] or 'B2' and '4' in bq2[3]:
                        if t_name_text.get() in bq2[0] or t_name_text.get() in bq2[1] \
                        or t_name_text.get() in bq2[2] or t_name_text.get() in bq2[3]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','B2 apartment 4 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 

        #BLOCK B APARTMENT B3
        while block_text.get() == 'B' and aptype_text.get() == 'B3':
            if apnum_text.get() == '1':
                try:
                    print(bq3[0])
                    print(t_name_text.get() in bq3[0])
                    if 'B3' and '1' in bq3[0]:
                        if t_name_text.get() in bq3[0]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','B3 apartment 1 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
        
            elif apnum_text.get() == '2':
                try:
                    if 'B3' and '2' in bq3[0] or 'B3' and '2' in bq3[1]:
                        if t_name_text.get() in bq3[0] or t_name_text.get() in bq3[1]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','B3 apartment 2 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 

            elif apnum_text.get() == '3':
                try:
                    if 'B3' and '3' in bq3[0] or 'B3' and '3' in bq3[1] \
                    or 'B3' and '3' in bq3[2]:
                        if t_name_text.get() in bq3[0] or t_name_text.get() in bq3[1] \
                        or t_name_text.get() in bq3[2]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','B3 apartment 3 is occupied')
                        break  
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
            
            elif apnum_text.get() == '4':
                try:
                    if 'B3' and '4' in bq3[0] or 'B3' and '4' in bq3[1] \
                    or 'B3' and '4' in bq3[2] or 'B3' and '4' in bq3[3]:
                        if t_name_text.get() in bq3[0] or t_name_text.get() in bq3[1] \
                        or t_name_text.get() in bq3[2] or t_name_text.get() in bq3[3]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','B3 apartment 4 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 

        #BLOCK B APARTMENT B4
        while block_text.get() == 'B' and aptype_text.get() == 'B4':
            if apnum_text.get() == '1':
                try:
                    if 'B4' and '1' in bq4[0]:
                        if t_name_text.get() in bq4[0]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','B4 apartment 1 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 

            elif apnum_text.get() == '2':
                try:
                    if 'B4' and '2' in bq4[0] or 'B4' and '2' in bq4[1]:
                        if t_name_text.get() in bq4[0] or t_name_text.get() in bq4[1]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','B4 apartment 2 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 

            elif apnum_text.get() == '3':
                try:
                    if 'B4' and '3' in bq4[0] or 'B4' and '3' in bq4[1] \
                    or 'B4' and '3' in bq4[2]:
                        if t_name_text.get() in bq4[0] or t_name_text.get() in bq4[1] \
                        or t_name_text.get() in bq4[2]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','B4 apartment 3 is occupied')
                        break                        
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
            
            elif apnum_text.get() == '4':
                try:
                    if 'B4' and '4' in bq4[0] or 'B4' and '4' in bq4[1] \
                    or 'B4' and '4' in bq4[2] or 'B4' and '4' in bq4[3]:
                        if t_name_text.get() in bq4[0] or t_name_text.get() in bq4[1] \
                        or t_name_text.get() in bq4[2] or t_name_text.get() in bq4[3]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','B4 apartment 4 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 

        #BLOCK C APARTMENT C1
        while block_text.get() == 'C' and aptype_text.get() == 'C1':
            if apnum_text.get() == '1':
                try:
                    if 'C1' and '1' in cq1[0]:
                        if t_name_text.get() in cq1[0]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','C1 apartment 1 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
        
            elif apnum_text.get() == '2':
                try:
                    if 'C1' and '2' in cq1[0] or 'C1' and '2' in cq1[1]:
                        if t_name_text.get() in cq1[0] or t_name_text.get() in cq1[1]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','C1 apartment 2 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 

            elif apnum_text.get() == '3':
                try:
                    if 'C1' and '3' in cq1[0] or 'C1' and '3' in cq1[1] \
                    or 'C1' and '3' in cq1[2]:
                        if t_name_text.get() in cq1[0] or t_name_text.get() in cq1[1] \
                        or t_name_text.get() in cq1[2]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','C1 apartment 3 is occupied')
                        break                        
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
            
            elif apnum_text.get() == '4':
                try:
                    if 'C1' and '4' in cq1[0] or 'C1' and '4' in cq1[1] \
                    or 'C1' and '4' in cq1[2] or 'C1' and '4' in cq1[3]:
                        if t_name_text.get() in cq1[0] or t_name_text.get() in cq1[1] \
                        or t_name_text.get() in cq1[2] or t_name_text.get() in cq1[3]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','C1 apartment 4 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 

        #BLOCK C APARTMENT C2
        while block_text.get() == 'C' and aptype_text.get() == 'C2':
            if apnum_text.get() == '1':
                try:
                    if 'C2' and '1' in cq2[0]:
                        if t_name_text.get() in cq2[0]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','C2 apartment 1 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
        
            elif apnum_text.get() == '2':
                try:
                    if 'C2' and '2' in cq2[0] or 'C2' and '2' in cq2[1]:
                        if t_name_text.get() in cq2[0] or t_name_text.get() in cq2[1]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','C2 apartment 2 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 

            elif apnum_text.get() == '3':
                try:
                    if 'C2' and '3' in cq2[0] or 'C2' and '3' in cq2[1] \
                    or 'C2' and '3' in cq2[2]:
                        if t_name_text.get() in cq2[0] or t_name_text.get() in cq2[1] \
                        or t_name_text.get() in cq2[2]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','C2 apartment 3 is occupied')
                        break                        
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
            
            elif apnum_text.get() == '4':
                try:
                    if 'C2' and '4' in cq2[0] or 'C2' and '4' in cq2[1] \
                    or 'C2' and '4' in cq2[2] or 'C2' and '4' in cq2[3]:
                        if t_name_text.get() in cq2[0] or t_name_text.get() in cq2[1] \
                        or t_name_text.get() in cq2[2] or t_name_text.get() in cq2[3]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','C2 apartment 4 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 

        #BLOCK C APARTMENT C3
        while block_text.get() == 'C' and aptype_text.get() == 'C3':
            if apnum_text.get() == '1':
                try:
                    if 'C3' and '1' in cq3[0]:
                        if t_name_text.get() in cq3[0]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','C3 apartment 1 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 

            elif apnum_text.get() == '2':
                try:
                    if 'C3' and '2' in cq3[0] or 'C3' and '2' in cq3[1]:
                        if t_name_text.get() in cq3[0] or t_name_text.get() in cq3[1]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','C3 apartment 2 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 

            elif apnum_text.get() == '3':
                try:
                    if 'C3' and '3' in cq3[0] or 'C3' and '3' in cq3[1] \
                    or 'C3' and '3' in cq3[2]:
                        if t_name_text.get() in cq3[0] or t_name_text.get() in cq3[1] \
                        or t_name_text.get() in cq3[2]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','C3 apartment 3 is occupied')
                        break                        
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
            
            elif apnum_text.get() == '4':
                try:
                    if 'C3' and '4' in cq3[0] or 'C3' and '4' in cq3[1] \
                    or 'C3' and '4' in cq3[2] or 'C3' and '4' in cq3[3]:
                        if t_name_text.get() in cq3[0] or t_name_text.get() in cq3[1] \
                        or t_name_text.get() in cq3[2] or t_name_text.get() in cq3[3]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','C3 apartment 4 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
                        
        #BLOCK C APARTMENT C4
        while block_text.get() == 'C' and aptype_text.get() == 'C4':
            if apnum_text.get() == '1':
                try:
                    if 'C4' and '1' in cq4[0]:
                        if t_name_text.get() in cq4[0]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','C4 apartment 1 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
        
            elif apnum_text.get() == '2':
                try:
                    if 'C4' and '2' in cq4[0] or 'C4' and '2' in cq4[1]:
                        if t_name_text.get() in cq4[0] or t_name_text.get() in cq4[1]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','C4 apartment 2 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 

            elif apnum_text.get() == '3':
                try:
                    if 'C4' and '3' in cq4[0] or 'C4' and '3' in cq4[1] \
                    or 'C4' and '3' in cq4[2]:
                        if t_name_text.get() in cq4[0] or t_name_text.get() in cq4[1] \
                        or t_name_text.get() in cq4[2]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','C4 apartment 3 is occupied')
                        break                        
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 

            elif apnum_text.get() == '4':
                try:
                    if 'C4' and '4' in cq4[0] or 'C4' and '4' in cq4[1] \
                    or 'C4' and '4' in cq4[2] or 'C4' and '4' in cq4[3]:
                        if t_name_text.get() in cq4[0] or t_name_text.get() in cq4[1] \
                        or t_name_text.get() in cq4[2] or t_name_text.get() in cq4[3]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','C4 apartment 4 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
                        
        #BLOCK D APARTMENT D1
        while block_text.get() == 'D' and aptype_text.get() == 'D1':
            if apnum_text.get() == '1':
                try:
                    if 'D1' and '1' in dq1[0]:
                        if t_name_text.get() in dq1[0]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','D1 apartment 1 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
        
            elif apnum_text.get() == '2':
                try:
                    if 'D1' and '2' in dq1[0] or 'D1' and '2' in dq1[1]:
                        if t_name_text.get() in dq1[0] or t_name_text.get() in dq1[1]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','D1 apartment 2 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 

            elif apnum_text.get() == '3':
                try:
                    if 'D1' and '3' in dq1[0] or 'D1' and '3' in dq1[1] \
                    or 'D1' and '3' in dq1[2]:
                        if t_name_text.get() in dq1[0] or t_name_text.get() in dq1[1] \
                        or t_name_text.get() in dq1[2]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','D1 apartment 3 is occupied')
                        break                        
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
            
            elif apnum_text.get() == '4':
                try:
                    if 'D1' and '4' in dq1[0] or 'D1' and '4' in dq1[1] \
                    or 'D1' and '4' in dq1[2] or 'D1' and '4' in dq1[3]:
                        if t_name_text.get() in dq1[0] or t_name_text.get() in dq1[1] \
                        or t_name_text.get() in dq1[2] or t_name_text.get() in dq1[3]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','D1 apartment 4 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
                    
        #BLOCK D APARTMENT D2
        while block_text.get() == 'D' and aptype_text.get() == 'D2':
            if apnum_text.get() == '1':
                try:
                    if 'D2' and '1' in dq2[0]:
                        if t_name_text.get() in dq2[0]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','D2 apartment 1 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
        
            elif apnum_text.get() == '2':
                try:
                    if 'D2' and '2' in dq2[0] or 'D2' and '2' in dq2[1]:
                        if t_name_text.get() in dq2[0] or t_name_text.get() in dq2[1]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','D2 apartment 2 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 

            elif apnum_text.get() == '3':
                try:
                    if 'D2' and '3' in dq2[0] or 'D2' and '3' in dq2[1] \
                    or 'D2' and '3' in dq2[2]:
                        if t_name_text.get() in dq2[0] or t_name_text.get() in dq2[1] \
                        or t_name_text.get() in dq2[2]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','D2 apartment 3 is occupied')
                        break                        
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
            
            elif apnum_text.get() == '4':
                try:
                    if 'D2' and '4' in dq2[0] or 'D2' and '4' in dq2[1] \
                    or 'D2' and '4' in dq2[2] or 'D2' and '4' in dq2[3]:
                        if t_name_text.get() in dq2[0] or t_name_text.get() in dq2[1] \
                        or t_name_text.get() in dq2[2] or t_name_text.get() in dq2[3]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','D2 apartment 4 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
                        
        #BLOCK D APARTMENT D3
        while block_text.get() == 'D' and aptype_text.get() == 'D3':
            if apnum_text.get() == '1':
                try:
                    if 'D3' and '1' in dq3[0]:
                        if t_name_text.get() in dq3[0]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','D3 apartment 1 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
        
            elif apnum_text.get() == '2':
                try:
                    if 'D3' and '2' in dq3[0] or 'D3' and '2' in dq3[1]:
                        if t_name_text.get() in dq3[0] or t_name_text.get() in dq3[1]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','D3 apartment 2 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 

            elif apnum_text.get() == '3':
                try:
                    if 'D3' and '3' in dq3[0] or 'D3' and '3' in dq3[1] \
                    or 'D3' and '3' in dq3[2]:
                        if t_name_text.get() in dq3[0] or t_name_text.get() in dq3[1] \
                        or t_name_text.get() in dq3[2]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','D3 apartment 3 is occupied')
                        break                        
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
            
            elif apnum_text.get() == '4':
                try:
                    if 'D3' and '4' in dq3[0] or 'D3' and '4' in dq3[1] \
                    or 'D3' and '4' in dq3[2] or 'D3' and '4' in dq3[3]:
                        if t_name_text.get() in dq3[0] or t_name_text.get() in dq3[1] \
                        or t_name_text.get() in dq3[2] or t_name_text.get() in dq3[3]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','D3 apartment 4 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
                        
        #BLOCK D APARTMENT D4
        while block_text.get() == 'D' and aptype_text.get() == 'D4':
            if apnum_text.get() == '1':
                try:
                    if 'D4' and '1' in dq4[0]:
                        if t_name_text.get() in dq4[0]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','D4 apartment 1 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
        
            elif apnum_text.get() == '2':
                try:
                    if 'D4' and '2' in dq4[0] or 'D4' and '2' in dq4[1]:
                        if t_name_text.get() in dq4[0] or t_name_text.get() in dq4[1]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','D4 apartment 2 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 

            elif apnum_text.get() == '3':
                try:
                    if 'D4' and '3' in dq4[0] or 'D4' and '3' in dq4[1] \
                    or 'D4' and '3' in dq4[2]:
                        if t_name_text.get() in dq4[0] or t_name_text.get() in dq4[1] \
                        or t_name_text.get() in dq4[2]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','D4 apartment 3 is occupied')
                        break                        
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
            
            elif apnum_text.get() == '4':
                try:
                    if 'D4' and '4' in dq4[0] or 'D4' and '4' in dq4[1] \
                    or 'D4' and '4' in dq4[2] or 'D4' and '4' in dq4[3]:
                        if t_name_text.get() in dq4[0] or t_name_text.get() in dq4[1] \
                        or t_name_text.get() in dq4[2] or t_name_text.get() in dq4[3]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','D4 apartment 4 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
                        
        #BLOCK E APARTMENT E1
        while block_text.get() == 'E' and aptype_text.get() == 'E1':
            if apnum_text.get() == '1':
                try:
                    if 'E1' and '1' in eq1[0]:
                        if t_name_text.get() in eq1[0]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','E1 apartment 1 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
        
            elif apnum_text.get() == '2':
                try:
                    if 'E1' and '2' in eq1[0] or 'E1' and '2' in eq1[1]:
                        if t_name_text.get() in eq1[0] or t_name_text.get() in eq1[1]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','E1 apartment 2 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 

            elif apnum_text.get() == '3':
                try:
                    if 'E1' and '3' in eq1[0] or 'E1' and '3' in eq1[1] \
                    or 'E1' and '3' in eq1[2]:
                        if t_name_text.get() in eq1[0] or t_name_text.get() in eq1[1] \
                        or t_name_text.get() in eq1[2]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','E1 apartment 3 is occupied')
                        break                        
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
            
            elif apnum_text.get() == '4':
                try:
                    if 'E1' and '4' in eq1[0] or 'E1' and '4' in eq1[1] \
                    or 'E1' and '4' in eq1[2] or 'E1' and '4' in eq1[3]:
                        if t_name_text.get() in eq1[0] or t_name_text.get() in eq1[1] \
                        or t_name_text.get() in eq1[2] or t_name_text.get() in eq1[3]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','E1 apartment 4 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
                        
        #BLOCK E APARTMENT E2
        while block_text.get() == 'E' and aptype_text.get() == 'E2':
            if apnum_text.get() == '1':
                try:
                    if 'E2' and '1' in eq2[0]:
                        if t_name_text.get() in eq2[0]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','E2 apartment 1 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
        
            elif apnum_text.get() == '2':
                try:
                    if 'E2' and '2' in eq2[0] or 'E2' and '2' in eq2[1]:
                        if t_name_text.get() in eq2[0] or t_name_text.get() in eq2[1]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','E2 apartment 2 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 

            elif apnum_text.get() == '3':
                try:
                    if 'E2' and '3' in eq2[0] or 'E2' and '3' in eq2[1] \
                    or 'E2' and '3' in eq2[2]:
                        if t_name_text.get() in eq2[0] or t_name_text.get() in eq2[1] \
                        or t_name_text.get() in eq2[2]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','E2 apartment 3 is occupied')
                        break                        
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
            
            elif apnum_text.get() == '4':
                try:
                    if 'E2' and '4' in eq2[0] or 'E2' and '4' in eq2[1] \
                    or 'E2' and '4' in eq2[2] or 'E2' and '4' in eq2[3]:
                        if t_name_text.get() in eq2[0] or t_name_text.get() in eq2[1] \
                        or t_name_text.get() in eq2[2] or t_name_text.get() in eq2[3]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','E2 apartment 4 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
                        
        #BLOCK E APARTMENT E3
        while block_text.get() == 'E' and aptype_text.get() == 'E3':
            if apnum_text.get() == '1':
                try:
                    if 'E3' and '1' in eq3[0]:
                        if t_name_text.get() in eq3[0]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','E3 apartment 1 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
        
            elif apnum_text.get() == '2':
                try:
                    if 'E3' and '2' in eq3[0] or 'E3' and '2' in eq3[1]:
                        if t_name_text.get() in eq3[0] or t_name_text.get() in eq3[1]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','E3 apartment 2 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 

            elif apnum_text.get() == '3':
                try:
                    if 'E3' and '3' in eq3[0] or 'E3' and '3' in eq3[1] \
                    or 'E3' and '3' in eq3[2]:
                        if t_name_text.get() in eq3[0] or t_name_text.get() in eq3[1] \
                        or t_name_text.get() in eq3[2]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','E3 apartment 3 is occupied')
                        break                        
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
            
            elif apnum_text.get() == '4':
                try:
                    if 'E3' and '4' in eq3[0] or 'E3' and '4' in eq3[1] \
                    or 'E3' and '4' in eq3[2] or 'E3' and '4' in eq3[3]:
                        if t_name_text.get() in eq3[0] or t_name_text.get() in eq3[1] \
                        or t_name_text.get() in eq3[2] or t_name_text.get() in eq3[3]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','E3 apartment 4 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
                        
        #BLOCK E APARTMENT E4
        while block_text.get() == 'E' and aptype_text.get() == 'E4':
            if apnum_text.get() == '1':
                try:
                    if 'E4' and '1' in eq4[0]:
                        if t_name_text.get() in eq4[0]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','E4 apartment 1 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(roomno_text.get(),
                                    block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    #RESET T-ENTRIES
                    e1.delete(0,END),
                    e2.current(0),
                    e3.delete(0,END),
                    e4.delete(0,END),
                    e5.delete(0,END),
                    e6.delete(0,END),
                    e7.delete(0,END),
                    e8.configure(state='readonly'),
                    e9.current(0),
                    date_calc(duration_text.get())
                    chk_out_text.set(evac)
                    e10.configure(state='readonly'),
                    #RESET R-ENTRIES
                    eb1.delete(0,END),
                    eb2.current(0),
                    eb3.current(0),
                    eb4.current(0),
                    eb5.current(0)
        
            elif apnum_text.get() == '2':
                try:
                    if 'E4' and '2' in eq4[0] or 'E4' and '2' in eq4[1]:
                        if t_name_text.get() in eq4[0] or t_name_text.get() in eq4[1]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','E4 apartment 2 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 

            elif apnum_text.get() == '3':
                try:
                    if 'E4' and '3' in eq4[0] or 'E4' and '3' in eq4[1] \
                    or 'E4' and '3' in eq4[2]:
                        if t_name_text.get() in eq4[0] or t_name_text.get() in eq4[1] \
                        or t_name_text.get() in eq4[2]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','E4 apartment 3 is occupied')
                        break                        
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
            
            elif apnum_text.get() == '4':
                try:
                    if 'E4' and '4' in eq4[0] or 'E4' and '4' in eq4[1] \
                    or 'E4' and '4' in eq4[2] or 'E4' and '4' in eq4[3]:
                        if t_name_text.get() in eq4[0] or t_name_text.get() in eq4[1] \
                        or t_name_text.get() in eq4[2] or t_name_text.get() in eq4[3]:
                            tkinter.messagebox.showinfo('Update Manager','your update was successful')
                            backend.t_update(t_name_text.get().title(),
                                            gender_text.get(),
                                            mob_num_text.get(),
                                            address_text.get().title(),
                                            email_text.get(),
                                            nation_text.get().title(),
                                            emg_num_text.get(),
                                            ct_name_text.get().title(),
                                            chk_in_text.get(),
                                            chk_out_text.get(),line[0])
                            backend.r_update(block_text.get(),
                                            aptype_text.get(),
                                            apnum_text.get(),
                                            status_text.get(),line[0])
                            reset_tenant_entries()
                            reset_room_entries()
                    else:
                        tkinter.messagebox.showerror('Update Manager','E4 apartment 4 is occupied')
                        break
                except IndexError:
                    tkinter.messagebox.showinfo('Update Manager','your update was successful')
                    backend.t_update(t_name_text.get().title(),
                                    gender_text.get(),
                                    mob_num_text.get(),
                                    address_text.get().title(),
                                    email_text.get(),
                                    nation_text.get().title(),
                                    emg_num_text.get(),
                                    ct_name_text.get().title(),
                                    chk_in_text.get(),
                                    chk_out_text.get(),line[0])
                    backend.r_update(block_text.get(),
                                    aptype_text.get(),
                                    apnum_text.get(),
                                    status_text.get(),line[0])
                    reset_tenant_entries()
                    reset_room_entries() 
                            
    else:
        tkinter.messagebox.showerror('Update Manager', 'your entries are missing key values')
        e1.focus_set()
        
def t_reset():
    chk_in_text.set(time.strftime('%Y-%m-%d'))
    chk_out_text.set(evac)
    e9.configure(state='readonly')
    e11.configure(state='readonly')
    view_area.delete(0,END),
    e1.delete(0,END),
    e2.current(0),
    e3.delete(0,END),
    e4.delete(0,END),
    e5.delete(0,END),
    e6.delete(0,END),
    e7.delete(0,END),
    e8.delete(0,END),
    e10.current(0)
    #ROOM ENTRIES
    eb1.current(0),
    eb2.current(0),
    eb3.current(0),
    eb4.current(0)

def searchfor():
    view_area.delete(0,END)
    e9.configure(state='normal')
    e11.configure(state='normal')
    e9.delete(0,END)
    e11.delete(0,END)
    search_data = myquery.t_rsearch(t_name_text.get().title(),gender_text.get(),mob_num_text.get(),
                                address_text.get(),email_text.get(),nation_text.get(),
                                emg_num_text.get(),ct_name_text.get(),chk_in_text.get(),
                                chk_out_text.get(),block_text.get(),aptype_text.get(),
                                apnum_text.get(),status_text.get())
    for row in search_data:
        view_area.insert(END,*row)
    
    chk_in_text.set(time.strftime('%Y-%m-%d'))
    chk_out_text.set(evac)
    e9.configure(state='readonly')
    e11.configure(state='readonly')


#create a function that controls the color coding, based on data in the database        
def time_convert(x):
    c_convert = dt.strptime(x,'%Y-%m-%d')
    c_fin = c_convert.date()
    return c_fin

def approx(days):
    #always make ref to month from a +1 pov eg, month is less than 10 months
    if 29 < days < 360:
        m = days/30
        months = ') has '+str(int(m.__round__()))+' month(s)'
        return months
    elif 13 < days < 30:
        w = days/7
        weeks = ') has '+str(int(w.__round__()))+' week(s)'
        return weeks
    elif 0 <= days < 14:
        day = ') has '+str(days)+' day(s)'
        return day  
    elif days < 0:
        res = ') has no more day(s)'
        return res  

    
def call_a():
    class A_manager():
        '''
        This class collects information from the A1 query and uses it 
        to calculate tenant duration. it returns a list that is used to 
        check for room availability
        '''
        def __init__(self,a1,a2,a3,a4):
            self.a1 = a1
            self.a2 = a2
            self.a3 = a3
            self.a4 = a4
            self.ap_type = ''
        
        @staticmethod
        def apt_checker(aprt):
            all_apt_nos = {'apt_1':'false','apt_2':'false','apt_3':'false','apt_4':'false'}
            for apts in aprt:
                for apt_nos in apts:
                    apt_no = apts[3]
                    if '1' in apt_no: all_apt_nos['apt_1']='True'
                    elif '2' in apt_no: all_apt_nos['apt_2']='True'
                    elif '3' in apt_no: all_apt_nos['apt_3']='True'
                    elif '4' in apt_no: all_apt_nos['apt_4']='True'
            return(all_apt_nos)
        
        def qa1(self):
            a1list = ['apt_1','apt_2','apt_3','apt_4'] #instead of an empty list. use a predefined list. eg a1list=[1,2,3,4]. then u can substitute qal for 1 and qa2 for 2 in that order
            if len(self.a1) == 0:
                a1list.append('A1 apartments are all vacant!')
            else:
                try:
                    if 'A1' and '1' in self.a1[0] or len(self.a1[0]) >1:
                        apt1 = self.a1[0]
                        d = apt1[10]      # d for date
                        a_d = time_convert(d) #a_d is d converted to date object
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days    
                        notif = apt1[0]+' in '+apt1[2]+' apartment ('+apt1[3]+ \
                                approx(find)+' left'
                        a1list[0] = notif
                    #else:
                        #a1list[0] = 'There is a vacancy in A1 apartment one!'
                except IndexError:
                    pass
                try:    
                    if 'A1' and '2' in self.a1[1] or len(self.a1[1]) >1:
                        apt2 = self.a1[1]
                        d = apt2[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt2[0]+' in '+apt2[2]+' apartment ('+apt2[3]+ \
                                approx(find)+' left' 
                        a1list[1] = notif                    
                        
                except IndexError:
                    rm_dict = A_manager.apt_checker(self.a1)
                    if rm_dict['apt_1']=='false':
                        a1list[1] = 'There is a vacancy in A1 apartment one!'
                    elif rm_dict['apt_2']=='false':
                        #if 'There is a vacancy in A1 apartment two!' not in a1list:
                        a1list[1] = 'There is a vacancy in A1 apartment two!'
                    #a1list[1] ='There is a vacancy in A1 apartment two!'
                    
                try:    
                    if 'A1' and '3' in self.a1[2] or len(self.a1[2]) >1:
                        apt3 = self.a1[2]
                        d = apt3[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt3[0]+' in '+apt3[2]+' apartment ('+apt3[3]+ \
                                approx(find)+' left'
                        a1list[2] = notif             
                except IndexError:
                    rm_dict = A_manager.apt_checker(self.a1)
                    if rm_dict['apt_1']=='false' and 'There is a vacancy in A1 apartment one!' not in a1list:
                        a1list[2] = 'There is a vacancy in A1 apartment one!'
                    elif rm_dict['apt_2']=='false':
                        if 'There is a vacancy in A1 apartment two!' not in a1list:
                            a1list[2] = 'There is a vacancy in A1 apartment two!' 
                    elif rm_dict['apt_3']=='false':
                        if 'There is a vacancy in A1 apartment three!' not in a1list:
                            a1list[2] = 'There is a vacancy in A1 apartment three!'
                    
                try:    
                    if 'A1' and '4' in self.a1[3] or len(self.a1[3]) >1:
                        apt4 = self.a1[3]
                        d = apt4[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt4[0]+' in '+apt4[2]+' apartment ('+apt4[3]+ \
                                approx(find)+' left'
                        a1list[3] = notif
                except IndexError:
                    rm_dict = A_manager.apt_checker(self.a1)
                    if rm_dict['apt_4']=='false':
                        a1list[3] = 'There is a vacancy in A1 apartment four!'
                    elif rm_dict['apt_3']=='false':
                        if 'There is a vacancy in A1 apartment three!' not in a1list:
                            a1list[3] = 'There is a vacancy in A1 apartment three!'
                    elif rm_dict['apt_2']=='false':
                        if 'There is a vacancy in A1 apartment two!' not in a1list:
                            a1list[3] = 'There is a vacancy in A1 apartment two!'
                    elif rm_dict['apt_1']=='false':
                        if 'There is a vacancy in A1 apartment one!' not in a1list:
                            a1list[3] = 'There is a vacancy in A1 apartment one!'
                        
            return a1list
                
        def qa2(self):
            a2list = []
            if len(self.a2) == 0:
                a2list.append('A2 apartments are all vacant!')
            else:
                try:
                    if 'A2' and '1' in self.a2[0] or len(self.a2[0]) >1:
                        apt1 = self.a2[0]
                        d = apt1[10]      # d for date
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days    
                        notif = apt1[0]+' in '+apt1[2]+' apartment ('+apt1[3]+ \
                                approx(find)+' left'
                        a2list.append(notif)
                    else:
                        a2list.append('There is a vacancy in A2!')
                except IndexError:
                    pass
                try:    
                    if 'A2' and '2' in self.a2[1] or len(self.a2[1]) >1:
                        apt2 = self.a2[1]
                        d = apt2[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt2[0]+' in '+apt2[2]+' apartment ('+apt2[3]+ \
                                approx(find)+' left' 
                        a2list.append(notif)                    
                        
                except IndexError:
                    a2list.append('There is a vacancy in A2!')
                    
                try:    
                    if 'A2' and '3' in self.a2[2] or len(self.a2[2]) >1:
                        apt3 = self.a2[2]
                        d = apt3[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt3[0]+' in '+apt3[2]+' apartment ('+apt3[3]+ \
                                approx(find)+' left'
                        a2list.append(notif)             
                except IndexError:
                    a2list.append('There is a vacancy in A2!')   
                    
                try:    
                    if 'A2' and '4' in self.a2[3] or len(self.a2[3]) >1:
                        apt4 = self.a2[3]
                        d = apt4[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt4[0]+' in '+apt4[2]+' apartment ('+apt4[3]+ \
                                approx(find)+' left'
                        a2list.append(notif)
                except IndexError:
                    a2list.append('There is a vacancy in A2!')
            return a2list

        def qa3(self):
            a3list = []
            if len(self.a3) == 0:
                a3list.append('A3 apartments are all vacant!')
            else:
                try:
                    if 'A3' and '1' in self.a3[0] or len(self.a3[0]) >1:
                        apt1 = self.a3[0]
                        d = apt1[10]      # d for date
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days    
                        notif = apt1[0]+' in '+apt1[2]+' apartment ('+apt1[3]+ \
                                approx(find)+' left'
                        a3list.append(notif)
                    else:
                        a3list.append('There is a vacancy in A3!')
                except IndexError:
                    pass
                try:    
                    if 'A3' and '2' in self.a3[1] or len(self.a3[1]) >1:
                        apt2 = self.a3[1]
                        d = apt2[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt2[0]+' in '+apt2[2]+' apartment ('+apt2[3]+ \
                                approx(find)+' left' 
                        a3list.append(notif)                    
                        
                except IndexError:
                    a3list.append('There is a vacancy in A3!')
                    
                try:    
                    if 'A3' and '3' in self.a3[2] or len(self.a3[2]) >1:
                        apt3 = self.a3[2]
                        d = apt3[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt3[0]+' in '+apt3[2]+' apartment ('+apt3[3]+ \
                                approx(find)+' left'
                        a3list.append(notif)             
                except IndexError:
                    a3list.append('There is a vacancy in A3!')   
                    
                try:    
                    if 'A3' and '4' in self.a3[3] or len(self.a3[3]) >1:
                        apt4 = self.a3[3]
                        d = apt4[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt4[0]+' in '+apt4[2]+' apartment ('+apt4[3]+ \
                                approx(find)+' left'
                        a3list.append(notif)
                except IndexError:
                    a3list.append('There is a vacancy in A3!')
            return a3list
                            
        def qa4(self):
            a4list = []
            if len(self.a4) == 0:
                a4list.append('A4 apartments are all vacant!')
            else:
                try:
                    if 'A4' and '1' in self.a4[0] or len(self.a4[0]) >1:
                        apt1 = self.a4[0]
                        d = apt1[10]      # d for date
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days    
                        notif = apt1[0]+' in '+apt1[2]+' apartment ('+apt1[3]+ \
                                approx(find)+' left'
                        a4list.append(notif)
                    else:
                        a4list.append('There is a vacancy in A4!')
                except IndexError:
                    pass
                try:    
                    if 'A4' and '2' in self.a4[1] or len(self.a4[1]) >1:
                        apt2 = self.a4[1]
                        d = apt2[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt2[0]+' in '+apt2[2]+' apartment ('+apt2[3]+ \
                                approx(find)+' left' 
                        a4list.append(notif)                    
                        
                except IndexError:
                    a4list.append('There is a vacancy in A4!')
                    
                try:    
                    if 'A4' and '3' in self.a4[2] or len(self.a4[2]) >1:
                        apt3 = self.a4[2]
                        d = apt3[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt3[0]+' in '+apt3[2]+' apartment ('+apt3[3]+ \
                                approx(find)+' left'
                        a4list.append(notif)             
                except IndexError:
                    a4list.append('There is a vacancy in A4!')   
                    
                try:    
                    if 'A4' and '4' in self.a4[3] or len(self.a4[3]) >1:
                        apt4 = self.a4[3]
                        d = apt4[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt4[0]+' in '+apt4[2]+' apartment ('+apt4[3]+ \
                                approx(find)+' left'
                        a4list.append(notif)
                except IndexError:
                    a4list.append('There is a vacancy in A4!')
            return a4list

        
    disp = A_manager(myquery.A1_query(),myquery.A2_query(),myquery.A3_query(),myquery.A4_query())
    global A1 
    global A2
    global A3
    global A4
    A1 = disp.qa1()
    A2 = disp.qa2()
    A3 = disp.qa3()
    A4 = disp.qa4()
call_a()

def call_b():
    class B_manager():
        def __init__(self,b1,b2,b3,b4):
            self.b1 = b1
            self.b2 = b2
            self.b3 = b3
            self.b4 = b4
            
        def qb1(self):
            b1list = []
            if len(self.b1) == 0:
                b1list.append('B1 apartments are all vacant!')
            else:
                try:
                    if 'B1' and '1' in self.b1[0] or len(self.b1[0]) >1:
                        apt1 = self.b1[0]
                        d = apt1[10]      # d for date
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days    
                        notif = apt1[0]+' in '+apt1[2]+' apartment ('+apt1[3]+ \
                                approx(find)+' left'
                        b1list.append(notif)
                    else:
                        b1list.append('There is a vacancy in B1!')
                except IndexError:
                    pass
                try:    
                    if 'B1' and '2' in self.b1[1] or len(self.b1[1]) >1:
                        apt2 = self.b1[1]
                        d = apt2[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt2[0]+' in '+apt2[2]+' apartment ('+apt2[3]+ \
                                approx(find)+' left' 
                        b1list.append(notif)                    
                        
                except IndexError:
                    b1list.append('There is a vacancy in B1!')
                    
                try:    
                    if 'B1' and '3' in self.b1[2] or len(self.b1[2]) >1:
                        apt3 = self.b1[2]
                        d = apt3[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt3[0]+' in '+apt3[2]+' apartment ('+apt3[3]+ \
                                approx(find)+' left'
                        b1list.append(notif)             
                except IndexError:
                    b1list.append('There is a vacancy in B1!')   
                    
                try:    
                    if 'B1' and '4' in self.b1[3] or len(self.b1[3]) >1:
                        apt4 = self.b1[3]
                        d = apt4[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt4[0]+' in '+apt4[2]+' apartment ('+apt4[3]+ \
                                approx(find)+' left'
                        b1list.append(notif)
                except IndexError:
                    b1list.append('There is a vacancy in B1!')
            return b1list
                
        def qb2(self):
            b2list = []
            if len(self.b2) == 0:
                b2list.append('B2 apartments are all vacant!')
            else:
                try:
                    if 'B2' in self.b2[0] and '1' in self.b2[0] or len(self.b2[0]) >1:
                        apt1 = self.b2[0]
                        d = apt1[10]      # d for date
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days    
                        notif = apt1[0]+' in '+apt1[2]+' apartment ('+apt1[3]+ \
                                approx(find)+' left'
                        b2list.append(notif)
                    else:
                        b2list.append('There is a vacancy in B2!')
                except IndexError:
                    pass
                try:    
                    if 'B2' in self.b2[1] and '2' in self.b2[1] or len(self.b2[1]) >1:
                        apt2 = self.b2[1]
                        d = apt2[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt2[0]+' in '+apt2[2]+' apartment ('+apt2[3]+ \
                                approx(find)+' left' 
                        b2list.append(notif)                    
                        
                except IndexError:
                    b2list.append('There is a vacancy in B2!')
                    
                try:    
                    if 'B2' in self.b2[2] and '3' in self.b2[2] or len(self.b2[2]) >1:
                        apt3 = self.b2[2]
                        d = apt3[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt3[0]+' in '+apt3[2]+' apartment ('+apt3[3]+ \
                                approx(find)+' left'
                        b2list.append(notif)             
                except IndexError:
                    b2list.append('There is a vacancy in B2!')   
                    
                try:    
                    if 'B2' in self.b2[3] and '4' in self.b2[3] or len(self.b2[3]) >1:
                        apt4 = self.b2[3]
                        d = apt4[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt4[0]+' in '+apt4[2]+' apartment ('+apt4[3]+ \
                                approx(find)+' left'
                        b2list.append(notif)
                except IndexError:
                    b2list.append('There is a vacancy in B2!')
            return b2list

        def qb3(self):
            b3list = []
            if len(self.b3) == 0:
                b3list.append('B3 apartments are all vacant!')
            else:
                try:
                    if 'B3' in self.b3[0] and '1' in self.b3[0] or len(self.b3[0]) >1:
                        apt1 = self.b3[0]
                        d = apt1[10]      # d for date
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days    
                        notif = apt1[0]+' in '+apt1[2]+' apartment ('+apt1[3]+ \
                                approx(find)+' left'
                        b3list.append(notif)
                    else:
                        b3list.append('There is a vacancy in B3!')
                except IndexError:
                    pass
                try:    
                    if 'B3' in self.b3[1] and '2' in self.b3[1] or len(self.b3[1]) >1:
                        apt2 = self.b3[1]
                        d = apt2[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt2[0]+' in '+apt2[2]+' apartment ('+apt2[3]+ \
                                approx(find)+' left' 
                        b3list.append(notif)                    
                        
                except IndexError:
                    b3list.append('There is a vacancy in B3!')
                    
                try:    
                    if 'B3' in self.b3[2] and '3' in self.b3[2] or len(self.b3[2]) >1:
                        apt3 = self.b3[2]
                        d = apt3[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt3[0]+' in '+apt3[2]+' apartment ('+apt3[3]+ \
                                approx(find)+' left'
                        b3list.append(notif)             
                except IndexError:
                    b3list.append('There is a vacancy in B3!')   
                    
                try:    
                    if 'B3' in self.b3[3] and '4' in self.b3[3] or len(self.b3[3]) >1:
                        apt4 = self.b3[3]
                        d = apt4[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt4[0]+' in '+apt4[2]+' apartment ('+apt4[3]+ \
                                approx(find)+' left'
                        b3list.append(notif)
                except IndexError:
                    b3list.append('There is a vacancy in B3!')
            return b3list
                            
        def qb4(self):
            b4list = []
            if len(self.b4) == 0:
                b4list.append('B4 apartments are all vacant!')
            else:
                try:
                    if 'B4' in self.b4[0] and '1' in self.b4[0] or len(self.b4[0]) >1:
                        apt1 = self.b4[0]
                        d = apt1[10]      # d for date
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days    
                        notif = apt1[0]+' in '+apt1[2]+' apartment ('+apt1[3]+ \
                                approx(find)+' left'
                        b4list.append(notif)
                    else:
                        b4list.append('There is a vacancy in B4!')
                except IndexError:
                    pass
                try:    
                    if 'B4' in self.b4[1] and '2' in self.b4[1] or len(self.b4[1]) >1:
                        apt2 = self.b4[1]
                        d = apt2[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt2[0]+' in '+apt2[2]+' apartment ('+apt2[3]+ \
                                approx(find)+' left' 
                        b4list.append(notif)                    
                        
                except IndexError:
                    b4list.append('There is a vacancy in B4!')
                    
                try:    
                    if 'B4' in self.b4[2] and '3' in self.b4[2] or len(self.b4[2]) >1:
                        apt3 = self.b4[2]
                        d = apt3[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt3[0]+' in '+apt3[2]+' apartment ('+apt3[3]+ \
                                approx(find)+' left'
                        b4list.append(notif)             
                except IndexError:
                    b4list.append('There is a vacancy in B4!')   
                    
                try:    
                    if 'B4' in self.b4[3] and '4' in self.b4[3] or len(self.b4[3]) >1:
                        apt4 = self.b4[3]
                        d = apt4[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt4[0]+' in '+apt4[2]+' apartment ('+apt4[3]+ \
                                approx(find)+' left'
                        b4list.append(notif)
                except IndexError:
                    b4list.append('There is a vacancy in B4!')
            return b4list

    
    disp_b = B_manager(myquery.B1_query(),myquery.B2_query(),myquery.B3_query(),myquery.B4_query()) 
    global B1 
    global B2
    global B3
    global B4
    B1 = disp_b.qb1()
    B2 = disp_b.qb2()
    B3 = disp_b.qb3()
    B4 = disp_b.qb4()
call_b()

def call_c():
    class C_manager():
        def __init__(self,c1,c2,c3,c4):
            self.c1 = c1
            self.c2 = c2
            self.c3 = c3
            self.c4 = c4
            
        def qc1(self):
            c1list = []
            if len(self.c1) == 0:
                c1list.append('C1 apartments are all vacant!')
            else:
                try:
                    if 'C1' and '1' in self.c1[0] or len(self.c1[0]) >1:
                        apt1 = self.c1[0]
                        d = apt1[10]      # d for date
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days    
                        notif = apt1[0]+' in '+apt1[2]+' apartment ('+apt1[3]+ \
                                approx(find)+' left'
                        c1list.append(notif)
                    else:
                        c1list.append('There is a vacancy in C1!')
                except IndexError:
                    pass
                try:    
                    if 'C1' and '2' in self.c1[1] or len(self.c1[1]) >1:
                        apt2 = self.c1[1]
                        d = apt2[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt2[0]+' in '+apt2[2]+' apartment ('+apt2[3]+ \
                                approx(find)+' left' 
                        c1list.append(notif)                    
                        
                except IndexError:
                    c1list.append('There is a vacancy in C1!')
                    
                try:    
                    if 'C1' and '3' in self.c1[2] or len(self.c1[2]) >1:
                        apt3 = self.c1[2]
                        d = apt3[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt3[0]+' in '+apt3[2]+' apartment ('+apt3[3]+ \
                                approx(find)+' left'
                        c1list.append(notif)             
                except IndexError:
                    c1list.append('There is a vacancy in C1!')   
                    
                try:    
                    if 'C1' and '4' in self.c1[3] or len(self.c1[3]) >1:
                        apt4 = self.c1[3]
                        d = apt4[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt4[0]+' in '+apt4[2]+' apartment ('+apt4[3]+ \
                                approx(find)+' left'
                        c1list.append(notif)
                except IndexError:
                    c1list.append('There is a vacancy in C1!')
            return c1list
                
        def qc2(self):
            c2list = []
            if len(self.c2) == 0:
                c2list.append('C2 apartments are all vacant!')
            else:
                try:
                    if 'C2' and '1' in self.c2[0] or len(self.c2[0]) >1:
                        apt1 = self.c2[0]
                        d = apt1[10]      # d for date
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days    
                        notif = apt1[0]+' in '+apt1[2]+' apartment ('+apt1[3]+ \
                                approx(find)+' left'
                        c2list.append(notif)
                    else:
                        c2list.append('There is a vacancy in C2!')
                except IndexError:
                    pass
                try:    
                    if 'C2' and '2'in self.c2[1] or len(self.c2[1]) >1:
                        apt2 = self.c2[1]
                        d = apt2[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt2[0]+' in '+apt2[2]+' apartment ('+apt2[3]+ \
                                approx(find)+' left' 
                        c2list.append(notif)                    
                        
                except IndexError:
                    c2list.append('There is a vacancy in C2!')
                    
                try:    
                    if 'C2' and '3' in self.c2[2] or len(self.c2[2]) >1:
                        apt3 = self.c2[2]
                        d = apt3[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt3[0]+' in '+apt3[2]+' apartment ('+apt3[3]+ \
                                approx(find)+' left'
                        c2list.append(notif)             
                except IndexError:
                    c2list.append('There is a vacancy in C2!')   
                    
                try:    
                    if 'C2' and '4' in self.c2[3] or len(self.c2[3]) >1:
                        apt4 = self.c2[3]
                        d = apt4[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt4[0]+' in '+apt4[2]+' apartment ('+apt4[3]+ \
                                approx(find)+' left'
                        c2list.append(notif)
                except IndexError:
                    c2list.append('There is a vacancy in C2!')
            return c2list

        def qc3(self):
            c3list = []
            if len(self.c3) == 0:
                c3list.append('C3 apartments are all vacant!')
            else:
                try:
                    if 'C3' and '1' in self.c3[0] or len(self.c3[0]) >1:
                        apt1 = self.c3[0]
                        d = apt1[10]      # d for date
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days    
                        notif = apt1[0]+' in '+apt1[2]+' apartment ('+apt1[3]+ \
                                approx(find)+' left'
                        c3list.append(notif)
                    else:
                        c3list.append('There is a vacancy in C3!')
                except IndexError:
                    pass
                try:    
                    if 'C3' and '2' in self.c3[1] or len(self.c3[1]) >1:
                        apt2 = self.c3[1]
                        d = apt2[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt2[0]+' in '+apt2[2]+' apartment ('+apt2[3]+ \
                                approx(find)+' left' 
                        c3list.append(notif)                    
                        
                except IndexError:
                    c3list.append('There is a vacancy in C3!')
                    
                try:    
                    if 'C3' and '3' in self.c3[2] or len(self.c3[2]) >1:
                        apt3 = self.c3[2]
                        d = apt3[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt3[0]+' in '+apt3[2]+' apartment ('+apt3[3]+ \
                                approx(find)+' left'
                        c3list.append(notif)             
                except IndexError:
                    c3list.append('There is a vacancy in C3!')   
                    
                try:    
                    if 'C3' and '4' in self.c3[3] or len(self.c3[3]) >1:
                        apt4 = self.c3[3]
                        d = apt4[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt4[0]+' in '+apt4[2]+' apartment ('+apt4[3]+ \
                                approx(find)+' left'
                        c3list.append(notif)
                except IndexError:
                    c3list.append('There is a vacancy in C3!')
            return c3list
                            
        def qc4(self):
            c4list = []
            if len(self.c4) == 0:
                c4list.append('C4 apartments are all vacant!')
            else:
                try:
                    if 'C4' and '1' in self.c4[0] or len(self.c4[0]) >1:
                        apt1 = self.c4[0]
                        d = apt1[10]      # d for date
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days    
                        notif = apt1[0]+' in '+apt1[2]+' apartment ('+apt1[3]+ \
                                approx(find)+' left'
                        c4list.append(notif)
                    else:
                        c4list.append('There is a vacancy in C4!')
                except IndexError:
                    pass
                try:    
                    if 'C4' and '2' in self.c4[1] or len(self.c4[1]) >1:
                        apt2 = self.c4[1]
                        d = apt2[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt2[0]+' in '+apt2[2]+' apartment ('+apt2[3]+ \
                                approx(find)+' left' 
                        c4list.append(notif)                    
                        
                except IndexError:
                    c4list.append('There is a vacancy in C4!')
                    
                try:    
                    if 'C4' and '3' in self.c4[2] or len(self.c4[2]) >1:
                        apt3 = self.c4[2]
                        d = apt3[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt3[0]+' in '+apt3[2]+' apartment ('+apt3[3]+ \
                                approx(find)+' left'
                        c4list.append(notif)             
                except IndexError:
                    c4list.append('There is a vacancy in C4!')   
                    
                try:    
                    if 'C4' and '4' in self.c4[3] or len(self.c4[3]) >1:
                        apt4 = self.c4[3]
                        d = apt4[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt4[0]+' in '+apt4[2]+' apartment ('+apt4[3]+ \
                                approx(find)+' left'
                        c4list.append(notif)
                except IndexError:
                    c4list.append('There is a vacancy in C4!')
            return c4list

        
    disp_c = C_manager(myquery.C1_query(),myquery.C2_query(),myquery.C3_query(),myquery.C4_query()) 
    global C1 
    global C2
    global C3
    global C4
    C1 = disp_c.qc1()
    C2 = disp_c.qc2()
    C3 = disp_c.qc3()
    C4 = disp_c.qc4()
call_c()

def call_d():
    class D_manager():
        def __init__(self,d1,d2,d3,d4):
            self.d1 = d1
            self.d2 = d2
            self.d3 = d3
            self.d4 = d4
            
        def qd1(self):
            d1list = []
            if len(self.d1) == 0:
                d1list.append('D1 apartments are all vacant!')
            else:
                try:
                    if 'D1' and '1' in self.d1[0] or len(self.d1[0]) >1:
                        apt1 = self.d1[0]
                        d = apt1[10]      # d for date
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days    
                        notif = apt1[0]+' in '+apt1[2]+' apartment ('+apt1[3]+ \
                                approx(find)+' left'
                        d1list.append(notif)
                    else:
                        d1list.append('There is a vacancy in D1!')
                except IndexError:
                    pass
                try:    
                    if 'D1' and '2' in self.d1[1] or len(self.d1[1]) >1:
                        apt2 = self.d1[1]
                        d = apt2[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt2[0]+' in '+apt2[2]+' apartment ('+apt2[3]+ \
                                approx(find)+' left' 
                        d1list.append(notif)                    
                        
                except IndexError:
                    d1list.append('There is a vacancy in D1!')
                    
                try:    
                    if 'D1' and '3' in self.d1[2] or len(self.d1[2]) >1:
                        apt3 = self.d1[2]
                        d = apt3[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt3[0]+' in '+apt3[2]+' apartment ('+apt3[3]+ \
                                approx(find)+' left'
                        d1list.append(notif)             
                except IndexError:
                    d1list.append('There is a vacancy in D1!')   
                    
                try:    
                    if 'D1' and '4' in self.d1[3] or len(self.d1[3]) >1:
                        apt4 = self.d1[3]
                        d = apt4[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt4[0]+' in '+apt4[2]+' apartment ('+apt4[3]+ \
                                approx(find)+' left'
                        d1list.append(notif)
                except IndexError:
                    d1list.append('There is a vacancy in D1!')
            return d1list
                
        def qd2(self):
            d2list = []
            if len(self.d2) == 0:
                d2list.append('D2 apartments are all vacant!')
            else:
                try:
                    if 'D2' and '1' in self.d2[0] or len(self.d2[0]) >1:
                        apt1 = self.d2[0]
                        d = apt1[10]      # d for date
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days    
                        notif = apt1[0]+' in '+apt1[2]+' apartment ('+apt1[3]+ \
                                approx(find)+' left'
                        d2list.append(notif)
                    else:
                        d2list.append('There is a vacancy in D2!')
                except IndexError:
                    pass
                try:    
                    if 'D2' and '2' in self.d2[1] or len(self.d2[1]) >1:
                        apt2 = self.d2[1]
                        d = apt2[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt2[0]+' in '+apt2[2]+' apartment ('+apt2[3]+ \
                                approx(find)+' left' 
                        d2list.append(notif)                    
                        
                except IndexError:
                    d2list.append('There is a vacancy in D2!')
                    
                try:    
                    if 'D2' and '3' in self.d2[2] or len(self.d2[2]) >1:
                        apt3 = self.d2[2]
                        d = apt3[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt3[0]+' in '+apt3[2]+' apartment ('+apt3[3]+ \
                                approx(find)+' left'
                        d2list.append(notif)             
                except IndexError:
                    d2list.append('There is a vacancy in D2!')   
                    
                try:    
                    if 'D2' and '4' in self.d2[3] or len(self.d2[3]) >1:
                        apt4 = self.d2[3]
                        d = apt4[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt4[0]+' in '+apt4[2]+' apartment ('+apt4[3]+ \
                                approx(find)+' left'
                        d2list.append(notif)
                except IndexError:
                    d2list.append('There is a vacancy in D2!')
            return d2list

        def qd3(self):
            d3list = []
            if len(self.d3) == 0:
                d3list.append('D3 apartments are all vacant!')
            else:
                try:
                    if 'D3' and '1' in self.d3[0] or len(self.d3[0]) >1:
                        apt1 = self.d3[0]
                        d = apt1[10]      # d for date
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days    
                        notif = apt1[0]+' in '+apt1[2]+' apartment ('+apt1[3]+ \
                                approx(find)+' left'
                        d3list.append(notif)
                    else:
                        d3list.append('There is a vacancy in D3!')
                except IndexError:
                    pass
                try:    
                    if 'D3' and '2' in self.d3[1] or len(self.d3[1]) >1:
                        apt2 = self.d3[1]
                        d = apt2[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt2[0]+' in '+apt2[2]+' apartment ('+apt2[3]+ \
                                approx(find)+' left' 
                        d3list.append(notif)                    
                        
                except IndexError:
                    d3list.append('There is a vacancy in D3!')
                    
                try:    
                    if 'D3' and '3' in self.d3[2] or len(self.d3[2]) >1:
                        apt3 = self.d3[2]
                        d = apt3[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt3[0]+' in '+apt3[2]+' apartment ('+apt3[3]+ \
                                approx(find)+' left'
                        d3list.append(notif)             
                except IndexError:
                    d3list.append('There is a vacancy in D3!')   
                    
                try:    
                    if 'D3' and '4' in self.d3[3] or len(self.d3[3]) >1:
                        apt4 = self.d3[3]
                        d = apt4[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt4[0]+' in '+apt4[2]+' apartment ('+apt4[3]+ \
                                approx(find)+' left'
                        d3list.append(notif)
                except IndexError:
                    d3list.append('There is a vacancy in D3!')
            return d3list
                            
        def qd4(self):
            d4list = []
            if len(self.d4) == 0:
                d4list.append('D4 apartments are all vacant!')
            else:
                try:
                    if 'D4' and '1' in self.d4[0] or len(self.d4[0]) >1:
                        apt1 = self.d4[0]
                        d = apt1[10]      # d for date
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days    
                        notif = apt1[0]+' in '+apt1[2]+' apartment ('+apt1[3]+ \
                                approx(find)+' left'
                        d4list.append(notif)
                    else:
                        d4list.append('There is a vacancy in D4!')
                except IndexError:
                    pass
                try:    
                    if 'D4' and '2' in self.d4[1] or len(self.d4[1]) >1:
                        apt2 = self.d4[1]
                        d = apt2[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt2[0]+' in '+apt2[2]+' apartment ('+apt2[3]+ \
                                approx(find)+' left' 
                        d4list.append(notif)                    
                        
                except IndexError:
                    d4list.append('There is a vacancy in D4!')
                    
                try:    
                    if 'D4' and '3' in self.d4[2] or len(self.d4[2]) >1:
                        apt3 = self.d4[2]
                        d = apt3[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt3[0]+' in '+apt3[2]+' apartment ('+apt3[3]+ \
                                approx(find)+' left'
                        d4list.append(notif)             
                except IndexError:
                    d4list.append('There is a vacancy in D4!')   
                    
                try:    
                    if 'D4' and '4' in self.d4[3] or len(self.d4[3]) >1:
                        apt4 = self.d4[3]
                        d = apt4[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt4[0]+' in '+apt4[2]+' apartment ('+apt4[3]+ \
                                approx(find)+' left'
                        d4list.append(notif)
                except IndexError:
                    d4list.append('There is a vacancy in D4!')
            return d4list


    disp_d = D_manager(myquery.D1_query(),myquery.D2_query(),myquery.D3_query(),myquery.D4_query()) 
    global D1 
    global D2
    global D3
    global D4
    D1 = disp_d.qd1()
    D2 = disp_d.qd2()
    D3 = disp_d.qd3()
    D4 = disp_d.qd4()
call_d()

def call_e():
    class E_manager():
        def __init__(self,e1,e2,e3,e4):
            self.e1 = e1
            self.e2 = e2
            self.e3 = e3
            self.e4 = e4
            
        def qe1(self):
            e1list = []
            if len(self.e1) == 0:
                e1list.append('E1 apartments are all vacant!')
            else:
                try:
                    if 'E1' and '1' in self.e1[0] or len(self.e1[0]) >1:
                        apt1 = self.e1[0]
                        d = apt1[10]      # d for date
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days    
                        notif = apt1[0]+' in '+apt1[2]+' apartment ('+apt1[3]+ \
                                approx(find)+' left'
                        e1list.append(notif)
                    else:
                        e1list.append('There is a vacancy in E1!')
                except IndexError:
                    pass
                try:    
                    if 'E1' and '2' in self.e1[1] or len(self.e1[1]) >1:
                        apt2 = self.e1[1]
                        d = apt2[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt2[0]+' in '+apt2[2]+' apartment ('+apt2[3]+ \
                                approx(find)+' left' 
                        e1list.append(notif)                    
                        
                except IndexError:
                    e1list.append('There is a vacancy in E1!')
                    
                try:    
                    if 'E1' and '3' in self.e1[2] or len(self.e1[2]) >1:
                        apt3 = self.e1[2]
                        d = apt3[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt3[0]+' in '+apt3[2]+' apartment ('+apt3[3]+ \
                                approx(find)+' left'
                        e1list.append(notif)             
                except IndexError:
                    e1list.append('There is a vacancy in E1!')   
                    
                try:    
                    if 'E1' and '4' in self.e1[3] or len(self.e1[3]) >1:
                        apt4 = self.e1[3]
                        d = apt4[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt4[0]+' in '+apt4[2]+' apartment ('+apt4[3]+ \
                                approx(find)+' left'
                        e1list.append(notif)
                except IndexError:
                    e1list.append('There is a vacancy in E1!')
            return e1list
                
        def qe2(self):
            e2list = []
            if len(self.e2) == 0:
                e2list.append('E2 apartments are all vacant!')
            else:
                try:
                    if 'E2' and '1' in self.e2[0] or len(self.e2[0]) >1:
                        apt1 = self.e2[0]
                        d = apt1[10]      # d for date
                        a_d = time_convert(d)
                        print(a_d)
                        today = dt.now().date()
                        print(today)
                        r = a_d - today
                        find = r.days
                        print(find)    
                        notif = apt1[0]+' in '+apt1[2]+' apartment ('+apt1[3]+ \
                                approx(find)+' left'
                        e2list.append(notif)
                    else:
                        e2list.append('There is a vacancy in E2!')
                except IndexError:
                    pass
                try:    
                    if 'E2' and '2' in self.e2[1] or len(self.e2[1]) >1:
                        apt2 = self.e2[1]
                        d = apt2[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt2[0]+' in '+apt2[2]+' apartment ('+apt2[3]+ \
                                approx(find)+' left' 
                        e2list.append(notif)                    
                        
                except IndexError:
                    e2list.append('There is a vacancy in E2!')
                    
                try:    
                    if 'E2' and '3' in self.e2[2] or len(self.e2[2]) >1:
                        apt3 = self.e2[2]
                        d = apt3[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt3[0]+' in '+apt3[2]+' apartment ('+apt3[3]+ \
                                approx(find)+' left'
                        e2list.append(notif)             
                except IndexError:
                    e2list.append('There is a vacancy in E2!')   
                    
                try:    
                    if 'E2' and '4' in self.e2[3] or len(self.e2[3]) >1:
                        apt4 = self.e2[3]
                        d = apt4[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt4[0]+' in '+apt4[2]+' apartment ('+apt4[3]+ \
                                approx(find)+' left'
                        e2list.append(notif)
                except IndexError:
                    e2list.append('There is a vacancy in E2!')
            return e2list

        def qe3(self):
            e3list = []
            if len(self.e3) == 0:
                e3list.append('E3 apartments are all vacant!')
            else:
                try:
                    if 'E3' and '1' in self.e3[0] or len(self.e3[0]) >1:
                        apt1 = self.e3[0]
                        d = apt1[10]      # d for date
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days    
                        notif = apt1[0]+' in '+apt1[2]+' apartment ('+apt1[3]+ \
                                approx(find)+' left'
                        e3list.append(notif)
                    else:
                        e3list.append('There is a vacancy in E3!')
                except IndexError:
                    pass
                try:    
                    if 'E3' and '2' in self.e3[1] or len(self.e3[1]) >1:
                        apt2 = self.e3[1]
                        d = apt2[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt2[0]+' in '+apt2[2]+' apartment ('+apt2[3]+ \
                                approx(find)+' left' 
                        e3list.append(notif)                    
                        
                except IndexError:
                    e3list.append('There is a vacancy in E3!')
                    
                try:    
                    if 'E3' and '3' in self.e3[2] or len(self.e3[2]) >1:
                        apt3 = self.e3[2]
                        d = apt3[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt3[0]+' in '+apt3[2]+' apartment ('+apt3[3]+ \
                                approx(find)+' left'
                        e3list.append(notif)             
                except IndexError:
                    e3list.append('There is a vacancy in E3!')   
                    
                try:    
                    if 'E3' and '4' in self.e3[3] or len(self.e3[3]) >1:
                        apt4 = self.e3[3]
                        d = apt4[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt4[0]+' in '+apt4[2]+' apartment ('+apt4[3]+ \
                                approx(find)+' left'
                        e3list.append(notif)
                except IndexError:
                    e3list.append('There is a vacancy in E3!')
            return e3list
                            
        def qe4(self):
            e4list = []
            if len(self.e4) == 0:
                e4list.append('E4 apartments are all vacant!')
            else:
                try:
                    if 'E4' and '1' in self.e4[0] or len(self.e4[0]) >1:
                        apt1 = self.e4[0]
                        d = apt1[10]      # d for date
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days    
                        notif = apt1[0]+' in '+apt1[2]+' apartment ('+apt1[3]+ \
                                approx(find)+' left'
                        e4list.append(notif)
                    else:
                        e4list.append('There is a vacancy in E4!')
                except IndexError:
                    pass
                try:    
                    if 'E4' and '2' in self.e4[1] or len(self.e4[1]) >1:
                        apt2 = self.e4[1]
                        d = apt2[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt2[0]+' in '+apt2[2]+' apartment ('+apt2[3]+ \
                                approx(find)+' left' 
                        e4list.append(notif)                    
                        
                except IndexError:
                    e4list.append('There is a vacancy in E4!')
                    
                try:    
                    if 'E4' and '3' in self.e4[2] or len(self.e4[2]) >1:
                        apt3 = self.e4[2]
                        d = apt3[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt3[0]+' in '+apt3[2]+' apartment ('+apt3[3]+ \
                                approx(find)+' left'
                        e4list.append(notif)             
                except IndexError:
                    e4list.append('There is a vacancy in E4!')   
                    
                try:    
                    if 'E4' and '4' in self.e4[3] or len(self.e4[3]) >1:
                        apt4 = self.e4[3]
                        d = apt4[10]
                        a_d = time_convert(d)
                        today = dt.now().date()
                        r = a_d - today
                        find = r.days
                        notif = apt4[0]+' in '+apt4[2]+' apartment ('+apt4[3]+ \
                                approx(find)+' left'
                        e4list.append(notif)
                except IndexError:
                    e4list.append('There is a vacancy in E4!')
            return e4list


    disp_e = E_manager(myquery.E1_query(),myquery.E2_query(),myquery.E3_query(),myquery.E4_query()) 
    global E1 
    global E2
    global E3
    global E4
    E1 = disp_e.qe1()
    E2 = disp_e.qe2()
    E3 = disp_e.qe3()
    E4 = disp_e.qe4()
call_e()

        
def db_length():
    l = myquery.t_rview()
    length = len(l)
    return(length)
    
            
def content_creator(id):
    #grabber = backend.t_view()
    pass
       

#---------CREATE FRAMES FOR DIVS---------#
master_frame = LabelFrame(win)
master_frame.pack(expand=TRUE)

#topview frame
top_frame1 = LabelFrame(master_frame,height=40,width=1000,bg='#e3e3e3',relief='flat')
top_frame1.grid(row=0,column=0,columnspan=4,sticky=W+E)

filler1 = Frame(top_frame1,height=36,bg='#e3e3e3')
filler1.grid(row=0,column=0)
filler2 = Frame(top_frame1,width=1080,bg='#e3e3e3')
filler2.grid(row=0,column=2)

#bottom frame
bottom_frame = LabelFrame(master_frame,height=20,width=1000,bd=2,relief='groove')
bottom_frame.grid(row=3,column=0,columnspan=4,sticky=W+E)

#left vertical frame
lv_frame = LabelFrame(master_frame,bg='#e5e5e5')
lv_frame.grid(row=1,column=0,rowspan=2,sticky=N+S)

l_frame = LabelFrame(lv_frame,text='Tenant Info')
l_frame.grid(row=0,column=0,pady=5)

sp_frame1 = Frame(l_frame,height=10)#space separator frame
sp_frame1.grid(row=11,column=0,columnspan=2,sticky=W+E)

l_bframe = LabelFrame(lv_frame,text='Room Info')
l_bframe.grid(row=1,column=0,sticky=W+E)

#seperator
sp_frame = Frame(lv_frame,height=5,bg='#e5e5e5')
sp_frame.grid(row=2,column=0,sticky=W+E+N+S)

s_frame = LabelFrame(lv_frame,text='Admin')
s_frame.grid(row=3,column=0,sticky=W+E+N+S)


#Top right frame containing listbox and notif...
a_frame = LabelFrame(master_frame,width = 100)
a_frame.grid(row=1,column=1)#,rowspan=2)#,sticky=N+S)

m_frame = Frame(a_frame,bg='#e5e5e5')
m_frame.grid(row=0,column=0,sticky=W)
#create Listbox

view_area = TkTreectrl.MultiListbox(m_frame,width=420,height=134,columns=('Tid','Name','Gender','Mobile Number','Address',\
'Email Address','Nationality','Emergency Contact','Contact Person','Check In','Check Out','Block','Apartment Type',\
'Apartment Number','Room Status'),xscrollsmoothing='True',yscrollsmoothing='True')#580
view_area.grid(row=1,rowspan=3,column=0)
view_area.bind('<Double-1>',grab_selection)

#create View_area scrollbar
sb1 = Scrollbar(m_frame,orient='vertical')
sb1.grid(row=1,rowspan=3,column=1,sticky=N+S)
view_area.configure(yscrollcommand=sb1.set)
sb1.configure(command=view_area.yview)

sb1a = Scrollbar(m_frame,orient='horizontal')
sb1a.grid(row=4,column=0,sticky=W+E)
view_area.configure(xscrollcommand=sb1a.set)
sb1a.configure(command=view_area.xview)


#topframe view_area
v_frame = Frame(m_frame,height=2)
v_frame.grid(row=0,column=0,sticky=W+E+N)

vlabel= Label(v_frame,text = 'view')
vlabel.grid(row=0,column=0)


#Bottom right frame containing listbox and notif...
r_frame = LabelFrame(master_frame)
r_frame.grid(row=1,column=2,sticky=W+N+S)

#no_frame = LabelFrame(r_frame,height=40,bg='#e5e5e5')
#no_frame.grid(row=0,column=0,sticky=W+E+N+S)

#nr_frame = LabelFrame(r_frame,text='note',height=40,width=10,bg='#e5e5e5')
#nr_frame.grid(row=0,column=2,sticky=W+E+N+S)

nr1_frame = Frame(r_frame,bg='#e5e5e5')
nr1_frame.grid(row=0,column=1,sticky=W+N+S)

nt_frame = Frame(nr1_frame,width=10,bg='#e5e5e5')
nt_frame.grid(row=0,column=0,sticky=W+E+N+S)

nb_frame = LabelFrame(nr1_frame,width=10,bg='#e5e5e5')
nb_frame.grid(row=1,column=0,sticky=W+E+N+S)

n_frame = LabelFrame(r_frame,text='Notification',bg='#e5e5e5')
n_frame.grid(row=0,column=0,sticky=W+E+N+S)

#sorted
notif_sort = Listbox(n_frame,width=64,height=9,bg='#f4f4f4',
relief='flat',activestyle='none',highlightcolor='#d0d0d0',selectbackground='#00008B')
notif_sort.grid(row=0,column=0)

#create a listbox for notification
view_notif = Listbox(n_frame,width=64,height=9,bg='#f4f4f4',
                    relief='flat',activestyle='none',highlightcolor='#d0d0d0',selectbackground='#00008B')
view_notif.grid(row=0,column=0)


chk = IntVar()
def cal_cb():
    pt=chk.get()
    if pt == 1:
        notif_sort.lift()
    elif pt == 0:
        view_notif.lift()
    else:
        view_notif.lift()

cb = Checkbutton(nt_frame,text='sort available',bg='#e5e5e5',variable=chk,command=cal_cb)
cb.grid(row=3,column=0,padx=2,sticky=W)
cb.deselect()

#notification box scrollbar
sv = Scrollbar(n_frame,orient='vertical',width=2)
sv.grid(row=0,column=1,sticky=N+S)
view_notif.configure(yscrollcommand=sv.set)
sv.configure(command=view_area.yview)

sh = Scrollbar(n_frame,orient='horizontal',width=4)
sh.grid(row=1,column=0,sticky=W+E)
view_notif.configure(xscrollcommand=sh.set)
sh.configure(command=view_area.xview)

#midspan frame
md_frame = LabelFrame(master_frame)
md_frame.grid(row=2,column=1,columnspan=2,sticky=W+E)

#frame for colorcoding
l_rframe = Frame(r_frame,width=440,bg='#e5e5e5')
l_rframe.grid(row=1,column=0,columnspan=2,sticky=W+E+N+S)

#pack 5 frames into left_right frame
w_frame1 = LabelFrame(md_frame,width=900,height=200,pady=5,bd=1,bg='#e5e5e5')
w_frame1.grid(row=0,column=0,sticky=W+E+N+S)

w_frame2 = LabelFrame(md_frame,text='Blocks',width=900,height =100,pady=5,bd=1,bg='#e5e5e5')
w_frame2.grid(row=1,column=0,sticky=W+E+N+S)

w_frame3 = LabelFrame(md_frame,text='Blocks',width=900,height =100,pady=5,bd=1,bg='#e5e5e5')
w_frame3.grid(row=2,column=0,sticky=W+E+N+S)

w_frame4 = LabelFrame(md_frame,text='Blocks',width=900,height =100,pady=5,bd=1,bg='#e5e5e5')
w_frame4.grid(row=3,column=0,sticky=W+E+N+S)

#w_frame5 = LabelFrame(md_frame,text='Block E',width=900,height =200,pady=5,bd=1,bg='#e5e5e5')#dcdcdc
#w_frame5.grid(row=4,column=0,sticky=W+E+N+S)



#---------CREATE LABELS---------#
#lv_frame labels
l1= Label(l_frame,text='Tenant Name')
l1.grid(row=0, column=0, sticky=E)

l2= Label(l_frame,text='Gender')
l2.grid(row=1, column=0,sticky=E)

l3= Label(l_frame,text='Mobile Number')
l3.grid(row=2, column=0,sticky=E)

l4= Label(l_frame,text='Address')
l4.grid(row=3, column=0,sticky=E)

l5= Label(l_frame,text='Email Address')
l5.grid(row=4, column=0,sticky=E)

l6= Label(l_frame,text='Nationality')
l6.grid(row=5, column=0,sticky=E)

l7= Label(l_frame,text='Emergency Contact')
l7.grid(row=6, column=0,sticky=E)

l8= Label(l_frame,text='Contact Person')
l8.grid(row=7, column=0,sticky=E)

l9= Label(l_frame,text='Check In Date')
l9.grid(row=8, column=0,sticky=E)

l10= Label(l_frame,text='Stay Duration')
l10.grid(row=9, column=0,sticky=E)
l10d = Label(l_frame,text=': in months')
l10d.grid(row=9, column=3,sticky=W)

l11= Label(l_frame,text='Check Out Date')
l11.grid(row=10, column=0,sticky=E)

#TopListbox text label
#l11= Label(m_frame,text = 'view',bg='#e5e5e5')
#l11.grid(row=5,column=0,sticky=W)

#room labels
lb1= Label(l_bframe,text='Block')
lb1.grid(row=0, column=0, sticky=E)

lb2= Label(l_bframe,text='ApartmentType')
lb2.grid(row=1, column=0, sticky=E)

lb3= Label(l_bframe,text='ApartmentNumber')
lb3.grid(row=2, column=0, sticky=E)

lb4= Label(l_bframe,text='Room Status')
lb4.grid(row=3, column=0, sticky=E)

#Notification labels
#n0 = Label(nb_frame,width=1,bg='#e5e5e5')
#n0.grid(row=2,column=0,padx=4,sticky=W)

n1 = Label(nb_frame,width=1,bg='green')
n1.grid(row=3,column=0,padx=4,sticky=W)
nt1 = Label(nb_frame,text='Vacant/Available',width=13,anchor='w',bg='#e5e5e5')
nt1.grid(row=3,column=1,columnspan=2,padx=4,pady=3,sticky=W)

n2 = Label(nb_frame,width=1,bg='red')
n2.grid(row=4,column=0,padx=4,pady=3,sticky=W)
nt2 = Label(nb_frame,text='Occupied',width=13,anchor='w',bg='#e5e5e5')
nt2.grid(row=4,column=1,padx=4,pady=3,sticky=W)

n3 = Label(nb_frame,width=1,bg='orange')
n3.grid(row=5,column=0,padx=4,pady=3,sticky=W)
nt3 = Label(nb_frame,text='Rent Due',width=13,anchor='w',bg='#e5e5e5')
nt3.grid(row=5,column=1,padx=4,pady=3,sticky=W)

#admin labels
s1 = Label(s_frame,width=13,text='Current Tenants: ')
s1.grid(row=0,column=0)
se = Label(s_frame,width=17,anchor=W,bg='white',relief='solid',bd=1,text=db_length())
se.grid(row=0,column=1,padx=20,sticky=E)

#time and top labels
tlabel = Label(top_frame1,font='ariel 10',bg='#e3e3e3',fg='green',anchor='s')
tlabel.grid(row=0,column=3,sticky=S)

ulabel = Label(top_frame1,text='Username: ',bg='#e3e3e3',anchor='s')
ulabel.grid(row=0,column=1,sticky=S)

ulabel2 = Label(top_frame1,text='UserID: ',bg='#e3e3e3',anchor='nw')
ulabel2.grid(row=0,column=1,sticky=N+W)


#def clicked_(event): 
#an event binding for when the a1 aprt one button is clicked
#    #a1_a1b.focus_force
#    a1_a1b['state']='active'

        
    


#notifier widgets labels for ALL BLOCKS
#---------------------------------- BLOCK A ----------------------------------#

ac_frame0=LabelFrame(w_frame1,padx=4,pady=4)
ac_frame0.grid(row=0,column=0,sticky=W+E)
a1_a1 = Label(ac_frame0,text='A1',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
a1_a1.grid(row=0,column=0)
a1_a1b = Button(ac_frame0,text='Apt1',height=1,bd=0,command=modals.a1a1)
a1_a1b.grid(row=0,column=1)
#a1_a1b.bind('<1>', clicked_)
#print(dir(a1_a1b))

ac_frame1=LabelFrame(w_frame1,padx=4,pady=4)
ac_frame1.grid(row=0,column=1,sticky=W+E)
a1_a2= Label(ac_frame1,text='A1',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
a1_a2.grid(row=0,column=0)
a1_a2b= Button(ac_frame1,text='Apt2',height=1,bd=0,command=modals.a1a2)
a1_a2b.grid(row=0,column=1)

ac_frame2=LabelFrame(w_frame1,padx=4,pady=4)
ac_frame2.grid(row=0,column=2,sticky=W+E)
a1_a3= Label(ac_frame2,text='A1',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
a1_a3.grid(row=0,column=0)
a1_a3b= Button(ac_frame2,text='Apt3',height=1,bd=0)
a1_a3b.grid(row=0,column=1)

ac_frame3=LabelFrame(w_frame1,padx=4,pady=4)
ac_frame3.grid(row=0,column=3,sticky=W+E)
a1_a4= Label(ac_frame3,text='A1',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
a1_a4.grid(row=0,column=0)
a1_a4b= Button(ac_frame3,text='Apt4',height=1,bd=0)
a1_a4b.grid(row=0,column=1)

ac_frame4=LabelFrame(w_frame1,padx=4,pady=4)
ac_frame4.grid(row=0,column=4,sticky=W+E)
a2_a1= Label(ac_frame4,text='A2',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
a2_a1.grid(row=0,column=0)
a2_a1b= Button(ac_frame4,text='Apt1',height=1,bd=0)
a2_a1b.grid(row=0,column=1)

ac_frame5=LabelFrame(w_frame1,padx=4,pady=4)
ac_frame5.grid(row=0,column=5,sticky=W+E)
a2_a2= Label(ac_frame5,text='A2',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
a2_a2.grid(row=0,column=0)
a2_a2b= Button(ac_frame5,text='Apt2',height=1,bd=0)
a2_a2b.grid(row=0,column=1)

ac_frame6=LabelFrame(w_frame1,padx=4,pady=4)
ac_frame6.grid(row=0,column=6,sticky=W+E)
a2_a3= Label(ac_frame6,text='A2',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
a2_a3.grid(row=0,column=0)
a2_a3b= Button(ac_frame6,text='Apt3',height=1,bd=0)
a2_a3b.grid(row=0,column=1)

ac_frame7=LabelFrame(w_frame1,padx=4,pady=4)
ac_frame7.grid(row=0,column=7,sticky=W+E)
a2_a4= Label(ac_frame7,text='A2',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
a2_a4.grid(row=0,column=0)
a2_a4b= Button(ac_frame7,text='Apt4',height=1,bd=0)
a2_a4b.grid(row=0,column=1)

#================================== A second row ==================================#
ac_frame8=LabelFrame(w_frame1,padx=4,pady=4)
ac_frame8.grid(row=0,column=8)
a3_a1= Label(ac_frame8,text='A3',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
a3_a1.grid(row=0,column=0)
a3_a1b= Button(ac_frame8,text='Apt1',height=1,bd=0)
a3_a1b.grid(row=0,column=1)

ac_frame9=LabelFrame(w_frame1,padx=4,pady=4)
ac_frame9.grid(row=0,column=9)
a3_a2= Label(ac_frame9,text='A3',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
a3_a2.grid(row=0,column=0)
a3_a2b= Button(ac_frame9,text='Apt2',height=1,bd=0)
a3_a2b.grid(row=0,column=1)

ac_frame10=LabelFrame(w_frame1,padx=4,pady=4)
ac_frame10.grid(row=1,column=0)
a3_a3= Label(ac_frame10,text='A3',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
a3_a3.grid(row=0,column=0)
a3_a3b= Button(ac_frame10,text='Apt3',height=1,bd=0)
a3_a3b.grid(row=0,column=1)

ac_frame11=LabelFrame(w_frame1,padx=4,pady=4)
ac_frame11.grid(row=1,column=1)
a3_a4= Label(ac_frame11,text='A3',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
a3_a4.grid(row=0,column=0)
a3_a4b= Button(ac_frame11,text='Apt4',height=1,bd=0)
a3_a4b.grid(row=0,column=1)

ac_frame12=LabelFrame(w_frame1,padx=4,pady=4)
ac_frame12.grid(row=1,column=2)
a4_a1= Label(ac_frame12,text='A4',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
a4_a1.grid(row=0,column=0)
a4_a1b= Button(ac_frame12,text='Apt1',height=1,bd=0)
a4_a1b.grid(row=0,column=1)

ac_frame13=LabelFrame(w_frame1,padx=4,pady=4)
ac_frame13.grid(row=1,column=3)
a4_a2= Label(ac_frame13,text='A4',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
a4_a2.grid(row=0,column=0)
a4_a2b= Button(ac_frame13,text='Apt2',height=1,bd=0)
a4_a2b.grid(row=0,column=1)

ac_frame14=LabelFrame(w_frame1,padx=4,pady=4)
ac_frame14.grid(row=1,column=4)
a4_a3= Label(ac_frame14,text='A4',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
a4_a3.grid(row=0,column=0)
a4_a3b= Button(ac_frame14,text='Apt3',height=1,bd=0)
a4_a3b.grid(row=0,column=1)

ac_frame15=LabelFrame(w_frame1,padx=4,pady=4)
ac_frame15.grid(row=1,column=5)
a4_a4= Label(ac_frame15,text='A4',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
a4_a4.grid(row=0,column=0)
a4_a4b= Button(ac_frame15,text='Apt4',height=1,bd=0)
a4_a4b.grid(row=0,column=1)

#---------------------------------- BLOCK B ----------------------------------#

bc_frame0=LabelFrame(w_frame1,padx=4,pady=4)
bc_frame0.grid(row=1,column=6)
b1_a1 = Label(bc_frame0,text='B1',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
b1_a1.grid(row=0,column=0)
b1_a1b = Button(bc_frame0,text='Apt1',height=1,bd=0)
b1_a1b.grid(row=0,column=1)

bc_frame1=LabelFrame(w_frame1,padx=4,pady=4)
bc_frame1.grid(row=1,column=7)
b1_a2= Label(bc_frame1,text='B1',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
b1_a2.grid(row=0,column=0)
b1_a2b= Button(bc_frame1,text='Apt2',height=1,bd=0)
b1_a2b.grid(row=0,column=1)

bc_frame2=LabelFrame(w_frame1,padx=4,pady=4)
bc_frame2.grid(row=1,column=8)
b1_a3= Label(bc_frame2,text='B1',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
b1_a3.grid(row=0,column=0)
b1_a3b= Button(bc_frame2,text='Apt3',height=1,bd=0)
b1_a3b.grid(row=0,column=1)

bc_frame3=LabelFrame(w_frame1,padx=4,pady=4)
bc_frame3.grid(row=1,column=9)
b1_a4= Label(bc_frame3,text='B1',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
b1_a4.grid(row=0,column=0)
b1_a4b= Button(bc_frame3,text='Apt4',height=1,bd=0)
b1_a4b.grid(row=0,column=1)
#-------
bc_frame4=LabelFrame(w_frame2,padx=4,pady=4)
bc_frame4.grid(row=0,column=0)
b2_a1= Label(bc_frame4,text='B2',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
b2_a1.grid(row=0,column=0)
b2_a1b= Button(bc_frame4,text='Apt1',height=1,bd=0)
b2_a1b.grid(row=0,column=1)

bc_frame5=LabelFrame(w_frame2,padx=4,pady=4)
bc_frame5.grid(row=0,column=1)
b2_a2= Label(bc_frame5,text='B2',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
b2_a2.grid(row=0,column=0)
b2_a2b= Button(bc_frame5,text='Apt2',height=1,bd=0)
b2_a2b.grid(row=0,column=1)

bc_frame6=LabelFrame(w_frame2,padx=4,pady=4)
bc_frame6.grid(row=0,column=2)
b2_a3= Label(bc_frame6,text='B2',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
b2_a3.grid(row=0,column=0)
b2_a3b= Button(bc_frame6,text='Apt3',height=1,bd=0)
b2_a3b.grid(row=0,column=1)

bc_frame7=LabelFrame(w_frame2,padx=4,pady=4)
bc_frame7.grid(row=0,column=3)
b2_a4= Label(bc_frame7,text='B2',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
b2_a4.grid(row=0,column=0)
b2_a4b= Button(bc_frame7,text='Apt4',height=1,bd=0)
b2_a4b.grid(row=0,column=1)

#================================== B second row ==================================#
bc_frame8=LabelFrame(w_frame2,padx=4,pady=4)
bc_frame8.grid(row=0,column=4)
b3_a1= Label(bc_frame8,text='B3',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
b3_a1.grid(row=0,column=0)
b3_a1b= Button(bc_frame8,text='Apt1',height=1,bd=0)
b3_a1b.grid(row=0,column=1)

bc_frame9=LabelFrame(w_frame2,padx=4,pady=4)
bc_frame9.grid(row=0,column=5)
b3_a2= Label(bc_frame9,text='B3',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
b3_a2.grid(row=0,column=0)
b3_a2b= Button(bc_frame9,text='Apt2',height=1,bd=0)
b3_a2b.grid(row=0,column=1)

bc_frame10=LabelFrame(w_frame2,padx=4,pady=4)
bc_frame10.grid(row=0,column=6)
b3_a3= Label(bc_frame10,text='B3',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
b3_a3.grid(row=0,column=0)
b3_a3b= Button(bc_frame10,text='Apt3',height=1,bd=0)
b3_a3b.grid(row=0,column=1)

bc_frame11=LabelFrame(w_frame2,padx=4,pady=4)
bc_frame11.grid(row=0,column=7)
b3_a4= Label(bc_frame11,text='B3',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
b3_a4.grid(row=0,column=0)
b3_a4b= Button(bc_frame11,text='Apt4',height=1,bd=0)
b3_a4b.grid(row=0,column=1)

bc_frame12=LabelFrame(w_frame2,padx=4,pady=4)
bc_frame12.grid(row=0,column=8)
b4_a1= Label(bc_frame12,text='B4',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
b4_a1.grid(row=0,column=0)
b4_a1b= Button(bc_frame12,text='Apt1',height=1,bd=0)
b4_a1b.grid(row=0,column=1)

bc_frame13=LabelFrame(w_frame2,padx=4,pady=4)
bc_frame13.grid(row=0,column=9)
b4_a2= Label(bc_frame13,text='B4',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
b4_a2.grid(row=0,column=0)
b4_a2b= Button(bc_frame13,text='Apt2',height=1,bd=0)
b4_a2b.grid(row=0,column=1)

bc_frame14=LabelFrame(w_frame2,padx=4,pady=4)
bc_frame14.grid(row=1,column=0)
b4_a3= Label(bc_frame14,text='B4',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
b4_a3.grid(row=0,column=0)
b4_a3b= Button(bc_frame14,text='Apt3',height=1,bd=0)
b4_a3b.grid(row=0,column=1)

bc_frame15=LabelFrame(w_frame2,padx=4,pady=4)
bc_frame15.grid(row=1,column=1)
b4_a4= Label(bc_frame15,text='B4',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
b4_a4.grid(row=0,column=0)
b4_a4b= Button(bc_frame15,text='Apt4',height=1,bd=0)
b4_a4b.grid(row=0,column=1)

#---------------------------------- BLOCK C ----------------------------------#

cc_frame0=LabelFrame(w_frame2,padx=4,pady=4)
cc_frame0.grid(row=1,column=2)
c1_a1= Label(cc_frame0,text='C1',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
c1_a1.grid(row=0,column=0)
c1_a1b= Button(cc_frame0,text='Apt1',height=1,bd=0)
c1_a1b.grid(row=0,column=1)

cc_frame1=LabelFrame(w_frame2,padx=4,pady=4)
cc_frame1.grid(row=1,column=3)
c1_a2= Label(cc_frame1,text='C1',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
c1_a2.grid(row=0,column=0)
c1_a2b= Button(cc_frame1,text='Apt2',height=1,bd=0)
c1_a2b.grid(row=0,column=1)

cc_frame2=LabelFrame(w_frame2,padx=4,pady=4)
cc_frame2.grid(row=1,column=4)
c1_a3= Label(cc_frame2,text='C1',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
c1_a3.grid(row=0,column=0)
c1_a3b= Button(cc_frame2,text='Apt3',height=1,bd=0)
c1_a3b.grid(row=0,column=1)

cc_frame3=LabelFrame(w_frame2,padx=4,pady=4)
cc_frame3.grid(row=1,column=5)
c1_a4= Label(cc_frame3,text='C1',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
c1_a4.grid(row=0,column=0)
c1_a4b= Button(cc_frame3,text='Apt4',height=1,bd=0)
c1_a4b.grid(row=0,column=1)

cc_frame4=LabelFrame(w_frame2,padx=4,pady=4)
cc_frame4.grid(row=1,column=6)
c2_a1= Label(cc_frame4,text='C2',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
c2_a1.grid(row=0,column=0)
c2_a1b= Button(cc_frame4,text='Apt1',height=1,bd=0)
c2_a1b.grid(row=0,column=1)

cc_frame5=LabelFrame(w_frame2,padx=4,pady=4)
cc_frame5.grid(row=1,column=7)
c2_a2= Label(cc_frame5,text='C2',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
c2_a2.grid(row=0,column=0)
c2_a2b= Button(cc_frame5,text='Apt2',height=1,bd=0)
c2_a2b.grid(row=0,column=1)

cc_frame6=LabelFrame(w_frame2,padx=4,pady=4)
cc_frame6.grid(row=1,column=8)
c2_a3= Label(cc_frame6,text='C2',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
c2_a3.grid(row=0,column=0)
c2_a3b= Button(cc_frame6,text='Apt3',height=1,bd=0)
c2_a3b.grid(row=0,column=1)

cc_frame7=LabelFrame(w_frame2,padx=4,pady=4)
cc_frame7.grid(row=1,column=9)
c2_a4= Label(cc_frame7,text='C2',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
c2_a4.grid(row=0,column=0)
c2_a4b= Button(cc_frame7,text='Apt4',height=1,bd=0)
c2_a4b.grid(row=0,column=1)

#================================== C second row =====================================#
cc_frame8=LabelFrame(w_frame3,padx=4,pady=4)
cc_frame8.grid(row=0,column=0)
c3_a1= Label(cc_frame8,text='C3',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
c3_a1.grid(row=0,column=0)
c3_a1b= Button(cc_frame8,text='Apt1',height=1,bd=0)
c3_a1b.grid(row=0,column=1)

cc_frame9=LabelFrame(w_frame3,padx=4,pady=4)
cc_frame9.grid(row=0,column=1)
c3_a2= Label(cc_frame9,text='C3',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
c3_a2.grid(row=0,column=0)
c3_a2b= Button(cc_frame9,text='Apt2',height=1,bd=0)
c3_a2b.grid(row=0,column=1)

cc_frame10=LabelFrame(w_frame3,padx=4,pady=4)
cc_frame10.grid(row=0,column=2)
c3_a3= Label(cc_frame10,text='C3',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
c3_a3.grid(row=0,column=0)
c3_a3b= Button(cc_frame10,text='Apt3',height=1,bd=0)
c3_a3b.grid(row=0,column=1)

cc_frame11=LabelFrame(w_frame3,padx=4,pady=4)
cc_frame11.grid(row=0,column=3)
c3_a4= Label(cc_frame11,text='C3',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
c3_a4.grid(row=0,column=0)
c3_a4b= Button(cc_frame11,text='Apt4',height=1,bd=0)
c3_a4b.grid(row=0,column=1)

cc_frame12=LabelFrame(w_frame3,padx=4,pady=4)
cc_frame12.grid(row=0,column=4)
c4_a1= Label(cc_frame12,text='C4',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
c4_a1.grid(row=0,column=0)
c4_a1b= Button(cc_frame12,text='Apt1',height=1,bd=0)
c4_a1b.grid(row=0,column=1)

cc_frame13=LabelFrame(w_frame3,padx=4,pady=4)
cc_frame13.grid(row=0,column=5)
c4_a2= Label(cc_frame13,text='C4',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
c4_a2.grid(row=0,column=0)
c4_a2b= Button(cc_frame13,text='Apt2',height=1,bd=0)
c4_a2b.grid(row=0,column=1)

cc_frame14=LabelFrame(w_frame3,padx=4,pady=4)
cc_frame14.grid(row=0,column=6)
c4_a3= Label(cc_frame14,text='C4',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
c4_a3.grid(row=0,column=0)
c4_a3b= Button(cc_frame14,text='Apt3',height=1,bd=0)
c4_a3b.grid(row=0,column=1)

cc_frame15=LabelFrame(w_frame3,padx=4,pady=4)
cc_frame15.grid(row=0,column=7)
c4_a4= Label(cc_frame15,text='C4',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
c4_a4.grid(row=0,column=0)
c4_a4b= Button(cc_frame15,text='Apt4',height=1,bd=0)
c4_a4b.grid(row=0,column=1)

#---------------------------------- BLOCK D ----------------------------------#

dc_frame0=LabelFrame(w_frame3,padx=4,pady=4)
dc_frame0.grid(row=0,column=8)
d1_a1= Label(dc_frame0,text='D1',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
d1_a1.grid(row=0,column=0)
d1_a1b= Button(dc_frame0,text='Apt1',height=1,bd=0)
d1_a1b.grid(row=0,column=1)

dc_frame1=LabelFrame(w_frame3,padx=4,pady=4)
dc_frame1.grid(row=0,column=9)
d1_a2= Label(dc_frame1,text='D1',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
d1_a2.grid(row=0,column=0)
d1_a2b= Button(dc_frame1,text='Apt2',height=1,bd=0)
d1_a2b.grid(row=0,column=1)

dc_frame2=LabelFrame(w_frame3,padx=4,pady=4)
dc_frame2.grid(row=1,column=0)
d1_a3= Label(dc_frame2,text='D1',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
d1_a3.grid(row=0,column=0)
d1_a3b= Button(dc_frame2,text='Apt3',height=1,bd=0)
d1_a3b.grid(row=0,column=1)

dc_frame3=LabelFrame(w_frame3,padx=4,pady=4)
dc_frame3.grid(row=1,column=1)
d1_a4= Label(dc_frame3,text='D1',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
d1_a4.grid(row=0,column=0)
d1_a4b= Button(dc_frame3,text='Apt4',height=1,bd=0)
d1_a4b.grid(row=0,column=1)

dc_frame4=LabelFrame(w_frame3,padx=4,pady=4)
dc_frame4.grid(row=1,column=2)
d2_a1= Label(dc_frame4,text='D2',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
d2_a1.grid(row=0,column=0)
d2_a1b= Button(dc_frame4,text='Apt1',height=1,bd=0)
d2_a1b.grid(row=0,column=1)

dc_frame5=LabelFrame(w_frame3,padx=4,pady=4)
dc_frame5.grid(row=1,column=3)
d2_a2= Label(dc_frame5,text='D2',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
d2_a2.grid(row=0,column=0)
d2_a2b= Button(dc_frame5,text='Apt2',height=1,bd=0)
d2_a2b.grid(row=0,column=1)

dc_frame6=LabelFrame(w_frame3,padx=4,pady=4)
dc_frame6.grid(row=1,column=4)
d2_a3= Label(dc_frame6,text='D2',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
d2_a3.grid(row=0,column=0)
d2_a3b= Button(dc_frame6,text='Apt3',height=1,bd=0)
d2_a3b.grid(row=0,column=1)

dc_frame7=LabelFrame(w_frame3,padx=4,pady=4)
dc_frame7.grid(row=1,column=5)
d2_a4= Label(dc_frame7,text='D2',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
d2_a4.grid(row=0,column=0)
d2_a4b= Button(dc_frame7,text='Apt4',height=1,bd=0)
d2_a4b.grid(row=0,column=1)

#================================== D second row =====================================#
dc_frame8=LabelFrame(w_frame3,padx=4,pady=4)
dc_frame8.grid(row=1,column=6)
d3_a1= Label(dc_frame8,text='D3',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
d3_a1.grid(row=0,column=0)
d3_a1b= Button(dc_frame8,text='Apt1',height=1,bd=0)
d3_a1b.grid(row=0,column=1)

dc_frame9=LabelFrame(w_frame3,padx=4,pady=4)
dc_frame9.grid(row=1,column=7)
d3_a2= Label(dc_frame9,text='D3',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
d3_a2.grid(row=0,column=0)
d3_a2b= Button(dc_frame9,text='Apt2',height=1,bd=0)
d3_a2b.grid(row=0,column=1)

dc_frame10=LabelFrame(w_frame3,padx=4,pady=4)
dc_frame10.grid(row=1,column=8)
d3_a3= Label(dc_frame10,text='D3',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
d3_a3.grid(row=0,column=0)
d3_a3b= Button(dc_frame10,text='Apt3',height=1,bd=0)
d3_a3b.grid(row=0,column=1)

dc_frame11=LabelFrame(w_frame3,padx=4,pady=4)
dc_frame11.grid(row=1,column=9)
d3_a4= Label(dc_frame11,text='D3',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
d3_a4.grid(row=0,column=0)
d3_a4b= Button(dc_frame11,text='Apt4',height=1,bd=0)
d3_a4b.grid(row=0,column=1)
#--------
dc_frame12=LabelFrame(w_frame4,padx=4,pady=4)
dc_frame12.grid(row=0,column=0)
d4_a1= Label(dc_frame12,text='D4',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
d4_a1.grid(row=0,column=0)
d4_a1b= Button(dc_frame12,text='Apt1',height=1,bd=0)
d4_a1b.grid(row=0,column=1)

dc_frame13=LabelFrame(w_frame4,padx=4,pady=4)
dc_frame13.grid(row=0,column=1)
d4_a2= Label(dc_frame13,text='D4',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
d4_a2.grid(row=0,column=0)
d4_a2b= Button(dc_frame13,text='Apt2',height=1,bd=0)
d4_a2b.grid(row=0,column=1)

dc_frame14=LabelFrame(w_frame4,padx=4,pady=4)
dc_frame14.grid(row=0,column=2)
d4_a3= Label(dc_frame14,text='D4',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
d4_a3.grid(row=0,column=0)
d4_a3b= Button(dc_frame14,text='Apt3',height=1,bd=0)
d4_a3b.grid(row=0,column=1)

dc_frame15=LabelFrame(w_frame4,padx=4,pady=4)
dc_frame15.grid(row=0,column=3)
d4_a4= Label(dc_frame15,text='D4',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
d4_a4.grid(row=0,column=0)
d4_a4b= Button(dc_frame15,text='Apt4',height=1,bd=0)
d4_a4b.grid(row=0,column=1)

#---------------------------------- BLOCK E ----------------------------------#

ec_frame0=LabelFrame(w_frame4,padx=4,pady=4)
ec_frame0.grid(row=0,column=4)
e1_a1= Label(ec_frame0,text='E1',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
e1_a1.grid(row=0,column=0)
e1_a1b= Button(ec_frame0,text='Apt1',height=1,bd=0)
e1_a1b.grid(row=0,column=1)

ec_frame1=LabelFrame(w_frame4,padx=4,pady=4)
ec_frame1.grid(row=0,column=5)
e1_a2= Label(ec_frame1,text='E1',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
e1_a2.grid(row=0,column=0)
e1_a2b= Button(ec_frame1,text='Apt2',height=1,bd=0)
e1_a2b.grid(row=0,column=1)

ec_frame2=LabelFrame(w_frame4,padx=4,pady=4)
ec_frame2.grid(row=0,column=6)
e1_a3= Label(ec_frame2,text='E1',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
e1_a3.grid(row=0,column=0)
e1_a3b= Button(ec_frame2,text='Apt3',height=1,bd=0)
e1_a3b.grid(row=0,column=1)

ec_frame3=LabelFrame(w_frame4,padx=4,pady=4)
ec_frame3.grid(row=0,column=7)
e1_a4= Label(ec_frame3,text='E1',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
e1_a4.grid(row=0,column=0)
e1_a4b= Button(ec_frame3,text='Apt4',height=1,bd=0)
e1_a4b.grid(row=0,column=1)

ec_frame4=LabelFrame(w_frame4,padx=4,pady=4)
ec_frame4.grid(row=0,column=8)
e2_a1= Label(ec_frame4,text='E2',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
e2_a1.grid(row=0,column=0)
e2_a1b= Button(ec_frame4,text='Apt1',height=1,bd=0)
e2_a1b.grid(row=0,column=1)

ec_frame5=LabelFrame(w_frame4,padx=4,pady=4)
ec_frame5.grid(row=0,column=9)
e2_a2= Label(ec_frame5,text='E2',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
e2_a2.grid(row=0,column=0)
e2_a2b= Button(ec_frame5,text='Apt2',height=1,bd=0)
e2_a2b.grid(row=0,column=1)
#-------
ec_frame6=LabelFrame(w_frame4,padx=4,pady=4)
ec_frame6.grid(row=1,column=0)
e2_a3= Label(ec_frame6,text='E2',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
e2_a3.grid(row=0,column=0)
e2_a3b= Button(ec_frame6,text='Apt3',height=1,bd=0)
e2_a3b.grid(row=0,column=1)

ec_frame7=LabelFrame(w_frame4,padx=4,pady=4)
ec_frame7.grid(row=1,column=1)
e2_a4= Label(ec_frame7,text='E2',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
e2_a4.grid(row=0,column=0)
e2_a4b= Button(ec_frame7,text='Apt4',height=1,bd=0)
e2_a4b.grid(row=0,column=1)

#================================== E second row =====================================#
ec_frame8=LabelFrame(w_frame4,padx=4,pady=4)
ec_frame8.grid(row=1,column=2)
e3_a1= Label(ec_frame8,text='E3',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
e3_a1.grid(row=0,column=0)
e3_a1b= Button(ec_frame8,text='Apt1',height=1,bd=0)
e3_a1b.grid(row=0,column=1)

ec_frame9=LabelFrame(w_frame4,padx=4,pady=4)
ec_frame9.grid(row=1,column=3)
e3_a2= Label(ec_frame9,text='E3',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
e3_a2.grid(row=0,column=0)
e3_a2b= Button(ec_frame9,text='Apt2',height=1,bd=0)
e3_a2b.grid(row=0,column=1)

ec_frame10=LabelFrame(w_frame4,padx=4,pady=4)
ec_frame10.grid(row=1,column=4)
e3_a3= Label(ec_frame10,text='E3',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
e3_a3.grid(row=0,column=0)
e3_a3b= Button(ec_frame10,text='Apt3',height=1,bd=0)
e3_a3b.grid(row=0,column=1)

ec_frame11=LabelFrame(w_frame4,padx=4,pady=4)
ec_frame11.grid(row=1,column=5)
e3_a4= Label(ec_frame11,text='E3',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
e3_a4.grid(row=0,column=0)
e3_a4b= Button(ec_frame11,text='Apt4',height=1,bd=0)
e3_a4b.grid(row=0,column=1)

ec_frame12=LabelFrame(w_frame4,padx=4,pady=4)
ec_frame12.grid(row=1,column=6)
e4_a1= Label(ec_frame12,text='E4',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
e4_a1.grid(row=0,column=0)
e4_a1b= Button(ec_frame12,text='Apt1',height=1,bd=0)
e4_a1b.grid(row=0,column=1)

ec_frame13=LabelFrame(w_frame4,padx=4,pady=4)
ec_frame13.grid(row=1,column=7)
e4_a2= Label(ec_frame13,text='E4',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
e4_a2.grid(row=0,column=0)
e4_a2b= Button(ec_frame13,text='Apt2',height=1,bd=0)
e4_a2b.grid(row=0,column=1)

ec_frame14=LabelFrame(w_frame4,padx=4,pady=4)
ec_frame14.grid(row=1,column=8)
e4_a3= Label(ec_frame14,text='E4',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
e4_a3.grid(row=0,column=0)
e4_a3b= Button(ec_frame14,text='Apt3',height=1,bd=0)
e4_a3b.grid(row=0,column=1)

ec_frame15=LabelFrame(w_frame4,padx=4,pady=4)
ec_frame15.grid(row=1,column=9)
e4_a4= Label(ec_frame15,text='E4',bg='green',width=7,height=2,relief = 'groove',bd=1,fg='white')
e4_a4.grid(row=0,column=0)
e4_a4b= Button(ec_frame15,text='Apt4',height=1,bd=0)
e4_a4b.grid(row=0,column=1)

#widget functions
def indicator():
#---------------------A1---------------------#
    
    try:
        if A1[0].__contains__('A1' and '(1)'):
            a1_a1.configure(bg='red')
            if A1[0].__contains__('1 month') or A1[0].__contains__('week(s)') \
            or A1[0].__contains__('day(s)'):
                a1_a1.configure(bg='orange')
        else:
            a1_a1.configure(bg='green')
        if A1[0].__contains__('A1' and '(2)'):
            a1_a2.configure(bg='red')
            if A1[0].__contains__('1 month') or A1[0].__contains__('week(s)') \
            or A1[0].__contains__('day(s)'):
                a1_a2.configure(bg='orange')
        else:
            a1_a2.configure(bg='green')
        if A1[0].__contains__('A1' and '(3)'):
            a1_a3.configure(bg='red')
            if A1[0].__contains__('1 month') or A1[0].__contains__('week(s)') \
            or A1[0].__contains__('day(s)'):
                a1_a3.configure(bg='orange')
        else:
            a1_a3.configure(bg='green')
        if A1[0].__contains__('A1' and '(4)'):
            a1_a4.configure(bg='red')
            if A1[0].__contains__('1 month') or A1[0].__contains__('week(s)') \
            or A1[0].__contains__('day(s)'):
                a1_a4.configure(bg='orange')
        else:
            a1_a4.configure(bg='green')
    except IndexError:
        pass
        
    try:
        if A1[1].__contains__('A1' and '(2)'):
            a1_a2.configure(bg='red')
            if A1[1].__contains__('1 month') or A1[1].__contains__('week(s)') \
            or A1[1].__contains__('day(s)'):
                a1_a2.configure(bg='orange')
        elif A1[1].__contains__('A1' and '(3)'):
            a1_a3.configure(bg='red')
            if A1[1].__contains__('1 month') or A1[1].__contains__('week(s)') \
            or A1[1].__contains__('day(s)'):
                a1_a3.configure(bg='orange')
        elif A1[1].__contains__('A1' and '(4)'):
            a1_a4.configure(bg='red')
            if A1[1].__contains__('1 month') or A1[1].__contains__('week(s)') \
            or A1[1].__contains__('day(s)'):
                a1_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if A1[2].__contains__('A1' and '(3)'):
            a1_a3.configure(bg='red')
            if A1[2].__contains__('1 month') or A1[2].__contains__('week(s)') \
            or A1[2].__contains__('day(s)'):
                a1_a3.configure(bg='orange')
        elif A1[2].__contains__('A1' and '(4)'):
            a1_a4.configure(bg='red')
            if A1[2].__contains__('1 month') or A1[2].__contains__('week(s)') \
            or A1[2].__contains__('day(s)'):
                a1_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if A1[3].__contains__('A1' and '(4)'):
            a1_a4.configure(bg='red')
            if A1[3].__contains__('1 month') or A1[3].__contains__('week(s)') \
            or A1[3].__contains__('day(s)'):
                a1_a4.configure(bg='orange')
    except IndexError:
        pass
        
#---------------------A2---------------------#
    
    try:
        if A2[0].__contains__('A2' and '(1)'):
            a2_a1.configure(bg='red')
            if A2[0].__contains__('1 month') or A2[0].__contains__('week(s)') \
            or A2[0].__contains__('day(s)'):
                a2_a1.configure(bg='orange')
        else:
            a2_a1.configure(bg='green')
        if A2[0].__contains__('A2' and '(2)'):
            a2_a2.configure(bg='red')
            if A2[0].__contains__('1 month') or A2[0].__contains__('week(s)') \
            or A2[0].__contains__('day(s)'):
                a2_a2.configure(bg='orange')
        else:
            a2_a2.configure(bg='green')
        if A2[0].__contains__('A2' and '(3)'):
            a2_a3.configure(bg='red')
            if A2[0].__contains__('1 month') or A2[0].__contains__('week(s)') \
            or A2[0].__contains__('day(s)'):
                a2_a3.configure(bg='orange')
        else:
            a2_a3.configure(bg='green')
        if A2[0].__contains__('A2' and '(4)'):
            a2_a4.configure(bg='red')
            if A2[0].__contains__('1 month') or A2[0].__contains__('week(s)') \
            or A2[0].__contains__('day(s)'):
                a2_a4.configure(bg='orange')
        else:
            a2_a4.configure(bg='green')
    except IndexError:
        pass
        
    try:
        if A2[1].__contains__('A2' and '(2)'):
            a2_a2.configure(bg='red')
            if A2[1].__contains__('1 month') or A2[1].__contains__('week(s)') \
            or A2[1].__contains__('day(s)'):
                a2_a2.configure(bg='orange')
        elif A2[1].__contains__('A2' and '(3)'):
            a2_a3.configure(bg='red')
            if A2[1].__contains__('1 month') or A2[1].__contains__('week(s)') \
            or A2[1].__contains__('day(s)'):
                a2_a3.configure(bg='orange')
        elif A2[1].__contains__('A2' and '(4)'):
            a2_a4.configure(bg='red')
            if A2[1].__contains__('1 month') or A2[1].__contains__('week(s)') \
            or A2[1].__contains__('day(s)'):
                a2_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if A2[2].__contains__('A2' and '(3)'):
            a2_a3.configure(bg='red')
            if A2[2].__contains__('1 month') or A2[2].__contains__('week(s)') \
            or A2[2].__contains__('day(s)'):
                a2_a3.configure(bg='orange')
        elif A2[2].__contains__('A2' and '(4)'):
            a2_a4.configure(bg='red')
            if A2[2].__contains__('1 month') or A2[2].__contains__('week(s)') \
            or A2[2].__contains__('day(s)'):
                a2_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if A2[3].__contains__('A2' and '(4)'):
            a2_a4.configure(bg='red')
            if A2[3].__contains__('1 month') or A2[3].__contains__('week(s)') \
            or A2[3].__contains__('day(s)'):
                a2_a4.configure(bg='orange')
    except IndexError:
        pass        
        
#---------------------A3---------------------#
    
    try:
        if A3[0].__contains__('A3' and '(1)'):
            a3_a1.configure(bg='red')
            if A3[0].__contains__('1 month') or A3[0].__contains__('week(s)') \
            or A3[0].__contains__('day(s)'):
                a3_a1.configure(bg='orange')
        else:
            a3_a1.configure(bg='green')
        if A3[0].__contains__('A3' and '(2)'):
            a3_a2.configure(bg='red')
            if A3[0].__contains__('1 month') or A3[0].__contains__('week(s)') \
            or A3[0].__contains__('day(s)'):
                a3_a2.configure(bg='orange')
        else:
            a3_a2.configure(bg='green')
        if A3[0].__contains__('A3' and '(3)'):
            a3_a3.configure(bg='red')
            if A3[0].__contains__('1 month') or A3[0].__contains__('week(s)') \
            or A3[0].__contains__('day(s)'):
                a3_a3.configure(bg='orange')
        else:
            a3_a3.configure(bg='green')
        if A3[0].__contains__('A3' and '(4)'):
            a3_a4.configure(bg='red')
            if A3[0].__contains__('1 month') or A3[0].__contains__('week(s)') \
            or A3[0].__contains__('day(s)'):
                a3_a4.configure(bg='orange')
        else:
            a3_a4.configure(bg='green')
    except IndexError:
        pass
        
    try:
        if A3[1].__contains__('A3' and '(2)'): 
            a3_a2.configure(bg='red')
            if A3[1].__contains__('1 month') or A3[1].__contains__('week(s)') \
            or A3[1].__contains__('day(s)'):
                a3_a2.configure(bg='orange')
        elif A3[1].__contains__('A3' and '(3)'):
            a3_a3.configure(bg='red')
            if A3[1].__contains__('1 month') or A3[1].__contains__('week(s)') \
            or A3[1].__contains__('day(s)'):
                a3_a3.configure(bg='orange')
        elif A3[1].__contains__('A3' and '(4)'):
            a3_a4.configure(bg='red')
            if A3[1].__contains__('1 month') or A3[1].__contains__('week(s)') \
            or A3[1].__contains__('day(s)'):
                a3_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if A3[2].__contains__('A3' and '(3)'):
            a3_a3.configure(bg='red')
            if A3[2].__contains__('1 month') or A3[2].__contains__('week(s)') \
            or A3[2].__contains__('day(s)'):
                a3_a3.configure(bg='orange')
        elif A3[2].__contains__('A3' and '(4)'):
            a3_a4.configure(bg='red')
            if A3[2].__contains__('1 month') or A3[2].__contains__('week(s)') \
            or A3[2].__contains__('day(s)'): 
                a3_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if A3[3].__contains__('A3' and '(4)'):
            a3_a4.configure(bg='red')
            if A3[3].__contains__('1 month') or A3[3].__contains__('week(s)') \
            or A3[3].__contains__('day(s)'):
                a3_a4.configure(bg='orange')
    except IndexError:
        pass 
        
#---------------------A4---------------------#
    
    try:
        if A4[0].__contains__('A4' and '(1)'):
            a4_a1.configure(bg='red')
            if A4[0].__contains__('1 month') or A4[0].__contains__('week(s)') \
            or A4[0].__contains__('day(s)'):
                a4_a1.configure(bg='orange')
        else:
            a4_a1.configure(bg='green')
        if A4[0].__contains__('A4' and '(2)'):
            a4_a2.configure(bg='red')
            if A4[0].__contains__('1 month') or A4[0].__contains__('week(s)') \
            or A4[0].__contains__('day(s)'):
                a4_a2.configure(bg='orange')
        else:
            a4_a2.configure(bg='green')
        if A4[0].__contains__('A4' and '(3)'):
            a4_a3.configure(bg='red')
            if A4[0].__contains__('1 month') or A4[0].__contains__('week(s)') \
            or A4[0].__contains__('day(s)'):
                a4_a3.configure(bg='orange')
        else:
            a4_a3.configure(bg='green')
        if A4[0].__contains__('A4' and '(4)'):
            a4_a4.configure(bg='red')
            if A4[0].__contains__('1 month') or A4[0].__contains__('week(s)') \
            or A4[0].__contains__('day(s)'):
                a4_a4.configure(bg='orange')
        else:
            a4_a4.configure(bg='green')
    except IndexError:
        pass
        
    try:
        if A4[1].__contains__('A4' and '(2)'):
            a4_a2.configure(bg='red')
            if A4[1].__contains__('1 month') or A4[1].__contains__('week(s)') \
            or A4[1].__contains__('day(s)'):
                a4_a2.configure(bg='orange')
        elif A4[1].__contains__('A4' and '(3)'):
            a4_a3.configure(bg='red')
            if A4[1].__contains__('1 month') or A4[1].__contains__('week(s)') \
            or A4[1].__contains__('day(s)'):
                a4_a3.configure(bg='orange')
        elif A4[1].__contains__('A4' and '(4)'):
            a4_a4.configure(bg='red')
            if A4[1].__contains__('1 month') or A4[1].__contains__('week(s)') \
            or A4[1].__contains__('day(s)'):
                a4_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if A4[2].__contains__('A4' and '(3)'):
            a4_a3.configure(bg='red')
            if A4[2].__contains__('1 month') or A4[2].__contains__('week(s)') \
            or A4[2].__contains__('day(s)'):
                a4_a3.configure(bg='orange')
        elif A4[2].__contains__('A4' and '(4)'):
            a4_a4.configure(bg='red')
            if A4[2].__contains__('1 month') or A4[2].__contains__('week(s)') \
            or A4[2].__contains__('day(s)'):
                a4_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if A4[3].__contains__('A4' and '(4)'):
            a4_a4.configure(bg='red')
            if A4[3].__contains__('1 month') or A4[3].__contains__('week(s)') \
            or A4[3].__contains__('day(s)'):
                a4_a4.configure(bg='orange')
    except IndexError:
        pass 
    
    
#---------------------B1---------------------#
    
    try:
        if B1[0].__contains__('B1' and '(1)'):
            b1_a1.configure(bg='red')
            if B1[0].__contains__('1 month') or B1[0].__contains__('week(s)') \
            or B1[0].__contains__('day(s)'):
                b1_a1.configure(bg='orange')
        else:
            b1_a1.configure(bg='green')
        if B1[0].__contains__('B1' and '(2)'):
            b1_a2.configure(bg='red')
            if B1[0].__contains__('1 month') or B1[0].__contains__('week(s)') \
            or B1[0].__contains__('day(s)'):
                b1_a2.configure(bg='orange')
        else:
            b1_a2.configure(bg='green')
        if B1[0].__contains__('B1' and '(3)'):
            b1_a3.configure(bg='red')
            if B1[0].__contains__('1 month') or B1[0].__contains__('week(s)') \
            or B1[0].__contains__('day(s)'):
                b1_a3.configure(bg='orange')
        else:
            b1_a3.configure(bg='green')
        if B1[0].__contains__('B1' and '(4)'):
            b1_a4.configure(bg='red')
            if B1[0].__contains__('1 month') or B1[0].__contains__('week(s)') \
            or B1[0].__contains__('day(s)'):
                b1_a4.configure(bg='orange')
        else:
            b1_a4.configure(bg='green')
    except IndexError:
        pass
        
    try:
        if B1[1].__contains__('B1' and '(2)'):
            b1_a2.configure(bg='red')
            if B1[1].__contains__('1 month') or B1[1].__contains__('week(s)') \
            or B1[1].__contains__('day(s)'):
                b1_a2.configure(bg='orange')
        elif B1[1].__contains__('B1' and '(3)'):
            b1_a3.configure(bg='red')
            if B1[1].__contains__('1 month') or B1[1].__contains__('week(s)') \
            or B1[1].__contains__('day(s)'):
                b1_a3.configure(bg='orange')
        elif B1[1].__contains__('B1' and '(4)'):
            b1_a4.configure(bg='red')
            if B1[1].__contains__('1 month') or B1[1].__contains__('week(s)') \
            or B1[1].__contains__('day(s)'):
                b1_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if B1[2].__contains__('B1' and '(3)'):
            b1_a3.configure(bg='red')
            if B1[2].__contains__('1 month') or B1[2].__contains__('week(s)') \
            or B1[2].__contains__('day(s)'):
                b1_a3.configure(bg='orange')
        elif B1[2].__contains__('B1' and '(4)'):
            b1_a4.configure(bg='red')
            if B1[2].__contains__('1 month') or B1[2].__contains__('week(s)') \
            or B1[2].__contains__('day(s)'):
                b1_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if B1[3].__contains__('B1' and '(4)'):
            b1_a4.configure(bg='red')
            if B1[3].__contains__('1 month') or B1[3].__contains__('week(s)') \
            or B1[3].__contains__('day(s)'):
                b1_a4.configure(bg='orange')
    except IndexError:
        pass
        
#---------------------B2---------------------#
    
    try:
        if B2[0].__contains__('B2' and '(1)'):
            b2_a1.configure(bg='red')
            if B2[0].__contains__('1 month') or B2[0].__contains__('week(s)') \
            or B2[0].__contains__('day(s)'):
                b2_a1.configure(bg='orange')
        else:
            b2_a1.configure(bg='green')
        if B2[0].__contains__('B2' and '(2)'):
            b2_a2.configure(bg='red')
            if B2[0].__contains__('1 month') or B2[0].__contains__('week(s)') \
            or B2[0].__contains__('day(s)'):
                b2_a2.configure(bg='orange')
        else:
            b2_a2.configure(bg='green')
        if B2[0].__contains__('B2' and '(3)'):
            b2_a3.configure(bg='red')
            if B2[0].__contains__('1 month') or B2[0].__contains__('week(s)') \
            or B2[0].__contains__('day(s)'):
                b2_a3.configure(bg='orange')
        else:
            b2_a3.configure(bg='green')
        if B2[0].__contains__('B2' and '(4)'):
            b2_a4.configure(bg='red')
            if B2[0].__contains__('1 month') or B2[0].__contains__('week(s)') \
            or B2[0].__contains__('day(s)'):
                b2_a4.configure(bg='orange')
        else:
            b2_a4.configure(bg='green')
    except IndexError:
        pass
        
    try:
        if B2[1].__contains__('B2' and '(2)'):
            b2_a2.configure(bg='red')
            if B2[1].__contains__('1 month') or B2[1].__contains__('week(s)') \
            or B2[1].__contains__('day(s)'):
                b2_a2.configure(bg='orange')
        elif B2[1].__contains__('B2' and '(3)'):
            b2_a3.configure(bg='red')
            if B2[1].__contains__('1 month') or B2[1].__contains__('week(s)') \
            or B2[1].__contains__('day(s)'):
                b2_a3.configure(bg='orange')
        elif B2[1].__contains__('B2' and '(4)'):
            b2_a4.configure(bg='red')
            if B2[1].__contains__('1 month') or B2[1].__contains__('week(s)') \
            or B2[1].__contains__('day(s)'):
                b2_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if B2[2].__contains__('B2' and '(3)'):
            b2_a3.configure(bg='red')
            if B2[2].__contains__('1 month') or B2[2].__contains__('week(s)') \
            or B2[2].__contains__('day(s)'):
                b2_a3.configure(bg='orange')
        elif B2[2].__contains__('B2' and '(4)'):
            b2_a4.configure(bg='red')
            if B2[2].__contains__('1 month') or B2[2].__contains__('week(s)') \
            or B2[2].__contains__('day(s)'):
                b2_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if B2[3].__contains__('B2' and '(4)'):
            b2_a4.configure(bg='red')
            if B2[3].__contains__('1 month') or B2[3].__contains__('week(s)') \
            or B2[3].__contains__('day(s)'):
                b2_a4.configure(bg='orange')
    except IndexError:
        pass        
        
#---------------------B3---------------------#
    
    try:
        if B3[0].__contains__('B3' and '(1)'):
            b3_a1.configure(bg='red')
            if B3[0].__contains__('1 month') or B3[0].__contains__('week(s)') \
            or B3[0].__contains__('day(s)'):
                b3_a1.configure(bg='orange')
        else:
            b3_a1.configure(bg='green')
        if B3[0].__contains__('B3' and '(2)'):
            b3_a2.configure(bg='red')
            if B3[0].__contains__('1 month') or B3[0].__contains__('week(s)') \
            or B3[0].__contains__('day(s)'):
                b3_a2.configure(bg='orange')
        else:
            b3_a2.configure(bg='green')
        if B3[0].__contains__('B3' and '(3)'):
            b3_a3.configure(bg='red')
            if B3[0].__contains__('1 month') or B3[0].__contains__('week(s)') \
            or B3[0].__contains__('day(s)'):
                b3_a3.configure(bg='orange')
        else:
            b3_a3.configure(bg='green')
        if B3[0].__contains__('B3' and '(4)'):
            b3_a4.configure(bg='red')
            if B3[0].__contains__('1 month') or B3[0].__contains__('week(s)') \
            or B3[0].__contains__('day(s)'):
                b3_a4.configure(bg='orange')
        else:
            b3_a4.configure(bg='green')
    except IndexError:
        pass
        
    try:
        if B3[1].__contains__('B3' and '(2)'): 
            b3_a2.configure(bg='red')
            if B3[1].__contains__('1 month') or B3[1].__contains__('week(s)') \
            or B3[1].__contains__('day(s)'):
                b3_a2.configure(bg='orange')
        elif B3[1].__contains__('B3' and '(3)'):
            b3_a3.configure(bg='red')
            if B3[1].__contains__('1 month') or B3[1].__contains__('week(s)') \
            or B3[1].__contains__('day(s)'):
                b3_a3.configure(bg='orange')
        elif B3[1].__contains__('B3' and '(4)'):
            b3_a4.configure(bg='red')
            if B3[1].__contains__('1 month') or B3[1].__contains__('week(s)') \
            or B3[1].__contains__('day(s)'):
                b3_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if B3[2].__contains__('B3' and '(3)'):
            b3_a3.configure(bg='red')
            if B3[2].__contains__('1 month') or B3[2].__contains__('week(s)') \
            or B3[2].__contains__('day(s)'):
                b3_a3.configure(bg='orange')
        elif B3[2].__contains__('B3' and '(4)'):
            b3_a4.configure(bg='red')
            if B3[2].__contains__('1 month') or B3[2].__contains__('week(s)') \
            or B3[2].__contains__('day(s)'): 
                b3_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if B3[3].__contains__('B3' and '(4)'):
            b3_a4.configure(bg='red')
            if B3[3].__contains__('1 month') or B3[3].__contains__('week(s)') \
            or B3[3].__contains__('day(s)'):
                b3_a4.configure(bg='orange')
    except IndexError:
        pass 
        
#---------------------B4---------------------#
    
    try:
        if B4[0].__contains__('B4' and '(1)'):
            b4_a1.configure(bg='red')
            if B4[0].__contains__('1 month') or B4[0].__contains__('week(s)') \
            or B4[0].__contains__('day(s)'):
                b4_a1.configure(bg='orange')
        else:
            b4_a1.configure(bg='green')
        if B4[0].__contains__('B4' and '(2)'):
            b4_a2.configure(bg='red')
            if B4[0].__contains__('1 month') or B4[0].__contains__('week(s)') \
            or B4[0].__contains__('day(s)'):
                b4_a2.configure(bg='orange')
        else:
            b4_a2.configure(bg='green')
        if B4[0].__contains__('B4' and '(3)'):
            b4_a3.configure(bg='red')
            if B4[0].__contains__('1 month') or B4[0].__contains__('week(s)') \
            or B4[0].__contains__('day(s)'):
                b4_a3.configure(bg='orange')
        else:
            b4_a3.configure(bg='green')
        if B4[0].__contains__('B4' and '(4)'):
            b4_a4.configure(bg='red')
            if B4[0].__contains__('1 month') or B4[0].__contains__('week(s)') \
            or B4[0].__contains__('day(s)'):
                b4_a4.configure(bg='orange')
        else:
            b4_a4.configure(bg='green')
    except IndexError:
        pass
        
    try:
        if B4[1].__contains__('B4' and '(2)'):
            b4_a2.configure(bg='red')
            if B4[1].__contains__('1 month') or B4[1].__contains__('week(s)') \
            or B4[1].__contains__('day(s)'):
                b4_a2.configure(bg='orange')
        elif B4[1].__contains__('B4' and '(3)'):
            b4_a3.configure(bg='red')
            if B4[1].__contains__('1 month') or B4[1].__contains__('week(s)') \
            or B4[1].__contains__('day(s)'):
                b4_a3.configure(bg='orange')
        elif B4[1].__contains__('B4' and '(4)'):
            b4_a4.configure(bg='red')
            if B4[1].__contains__('1 month') or B4[1].__contains__('week(s)') \
            or B4[1].__contains__('day(s)'):
                b4_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if B4[2].__contains__('B4' and '(3)'):
            b4_a3.configure(bg='red')
            if B4[2].__contains__('1 month') or B4[2].__contains__('week(s)') \
            or B4[2].__contains__('day(s)'):
                b4_a3.configure(bg='orange')
        elif B4[2].__contains__('B4' and '(4)'):
            b4_a4.configure(bg='red')
            if B4[2].__contains__('1 month') or B4[2].__contains__('week(s)') \
            or B4[2].__contains__('day(s)'):
                b4_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if B4[3].__contains__('B4' and '(4)'):
            b4_a4.configure(bg='red')
            if B4[3].__contains__('1 month') or B4[3].__contains__('week(s)') \
            or B4[3].__contains__('day(s)'):
                b4_a4.configure(bg='orange')
    except IndexError:
        pass 
        
#---------------------C1---------------------#
    
    try:
        if C1[0].__contains__('C1' and '(1)'):
            c1_a1.configure(bg='red')
            if C1[0].__contains__('1 month') or C1[0].__contains__('week(s)') \
            or C1[0].__contains__('day(s)'):
                c1_a1.configure(bg='orange')
        else:
            c1_a1.configure(bg='green')
        if C1[0].__contains__('C1' and '(2)'):
            c1_a2.configure(bg='red')
            if C1[0].__contains__('1 month') or C1[0].__contains__('week(s)') \
            or C1[0].__contains__('day(s)'):
                c1_a2.configure(bg='orange')
        else:
            c1_a2.configure(bg='green')
        if C1[0].__contains__('C1' and '(3)'):
            c1_a3.configure(bg='red')
            if C1[0].__contains__('1 month') or C1[0].__contains__('week(s)') \
            or C1[0].__contains__('day(s)'):
                c1_a3.configure(bg='orange')
        else:
            c1_a3.configure(bg='green')
        if C1[0].__contains__('C1' and '(4)'):
            c1_a4.configure(bg='red')
            if C1[0].__contains__('1 month') or C1[0].__contains__('week(s)') \
            or C1[0].__contains__('day(s)'):
                c1_a4.configure(bg='orange')
        else:
            c1_a4.configure(bg='green')
    except IndexError:
        pass
        
    try:
        if C1[1].__contains__('C1' and '(2)'):
            c1_a2.configure(bg='red')
            if C1[1].__contains__('1 month') or C1[1].__contains__('week(s)') \
            or C1[1].__contains__('day(s)'):
                c1_a2.configure(bg='orange')
        elif C1[1].__contains__('C1' and '(3)'):
            c1_a3.configure(bg='red')
            if C1[1].__contains__('1 month') or C1[1].__contains__('week(s)') \
            or C1[1].__contains__('day(s)'):
                c1_a3.configure(bg='orange')
        elif C1[1].__contains__('C1' and '(4)'):
            c1_a4.configure(bg='red')
            if C1[1].__contains__('1 month') or C1[1].__contains__('week(s)') \
            or C1[1].__contains__('day(s)'):
                c1_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if C1[2].__contains__('C1' and '(3)'):
            c1_a3.configure(bg='red')
            if C1[2].__contains__('1 month') or C1[2].__contains__('week(s)') \
            or C1[2].__contains__('day(s)'):
                c1_a3.configure(bg='orange')
        elif C1[2].__contains__('C1' and '(4)'):
            c1_a4.configure(bg='red')
            if C1[2].__contains__('1 month') or C1[2].__contains__('week(s)') \
            or C1[2].__contains__('day(s)'):
                c1_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if C1[3].__contains__('C1' and '(4)'):
            c1_a4.configure(bg='red')
            if C1[3].__contains__('1 month') or C1[3].__contains__('week(s)') \
            or C1[3].__contains__('day(s)'):
                c1_a4.configure(bg='orange')
    except IndexError:
        pass
        
#---------------------C2---------------------#
    
    try:
        if C2[0].__contains__('C2' and '(1)'):
            c2_a1.configure(bg='red')
            if C2[0].__contains__('1 month') or C2[0].__contains__('week(s)') \
            or C2[0].__contains__('day(s)'):
                c2_a1.configure(bg='orange')
        else:
            c2_a1.configure(bg='green')
        if C2[0].__contains__('C2' and '(2)'):
            c2_a2.configure(bg='red')
            if C2[0].__contains__('1 month') or C2[0].__contains__('week(s)') \
            or C2[0].__contains__('day(s)'):
                c2_a2.configure(bg='orange')
        else:
            c2_a2.configure(bg='green')
        if C2[0].__contains__('C2' and '(3)'):
            c2_a3.configure(bg='red')
            if C2[0].__contains__('1 month') or C2[0].__contains__('week(s)') \
            or C2[0].__contains__('day(s)'):
                c2_a3.configure(bg='orange')
        else:
            c2_a3.configure(bg='green')
        if C2[0].__contains__('C2' and '(4)'):
            c2_a4.configure(bg='red')
            if C2[0].__contains__('1 month') or C2[0].__contains__('week(s)') \
            or C2[0].__contains__('day(s)'):
                c2_a4.configure(bg='orange')
        else:
            c2_a4.configure(bg='green')
    except IndexError:
        pass
        
    try:
        if C2[1].__contains__('C2' and '(2)'):
            c2_a2.configure(bg='red')
            if C2[1].__contains__('1 month') or C2[1].__contains__('week(s)') \
            or C2[1].__contains__('day(s)'):
                c2_a2.configure(bg='orange')
        elif C2[1].__contains__('C2' and '(3)'):
            c2_a3.configure(bg='red')
            if C2[1].__contains__('1 month') or C2[1].__contains__('week(s)') \
            or C2[1].__contains__('day(s)'):
                c2_a3.configure(bg='orange')
        elif C2[1].__contains__('C2' and '(4)'):
            c2_a4.configure(bg='red')
            if C2[1].__contains__('1 month') or C2[1].__contains__('week(s)') \
            or C2[1].__contains__('day(s)'):
                c2_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if C2[2].__contains__('C2' and '(3)'):
            c2_a3.configure(bg='red')
            if C2[2].__contains__('1 month') or C2[2].__contains__('week(s)') \
            or C2[2].__contains__('day(s)'):
                c2_a3.configure(bg='orange')
        elif C2[2].__contains__('C2' and '(4)'):
            c2_a4.configure(bg='red')
            if C2[2].__contains__('1 month') or C2[2].__contains__('week(s)') \
            or C2[2].__contains__('day(s)'):
                c2_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if C2[3].__contains__('C2' and '(4)'):
            c2_a4.configure(bg='red')
            if C2[3].__contains__('1 month') or C2[3].__contains__('week(s)') \
            or C2[3].__contains__('day(s)'):
                c2_a4.configure(bg='orange')
    except IndexError:
        pass        
        
#---------------------C3---------------------#
    
    try:
        if C3[0].__contains__('C3' and '(1)'):
            c3_a1.configure(bg='red')
            if C3[0].__contains__('1 month') or C3[0].__contains__('week(s)') \
            or C3[0].__contains__('day(s)'):
                c3_a1.configure(bg='orange')
        else:
            c3_a1.configure(bg='green')
        if C3[0].__contains__('C3' and '(2)'):
            c3_a2.configure(bg='red')
            if C3[0].__contains__('1 month') or C3[0].__contains__('week(s)') \
            or C3[0].__contains__('day(s)'):
                c3_a2.configure(bg='orange')
        else:
            c3_a2.configure(bg='green')
        if C3[0].__contains__('C3' and '(3)'):
            c3_a3.configure(bg='red')
            if C3[0].__contains__('1 month') or C3[0].__contains__('week(s)') \
            or C3[0].__contains__('day(s)'):
                c3_a3.configure(bg='orange')
        else:
            c3_a3.configure(bg='green')
        if C3[0].__contains__('C3' and '(4)'):
            c3_a4.configure(bg='red')
            if C3[0].__contains__('1 month') or C3[0].__contains__('week(s)') \
            or C3[0].__contains__('day(s)'):
                c3_a4.configure(bg='orange')
        else:
            c3_a4.configure(bg='green')
    except IndexError:
        pass
        
    try:
        if C3[1].__contains__('C3' and '(2)'): 
            c3_a2.configure(bg='red')
            if C3[1].__contains__('1 month') or C3[1].__contains__('week(s)') \
            or C3[1].__contains__('day(s)'):
                c3_a2.configure(bg='orange')
        elif C3[1].__contains__('C3' and '(3)'):
            c3_a3.configure(bg='red')
            if C3[1].__contains__('1 month') or C3[1].__contains__('week(s)') \
            or C3[1].__contains__('day(s)'):
                c3_a3.configure(bg='orange')
        elif C3[1].__contains__('C3' and '(4)'):
            c3_a4.configure(bg='red')
            if C3[1].__contains__('1 month') or C3[1].__contains__('week(s)') \
            or C3[1].__contains__('day(s)'):
                c3_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if C3[2].__contains__('C3' and '(3)'):
            c3_a3.configure(bg='red')
            if C3[2].__contains__('1 month') or C3[2].__contains__('week(s)') \
            or C3[2].__contains__('day(s)'):
                c3_a3.configure(bg='orange')
        elif C3[2].__contains__('C3' and '(4)'):
            c3_a4.configure(bg='red')
            if C3[2].__contains__('1 month') or C3[2].__contains__('week(s)') \
            or C3[2].__contains__('day(s)'): 
                c3_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if C3[3].__contains__('C3' and '(4)'):
            c3_a4.configure(bg='red')
            if C3[3].__contains__('1 month') or C3[3].__contains__('week(s)') \
            or C3[3].__contains__('day(s)'):
                c3_a4.configure(bg='orange')
    except IndexError:
        pass 
        
#---------------------C4---------------------#
    
    try:
        if C4[0].__contains__('C4' and '(1)'):
            c4_a1.configure(bg='red')
            if C4[0].__contains__('1 month') or C4[0].__contains__('week(s)') \
            or C4[0].__contains__('day(s)'):
                c4_a1.configure(bg='orange')
        else:
            c4_a1.configure(bg='green')
        if C4[0].__contains__('C4' and '(2)'):
            c4_a2.configure(bg='red')
            if C4[0].__contains__('1 month') or C4[0].__contains__('week(s)') \
            or C4[0].__contains__('day(s)'):
                c4_a2.configure(bg='orange')
        else:
            c4_a2.configure(bg='green')
        if C4[0].__contains__('C4' and '(3)'):
            c4_a3.configure(bg='red')
            if C4[0].__contains__('1 month') or C4[0].__contains__('week(s)') \
            or C4[0].__contains__('day(s)'):
                c4_a3.configure(bg='orange')
        else:
            c4_a3.configure(bg='green')
        if C4[0].__contains__('C4' and '(4)'):
            c4_a4.configure(bg='red')
            if C4[0].__contains__('1 month') or C4[0].__contains__('week(s)') \
            or C4[0].__contains__('day(s)'):
                c4_a4.configure(bg='orange')
        else:
            c4_a4.configure(bg='green')
    except IndexError:
        pass
        
    try:
        if C4[1].__contains__('C4' and '(2)'):
            c4_a2.configure(bg='red')
            if C4[1].__contains__('1 month') or C4[1].__contains__('week(s)') \
            or C4[1].__contains__('day(s)'):
                c4_a2.configure(bg='orange')
        elif C4[1].__contains__('C4' and '(3)'):
            c4_a3.configure(bg='red')
            if C4[1].__contains__('1 month') or C4[1].__contains__('week(s)') \
            or C4[1].__contains__('day(s)'):
                c4_a3.configure(bg='orange')
        elif C4[1].__contains__('C4' and '(4)'):
            c4_a4.configure(bg='red')
            if C4[1].__contains__('1 month') or C4[1].__contains__('week(s)') \
            or C4[1].__contains__('day(s)'):
                c4_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if C4[2].__contains__('C4' and '(3)'):
            c4_a3.configure(bg='red')
            if C4[2].__contains__('1 month') or C4[2].__contains__('week(s)') \
            or C4[2].__contains__('day(s)'):
                c4_a3.configure(bg='orange')
        elif C4[2].__contains__('C4' and '(4)'):
            c4_a4.configure(bg='red')
            if C4[2].__contains__('1 month') or C4[2].__contains__('week(s)') \
            or C4[2].__contains__('day(s)'):
                c4_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if C4[3].__contains__('C4' and '(4)'):
            c4_a4.configure(bg='red')
            if C4[3].__contains__('1 month') or C4[3].__contains__('week(s)') \
            or C4[3].__contains__('day(s)'):
                c4_a4.configure(bg='orange')
    except IndexError:
        pass 
              
              
#---------------------D1---------------------#
    
    try:
        if D1[0].__contains__('D1' and '(1)'):
            d1_a1.configure(bg='red')
            if D1[0].__contains__('1 month') or D1[0].__contains__('week(s)') \
            or D1[0].__contains__('day(s)'):
                d1_a1.configure(bg='orange')
        else:
            d1_a1.configure(bg='green')
        if D1[0].__contains__('D1' and '(2)'):
            d1_a2.configure(bg='red')
            if D1[0].__contains__('1 month') or D1[0].__contains__('week(s)') \
            or D1[0].__contains__('day(s)'):
                d1_a2.configure(bg='orange')
        else:
            d1_a2.configure(bg='green')
        if D1[0].__contains__('D1' and '(3)'):
            d1_a3.configure(bg='red')
            if D1[0].__contains__('1 month') or D1[0].__contains__('week(s)') \
            or D1[0].__contains__('day(s)'):
                d1_a3.configure(bg='orange')
        else:
            d1_a3.configure(bg='green')
        if D1[0].__contains__('D1' and '(4)'):
            d1_a4.configure(bg='red')
            if D1[0].__contains__('1 month') or D1[0].__contains__('week(s)') \
            or D1[0].__contains__('day(s)'):
                d1_a4.configure(bg='orange')
        else:
            d1_a4.configure(bg='green')
    except IndexError:
        pass
        
    try:
        if D1[1].__contains__('D1' and '(2)'):
            d1_a2.configure(bg='red')
            if D1[1].__contains__('1 month') or D1[1].__contains__('week(s)') \
            or D1[1].__contains__('day(s)'):
                d1_a2.configure(bg='orange')
        elif D1[1].__contains__('D1' and '(3)'):
            d1_a3.configure(bg='red')
            if D1[1].__contains__('1 month') or D1[1].__contains__('week(s)') \
            or D1[1].__contains__('day(s)'):
                d1_a3.configure(bg='orange')
        elif D1[1].__contains__('D1' and '(4)'):
            d1_a4.configure(bg='red')
            if D1[1].__contains__('1 month') or D1[1].__contains__('week(s)') \
            or D1[1].__contains__('day(s)'):
                d1_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if D1[2].__contains__('D1' and '(3)'):
            d1_a3.configure(bg='red')
            if D1[2].__contains__('1 month') or D1[2].__contains__('week(s)') \
            or D1[2].__contains__('day(s)'):
                d1_a3.configure(bg='orange')
        elif D1[2].__contains__('D1' and '(4)'):
            d1_a4.configure(bg='red')
            if D1[2].__contains__('1 month') or D1[2].__contains__('week(s)') \
            or D1[2].__contains__('day(s)'):
                d1_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if D1[3].__contains__('D1' and '(4)'):
            d1_a4.configure(bg='red')
            if D1[3].__contains__('1 month') or D1[3].__contains__('week(s)') \
            or D1[3].__contains__('day(s)'):
                d1_a4.configure(bg='orange')
    except IndexError:
        pass
        
#---------------------D2---------------------#
    
    try:
        if D2[0].__contains__('D2' and '(1)'):
            d2_a1.configure(bg='red')
            if D2[0].__contains__('1 month') or D2[0].__contains__('week(s)') \
            or D2[0].__contains__('day(s)'):
                d2_a1.configure(bg='orange')
        else:
            d2_a1.configure(bg='green')
        if D2[0].__contains__('D2' and '(2)'):
            d2_a2.configure(bg='red')
            if D2[0].__contains__('1 month') or D2[0].__contains__('week(s)') \
            or D2[0].__contains__('day(s)'):
                d2_a2.configure(bg='orange')
        else:
            d2_a2.configure(bg='green')
        if D2[0].__contains__('D2' and '(3)'):
            d2_a3.configure(bg='red')
            if D2[0].__contains__('1 month') or D2[0].__contains__('week(s)') \
            or D2[0].__contains__('day(s)'):
                d2_a3.configure(bg='orange')
        else:
            d2_a3.configure(bg='green')
        if D2[0].__contains__('D2' and '(4)'):
            d2_a4.configure(bg='red')
            if D2[0].__contains__('1 month') or D2[0].__contains__('week(s)') \
            or D2[0].__contains__('day(s)'):
                d2_a4.configure(bg='orange')
        else:
            d2_a4.configure(bg='green')
    except IndexError:
        pass
        
    try:
        if D2[1].__contains__('D2' and '(2)'):
            d2_a2.configure(bg='red')
            if D2[1].__contains__('1 month') or D2[1].__contains__('week(s)') \
            or D2[1].__contains__('day(s)'):
                d2_a2.configure(bg='orange')
        elif D2[1].__contains__('D2' and '(3)'):
            d2_a3.configure(bg='red')
            if D2[1].__contains__('1 month') or D2[1].__contains__('week(s)') \
            or D2[1].__contains__('day(s)'):
                d2_a3.configure(bg='orange')
        elif D2[1].__contains__('D2' and '(4)'):
            d2_a4.configure(bg='red')
            if D2[1].__contains__('1 month') or D2[1].__contains__('week(s)') \
            or D2[1].__contains__('day(s)'):
                d2_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if D2[2].__contains__('D2' and '(3)'):
            d2_a3.configure(bg='red')
            if D2[2].__contains__('1 month') or D2[2].__contains__('week(s)') \
            or D2[2].__contains__('day(s)'):
                d2_a3.configure(bg='orange')
        elif D2[2].__contains__('D2' and '(4)'):
            d2_a4.configure(bg='red')
            if D2[2].__contains__('1 month') or D2[2].__contains__('week(s)') \
            or D2[2].__contains__('day(s)'):
                d2_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if D2[3].__contains__('D2' and '(4)'):
            d2_a4.configure(bg='red')
            if D2[3].__contains__('1 month') or D2[3].__contains__('week(s)') \
            or D2[3].__contains__('day(s)'):
                d2_a4.configure(bg='orange')
    except IndexError:
        pass        
        
#---------------------D3---------------------#
    
    try:
        if D3[0].__contains__('D3' and '(1)'):
            d3_a1.configure(bg='red')
            if D3[0].__contains__('1 month') or D3[0].__contains__('week(s)') \
            or D3[0].__contains__('day(s)'):
                d3_a1.configure(bg='orange')
        else:
            d3_a1.configure(bg='green')
        if D3[0].__contains__('D3' and '(2)'):
            d3_a2.configure(bg='red')
            if D3[0].__contains__('1 month') or D3[0].__contains__('week(s)') \
            or D3[0].__contains__('day(s)'):
                d3_a2.configure(bg='orange')
        else:
            d3_a2.configure(bg='green')
        if D3[0].__contains__('D3' and '(3)'):
            d3_a3.configure(bg='red')
            if D3[0].__contains__('1 month') or D3[0].__contains__('week(s)') \
            or D3[0].__contains__('day(s)'):
                d3_a3.configure(bg='orange')
        else:
            d3_a3.configure(bg='green')
        if D3[0].__contains__('D3' and '(4)'):
            d3_a4.configure(bg='red')
            if D3[0].__contains__('1 month') or D3[0].__contains__('week(s)') \
            or D3[0].__contains__('day(s)'):
                d3_a4.configure(bg='orange')
        else:
            d3_a4.configure(bg='green')
    except IndexError:
        pass
        
    try:
        if D3[1].__contains__('D3' and '(2)'): 
            d3_a2.configure(bg='red')
            if D3[1].__contains__('1 month') or D3[1].__contains__('week(s)') \
            or D3[1].__contains__('day(s)'):
                d3_a2.configure(bg='orange')
        elif D3[1].__contains__('D3' and '(3)'):
            d3_a3.configure(bg='red')
            if D3[1].__contains__('1 month') or D3[1].__contains__('week(s)') \
            or D3[1].__contains__('day(s)'):
                d3_a3.configure(bg='orange')
        elif D3[1].__contains__('D3' and '(4)'):
            d3_a4.configure(bg='red')
            if D3[1].__contains__('1 month') or D3[1].__contains__('week(s)') \
            or D3[1].__contains__('day(s)'):
                d3_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if D3[2].__contains__('D3' and '(3)'):
            d3_a3.configure(bg='red')
            if D3[2].__contains__('1 month') or D3[2].__contains__('week(s)') \
            or D3[2].__contains__('day(s)'):
                d3_a3.configure(bg='orange')
        elif D3[2].__contains__('D3' and '(4)'):
            d3_a4.configure(bg='red')
            if D3[2].__contains__('1 month') or D3[2].__contains__('week(s)') \
            or D3[2].__contains__('day(s)'): 
                d3_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if D3[3].__contains__('D3' and '(4)'):
            d3_a4.configure(bg='red')
            if D3[3].__contains__('1 month') or D3[3].__contains__('week(s)') \
            or D3[3].__contains__('day(s)'):
                d3_a4.configure(bg='orange')
    except IndexError:
        pass 
        
#---------------------D4---------------------#
    
    try:
        if D4[0].__contains__('D4' and '(1)'):
            d4_a1.configure(bg='red')
            if D4[0].__contains__('1 month') or D4[0].__contains__('week(s)') \
            or D4[0].__contains__('day(s)'):
                d4_a1.configure(bg='orange')
        else:
            d4_a1.configure(bg='green')
        if D4[0].__contains__('D4' and '(2)'):
            d4_a2.configure(bg='red')
            if D4[0].__contains__('1 month') or D4[0].__contains__('week(s)') \
            or D4[0].__contains__('day(s)'):
                d4_a2.configure(bg='orange')
        else:
            d4_a2.configure(bg='green')
        if D4[0].__contains__('D4' and '(3)'):
            d4_a3.configure(bg='red')
            if D4[0].__contains__('1 month') or D4[0].__contains__('week(s)') \
            or D4[0].__contains__('day(s)'):
                d4_a3.configure(bg='orange')
        else:
            d4_a3.configure(bg='green')
        if D4[0].__contains__('D4' and '(4)'):
            d4_a4.configure(bg='red')
            if D4[0].__contains__('1 month') or D4[0].__contains__('week(s)') \
            or D4[0].__contains__('day(s)'):
                d4_a4.configure(bg='orange')
        else:
            d4_a4.configure(bg='green')
    except IndexError:
        pass
        
    try:
        if D4[1].__contains__('D4' and '(2)'):
            d4_a2.configure(bg='red')
            if D4[1].__contains__('1 month') or D4[1].__contains__('week(s)') \
            or D4[1].__contains__('day(s)'):
                d4_a2.configure(bg='orange')
        elif D4[1].__contains__('D4' and '(3)'):
            d4_a3.configure(bg='red')
            if D4[1].__contains__('1 month') or D4[1].__contains__('week(s)') \
            or D4[1].__contains__('day(s)'):
                d4_a3.configure(bg='orange')
        elif D4[1].__contains__('D4' and '(4)'):
            d4_a4.configure(bg='red')
            if D4[1].__contains__('1 month') or D4[1].__contains__('week(s)') \
            or D4[1].__contains__('day(s)'):
                d4_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if D4[2].__contains__('D4' and '(3)'):
            d4_a3.configure(bg='red')
            if D4[2].__contains__('1 month') or D4[2].__contains__('week(s)') \
            or D4[2].__contains__('day(s)'):
                d4_a3.configure(bg='orange')
        elif D4[2].__contains__('D4' and '(4)'):
            d4_a4.configure(bg='red')
            if D4[2].__contains__('1 month') or D4[2].__contains__('week(s)') \
            or D4[2].__contains__('day(s)'):
                d4_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if D4[3].__contains__('D4' and '(4)'):
            d4_a4.configure(bg='red')
            if D4[3].__contains__('1 month') or D4[3].__contains__('week(s)') \
            or D4[3].__contains__('day(s)'):
                d4_a4.configure(bg='orange')
    except IndexError:
        pass 

#---------------------E1---------------------#
    
    try:
        if E1[0].__contains__('E1' and '(1)'):
            e1_a1.configure(bg='red')
            if E1[0].__contains__('1 month') or E1[0].__contains__('week(s)') \
            or E1[0].__contains__('day(s)'):
                e1_a1.configure(bg='orange')
        else:
            e1_a1.configure(bg='green')
        if E1[0].__contains__('E1' and '(2)'):
            e1_a2.configure(bg='red')
            if E1[0].__contains__('1 month') or E1[0].__contains__('week(s)') \
            or E1[0].__contains__('day(s)'):
                e1_a2.configure(bg='orange')
        else:
            e1_a2.configure(bg='green')
        if E1[0].__contains__('E1' and '(3)'):
            e1_a3.configure(bg='red')
            if E1[0].__contains__('1 month') or E1[0].__contains__('week(s)') \
            or E1[0].__contains__('day(s)'):
                e1_a3.configure(bg='orange')
        else:
            e1_a3.configure(bg='green')
        if E1[0].__contains__('E1' and '(4)'):
            e1_a4.configure(bg='red')
            if E1[0].__contains__('1 month') or E1[0].__contains__('week(s)') \
            or E1[0].__contains__('day(s)'):
                e1_a4.configure(bg='orange')
        else:
            e1_a4.configure(bg='green')
    except IndexError:
        pass
        
    try:
        if E1[1].__contains__('E1' and '(2)'):
            e1_a2.configure(bg='red')
            if E1[1].__contains__('1 month') or E1[1].__contains__('week(s)') \
            or E1[1].__contains__('day(s)'):
                e1_a2.configure(bg='orange')
        elif E1[1].__contains__('E1' and '(3)'):
            e1_a3.configure(bg='red')
            if E1[1].__contains__('1 month') or E1[1].__contains__('week(s)') \
            or E1[1].__contains__('day(s)'):
                e1_a3.configure(bg='orange')
        elif E1[1].__contains__('E1' and '(4)'):
            e1_a4.configure(bg='red')
            if E1[1].__contains__('1 month') or E1[1].__contains__('week(s)') \
            or E1[1].__contains__('day(s)'):
                e1_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if E1[2].__contains__('E1' and '(3)'):
            e1_a3.configure(bg='red')
            if E1[2].__contains__('1 month') or E1[2].__contains__('week(s)') \
            or E1[2].__contains__('day(s)'):
                e1_a3.configure(bg='orange')
        elif E1[2].__contains__('E1' and '(4)'):
            e1_a4.configure(bg='red')
            if E1[2].__contains__('1 month') or E1[2].__contains__('week(s)') \
            or E1[2].__contains__('day(s)'):
                e1_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if E1[3].__contains__('E1' and '(4)'):
            e1_a4.configure(bg='red')
            if E1[3].__contains__('1 month') or E1[3].__contains__('week(s)') \
            or E1[3].__contains__('day(s)'):
                e1_a4.configure(bg='orange')
    except IndexError:
        pass
        
#---------------------E2---------------------#
    
    try:
        if E2[0].__contains__('E2' and '(1)'):
            e2_a1.configure(bg='red')
            if E2[0].__contains__('1 month') or E2[0].__contains__('week(s)') \
            or E2[0].__contains__('day(s)'):
                e2_a1.configure(bg='orange')
        else:
            e2_a1.configure(bg='green')
        if E2[0].__contains__('E2' and '(2)'):
            e2_a2.configure(bg='red')
            if E2[0].__contains__('1 month') or E2[0].__contains__('week(s)') \
            or E2[0].__contains__('day(s)'):
                e2_a2.configure(bg='orange')
        else:
            e2_a2.configure(bg='green')
        if E2[0].__contains__('E2' and '(3)'):
            e2_a3.configure(bg='red')
            if E2[0].__contains__('1 month') or E2[0].__contains__('week(s)') \
            or E2[0].__contains__('day(s)'):
                e2_a3.configure(bg='orange')
        else:
            e2_a3.configure(bg='green')
        if E2[0].__contains__('E2' and '(4)'):
            e2_a4.configure(bg='red')
            if E2[0].__contains__('1 month') or E2[0].__contains__('week(s)') \
            or E2[0].__contains__('day(s)'):
                e2_a4.configure(bg='orange')
        else:
            e2_a4.configure(bg='green')
    except IndexError:
        pass
        
    try:
        if E2[1].__contains__('E2' and '(2)'):
            e2_a2.configure(bg='red')
            if E2[1].__contains__('1 month') or E2[1].__contains__('week(s)') \
            or E2[1].__contains__('day(s)'):
                e2_a2.configure(bg='orange')
        elif E2[1].__contains__('E2' and '(3)'):
            e2_a3.configure(bg='red')
            if E2[1].__contains__('1 month') or E2[1].__contains__('week(s)') \
            or E2[1].__contains__('day(s)'):
                e2_a3.configure(bg='orange')
        elif E2[1].__contains__('E2' and '(4)'):
            e2_a4.configure(bg='red')
            if E2[1].__contains__('1 month') or E2[1].__contains__('week(s)') \
            or E2[1].__contains__('day(s)'):
                e2_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if E2[2].__contains__('E2' and '(3)'):
            e2_a3.configure(bg='red')
            if E2[2].__contains__('1 month') or E2[2].__contains__('week(s)') \
            or E2[2].__contains__('day(s)'):
                e2_a3.configure(bg='orange')
        elif E2[2].__contains__('E2' and '(4)'):
            e2_a4.configure(bg='red')
            if E2[2].__contains__('1 month') or E2[2].__contains__('week(s)') \
            or E2[2].__contains__('day(s)'):
                e2_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if E2[3].__contains__('E2' and '(4)'):
            e2_a4.configure(bg='red')
            if E2[3].__contains__('1 month') or E2[3].__contains__('week(s)') \
            or E2[3].__contains__('day(s)'):
                e2_a4.configure(bg='orange')
    except IndexError:
        pass        
        
#---------------------E3---------------------#
    
    try:
        if E3[0].__contains__('E3' and '(1)'):
            e3_a1.configure(bg='red')
            if E3[0].__contains__('1 month') or E3[0].__contains__('week(s)') \
            or E3[0].__contains__('day(s)'):
                e3_a1.configure(bg='orange')
        else:
            e3_a1.configure(bg='green')
        if E3[0].__contains__('E3' and '(2)'):
            e3_a2.configure(bg='red')
            if E3[0].__contains__('1 month') or E3[0].__contains__('week(s)') \
            or E3[0].__contains__('day(s)'):
                e3_a2.configure(bg='orange')
        else:
            e3_a2.configure(bg='green')
        if E3[0].__contains__('E3' and '(3)'):
            e3_a3.configure(bg='red')
            if E3[0].__contains__('1 month') or E3[0].__contains__('week(s)') \
            or E3[0].__contains__('day(s)'):
                e3_a3.configure(bg='orange')
        else:
            e3_a3.configure(bg='green')
        if E3[0].__contains__('E3' and '(4)'):
            e3_a4.configure(bg='red')
            if E3[0].__contains__('1 month') or E3[0].__contains__('week(s)') \
            or E3[0].__contains__('day(s)'):
                e3_a4.configure(bg='orange')
        else:
            e3_a4.configure(bg='green')
    except IndexError:
        pass
        
    try:
        if E3[1].__contains__('E3' and '(2)'): 
            e3_a2.configure(bg='red')
            if E3[1].__contains__('1 month') or E3[1].__contains__('week(s)') \
            or E3[1].__contains__('day(s)'):
                e3_a2.configure(bg='orange')
        elif E3[1].__contains__('E3' and '(3)'):
            e3_a3.configure(bg='red')
            if E3[1].__contains__('1 month') or E3[1].__contains__('week(s)') \
            or E3[1].__contains__('day(s)'):
                e3_a3.configure(bg='orange')
        elif E3[1].__contains__('E3' and '(4)'):
            e3_a4.configure(bg='red')
            if E3[1].__contains__('1 month') or E3[1].__contains__('week(s)') \
            or E3[1].__contains__('day(s)'):
                e3_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if E3[2].__contains__('E3' and '(3)'):
            e3_a3.configure(bg='red')
            if E3[2].__contains__('1 month') or E3[2].__contains__('week(s)') \
            or E3[2].__contains__('day(s)'):
                e3_a3.configure(bg='orange')
        elif E3[2].__contains__('E3' and '(4)'):
            e3_a4.configure(bg='red')
            if E3[2].__contains__('1 month') or E3[2].__contains__('week(s)') \
            or E3[2].__contains__('day(s)'): 
                e3_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if E3[3].__contains__('E3' and '(4)'):
            e3_a4.configure(bg='red')
            if E3[3].__contains__('1 month') or E3[3].__contains__('week(s)') \
            or E3[3].__contains__('day(s)'):
                e3_a4.configure(bg='orange')
    except IndexError:
        pass 
        
#---------------------E4---------------------#
    
    try:
        if E4[0].__contains__('E4' and '(1)'):
            e4_a1.configure(bg='red')
            if E4[0].__contains__('1 month') or E4[0].__contains__('week(s)') \
            or E4[0].__contains__('day(s)'):
                e4_a1.configure(bg='orange')
        else:
            e4_a1.configure(bg='green')
        if E4[0].__contains__('E4' and '(2)'):
            e4_a2.configure(bg='red')
            if E4[0].__contains__('1 month') or E4[0].__contains__('week(s)') \
            or E4[0].__contains__('day(s)'):
                e4_a2.configure(bg='orange')
        else:
            e4_a2.configure(bg='green')
        if E4[0].__contains__('E4' and '(3)'):
            e4_a3.configure(bg='red')
            if E4[0].__contains__('1 month') or E4[0].__contains__('week(s)') \
            or E4[0].__contains__('day(s)'):
                e4_a3.configure(bg='orange')
        else:
            e4_a3.configure(bg='green')
        if E4[0].__contains__('E4' and '(4)'):
            e4_a4.configure(bg='red')
            if E4[0].__contains__('1 month') or E4[0].__contains__('week(s)') \
            or E4[0].__contains__('day(s)'):
                e4_a4.configure(bg='orange')
        else:
            e4_a4.configure(bg='green')
    except IndexError:
        pass
        
    try:
        if E4[1].__contains__('E4' and '(2)'):
            e4_a2.configure(bg='red')
            if E4[1].__contains__('1 month') or E4[1].__contains__('week(s)') \
            or E4[1].__contains__('day(s)'):
                e4_a2.configure(bg='orange')
        elif E4[1].__contains__('E4' and '(3)'):
            e4_a3.configure(bg='red')
            if E4[1].__contains__('1 month') or E4[1].__contains__('week(s)') \
            or E4[1].__contains__('day(s)'):
                e4_a3.configure(bg='orange')
        elif E4[1].__contains__('E4' and '(4)'):
            e4_a4.configure(bg='red')
            if E4[1].__contains__('1 month') or E4[1].__contains__('week(s)') \
            or E4[1].__contains__('day(s)'):
                e4_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if E4[2].__contains__('E4' and '(3)'):
            e4_a3.configure(bg='red')
            if E4[2].__contains__('1 month') or E4[2].__contains__('week(s)') \
            or E4[2].__contains__('day(s)'):
                e4_a3.configure(bg='orange')
        elif E4[2].__contains__('E4' and '(4)'):
            e4_a4.configure(bg='red')
            if E4[2].__contains__('1 month') or E4[2].__contains__('week(s)') \
            or E4[2].__contains__('day(s)'):
                e4_a4.configure(bg='orange')
    except IndexError:
        pass
        
    try:
        if E4[3].__contains__('E4' and '(4)'):
            e4_a4.configure(bg='red')
            if E4[3].__contains__('1 month') or E4[3].__contains__('week(s)') \
            or E4[3].__contains__('day(s)'):
                e4_a4.configure(bg='orange')
    except IndexError:
        pass 

indicator()

#NOTIFICATIONS 
def notification():
#------------------BLOCK A------------------#    
    try:
        view_notif.delete(0,END)
        view_notif.insert(END,A1[0],str(''))
        view_notif.itemconfig(1,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,A1[1],str(''))
        view_notif.itemconfig(3,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,A1[2],str(''))
        view_notif.itemconfig(5,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,A1[3],str(''))
        view_notif.itemconfig(7,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,A2[0],str(''))
        view_notif.itemconfig(9,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,A2[1],str(''))
        view_notif.itemconfig(11,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,A2[2],str(''))
        view_notif.itemconfig(13,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,A2[3],str(''))
        view_notif.itemconfig(15,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,A3[0],str(''))
        view_notif.itemconfig(17,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,A3[1],str(''))
        view_notif.itemconfig(19,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,A3[2],str(''))
        view_notif.itemconfig(21,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,A3[3],str(''))
        view_notif.itemconfig(23,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,A4[0],str(''))
        view_notif.itemconfig(25,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,A4[1],str(''))
        view_notif.itemconfig(27,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,A4[2],str(''))
        view_notif.itemconfig(29,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,A4[3],str(''))
        view_notif.itemconfig(31,bg='#e8e8e8')
    except:
        pass

#------------------BLOCK B------------------#
    try:
        view_notif.insert(END,B1[0],str(''))
        view_notif.itemconfig(33,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,B1[1],str(''))
        view_notif.itemconfig(35,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,B1[2],str(''))
        view_notif.itemconfig(37,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,B1[3],str(''))
        view_notif.itemconfig(39,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,B2[0],str(''))
        view_notif.itemconfig(41,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,B2[1],str(''))
        view_notif.itemconfig(43,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,B2[2],str(''))
        view_notif.itemconfig(45,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,B2[3],str(''))
        view_notif.itemconfig(47,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,B3[0],str(''))
        view_notif.itemconfig(49,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,B3[1],str(''))
        view_notif.itemconfig(51,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,B3[2],str(''))
        view_notif.itemconfig(53,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,B3[3],str(''))
        view_notif.itemconfig(55,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,B4[0],str(''))
        view_notif.itemconfig(57,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,B4[1],str(''))
        view_notif.itemconfig(59,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,B4[2],str(''))
        view_notif.itemconfig(61,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,B4[3],str(''))
        view_notif.itemconfig(63,bg='#e8e8e8')
    except:
        pass
        
#------------------BLOCK C------------------#
    try:
        view_notif.insert(END,C1[0],str(''))
        view_notif.itemconfig(65,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,C1[1],str(''))
        view_notif.itemconfig(67,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,C1[2],str(''))
        view_notif.itemconfig(69,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,C1[3],str(''))
        view_notif.itemconfig(71,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,C2[0],str(''))
        view_notif.itemconfig(73,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,C2[1],str(''))
        view_notif.itemconfig(75,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,C2[2],str(''))
        view_notif.itemconfig(77,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,C2[3],str(''))
        view_notif.itemconfig(79,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,C3[0],str(''))
        view_notif.itemconfig(81,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,C3[1],str(''))
        view_notif.itemconfig(83,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,C3[2],str(''))
        view_notif.itemconfig(85,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,C3[3],str(''))
        view_notif.itemconfig(87,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,C4[0],str(''))
        view_notif.itemconfig(89,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,C4[1],str(''))
        view_notif.itemconfig(91,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,C4[2],str(''))
        view_notif.itemconfig(93,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,C4[3],str(''))
        view_notif.itemconfig(95,bg='#e8e8e8')
    except:
        pass

#------------------BLOCK D------------------#
    try:
        view_notif.insert(END,D1[0],str(''))
        view_notif.itemconfig(97,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,D1[1],str(''))
        view_notif.itemconfig(99,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,D1[2],str(''))
        view_notif.itemconfig(101,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,D1[3],str(''))
        view_notif.itemconfig(103,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,D2[0],str(''))
        view_notif.itemconfig(105,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,D2[1],str(''))
        view_notif.itemconfig(107,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,D2[2],str(''))
        view_notif.itemconfig(109,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,D2[3],str(''))
        view_notif.itemconfig(111,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,D3[0],str(''))
        view_notif.itemconfig(113,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,D3[1],str(''))
        view_notif.itemconfig(115,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,D3[2],str(''))
        view_notif.itemconfig(117,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,D3[3],str(''))
        view_notif.itemconfig(119,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,D4[0],str(''))
        view_notif.itemconfig(121,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,D4[1],str(''))
        view_notif.itemconfig(123,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,D4[2],str(''))
        view_notif.itemconfig(125,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,D4[3],str(''))
        view_notif.itemconfig(127,bg='#e8e8e8')
    except:
        pass
        
#------------------BLOCK E------------------#
    try:
        view_notif.insert(END,E1[0],str(''))
        view_notif.itemconfig(129,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,E1[1],str(''))
        view_notif.itemconfig(131,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,E1[2],str(''))
        view_notif.itemconfig(133,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,E1[3],str(''))
        view_notif.itemconfig(135,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,E2[0],str(''))
        view_notif.itemconfig(137,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,E2[1],str(''))
        view_notif.itemconfig(139,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,E2[2],str(''))
        view_notif.itemconfig(141,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,E2[3],str(''))
        view_notif.itemconfig(143,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,E3[0],str(''))
        view_notif.itemconfig(145,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,E3[1],str(''))
        view_notif.itemconfig(147,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,E3[2],str(''))
        view_notif.itemconfig(149,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,E3[3],str(''))
        view_notif.itemconfig(151,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,E4[0],str(''))
        view_notif.itemconfig(153,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,E4[1],str(''))
        view_notif.itemconfig(155,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,E4[2],str(''))
        view_notif.itemconfig(157,bg='#e8e8e8')
    except:
        pass
    try:
        view_notif.insert(END,E4[3],str(''))
        view_notif.itemconfig(159,bg='#e8e8e8')
    except:
        pass
        
#-----------------------------------------------------------------------#
#-----------------------sorted------------------------------#
    try:
        notif_sort.delete(0,END)
        if A1[0].__contains__('vacan'):
            notif_sort.insert(END,A1[0],str(''))
    except IndexError:
        pass
    try:
        if A1[1].__contains__('vacan'):
            notif_sort.insert(END,A1[1],str(''))
    except IndexError:
        pass
    try:
        if A1[2].__contains__('vacan'):
            notif_sort.insert(END,A1[2],str(''))
    except IndexError:
        pass
    try:
        if A1[3].__contains__('vacan'):
            notif_sort.insert(END,A1[3],str(''))
    except IndexError:
        pass
    try:
        if A2[0].__contains__('vacan'):
            notif_sort.insert(END,A2[0],str(''))
    except IndexError:
        pass
    try:
        if A2[1].__contains__('vacan'):
            notif_sort.insert(END,A2[1],str(''))
    except IndexError:
        pass
    try:
        if A2[2].__contains__('vacan'):
            notif_sort.insert(END,A2[2],str(''))
    except IndexError:
        pass
    try:
        if A2[3].__contains__('vacan'):
            notif_sort.insert(END,A2[3],str(''))
    except IndexError:
        pass
    try:
        if A3[0].__contains__('vacan'):
            notif_sort.insert(END,A3[0],str(''))
    except IndexError:
        pass
    try:
        if A3[1].__contains__('vacan'):
            notif_sort.insert(END,A3[1],str(''))
    except IndexError:
        pass
    try:
        if A3[2].__contains__('vacan'):
            notif_sort.insert(END,A3[2],str(''))
    except IndexError:
        pass
    try:
        if A3[3].__contains__('vacan'):
            notif_sort.insert(END,A3[3],str(''))
    except IndexError:
        pass
    try:
        if A4[0].__contains__('vacan'):
            notif_sort.insert(END,A4[0],str(''))
    except IndexError:
        pass
    try:
        if A4[1].__contains__('vacan'):
            notif_sort.insert(END,A4[1],str(''))
    except IndexError:
        pass
    try:
        if A4[2].__contains__('vacan'):
            notif_sort.insert(END,A4[2],str(''))
    except IndexError:
        pass
    try:
        if A4[3].__contains__('vacacny'):
            notif_sort.insert(END,A4[3],str(''))
    except IndexError:
        pass

#------------------BLOCK B------------------#
    try:
        if B1[0].__contains__('vacan'):
            notif_sort.insert(END,B1[0],str(''))
    except IndexError:
        pass
    try:
        if B1[1].__contains__('vacan'):
            notif_sort.insert(END,B1[1],str(''))
    except IndexError:
        pass
    try:
        if B1[2].__contains__('vacan'):
            notif_sort.insert(END,B1[2],str(''))
    except IndexError:
        pass
    try:
        if B1[3].__contains__('vacan'):
            notif_sort.insert(END,B1[3],str(''))
    except IndexError:
        pass
    try:
        if B2[0].__contains__('vacan'):
            notif_sort.insert(END,B2[0],str(''))
    except IndexError:
        pass
    try:
        if B2[1].__contains__('vacan'):
            notif_sort.insert(END,B2[1],str(''))
    except IndexError:
        pass
    try:
        if B2[2].__contains__('vacan'):
            notif_sort.insert(END,B2[2],str(''))
    except IndexError:
        pass
    try:
        if B2[3].__contains__('vacan'):
            notif_sort.insert(END,B2[3],str(''))
    except IndexError:
        pass
    try:
        if B3[0].__contains__('vacan'):
            notif_sort.insert(END,B3[0],str(''))
    except IndexError:
        pass
    try:
        if B3[1].__contains__('vacan'):
            notif_sort.insert(END,B3[1],str(''))
    except IndexError:
        pass
    try:
        if B3[2].__contains__('vacan'):
            notif_sort.insert(END,B3[2],str(''))
    except IndexError:
        pass
    try:
        if B3[3].__contains__('vacan'):
            notif_sort.insert(END,B3[3],str(''))
    except IndexError:
        pass
    try:
        if B4[0].__contains__('vacan'):
            notif_sort.insert(END,B4[0],str(''))
    except IndexError:
        pass
    try:
        if B4[1].__contains__('vacan'):
            notif_sort.insert(END,B4[1],str(''))
    except IndexError:
        pass
    try:
        if B4[2].__contains__('vacan'):
            notif_sort.insert(END,B4[2],str(''))
    except IndexError:
        pass
    try:
        if B4[3].__contains__('vacan'):
            notif_sort.insert(END,B4[3],str(''))
    except IndexError:
        pass
        
#------------------BLOCK C------------------#
    try:
        if C1[0].__contains__('vacan'):
            notif_sort.insert(END,C1[0],str(''))
    except IndexError:
        pass
    try:
        if C1[1].__contains__('vacan'):
            notif_sort.insert(END,C1[1],str(''))
    except IndexError:
        pass
    try:
        if C1[2].__contains__('vacan'):
            notif_sort.insert(END,C1[2],str(''))
    except IndexError:
        pass
    try:
        if C1[3].__contains__('vacan'):
            notif_sort.insert(END,C1[3],str(''))
    except IndexError:
        pass
    try:
        if C2[0].__contains__('vacan'):
            notif_sort.insert(END,C2[0],str(''))
    except IndexError:
        pass
    try:
        if C2[1].__contains__('vacan'):
            notif_sort.insert(END,C2[1],str(''))
    except IndexError:
        pass
    try:
        if C2[2].__contains__('vacan'):
            notif_sort.insert(END,C2[2],str(''))
    except IndexError:
        pass
    try:
        if C2[3].__contains__('vacan'):
            notif_sort.insert(END,C2[3],str(''))
    except IndexError:
        pass
    try:
        if C3[0].__contains__('vacan'):
            notif_sort.insert(END,C3[0],str(''))
    except IndexError:
        pass
    try:
        if C3[1].__contains__('vacan'):
            notif_sort.insert(END,C3[1],str(''))
    except IndexError:
        pass
    try:
        if C3[2].__contains__('vacan'):
            notif_sort.insert(END,C3[2],str(''))
    except IndexError:
        pass
    try:
        if C3[3].__contains__('vacan'):
            notif_sort.insert(END,C3[3],str(''))
    except IndexError:
        pass
    try:
        if C4[0].__contains__('vacan'):
            notif_sort.insert(END,C4[0],str(''))
    except IndexError:
        pass
    try:
        if C4[1].__contains__('vacan'):
            notif_sort.insert(END,C4[1],str(''))
    except IndexError:
        pass
    try:
        if C4[2].__contains__('vacan'):
            notif_sort.insert(END,C4[2],str(''))
    except IndexError:
        pass
    try:
        if C4[3].__contains__('vacan'):
            notif_sort.insert(END,C4[3],str(''))
    except IndexError:
        pass

#------------------BLOCK D------------------#
    try:
        if D1[0].__contains__('vacan'):
            notif_sort.insert(END,D1[0],str(''))
    except IndexError:
        pass
    try:
        if D1[1].__contains__('vacan'):
            notif_sort.insert(END,D1[1],str(''))
    except IndexError:
        pass
    try:
        if D1[2].__contains__('vacan'):
            notif_sort.insert(END,D1[2],str(''))
    except IndexError:
        pass
    try:
        if D1[3].__contains__('vacan'):
            notif_sort.insert(END,D1[3],str(''))
    except IndexError:
        pass
    try:
        if D2[0].__contains__('vacan'):
            notif_sort.insert(END,D2[0],str(''))
    except IndexError:
        pass
    try:
        if D2[1].__contains__('vacan'):
            notif_sort.insert(END,D2[1],str(''))
    except IndexError:
        pass
    try:
        if D2[2].__contains__('vacan'):
            notif_sort.insert(END,D2[2],str(''))
    except IndexError:
        pass
    try:
        if D2[3].__contains__('vacan'):
            notif_sort.insert(END,D2[3],str(''))
    except IndexError:
        pass
    try:
        if D3[0].__contains__('vacan'):
            notif_sort.insert(END,D3[0],str(''))
    except IndexError:
        pass
    try:
        if D3[1].__contains__('vacan'):
            notif_sort.insert(END,D3[1],str(''))
    except IndexError:
        pass
    try:
        if D3[2].__contains__('vacan'):
            notif_sort.insert(END,D3[2],str(''))
    except IndexError:
        pass
    try:
        if D3[3].__contains__('vacan'):
            notif_sort.insert(END,D3[3],str(''))
    except IndexError:
        pass
    try:
        if D4[0].__contains__('vacan'):
            notif_sort.insert(END,D4[0],str(''))
    except IndexError:
        pass
    try:
        if D4[1].__contains__('vacan'):
            notif_sort.insert(END,D4[1],str(''))
    except IndexError:
        pass
    try:
        if D4[2].__contains__('vacan'):
            notif_sort.insert(END,D4[2],str(''))
    except IndexError:
        pass
    try:
        if D4[3].__contains__('vacan'):
            notif_sort.insert(END,D4[3],str(''))
    except IndexError:
        pass
    try:
        if E1[0].__contains__('vacan'):
            notif_sort.insert(END,E1[0],str(''))
    except IndexError:
        pass
    try:
        if E1[1].__contains__('vacan'):
            notif_sort.insert(END,E1[1],str(''))
    except IndexError:
        pass
    try:
        if E1[2].__contains__('vacan'):
            notif_sort.insert(END,E1[2],str(''))
    except IndexError:
        pass
    try:
        if E1[3].__contains__('vacan'):
            notif_sort.insert(END,E1[3],str(''))
    except IndexError:
        pass
    try:
        if E2[0].__contains__('vacan'):
            notif_sort.insert(END,E2[0],str(''))
    except IndexError:
        pass
    try:
        if E2[1].__contains__('vacan'):
            notif_sort.insert(END,E2[1],str(''))
    except IndexError:
        pass
    try:
        if E2[2].__contains__('vacan'):
            notif_sort.insert(END,E2[2],str(''))
    except IndexError:
        pass
    try:
        if E2[3].__contains__('vacan'):
            notif_sort.insert(END,E2[3],str(''))
    except IndexError:
        pass
    try:
        if E3[0].__contains__('vacan'):
            notif_sort.insert(END,E3[0],str(''))
    except IndexError:
        pass
    try:
        if E3[1].__contains__('vacan'):
            notif_sort.insert(END,E3[1],str(''))
    except IndexError:
        pass
    try:
        if E3[2].__contains__('vacan'):
            notif_sort.insert(END,E3[2],str(''))
    except IndexError:
        pass
    try:
        if E3[3].__contains__('vacan'):
            notif_sort.insert(END,E3[3],str(''))
    except IndexError:
        pass
    try:
        if E4[0].__contains__('vacan'):
            notif_sort.insert(END,E4[0],str(''))
    except IndexError:
        pass
    try:
        if E4[1].__contains__('vacan'):
            notif_sort.insert(END,E4[1],str(''))
    except IndexError:
        pass
    try:
        if E4[2].__contains__('vacan'):
            notif_sort.insert(END,E4[2],str(''))
    except IndexError:
        pass
    try:
        if E4[3].__contains__('vacan'):
            notif_sort.insert(END,E4[3],str(''))
    except IndexError:
        pass

notification()

def notif_stripes_monitor():
    if view_notif.size() == 160:
        pass
notif_stripes_monitor()

def backup_timer(num): # this function is to print the data in the database to a txt file(a log)
    pass

def backup_call():
    today = dt.now().date()
    if (28 < today.day <= 1):
        backend.backup2()
    else:
        pass
backup_call()
    
def display_time():
    cur_time = time.strftime('%a  | %D  | %H:%M:%S')
    tlabel['text']=cur_time
    win.after(200,display_time)            
display_time() 
    
#def keypointer(event):
#    e2.current(2)
    
#---------CREATE ENTRIES---------#
#Tenant entries#
##--conventions--##
relief='sunken'
##---------------##
e1 = Entry(l_frame,textvariable=t_name_text)
e1.grid(row=0,column=1,pady=5,padx=10)

e2= ttk.Combobox(l_frame, state='readonly',width=17,values=('--Select--','MALE','FEMALE'), 
textvariable=gender_text)
e2.current(0)
e2.grid(row=1,column=1,pady=5)
e2.bind('<f>', lambda event:e2.current(2))
e2.bind('<m>', lambda event:e2.current(1))

e3 = Entry(l_frame,textvariable=mob_num_text,relief=relief)
e3.grid(row=2,column=1,pady=5)

e4 = Entry(l_frame,textvariable=address_text,relief=relief)
e4.grid(row=3,column=1,pady=5)

e5 = Entry(l_frame,textvariable=email_text,relief=relief)
e5.grid(row=4,column=1,pady=5)

e6 = Entry(l_frame,textvariable=nation_text,relief=relief)
e6.grid(row=5,column=1,pady=5)

e7 = Entry(l_frame,textvariable=emg_num_text,relief=relief)
e7.grid(row=6,column=1,pady=5)

e8= Entry(l_frame,textvariable=ct_name_text,relief=relief) 
e8.grid(row=7,column=1,pady=5)

chk_in_text.set(time.strftime('%Y-%m-%d'))
e9 = Entry(l_frame,textvariable=chk_in_text,relief=relief,state='readonly')
e9.grid(row=8,column=1,pady=5)

e10 = ttk.Combobox(l_frame,state='readonly',width=17,values=tuple(x for x in range(25)), textvariable=duration_text)
e10.current(0)
e10.grid(row=9,column=1,pady=5)

e11 = Entry(l_frame,textvariable=chk_out_text,relief=relief,state='readonly')
e11.grid(row=10,column=1,pady=5)


#---------CREATE BUTTONS---------#
def on_enter(e):
	b4['background'] = '#cec4ce'
	
def on_leave(e):
	b4['background'] = 'SystemButtonFace'
	
#Tenant buttons
b4 = Button(l_frame,text='Display',width=10,bd=1.2,command=t_display)
b4.grid(row=0,column=3)
b4.bind('<Enter>',on_enter)
b4.bind('<Leave>',on_leave)

b5 = Button(l_frame,text='Add Entry',width=10,bd=1.2,command=t_add)
b5.grid(row=1,column=3)

b6 = Button(l_frame,text='Update',width=10,bd=1.2,command=t_update)
b6.grid(row=2,column=3)

b7 = Button(l_frame,text='Search',width=10,bd=1.2,command=searchfor)
b7.grid(row=3,column=3)

b8 = Button(l_frame,text='Delete',width=10,bd=1.2,command=t_remove)
b8.grid(row=4,column=3)

b9 = Button(l_frame,text='Reset',width=10,bd=1.2,command=t_reset)
b9.grid(row=5,column=3)

b10 = Button(l_frame,text='Exit',width=10,bd=1.2)
b10.grid(row=6,column=3)

#Room buttons
'''
r1 = Button(l_bframe,text='Display',width=10,bd=1.2,command=t_display)
r1.grid(row= 0,column=3,pady=2)

r2 = Button(l_bframe,text='Add Entry',width=10,bd=1.2,command=t_add)
r2.grid(row= 1,column=3,pady=2)

r3 = Button(l_bframe,text='Update',width=10,bd=1.2,command=t_update)
r3.grid(row= 2,column=3,pady=2)

r4 = Button(l_bframe,text='Search',width=10,bd=1.2,command=searchfor)
r4.grid(row= 3,column=3,pady=5)

r5 = Button(l_bframe,text='Delete',width=10,bd=1.2,command=t_remove)
r5.grid(row= 4,column=3,pady=2)

r6 = Button(l_bframe,text='Reset',width=10,height=1,bd=1,command=t_reset)
r6.grid(row= 5,column=3,pady=2)
'''

#notification clear Button
notifb = Button(nt_frame,text='clear',width=10,bd=1,relief=RIDGE)
notifb.grid(row=1,column=0,padx=5,sticky=W)

notifb1 = Button(nt_frame,text='Refresh',width=10,bd=1,relief=RIDGE)
notifb1.grid(row=0,column=0,padx=5,pady=7,sticky=W)

#===========================================================================
duration = duration_text.get()
def date_calc():
    global evac
    eva = dt.strptime(chk_in_text.get(),'%Y-%m-%d') + rd(months =+ duration_text.get())
    evac = eva.date()
    e10['state']=('normal')
    chk_out_text.set(evac)
    e10['state']=('readonly')
    win.after(200,date_calc)
date_calc()    

def blockctrl():
    if block_text.get() == '--Select--':
        eb2['value']=('--Select--')
    elif block_text.get() == 'A':
        eb2['value']=('--Select--','A1','A2','A3','A4')
    elif block_text.get() == 'B':
        eb2['value']=('--Select--','B1','B2','B3','B4')
    elif block_text.get() == 'C':
        eb2['value']=('--Select--','C1','C2','C3','C4')
    elif block_text.get() == 'D':
        eb2['value']=('--Select--','D1','D2','D3','D4')
    elif block_text.get() == 'E':
        eb2['value']=('--Select--','E1','E2','E3','E4')
    win.after(300,blockctrl)
blockctrl()

def entry_checker():
    '''
    #this function checks the first characters of the contact entry box 
    #to make sure it doesnt start with an alphabet
    '''
    if len(mob_num_text.get()) >=10 and mob_num_text.get().startswith('0') or \
    len(mob_num_text.get()) >=10 and mob_num_text.get().startswith('+'):
        e3.config(highlightthickness = 0)
        b5.config(state='normal')
        b6.config(state='normal')
    else:
        e3.config(highlightthickness = 1, highlightcolor ='red')
        b5.config(state='disabled')
        b6.config(state='disabled')
        
    if len(emg_num_text.get()) >=10 and emg_num_text.get().startswith('0') or \
    len(emg_num_text.get()) >=10 and emg_num_text.get().startswith('+'):
        e7.config(highlightthickness = 0)
        b5.config(state='normal')
        b6.config(state='normal')
        if len(mob_num_text.get()) <10:
            b5.config(state='disabled')
            b6.config(state='disabled')
    else:
        e7.config(highlightthickness = 1, highlightcolor ='red')
        b5.config(state='disabled')
        b6.config(state='disabled')
    win.after(200,entry_checker)
entry_checker()

def name_validate():
    sanitized_name = t_name_text.get().replace('/','').replace('*','').replace('#','').replace('@','')
    return sanitized_name


#Room Entries

eb1 = ttk.Combobox(l_bframe,state='readonly',width=17,values=('--Select--','A','B','C','D','E'),textvariable=block_text)
eb1.current(0)
eb1.grid(row=0,column=1,pady=5,padx=10)

eb2 = ttk.Combobox(l_bframe, state='readonly',width=17,values=('--Select--'),textvariable=aptype_text)
eb2.current(0)
eb2.grid(row=1,column=1, pady=5,padx=10)

eb3 = ttk.Combobox(l_bframe,state='readonly',width=17,values=('--Select--','1','2','3','4'),textvariable=apnum_text)
eb3.current(0)
eb3.grid(row=2,column=1,pady=5,padx=10)

eb4 = ttk.Combobox(l_bframe, state='readonly',width=17,textvariable=status_text)
eb4['value']=('--Select--','Occupied','Available','Unavailable','Vacant')
eb4.current(0)
eb4.grid(row=3,column=1,pady=5,padx=10)

#Notification search entry

#sbt = Button(l_bframe,text='search',width=10, bd =1,relief=RIDGE,command=t_lookup)
#sbt.grid(row=6,column=3,sticky=W)




def refrsh():
    #refresh admin frame
    db_length()
    se['text']=db_length()
    #refresh backend dependent functions
    call_a()
    call_b()
    call_c()
    call_d()
    call_e()
    #refresh frontend beneficiaries
    indicator()
    notification()
    e1.focus_set()
    #reset check-in date
    chk_in_text.set(time.strftime('%Y-%m-%d'))

#admin buttons
s1 = Button(s_frame,text='Refresh',width=9,bd=1,bg='#e3e3e3',command=refrsh)
s1.grid(row=0,column=3,sticky=E)

s2 = Button(s_frame,text='Exit',width=9,bd=1.2)
s2.grid(row=1,column=3,pady=16,sticky=E)

#refresh button



def on_closing():
    reply = tkinter.messagebox.askyesno('Exit Manager','You are about to close the program \n Are you sure you want to continue?')
    if reply > 0:
        win.destroy()



    
win.protocol('WM_DELETE_WINDOW',on_closing)   
win.mainloop()
