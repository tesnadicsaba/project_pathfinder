import tkinter as tk
from tkinter import messagebox
from pathfinder import *


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.title = tk.Label(master=self, text="Helvetica", font=("Helvetica", 22), width=40)
        self.title["text"] = "PATHFINDER"
        self.title.pack()

        self.main_frame = tk.Frame(self, borderwidth=5, relief=tk.SUNKEN)
        self.main_frame.rowconfigure(0, minsize=5)
        self.main_frame.columnconfigure(0, minsize=5)

        #### option frame ####
        self.frame1 = tk.Frame(self.main_frame, borderwidth=1)
        self.frame1.rowconfigure(0, minsize=5)
        self.frame1.columnconfigure(0, minsize=5)

        self.option_label = tk.Label(master=self.frame1, text="Options", font=14)
        self.option_label.grid(row=0, column=0, pady=5, sticky="w")

        self.op3 = tk.IntVar()
        self.option3 = tk.Checkbutton(master=self.frame1, text="Show animation", variable=self.op3)
        self.option3.grid(row=3, column=0, pady=2, sticky="w")
        self.op4 = tk.IntVar()
        self.option4 = tk.Checkbutton(master=self.frame1, text="Show route", variable=self.op4)
        self.option4.grid(row=4, column=0, pady=2, sticky="w")

        self.frame1.grid(row=0, column=0, sticky='w')

        #### Coordinates ####

        self.frame2 = tk.Frame(self.main_frame, borderwidth=1)
        self.frame2.rowconfigure(0, minsize=5)
        self.frame2.columnconfigure(0, minsize=5)

        self.coord_label = tk.Label(master=self.frame2, text="Coordinates", font=14)
        self.coord_label.grid(row=0, column=0, pady=5, sticky="w")

        self.start_label = tk.Label(master=self.frame2, text="Start (X and Y, between 0-249):")
        self.start_label.grid(row=1, column=0, pady=5)

        self.start_X = tk.IntVar()
        self.start_entry_X = tk.Entry(master=self.frame2, width=5, textvariable=self.start_X)
        self.start_entry_X.grid(row=1, column=1, padx=5, pady=5)
        self.start_Y = tk.IntVar()
        self.start_entry_Y = tk.Entry(master=self.frame2, width=5, textvariable=self.start_Y)
        self.start_entry_Y.grid(row=1, column=2, pady=5)

        self.goal_label = tk.Label(master=self.frame2, text="Goal (X and Y, between 0-249):")
        self.goal_label.grid(row=2, column=0, pady=5)

        self.goal_X = tk.IntVar()
        self.goal_entry_X = tk.Entry(master=self.frame2, width=5, textvariable=self.goal_X)
        self.goal_entry_X.grid(row=2, column=1, padx=5, pady=5)
        self.goal_Y = tk.IntVar()
        self.goal_entry_Y = tk.Entry(master=self.frame2, width=5, textvariable=self.goal_Y)
        self.goal_entry_Y.grid(row=2, column=2, pady=5)

        #### number of neighbours ####

        self.nrn_label = tk.Label(master=self.frame2, text="Number of neighbours", font=14)
        self.nrn_label.grid(row=3, column=0, pady=5, sticky="w")

        self.radio_b_value = tk.IntVar()
        self.radio_b_value.set(8)
        self.radio_b_1 = tk.Radiobutton(master=self.frame2, text='4 neighbours', variable=self.radio_b_value, value=4)
        self.radio_b_1.grid(row=4, column=0, sticky="w")
        self.radio_b_2 = tk.Radiobutton(master=self.frame2, text='8 neighbours', variable=self.radio_b_value, value=8)
        self.radio_b_2.grid(row=5, column=0, sticky="w")

        #### start button ####

        self.start_button = tk.Button(self.main_frame, text="START", width=20, command=self.start)
        self.start_button.grid(row=3, column=0, sticky="s", pady=20)

        self.frame2.grid(row=1, column=0, sticky='w')
        self.main_frame.pack(side=tk.LEFT, pady=20)

        img = tk.PhotoImage('fig.png')
        self.llable = tk.Label(self, image=img)
        self.llable.pack()

    def start(self):

        if self.start_X.get() < 0 or self.start_X.get() > 249 \
                or self.start_Y.get() < 0 or self.start_Y.get() > 249 \
                or self.goal_X.get() < 0 or self.goal_X.get() > 249 \
                or self.goal_Y.get() < 0 or self.goal_Y.get() > 249:
            messagebox.showerror('Invalid input', 'Please give valid values to the coordinates\n (Integers between 0-249)')
        else:
            self.broadcast_data()

    def broadcast_data(self):
        pathf = pathfinder([self.start_X.get(), self.start_Y.get()], [self.goal_X.get(), self.goal_Y.get()],
                           self.op3.get(), self.op4.get(),
                           self.radio_b_value.get())
        distance, steps = pathf.show_dist_steps()

        messagebox.showinfo('Result', f'Distance to goal: {distance}\nSteps to goal: {steps} ')

        if self.op4.get() == 1:
            pathf.show_path()


root = tk.Tk()
root.geometry('310x540')
app = App(master=root)
app.mainloop()
