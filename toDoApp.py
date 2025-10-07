# toDoApp.py
import os

def clearScreen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')

tasks=[]
file_path = "addtask.txt"
if os.path.exists(file_path):
    with open("addtask.txt", 'r') as file:
            str = file.readlines()
            for s in str:
                tasks.append(s.strip())

def addTask(task) :
    tasks.append(task)
    print("Task Added!")
    writeFile()

def showTasks( ):
    if len(tasks)==0 :
      print("No Tasks Present")
    else:
     for i in range (len(tasks)):
      print(i+1,".",tasks[i])

def removeTask(tasknumber):
    tasks.pop(tasknumber-1) 
    print("Task Removed!")
    writeFile()

def writeFile():
    with open("addtask.txt", "w") as f:    
        for str in tasks:
            f.write(str + "\n")

def main():
    while True:
        print("="*20)      
        print("[1] - Add Task")
        print("[2] - Show Tasks")
        print("[3] - Remove Task")
        print("[4] - Exit")
        print("="*20) 

        ch = input("Enter Number Choice(1-4): ")
        if ch=="1":
            clearScreen()
            t = input("Enter Task Name: ")
            addTask(t)
        elif ch=="2":
            clearScreen()
            showTasks()
        elif ch=="3":
            clearScreen()
            print("0 . Cancel")
            showTasks()
            while True:
                n=int(input("Enter Task Number to Remove: "))
                if (0<n and n<=(len(tasks))):
                    removeTask(n)
                    break
                elif (n==0):
                    break
                else:
                    print("Choice was Invalid Please Try Again")
        elif ch=="4":
            break
        else:
            print("Choice was Invalid Please Try Again")
main()
