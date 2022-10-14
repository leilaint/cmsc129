#this file is the GUI component of the program

from asyncio.windows_events import NULL
from tkinter import*
from tkinter import filedialog
import tkinter
from Main import *
from err_checking import dfaerrchecking
import tkinter.messagebox

#these varibles store the file paths of the table and the input file
dfa_path = ""
input_path = ""

#the gui class main, imports the tkinter import
def main():
    root = Tk()
    gui = Window(root)
    gui.root.mainloop()
    return None

#this class contains all the buttons, methods and properties of the window
class Window:

    def __init__(self, root):
        self.root = root
        self.root.title("Strings and DFA")

        #row0, "margins"
        Label(self.root,text="     ").grid(row=0, column=0, columnspan=8)
        Label(self.root,text="     ").grid(row=0, column=0, rowspan=6)
        Label(self.root,text="     ").grid(row=0, column=8, rowspan=6)
        Label(self.root,text="     ").grid(row=7, column=0, columnspan=8)

        #row1, buttons
        button1 = Button(self.root, text="Load File", justify="center", padx="100", pady="10", command=self.load_file).grid(row=1, column=1, columnspan=5)
        Label(self.root,text="     ").grid(row=1, column=6)
        button2 = Button(self.root, text="Process", justify="center", padx="50", pady="10", command=self.process_file).grid(row=1, column=7)

        #row2, labels
        Label(self.root,text="Transition Table", pady=10).grid(row=2, column=1, columnspan=4, sticky="w")
        Label(self.root,text="Input").grid(row=2, column=5, sticky="w")
        Label(self.root,text="Output").grid(row=2, column=7, sticky="w")

    #this function serves as the function to open the files and call for errorchecking before displaying in the window
    def load_file(self):
        
        filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File")

        tdfa = open(filename, 'r').read()
        tdfa_lines = open(filename, 'r').read().splitlines()
        total_rows = len(tdfa_lines)

        #processes the dfa file for display
        if filename.endswith('.dfa'):
            Label(self.root, text="State", padx="1").grid(row=3, column=2, sticky="w")
            
            #error checking for the dfa table
            err = dfaerrchecking(filename)

            if (err == True):
                
                global dfa_path
                dfa_path = filename
                
                temp = 0
                columnj = 3

                for i in range(total_rows):
                    rowi = i + 3
                    total_columns = len(tdfa_lines[i])

                    for j in range(total_columns):

                        if (tdfa[temp]=="," and tdfa[temp-1]=="\n"):
                            columnj += 1

                        if (tdfa[temp]==","):
                            temp = temp + 1

                        if (tdfa[temp]=="\n"):
                            columnj = 1
                            temp = temp + 1
                            break

                        else:
                            Label(self.root, text=tdfa[temp]).grid(row=rowi, column=columnj, sticky="w")
                            columnj += 1
                            temp = temp + 1
            else:
                tkinter.messagebox.showerror("Error","Error in dfa file")
        
        #processes the .in file for display
        if filename.endswith('.in'):
            
            global input_path
            input_path = filename

            temp = 0

            for i in range(total_rows):
                rowi = i + 3
                columnj = 5

                Label(self.root, text=tdfa_lines[temp]).grid(row=rowi, column=columnj, sticky="w")
                temp = temp + 1

    #function that calls the main to process the fike and produce results
    def process_file(self):
        open_dfafile(dfa_path, input_path)

        #display output
        output = open('strings.out', 'r').read().splitlines()
        total_rows = len(output)
        temp = 0

        for i in range(total_rows):
            row = i+3
            Label(self.root, text=output[i]).grid(row=row, column=7, sticky="w")

main()