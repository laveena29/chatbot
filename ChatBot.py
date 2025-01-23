import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import sys
import turtle 
import time
import random
import datefinder
import winsound
#import wolframalpha
import tkinter as tk
#from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer
from playsound import playsound
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
from fpdf import FPDF


'''try:
    app = wolframalpha.Client('QQ2RT6-VYLTGH6LE7')
except Exception:
    print("Sorry some feature is not working")'''


engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)
print(voice[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
        print("Good morning!")
    elif hour>=12 and hour<17:
        speak("Good afternoon!")
        print("Good afternoon!")  
    else:
        speak("Good evening!")
        print("Good evening!")
    speak("Jarvis signing in, fueled and ready, sir")
    print("Jarvis signing in, fueled and ready, sir")
    
    speak("For more information just ask what can you do")
    
    

def takeCommand():
    # it takes a microphone input and retuns output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-in')
        print("User said", query)

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("krishpandey2004@gmail.com","68apex68")
    server.sendmail("krishpandey2004@gmail.com",to,content)
    server.close




if __name__ == '__main__':
    wishMe()
    #while True:
    while True:
        query = input()
        if "wikipedia" in query:
            input("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "what can you do" in query:
            speak("You can tell me to open google, youtube, play music, tell you the time, search on wikipedia or send an email and more")
            speak('Here is a list to help you:')
            print('''          Just say == it will do this
                    something wikipedia == search wikipedia for that something
                    open youtube        == opens youtube
                    open google         == opens google
                    play music          == plays music
                    the time            == tells the time
                    open vs code        == opens vs code
                    sends an email      == sends email
                    convert text        == opens file converter
                    set alarm           == sets alarm
                    a list              == opens a to do list
                    can we talk         == starts the chatbot feature 
                    play game           == asks to play which game (snake game and rock paper scicorrs) 
                    Note:
                    Inside play game you can play snake game or rock paper scissors
                    play snake game     == opens snake game
                    play rps            == opens rock paper scissors
                    ''')
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "play music" in query:
            music_dir = "C:\\Users\\lavee\\Downloads\\project"
            songs = os.listdir(music_dir) 
            os.startfile(os.path.join(music_dir , songs[0]))
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("The time is")
            speak(strTime)
        elif "open vs code" in query:    
            codePath = ""
            os.startfile(codePath)
        elif "send email" in query:
            try:
                speak("Write the email address of the receiver")
                to = str(input("Write the email address of the receiver: "))

                speak("what should i write in the email")    
                content = input()
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("sorry my friend. I am not able to send the email ")

        #elif "temperature" or "whether" or "a question" in query:
            '''res = app.query(query)
            op = next(res.results).text
            print(res)'''
            
      
           

        elif "convert text" in query:
            root= tk.Tk()

            canvas1 = tk.Canvas(root, width = 300, height = 600, bg = 'black', relief = "raised")
            canvas1.pack()

            label1 = tk.Label(root, text='File Conversion Tool', bg = 'black',fg = 'white')
            label1.config(font=('helvetica', 20))
            canvas1.create_window(150, 60, window=label1)

            def getTxt ():
                global read_file
                
                import_file_path = filedialog.askopenfilename()
                read_file = pd.read_csv(import_file_path)
                
            browseButtonTxt = tk.Button(text="      Import Text File     ", command=getTxt, bg='green', fg='white', font=('helvetica', 12, 'bold'))
            canvas1.create_window(150, 130, window=browseButtonTxt)

            def convertToCsv ():
                global read_file
                
                export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
                read_file.to_csv (export_file_path, index = None)

            saveAsButtonCsv = tk.Button(text='Convert Text To CSV', command=convertToCsv, bg='green', fg='white', font=('helvetica', 12, 'bold'))
            canvas1.create_window(150, 180, window=saveAsButtonCsv)
            def con_pdf():
                # save FPDF() class into  
                # a variable pdf 
                pdf = FPDF()    
                
                # Add a page 
                pdf.add_page() 
                
                # set style and size of font  
                # that you want in the pdf 
                pdf.set_font("Arial", size = 15) 
                
                # open the text file in read mode 
                f = open(filedialog.askopenfilename(),'r')
                
                # insert the texts in pdf 
                for x in f: 
                    pdf.cell(200, 10, txt = x, ln = 1, align = 'C') 
                
                # save the pdf with name .pdf 
                export_file_path = filedialog.asksaveasfilename(defaultextension='.pdf')
                pdf.output(export_file_path+'.pdf') 

                
            saveAsButtonPdf = tk.Button(text='Import And Convert Text To PDF', command=con_pdf, bg='green', fg='white', font=('helvetica', 12, 'bold'))
            canvas1.create_window(150, 230, window=saveAsButtonPdf)
            def exitApplication():
                MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
                if MsgBox == 'yes':
                    root.destroy()

                
            exitButton = tk.Button (root, text='       Exit Application     ',command=exitApplication, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
            canvas1.create_window(150, 280, window=exitButton)

            


            root.mainloop()
        
        elif "set alarm" in query:
            from datetime import datetime
            speak("Enter the time at which the alarm will ring")
            alarmtime = str(input("Enter the time at which the alarm will ring: "))
            while True:
                lcltime = datetime.now().strftime('%H:%M')
                if lcltime == alarmtime:
                    playsound("Alarm01.wav")
                    break
                else:
                    print("not yet")
                    time.sleep(30)



               
       
        
        elif "a list" in query:
            def add(event):
                
            
                lst.insert(tk.END, entry.get())
                v.set("")
            
            
            def delete(event):
                
                lst.delete(tk.ANCHOR)
            
            
            def save(event):
                
                with open("data.txt", "w") as file:
                    file.write("\n".join(lv.get()))
                label["text"] = "Data saved"
            
            
            def getdata():
                "grab saved data"
                if "data.txt" in os.listdir():
                    with open("data.txt") as file:
                        for line in file:
                            lst.insert(tk.END, line.strip())
            
            
            root = tk.Tk()
            root.geometry("400x400+500+10")
            root.title("To do list ")
            lab1 = tk.Label(
                root, text="TODO List, \nEnter to add items, \nSelect to delete Items, ctr+s to save")
            lab1.pack()
            
            v = tk.StringVar()
            entry = tk.Entry(root, textvariable=v)
            entry.pack()
            
            
            lv = tk.Variable()
            lst = tk.Listbox(root, listvariable=lv)
            lst.pack()
            lst.bind("<Double-Button>", delete)
            
            entry.bind("<Return>", add)
            root.bind("<Control-s>", save)
            
            label = tk.Label(root)
            label.pack()
            
            # Grab the saved data
            getdata()
            
            root.mainloop()
        
                
       
        elif "can we talk" in query:
            chatbot = ChatBot('bot')

            trainer = ChatterBotCorpusTrainer(chatbot)

            trainer.train('chatterbot.corpus.english')

            while True:
                queryT = takeCommand()
                speak(chatbot.get_response(queryT))
                if "exit" in queryT:
                    break



        elif "play Rock" or "am bored" in query:
            if "play game" in query:
                speak("Would you like to play snake game or rock paper scissor")
                ty = input()
                if "play RPS" in ty:
                    comp_wins = 0
                    player_wins = 0

                    def Choose_Option():
                        print("Chose rock, paper or scissors:")
                        speak("Chose rock, paper or scissors:")
                        user_choice = input()
                        if user_choice in ["Rock", "rock"]:
                            user_choice = "r"
                        elif user_choice in ["Paper", "paper"]:
                            user_choice = "p"
                        elif user_choice in ["Scissors", "scissors"]:
                            user_choice = "s"
                        else:
                            print("I don't understand, try again.")
                            speak("I don't understand, try again.")
                        
                        return user_choice
                    def Computer_Option():
                        comp_choice = random.randint(1,3)
                        if comp_choice == 1:
                            comp_choice = "r"
                        if comp_choice == 2:
                            comp_choice = "p"
                        if comp_choice == 3:
                            comp_choice = "s"
                        return comp_choice

                    speak("would you like to play rock paper scissors?")
                    g = input()
                    if g == "yes":
                        while True:
                            print("")
                            user_choice = Choose_Option()
                            comp_choice = Computer_Option()
                            print("")
                            

                            if user_choice == "r":
                                if comp_choice == "r":
                                    print("You chose rock. \nThe computer chose rock.\nIts a tie")
                                    speak("You chose rock. \nThe computer chose rock.\nIts a tie")
                                if comp_choice == "p":
                                    print("You chose rock. \nThe computer chose paper.\nThe computer wins")
                                    speak("You chose rock. \nThe computer chose paper.\nThe computer wins")
                                    comp_wins += 1
                                if comp_choice == "s":
                                    print("You chose rock. \nThe computer chose scissors.\nYou win")
                                    speak("You chose rock. \nThe computer chose scissors.\nYou win")
                                    player_wins += 1
                            if user_choice == "p":
                                if comp_choice == "r":
                                    print("You chose paper. \nThe computer chose rock.\nYou win")
                                    speak("You chose paper. \nThe computer chose rock.\nYou win")
                                    player_wins += 1
                                if comp_choice == "p":
                                    print("You chose paper. \nThe computer chose paper.\nIts a tie")
                                    speak("You chose paper. \nThe computer chose paper.\nIts a tie")
                                if comp_choice == "s":
                                    print("You chose paper. \nThe computer chose scissors.\nThe computer wins")
                                    speak("You chose paper. \nThe computer chose scissors.\nThe computer wins")
                                    comp_wins += 1
                            if user_choice == "s":
                                if comp_choice == "r":
                                    print("You chose scissors. \nThe computer chose rock.\nThe computer wins")
                                    speak("You chose scissors. \nThe computer chose rock.\nThe computer wins")
                                    comp_wins += 1
                                if comp_choice == "p":
                                    print("You chose scissors. \nThe computer chose paper.\nYou win")
                                    speak("You chose scissors. \nThe computer chose paper.\nYou win")
                                    player_wins += 1
                                if comp_choice == "s":
                                    print("You chose scissors. \nThe computer chose scissors.\nIts a tie")
                                    speak("You chose scissors. \nThe computer chose scissors.\nIts a tie")
                            print("")
                            print("Your wins :"+ str(player_wins))
                            speak("Your wins:"+ str(player_wins))
                            print("My wins:"+ str(comp_wins))
                            speak("My wins:"+ str(comp_wins))
                            print("")
                            
                            speak("Do you want to play(yes or no)")
                            user_choice = takeCommand()
                            if user_choice in["no"]:
                                break
                            elif user_choice in ["yes"]:
                                pass
                            else:
                                break
                elif "play snake game" in ty:
                    delay = 0.1

                    # Score
                    score = 0
                    high_score = 0 

                    # Set up the screen
                    wn = turtle.Screen()
                    wn.title("@Snake game")
                    wn.bgcolor("black")
                    wn.setup(width=600, height=600)
                    wn.tracer(0) # Turns off the screen updates

                    # Snake head
                    head = turtle.Turtle()
                    head.speed(0)
                    head.shape("square")
                    head.color("green")
                    head.penup()
                    head.goto(0,0)
                    head.direction = "stop"

                    # Snake food
                    food = turtle.Turtle()
                    food.speed(0)
                    food.shape("circle")
                    food.color("red")
                    food.penup()
                    food.goto(0,100)
                    food.shapesize(0.5)

                    segments = []

                    # Pen
                    pen = turtle.Turtle()
                    pen.speed(0)
                    pen.shape("square")
                    pen.color("white")
                    pen.penup()
                    pen.hideturtle()
                    pen.goto(0, 260)
                    pen.write("Score: 0  High Score: 0", align="center", font=("Ariel", 24, "normal"))

                    # Functions
                    def go_up():
                        if head.direction != "down":
                            head.direction = "up"

                    def go_down():
                        if head.direction != "up":
                            head.direction = "down"

                    def go_left():
                        if head.direction != "right":
                            head.direction = "left"

                    def go_right():
                        if head.direction != "left":
                            head.direction = "right"

                    def move():
                        if head.direction == "up":
                            y = head.ycor()
                            head.sety(y + 20)

                        if head.direction == "down":
                            y = head.ycor()
                            head.sety(y - 20)

                        if head.direction == "left":
                            x = head.xcor()
                            head.setx(x - 20)

                        if head.direction == "right":
                            x = head.xcor()
                            head.setx(x + 20)

                    # Keyboard bindings
                    wn.listen()
                    wn.onkeypress(go_up, "w")
                    wn.onkeypress(go_down, "s")
                    wn.onkeypress(go_left, "a")
                    wn.onkeypress(go_right, "d")

                    # Main game loop
                    while True:
                        wn.update()

                        # Check for a collision with the border
                        if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
                            time.sleep(1)
                            head.goto(0,0)
                            head.direction = "stop"

                            # Hide the segments
                            for segment in segments:
                                segment.goto(1000, 1000)
                            
                            # Clear the segments list
                            segments.clear()

                            # Reset the score
                            score = 0

                            # Reset the delay
                            delay = 0.1

                            pen.clear()
                            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


                        # Check for a collision with the food
                        if head.distance(food) < 20:
                            # Move the food to a random spot
                            x = random.randint(-290, 290)
                            y = random.randint(-290, 290)
                            food.goto(x,y)

                            # Add a segment
                            new_segment = turtle.Turtle()
                            new_segment.speed(0)
                            new_segment.shape("square")
                            new_segment.color("grey")
                            new_segment.penup()
                            segments.append(new_segment)

                            # Shorten the delay
                            delay -= 0.001

                            # Increase the score
                            score += 10

                            if score > high_score:
                                high_score = score
                            
                            pen.clear()
                            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

                        # Move the end segments first in reverse order
                        for index in range(len(segments)-1, 0, -1):
                            x = segments[index-1].xcor()
                            y = segments[index-1].ycor()
                            segments[index].goto(x, y)

                        # Move segment 0 to where the head is
                        if len(segments) > 0:
                            x = head.xcor()
                            y = head.ycor()
                            segments[0].goto(x,y)

                        move()    

                        # Check for head collision with the body segments
                        for segment in segments:
                            if segment.distance(head) < 20:
                                time.sleep(1)
                                head.goto(0,0)
                                head.direction = "stop"
                            
                                # Hide the segments
                                for segment in segments:
                                    segment.goto(1000, 1000)
                            
                                # Clear the segments list
                                segments.clear()

                                # Reset the score
                                score = 0

                                # Reset the delay
                                delay = 0.1
                            
                                # Update the score display
                                pen.clear()
                                pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

                        time.sleep(delay)

                    wn.mainloop() 
                else:
                    speak("ok")
            else:
                if "exit" in query:
                    speak("Alright then it was nice talking to you")
                    exit()
                else:
                    speak("soryy i did not understand")