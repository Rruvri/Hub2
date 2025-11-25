import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
window.title("RaviHUB")



#mainframe.grid(column=0, row=0)


def goals_gui_constructor(mastergoals):
    mainframe = ttk.Frame(window)
    title = tk.Label(master=mainframe, text="Daily Goals")
    title.pack()
    for item in mastergoals.active_goals:
        goal_label = tk.Label(master=mainframe, text=item)
        goal_content = tk.Label(master=mainframe, text=mastergoals.active_goals[item])
        goal_label.pack()
        goal_content.pack()
    
    window.mainloop()


