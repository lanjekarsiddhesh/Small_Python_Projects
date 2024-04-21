from tkinter import *
import datetime

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    min_ = time.strftime('%M')
    sec = time.strftime('%S')
    am_pm_ = time.strftime('%p')
    dt = time.strftime('%d')
    mt = time.strftime('%m')
    yer = time.strftime('%y')
    dy = time.strftime('%a')

    hour.config(text=hr)
    minutes.config(text=min_)
    second.config(text=sec)
    Am_Pm.config(text=am_pm_)

    date.config(text=dt)
    minutes.config(text=mt)
    year.config(text=yer)
    day.config(text=dy)

    hour.after(200,date_time)



tk = Tk()
tk.title("Digital Clock")
tk.geometry('900x500')
tk.config(bg='#77B0AA')

#----------------------------------------------Clock------------------------------------------------------------------------


hour = Label(tk,text='00',font=('Time New Roman',80,'bold'),bg='#135D66',fg='#E3FEF7')
hour.place(x=50,y=80,height=130,width=130)
hour_lbl = Label(tk,text='hour',font=('Time New Roman',20,'bold'),bg='#135D66',fg='#E3FEF7')
hour_lbl.place(x=50,y=220,height=40,width=130)


minutes = Label(tk,text='00',font=('Time New Roman',80,'bold'),bg='#135D66',fg='#E3FEF7')
minutes.place(x=230,y=80,height=130,width=130)
minutes_lbl = Label(tk,text='Min.',font=('Time New Roman',20,'bold'),bg='#135D66',fg='#E3FEF7')
minutes_lbl.place(x=230,y=220,height=40,width=130)


second = Label(tk,text='00',font=('Time New Roman',80,'bold'),bg='#135D66',fg='#E3FEF7')
second.place(x=410,y=80,height=130,width=130)
second_lbl = Label(tk,text='Sec.',font=('Time New Roman',20,'bold'),bg='#135D66',fg='#E3FEF7')
second_lbl.place(x=410,y=220,height=40,width=130)


Am_Pm = Label(tk,text='AM',font=('Time New Roman',80,'bold'),bg='#135D66',fg='#E3FEF7')
Am_Pm.place(x=590,y=80,height=130,width=200)
Am_Pm_lbl = Label(tk,text='AM/PM',font=('Time New Roman',20,'bold'),bg='#135D66',fg='#E3FEF7')
Am_Pm_lbl.place(x=590,y=220,height=40,width=200)


#----------------------------------------------Calender------------------------------------------------------------------------


date = Label(tk,text='11',font=('Time New Roman',80,'bold'),bg='#135D66',fg='#E3FEF7')
date.place(x=50,y=300,height=130,width=130)
date_lbl = Label(tk,text='Date',font=('Time New Roman',20,'bold'),bg='#135D66',fg='#E3FEF7')
date_lbl.place(x=50,y=440,height=40,width=130)


month = Label(tk,text='08',font=('Time New Roman',80,'bold'),bg='#135D66',fg='#E3FEF7')
month.place(x=230,y=300,height=130,width=130)
month_lbl = Label(tk,text='Month',font=('Time New Roman',20,'bold'),bg='#135D66',fg='#E3FEF7')
month_lbl.place(x=230,y=440,height=40,width=130)


year = Label(tk,text='08',font=('Time New Roman',80,'bold'),bg='#135D66',fg='#E3FEF7')
year.place(x=410,y=300,height=130,width=130)
year_lbl = Label(tk,text='Year',font=('Time New Roman',20,'bold'),bg='#135D66',fg='#E3FEF7')
year_lbl.place(x=410,y=440,height=40,width=130)


day = Label(tk,text='MON',font=('Time New Roman',60,'bold'),bg='#135D66',fg='#E3FEF7')
day.place(x=590,y=300,height=130,width=200)
day_lbl = Label(tk,text='Day',font=('Time New Roman',20,'bold'),bg='#135D66',fg='#E3FEF7')
day_lbl.place(x=590,y=440,height=40,width=200)

date_time()

tk.mainloop()