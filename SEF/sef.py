import json
import tkinter as root
from tkinter import *
import tkinter.font as rootfont
import random

with open('./data.json', encoding="utf8") as f:
    data = json.load(f)
    
questions = [v for v in data[0].values()]
answers_choice = [v for v in data[1].values()]
answers = [1,1,1,1,1,1,2,1,3,3,1,2] 
user_answer = []
indexes = []

def gen():
    global indexes
    while(len(indexes) < 5):
        x = random.randint(0,11)
        if x in indexes:
            continue
        else:
            indexes.append(x)

def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(root1,background = "#ffffff",border = 0,)
    labelimage.pack(pady=(50,30))
    labelresulttext = Label(root1,font = ("Consolas",20),background = "#ffffff",)
    labelresulttext.pack(pady=(0,5))
    labelresult = Label(root1,text=str(score)+" / 25",font = ("Consolas",15),background = "#e6e6e6",)
    labelresult.pack()
    if score >= 20:
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Are Excellent !!")
    elif (score >= 10 and score < 20):
        img = PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Can Be Better !!")
    else:
        img = PhotoImage(file="bad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Should Work Hard !!")

def calc():
    global indexes,user_answer,answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
        x += 1
    print(score)
    showresult(score)

ques = 1
def selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2,r3,r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 5:
        lblQuestion.config(text= questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques += 1
    else:
        calc()
    
def startquiz():
    global lblQuestion,r1,r2,r3,r4
    lblQuestion = Label(root1,text = questions[indexes[0]],font = ("Consolas", 16),width = 500,justify = "center",wraplength = 400,background = "#ffffff",)
    lblQuestion.pack(pady=(100,30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(root1,text = answers_choice[indexes[0]][0],font = ("Times", 12),value = 0,variable = radiovar,command = selected,background = "#ffffff",)
    r1.pack(pady=5)

    r2 = Radiobutton(root1,text = answers_choice[indexes[0]][1],font = ("Times", 12),value = 1,variable = radiovar,command = selected,background = "#ffffff",)
    r2.pack(pady=5)

    r3 = Radiobutton(root1,text = answers_choice[indexes[0]][2],font = ("Times", 12),value = 2,variable = radiovar,command = selected,background = "#ffffff",)
    r3.pack(pady=5)

    r4 = Radiobutton(root1,text = answers_choice[indexes[0]][3],font = ("Times", 12),value = 3,variable = radiovar,command = selected,background = "#ffffff",)
    r4.pack(pady=5)

def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    btnStart1.destroy()
    label2.destroy()
    gen()
    startquiz()
def jumbleIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    label1.destroy()
    btnStart.destroy()
    btnStart1.destroy()
    text1 = root.Text(root1,bg='white',fg='green',height=30, width=70)
    text1.insert(root.END, '\n')
    text1.pack(side=root.LEFT,pady=10)
    text3= root.Text(root1,bg='black',fg='white',height=5, width=30)
    text3.pack(side=root.BOTTOM,padx=0,pady=40)
    fon = rootfont.Font(family="Arial", size=10, weight="bold")
    text3.configure(font=fon)
    text3.insert("1.0","Required Output:\n")
    with open('cpgo.txt', 'r') as f:
        text3.insert("2.0", f.read())
    text3.configure(state='disabled')
    with open('cpg1.txt', 'r') as f:
        text1.insert("1.0", f.read())
    text2 = root.Text(root1, height=5, width=30,bg='black',fg='white')
    scroll = root.Scrollbar(root1, command=text2.yview)
    text2.configure(yscrollcommand=scroll.set)
    text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
    text2.tag_configure('big', font=('Verdana', 20, 'bold'))
    text2.tag_configure('color',foreground='white',font=('Tempus Sans ITC', 12, 'bold'))
    text2.tag_bind('follow','<1>',lambda e, t=text2: t.insert(root1.END, "Not now, maybe later!"))
    quote = """
    \n\t       Status
    """
    fontExample = rootfont.Font(family="Verdana", size=10, weight="bold", slant="italic")
    text2.insert(root.END, quote, 'color')
    text2.pack(side=root.LEFT,padx=10,pady=10)
    text2.configure(font=fontExample)
    def ok():
        text2.delete(1.0,root.END)
        s=text1.get("1.0",'end-1c')
        print(s)
        with open('sample.txt','w') as o:
            o.write(s)
        with open('cpg.txt','r') as o:
           with open('sample.txt','r') as o1:
               quote=""" """
               l=o.readlines()
               l1=o1.readlines()
               c,k=0,0
               c1=len(l)
               for i in range(len(l)):
                   if(l[i]==l1[i]):
                       c=c+1
               if(c>c1):
                   c=c-2*(c-c1)
               k=round((c/c1)*100,2)
               per="\nAccuracy: "+str(k)+"%"
               text2.insert("4.0","")
               if(l==l1):
                   quote="""Status:\n\tHurray! You got it\n"""
               else:
                   quote="""Status:\n\tTry Again\n"""
               text2.insert("2.0",quote)
               text2.insert("3.0",per)
    b= Button(root1,text='Submit',height=2,width=10,command=ok)
    b.pack(side=root.BOTTOM)
root1 = root.Tk()
root1.title("Student Evaluation Form")
root1.geometry('1000x700')
root1.configure(bg='#e6e6e6')
root1.resizable(0,0)

img1 = PhotoImage(file="std1.png")

labelimage = Label(root1,image = img1,background = "#ffffff",)
labelimage.pack(pady=(40,0))

labeltext = Label(root1,text = "Student Evaluation Form",font = ("Comic sans MS",28,"bold"),background = "#e6e6e6",)
labeltext.pack(pady=(0,50))

start = PhotoImage(file="Start3.png")
label1 = Label(root1,text = "Quiz",font = ("Comic sans MS",22,"bold"),background = "#e6e6e6",)
label2 = Label(root1,text = "JCS",font = ("Comic sans MS",22,"bold"),background = "#e6e6e6",)
btnStart = Button(root1,text="Quiz",image=start,relief = FLAT,border = 0,command = startIspressed,)
btnStart1 = Button(root1,text="Jumbled Code",image=start,relief = FLAT,border = 0,command = jumbleIspressed,)
label1.pack()
btnStart.pack()
label2.pack()
btnStart1.pack()

lblInstruction = Label(root1,text = "Read The Rules And\nClick Start Once You Are ready",background = "#e6e6e6",font = ("Consolas",14),justify = "center",)
lblInstruction.pack(pady=(10,10))

value = "<1> This quiz contains 5 questions\nOnce you select a radio button that will be a final choice\nhence think before you select\n\n<2> Solve the Jumbled Code Accurately"

lblRules = Label(root1,text =value ,width = 200,font = ("Times",14),background = "#000000",foreground = "#FACA2F",)
lblRules.pack(side=BOTTOM)

root1.mainloop()