import os
import tkinter as tk
from tkinter import ttk

# FUNCTION DEFINITIONS 
def shutdown():
    os.system("shutdown /s /t 1") 

def reboot():
    os.system("shutdown /r /t 1")

def logoff():
    os.system("shutdown /l")

def lockpc():
    os.system(r'"C:\Windows\System32\rundll32.exe user32.dll,LockWorkStation"')


# TKINTER WINDOW
root = tk.Tk()
root.geometry('300x400')
root.resizable(False, False)
root.title('Power Options')


# SHUTDOWN BUTTONS
shutd_button = ttk.Button(
    root,
    text = "Power Off",
    command = shutdown
)
shutd_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

# REEBOT BUTTON
reboot_button = ttk.Button(
    root,
    text = "Reebot",
    command = reboot
)
reboot_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

# LOG OFF BUTTON
logoff_button = ttk.Button(
    root,
    text = "Log Off",
    command = logoff
)
logoff_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

# LOCK BUTTON
lock_button = ttk.Button(
    root,
    text = "Lock",
    command = lockpc
)
lock_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

# EXIT BUTTON
exit_button = ttk.Button(
    root,
    text='Exit',
    command=lambda: root.quit()
)
exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()