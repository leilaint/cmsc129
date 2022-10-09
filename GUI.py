from ctypes import alignment
from tkinter import*
from tkinter import filedialog
from tkinter.ttk import Treeview

def main():
    root = Tk()
    gui = Window(root)
    gui.root.mainloop()
    return None

class Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Strings and DFA")
        #self.root.geometry("450x400")

        #row0, "margins"
        Label(self.root,text="     ").grid(row=0, column=0, columnspan=5)
        Label(self.root,text="     ").grid(row=0, column=0, rowspan=5)
        Label(self.root,text="     ").grid(row=0, column=5, rowspan=5)
        Label(self.root,text="     ").grid(row=6, column=0, columnspan=5)

        #row1, buttons
        button1 = Button(self.root, text="Load File", justify="center", padx="100", pady="10", command="load_file").grid(row=1, column=1, columnspan=2)
        Label(self.root,text="     ").grid(row=1, column=3)
        button2 = Button(self.root, text="Process", justify="center", padx="50", pady="10", command="process_file").grid(row=1, column=4)

        #row2, labels
        Label(self.root,text="Transition Table", pady=10).grid(row=2, column=1, sticky="w")
        Label(self.root,text="Input").grid(row=2, column=2, sticky="w")
        Label(self.root,text="Output").grid(row=2, column=4, sticky="w")

        #row3, trans table, input, output
        transition = [('-','A','B','A'),
            (' ','B','B','C'),
            ('+','C','B','A')]

        total_rows = len(transition)
        total_columns = len(transition[0])
        
        for i in range(total_rows):
            for j in range(total_columns):
                 Label(self.root, text=transition[i][j]).grid(row=i+3, column=j,sticky="w") #di nako makuha how to get rid mga spaces T_T

       # input  = 
            

    def load_file():
        filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("dfa files",
                                                        "*.dfa*"),
                                                       ("in files",
                                                        "*.in")))
        

    def process_file():
        pass

main()