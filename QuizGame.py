from tkinter import*
import random
from tkinter import messagebox

window= Tk()

def quizgame():
    global label3,list1,x,label2,label1,entry,j,score,wan,score1
    window = Tk()
    window.geometry("620x540")
    score=0
    wan=0
    list1=["Δίνεται μια μεταβλητή b=19. Τι θα εμφανίζει η εντολή print(b//5);\n1) b//5\n2) 3\n3) 3.8\n4) 19//5","2"],\
    ["Δίνεται μια μεταβλητή a=3. Τι θα εμφανίζει η εντολή print(a**5);\n1) 243\n2) a**5\n3) 15\n4) 3**5","1"],\
    ["Τι επιστρέφει μια συνάρτηση η οποία δεν περιέχει την εντολή return;\n1) nothing\n2) none\n3) return\n4) -","2"],\
    ["Με ποια εντολή η python μετατρέπει κείμενο σε ακέραιο;\n1) str\n2) float\n3) int\n4) num","3"],\
    ["Τι θα εμφανίσει η εντολή print( 10%3);\n1) 3.3\n2) 3\n3) 10%3\n4) 1","4"],\
    ["Τι θα εμφανίσει η εντολή print((4 + 8) / 2);\n1) (4 + 8) / 2 \n2) 6\n3) 6.0\n4) Τίποτα. Περιέχει λάθος","3"],\
    ["this_is_a_list=[7,'yoda',3,'error'],\n Τι εκτυπώνει η εντολή print(this_is_a_list[3]);\n1) yoda \n2) 3\n3) 7\n4)error","4"]

    j=0

    score1=score


    def start(event):
        global label3, list1, score, wan, j,entry,x,score1
        x = 1

        if x==1:

            entry = Entry(window, font=('Times', 20, 'bold'), width=16)
            entry.grid(column=0, row=2, pady=3, padx=40)
            entry.delete(0, "end")
            label2.destroy()
            label3.configure(text=list1[j][0])

            if entry.get() == list1[j][1]:
                score1 = score1 +1
                yordle()
            else:
                wan=wan+1
                yordle()



            print(j)


    def yordle():

        global j,x,label3,score,wan

        if j <= 5:
            j = j + 1
        elif j == 6:
            x = 0
            messagebox.showinfo("Your Score", "Correct Answers: " + str(score1) + "\nFalse Answers: " + str(wan))
            print(score1)




    label1 = Label(window, text="Python Test!", font=('Times', 20, 'bold'))
    label1.grid(column=0, row=0, pady=3, padx=40)
    label2 = Label(window, text="Press Enter to Start!", font=('Times', 20, 'bold'))
    label2.grid(column=0, row=1, pady=3, padx=40)
    label3 = Label(window, text="", font=('Times', 20, 'bold'))
    label3.grid(column=0, row=1, pady=3, padx=20)




    window.bind("<Return>",start)
def colorgame():
    global time
    global score
    colors = ['Red', 'Blue', 'White', 'Black', 'Pink', 'Yellow', 'Orange', 'Purple', 'Cyan', 'Brown']

    score = 0
    time = 30

    win = Tk()
    win.geometry('250x300')

    def startgame(event):
        if time == 30:
            countdown()
        nextColor()

    def nextColor():
        global score
        global time
        if time > 0:
            txt1.focus_set()
            if txt1.get().lower() == colors[1].lower():
                score += 1

            txt1.delete(0, END)
            random.shuffle(colors)
            lbl4.config(fg=str(colors[1]), text=str(colors[0]))
            lbl2.config(text="Score: " + str(score))

    def countdown():
        global time
        if time > 0:
            time -= 1
            lbl3.config(text="Time left: " + str(time))
            lbl3.after(1000, countdown)

    lbl1 = Label(win, text="Type in the color of the words shown below.")
    lbl1.grid(column=0, row=0)
    lbl2 = Label(win, text="Press Enter to start")
    lbl2.grid(column=0, row=1)
    lbl3 = Label(win, text="Time left:")
    lbl3.grid(column=0, row=3)
    lbl4 = Label(win)
    lbl4.grid(column=0, row=4)

    txt1 = Entry(win)
    txt1.grid(column=0, row=6)

    win.bind('<Return>', startgame)
def exit():
    window.destroy()


lbl1= Label(window, text= "Welcome", width= 20, height= 20, font=('Times', 15, 'bold'))
lbl1.grid(column= 0, row= 0)
lbl2= Label(window, text= "What is you Name?", font=('Times', 15))
lbl2.grid(column=0, row= 1)
txt1= Entry(window, width= 30)
txt1.grid(column=1, row= 1)
btn1= Button(window, text= "ColorGame", width= 10, height= 8, relief= 'raised', command= colorgame)
btn1.grid(column= 1, row= 3)
btn2= Button(window, text= "QuizGame", width= 10, height= 8, relief= 'raised', command= quizgame)
btn2.grid(column= 1, row= 4)
btn3= Button(window, text= "Exit", width= 10, height= 8, relief= 'raised', command= exit )
btn3.grid(column= 1, row= 5)

window.mainloop()