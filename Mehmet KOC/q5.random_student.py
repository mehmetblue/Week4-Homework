"""
BONUS QUESTION 
5) Random Student (Problem Solving Example)

General Information:
I want to choose a random student in Pyton Class-2 Coursiers

Acceptance Criteria:

* Make changes to the random student codes that has been shared with you.
* In current state, the program chooses a random one from the list when the button is pressed.
* What is expected of you is to ensure that the selected person is not selected during 3 hands.
(As we talk about in the lesson)

"""

from multiprocessing.connection import wait
import random
import tkinter as tk


def random_student(std_list=["Emrullah Bey", "Ertan Bey", "Fethullah Bey", "Furkan Bey", 
    "Hasan Bey", "Mehmet Bey", "Ömer Bey", "Tayyip Bey", 
    "Yunus Emre Bey", "Merve Hanım", "Mustafa Bey", "Murat Bey"],
    waiting_list = []):
    
    ## selecting a random student from the list
    student = random.sample(std_list, 1)

    ## removing the selected student from the list
    std_list.remove(student[0])

    ## adding the removed student to the waiting list
    waiting_list += student

    ## checking the waiting list len for 
    # waiting the selected student
    if len(waiting_list) == 4:

        ## if waiting list is equal in len with waiting loop number,
        # append the selected student to the waiting list at the last index
        std_list.append(waiting_list[0])

        ## and delete the first index (waiting list len always be 3)
        del waiting_list[0]
    
    
    ## empty str for assinging the selected student
    str = ''
    
    ## for loop for converting item from list to string
    for i in student:
        str += i
    print(str)

    ## sending the selected student to the window
    label.config(text=str)       



## tkinker part

window = tk.Tk()



window.title("Random Student")
window.geometry("600x300")


key_application = tk.Frame(window)
key_application.grid()


# label
label_txt = tk.Label(key_application, text="Student name:", font="arial 15 bold")
label_txt.grid(padx=110, pady=10)


# label
label = tk.Label(key_application, text="Please push the botton to choose a next student ", font="arial 12")
label.grid(padx=110, pady=20)


# button
button1 = tk.Button(key_application, text=" CHOOSE ", width=50, height=5, command=random_student)
button1.grid(padx=110, pady=40)

window.mainloop()