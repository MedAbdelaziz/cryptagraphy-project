from tkinter import ttk
import tkinter as tk
import Porta as pr
import viginere as vg
import transposition as tr
import chiffre_affine as ca
import construction_verticale as cv 

#msg="SRMYT EPFOG CBYAH"
#key='NAPLES'

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        # Create the application variable.
        self.algo=0
        self.msg = tk.StringVar()
        self.key = tk.StringVar()
        self.submit=tk.Button(root,text="submit")
        self.submit.pack(side="bottom" )
        self.pack()
        self.menuBar=tk.Menu(master)
        menu_file= tk.Menu(self.menuBar, tearoff=0)
        menu_file.add_command(label="Horizontale",command=lambda: self.execute_algo(1))
        menu_file.add_command(label="Verticale",command=lambda: self.execute_algo(2))
        menu_file.add_command(label="tranposition",command=lambda: self.execute_algo(3))
        menu_file.add_command(label="Vigenere",command=lambda: self.execute_algo(4))
        menu_file.add_command(label="Porta", command=lambda: self.execute_algo(5))
        self.menuBar.add_cascade(label="algorithm", menu=menu_file)
        master.config(menu=self.menuBar)
        self.msgInput = tk.Entry(self, textvariable=self.msg.get())
        self.keyInput = tk.Entry(self, textvariable=self.key.get())
        self.msgInput.pack()
        self.keyInput.pack()

        
        # Set it to some value.
        self.msg.set("write the message here")
        self.key.set("put key here")
        # Tell the entry widget to watch this variable.
        #self.keyInput["textvariable"] = self.key

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.msgInput.bind('<Key-Return>',
                             self.print_contents)
        self.keyInput.bind('<Key-Return>',
                             self.print_contents)       

    def print_contents(self, event):
        print("The crypted message:",
              self.msg.get())
        print("the key is:", self.key.get())
        print(pr.dechiffrer(self.key.get(),self.msg.get()))
    
    def execute_algo(self,i=0):
        self.algo=i
        


root = tk.Tk()
myapp = App(root)
myapp.master.title("Cryptography App")
myapp.master.minsize(500,400)
myapp.mainloop()