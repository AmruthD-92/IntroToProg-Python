# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Amruth D,17thMay2023,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
try:
    with open(objFile, "r") as file:
        for line in file:
            task, priority = line.strip().split(",")
            dicRow = {"Task": task, "Priority": priority}
            lstTable.append(dicRow)
except FileNotFoundError:
    print("No existing data file found. Starting with an empty list.")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        if not lstTable:
            print("No data available.")
        else:
            print("Current Data:")
            for row in lstTable:
                print(f"Task: {row['Task']}, Priority: {row['Priority']}")
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        task = input("Enter the task: ")
        priority = input("Enter the priority: ")
        dicRow = {"Task": task, "Priority": priority}
        lstTable.append(dicRow)
        print("Task added.")
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        if not lstTable:
            print("No data available.")
        else:
            task = input("Enter the task to remove: ")
            found = False
            for row in lstTable:
                if row["Task"].lower() == task.lower():
                    lstTable.remove(row)
                    found = True
                    break
            if found:
                print("Task removed.")
            else:
                print("Task not found.")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        with open(objFile, "w") as file:
            for row in lstTable:
                file.write(f"{row['Task']},{row['Priority']}\n")
        print("Data saved to file.")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        input('Press Enter to exit .... !') #Confirming before exiting
        break  # and Exit the program
