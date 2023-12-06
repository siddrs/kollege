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


# IMAGE PATHS
# poweroff_icon = tk.PhotoImage(file=r".\assets\poweroff.png")
# reboot_icon = tk.PhotoImage(file=r".\assets\reboot.png")
# lock_icon = tk.PhotoImage(file=r".\assets\lock.png")
# logoff_icon = tk.PhotoImage(file=r".\assets\logoff.png")
# exit_icon = tk.PhotoImage(file=r".\assets\cancel.png")
# bolt_icon = tk.PhotoImage(file=r".\assets\bolt.png")
# root.iconbitmap(bolt_icon)

# SHUTDOWN BUTTONS
shutd_button = ttk.Button(
    root,
    text = "Power Off",
    # image = poweroff_icon,
    compound = tk.LEFT,
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
    # image = reboot_icon,
    compound = tk.LEFT,
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
    # image = logoff_icon,
    compound = tk.LEFT,
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
    # image = lock_icon,
    compound = tk.LEFT,
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
    # image = exit_icon,
    compound = tk.LEFT,
    command=lambda: root.quit()
)
exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()