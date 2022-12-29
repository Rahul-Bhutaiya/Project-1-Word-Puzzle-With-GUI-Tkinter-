from tkinter import *
from random import sample
from tkinter import messagebox

main_layout=Tk()
main_layout.title('Word Puzzle')
# main_layout.attributes('-fullscreen',True)
main_layout.state('zoomed')
main_layout.iconbitmap('image\puzzle_logo.ico')

count,score=0,0
word_list=['father','break','country','green','aeroplane','india','creative','power','computer','python','website','koo','neuralink','english','vaccine','engine','advocate','ancient','beyond','campaign','champion','circle','citizen']

def play():

    btn1.config(state='disabled')
    words=sample(word_list,5)



    def loop(btn3):
        if count>0:
            btn3.config(state='disabled')
            
        def check(word,user_val,ent_obj):
            btn2.config(state='disabled')
            if word.lower()==user_val.lower():
                lbl6=Label(page,text='Correct Answer',font=('Baskerville Old Face',15,'underline','bold'),bg='#AA00FF')
                lbl6.place(x=545,y=350)
                glob=globals()
                glob['score']+=100
                lbl5.config(text='score : %d'%glob['score'])
            else:
                ent_obj.delete(0,END)
                ent_obj.insert(0,'Incorrect Answer')

                lbl7=Label(page,text='Correct Answer : %s'%word.upper(),font=('Baskerville Old Face',15,'underline','bold'),bg='#AA00FF')
                lbl7.place(x=545,y=350)
                
                glob=globals()
                glob['score']-=100
                lbl5.config(text='score : %d'%glob['score'])

            if count<5:
                btn3=Button(page,text='Next',bg='#AA00FF',font=('Baskerville Old Face',14,'bold'),borderwidth=2,relief='solid',width=6,activebackground='#1c1d1e',activeforeground='#fff',command=lambda:loop(btn3))
                btn3.place(x=650,y=550)
            else:
                lbl5.config(text='Final Score : %d'%score)
                lbl5.place(x=550,y=500)


        
        glob_count=globals()
        glob_count['count']+=1

        page=Toplevel(bg='#AA00FF')
        page.state('zoomed')
        page.iconbitmap('image\puzzle_logo.ico')

        lbl3=Label(page,text='Arrange The Following Word',font=('Baskerville Old Face',25,'underline','bold'),bg='#AA00FF')
        lbl3.place(x=475,y=100)
        lbl4=Label(page,text='%d. %s'%(count,''.join(sample(words[count-1],len(words[count-1]))).upper()),font=('Baskerville Old Face',20,'bold'),bg='#AA00FF')
        lbl4.place(x=540,y=250)
        lbl5=Label(page,text='score : %d'%score,font=('Baskerville Old Face',20,'bold'),bg='#AA00FF')
        lbl5.place(x=10,y=665)

        ent_obj=Entry(page,width=20,font=('Baskerville Old Face',20,'bold'))
        ent_obj.place(x=545,y=300)
        btn2=Button(page,text='check',bg='#AA00FF',font=('Baskerville Old Face',14,'bold'),borderwidth=2,relief='solid',width=6,activebackground='#1c1d1e',activeforeground='#fff',command=lambda:check(words[count-1],ent_obj.get(),ent_obj))
        btn2.place(x=840,y=300)

        btn4=Button(page,text='Exit',bg='#AA00FF',font=('Baskerville Old Face',14,'bold'),borderwidth=2,relief='solid',width=6,activebackground='#1c1d1e',activeforeground='#fff',command=main_layout.destroy)
        btn4.place(x=1250,y=30)

        page.mainloop()
            
    loop(count)


fr1=Frame(main_layout,height=1000,width=1500,bg='#AA00FF')
fr1.grid(row=0, column=0)

lbl1=Label(fr1,text='Word Puzzle',font=('Baskerville Old Face',30,'underline','bold'),bg='#AA00FF')
lbl1.place(x=575,y=100)

lbl2=Label(fr1,text="Hey! You Have To Arrange The Letters to Form Valid Words...",font=('Baskerville Old Face',15,'bold'),bg='#AA00FF')
lbl2.place(x=400,y=150)

btn1=Button(fr1,text='Start',bg='#AA00FF',font=('Baskerville Old Face',15,'bold'),borderwidth=2,relief='solid',width=10,activebackground='#1c1d1e',activeforeground='#fff',command=play)
btn1.place(x=618,y=250)

btn4=Button(fr1,text='Exit',bg='#AA00FF',font=('Baskerville Old Face',14,'bold'),borderwidth=2,relief='solid',width=6,activebackground='#1c1d1e',activeforeground='#fff',command=main_layout.destroy)
btn4.place(x=1250,y=30)

main_layout.mainloop()
