from tkinter import *
from tkinter import ttk

class ChatBot: 
    def __init__(self,root):
        self.root=root
        self.root.title("Get Help")
        self.root.geometry("800x600+0+0")
        self.root.bind('<Return>',self.enter_func)
        self.root.configure(bg="#2980B9")

        main_frame=Frame(self.root,bd=4,bg='#2980B9',width=610)
        main_frame.pack()

        title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,text="I'm here to help",font=('Times New Roman',30,'bold'),fg='#800080',bg='#1ABC9C')
        title_label.pack(side=TOP)

        title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,text="Tell us your problem so we can get you the right help and support.",font=("Times New Roman",20),fg='#800080',bg='#1ABC9C')
        title_label.pack(side=TOP)

        title_label=Label(main_frame,relief=RAISED,anchor='n',text="Example:What is python?",font=("Times New Roman",20),fg='#800080',bg='#1ABC9C')
        title_label.pack(side=BOTTOM)


        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=20,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()


        btn_frame=Frame(self.root,bd=2,bg='Teal',width=800)
        btn_frame.pack()

        self.entry=StringVar() 
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=('arial',16,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="Send",command=self.send,font=('arial',16,'italic'),width=8,bg='#85929E')
        self.send.grid(row=0,column=2,padx=5,sticky=W)
        
        self.clear=Button(btn_frame,text="Clear",command=self.clear,font=('arial',16,'italic',),width=8,bg='#85929E',fg='black')
        self.clear.grid(row=0,column=0,padx=5,sticky=W)

        self.msg=''
        self.label_2=Label(btn_frame,text=self.msg,font=('Times new roman',15,'bold'),fg='#00FFFF',bg='#008080')
        self.label_2.grid(row=1,column=1,padx=5,sticky=W)


    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')

    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')

    def send(self):
        send='YOU: '+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)

        if(self.entry.get()==''):
            self.msg='Please enter some input'
            self.label_2.config(text=self.msg,fg='pink')

        else:
            self.msg=''
            self.label_2.config(text=self.msg,fg='purple')

        if(self.entry.get()=='hello'):
            self.text.insert(END,'\n'+"Alex: Hi")
            
        elif(self.entry.get()=='hi'):
            self.text.insert(END,'\n'+"Alex: hello")

        elif(self.entry.get()=='hey'):
            self.text.insert(END,'\n'+"Alex: hello")

        elif(self.entry.get()=='hai'):
            self.text.insert(END,'\n'+"Alex: hello")

        elif(self.entry.get()=='I am good'):
            self.text.insert(END,'\n'+"Alex: That's nice")

        elif(self.entry.get()=='i am good'):
            self.text.insert(END,'\n'+"Alex: That's nice")    

        elif(self.entry.get()=='i am your owner'):
            self.text.insert(END,'\n'+"Alex: Hello! I'm your virtual Assistant")
        
        elif(self.entry.get()=='who are you'):
            self.text.insert(END,'\n'+"Alex: I am bot your personal assisstant")

        elif(self.entry.get()=='how are you'):
            self.text.insert(END,"\n"+"Alex: I doing fine and you are")

        elif(self.entry.get()=='what about you'):
            self.text.insert(END,"\n"+"Alex: I doing good")

        elif(self.entry.get()=='do you have any feelings'):
            self.text.insert(END,"\n"+"Alex: I am a bot, I don't have any feelings")

        elif(self.entry.get()=='good'):
            self.text.insert(END,'\n'+"Alex: That's great")

        elif(self.entry.get()=='i am hungry'):
            self.text.insert(END,'\n'+'Alex: Then eat something you are craving for')

        elif(self.entry.get()=='not good'):
            self.text.insert(END,'\n'+'Alex: Why what happen')
            
        elif(self.entry.get()=='bye'):
            self.text.insert(END,'\n'+'Alex: See ya!')

        elif(self.entry.get()=='thank you'):
            self.text.insert(END,'\n'+'Alex: Your welcome!')

        elif(self.entry.get()=='do you love music'):
            self.text.insert(END,'\n'+'Alex: yes I do')

        elif(self.entry.get()=='i love musics'):
            self.text.insert(END,'\n'+'Alex: I too love it!')

        elif(self.entry.get()=='I am hungry'):
            self.text.insert(END,'\n'+'Alex: Then eat something you are craving for')

        elif(self.entry.get()=='give me some advice'):
            self.text.insert(END,'\n'+'Alex: About what?')

        elif(self.entry.get()=='I am not feeling well'):
            self.text.insert(END,'\n'+'Alex: If I were you, I would go to the internet and type exactly what you wrote here')

        elif(self.entry.get()=='have you done eating'):
            self.text.insert(END,'\n'+"Alex: I don't like eating anything because I'm a bot obviosly")
  
        elif(self.entry.get()=='what is your name'):
            self.text.insert(END,'\n'+"Alex: I'm Alex, a bot")

        elif(self.entry.get()=='I am sad'):
            self.text.insert(END,'\n'+'Alex: Hear some musics')

        elif(self.entry.get()=='what is python?'):
            self.text.insert(END,'\n'+"Alex: Python is a multi-paradigm programming language")

        elif(self.entry.get()=='What is python?'):
            self.text.insert(END,'\n'+"Alex: Python is a multi-paradigm programming language")

        elif(self.entry.get()=='What is python'):
            self.text.insert(END,'\n'+"Alex: Python is a multi-paradigm programming language")

        elif(self.entry.get()=='what is the use of python'):
            self.text.insert(END,"\n"+"Alex: python is mainly used in Artificial intelligence and Data Science")

        elif(self.entry.get()=='what is meant by bot or chatbot'):
            self.text.insert(END,"\n"+"Alex: Chatbot is a computer program, which is used to help humans to solve their issues.")

        else:
            self.text.insert(END,'\n'+"Alex: My apologise! I didn't get it")
            
       
if __name__ == '__main__':
    root=Tk()
    obj=ChatBot(root)
    root.mainloop()
