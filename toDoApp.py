# toDoApp.py
import os

def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')

tasks=[]

def addtask(task) :
  tasks.append(task)
  print("Task Added!")

def showTasks( ):
    if len(tasks)==0 :
      print("No Tasks Present")
    else:
     for i in range (len(tasks)):
      print(i+1,".",tasks[i])

def removetask(tasknumber):
    tasks.pop(tasknumber-1) 
    print("Task Removed!")

def main():
    while True:
        #TO DO Make Beautiful GUI
        print("1.Add Task")
        print("2.Show Tasks")
        print("3.Remove Task")
        print("4.Exit")

        ch = input("Enter Number Choice(1-4): ")
        if ch=="1":
            clear_screen()
            t = input("Enter Task Name: ")
            addtask(t)
        elif ch=="2":
            clear_screen()
            showTasks()
        elif ch=="3":
            clear_screen()
            showTasks()
            n=int(input("Enter Task Number to Remove: "))
            removetask(n)   
        elif ch=="4":
            break
        else:
            print("Choice was Invalid Please Try Again")
main()
