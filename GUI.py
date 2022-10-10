from ctypes import alignment
from tkinter import*
from tkinter import filedialog

from parso import split_lines

def main():
    root = Tk()
    gui = Window(root)
    gui.root.mainloop()
    return None

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
        button2 = Button(self.root, text="Process", justify="center", padx="50", pady="10", command="process_file").grid(row=1, column=7)

        #row2, labels
        Label(self.root,text="Transition Table", pady=10).grid(row=2, column=1, columnspan=4, sticky="w")
        Label(self.root,text="Input").grid(row=2, column=5, sticky="w")
        Label(self.root,text="Output").grid(row=2, column=7, sticky="w")

        #row3, trans table, input, output
        Label(self.root, text="State").grid(row=3, column=2, sticky="w")

            

    def load_file(self):
        filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File")
        tdfa = open(filename, 'r').read()
        tdfa_lines = open(filename, 'r').read().splitlines()
        print(tdfa)

        total_rows = len(tdfa_lines)
        temp = 4

        Label(self.root, text=tdfa[0]).grid(row=3, column=3, sticky="w")
        Label(self.root, text=tdfa[2]).grid(row=3, column=4, sticky="w")

        for i in range(total_rows):
            rowi = i + 4
            columnj = 1
            total_columns = len(tdfa_lines[i]) + 1

            for j in range(total_columns):

                if (tdfa[temp]=="," and tdfa[temp-1]=="\n"):
                    columnj += 1

                if (tdfa[temp]==","):
                    temp = temp + 1

                if (tdfa[temp]=="\n"):
                    temp = temp + 1
                    break

                else:
                    Label(self.root, text=tdfa[temp]).grid(row=rowi, column=columnj, sticky="w") 
                    columnj += 1
                    temp = temp + 1 
                
        filenamein = filedialog.askopenfilename(initialdir = "/", title = "Select a File") 
        fileinput = open(filenamein, 'r').read()
        lines = len(fileinput.readlines())
        
    def process_file():
        pass

main()