students = []
a = []
b = []
c = []

# FUNCTION FOR POPULATING LISTS
def genList(LIST=[]):
    n = int(input("Enter the Number of Students: "))
    print("Enter the Roll Numbers: ")
    for i in range(0, n):
        e = int(input())
        LIST.append(e)
    return LIST

# REMOVING DUPLICATES
def removeDup(LIST, TEMP = []):
    for i in LIST:
        if i not in TEMP:
            TEMP.append(i)
    return TEMP

# POPULATING THE LISTS

#print("---- Class Details ----")
#students = genList()
#studets = removeDup(students)
#print ("\n ---- For Group A ----")
#a = genList()
#a = removeDup(a)
#print("\n ---- For Group B ----")
#b = genList()
#b = removeDup(b)
#print("\n ---- For Group C ----")
#c = genList()
#c = removeDup(c)

print ("\n ---------- MENU ----------")
while True:
    print("Choose a Task from 1, 2, 3, 4, 5")
    print("1: Task A")
    print("2: Task B")
    print("3: Task C")
    print("4: Task D")
    print("5: Exit")
    choice = int(input("Enter the Task Choice: "))
    if choice == 1:
        print("TASK 1")
    elif choice == 2:
        print("TASK 2")
    elif choice == 2:
        print("TASK 2")
    elif choice == 2:
        print("TASK 2")
    elif choice == 5:
        break
    else:
        print("Enter a Valid Task Choice: (1, 2, 3, 4, 5)")
