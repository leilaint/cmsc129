from ctypes import alignment
from tkinter import*

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

        #row4, status


    def load_file():

        pass

    def process_file():
        pass

main()