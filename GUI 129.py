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
        self.root.geometry("450x400")

        self.frame = Frame(self.root)

        Label(self.root,text="Transition Table",anchor="center").grid(row=1, column=0)
        Label(self.root,text="Input",anchor="center").grid(row=1, column=1)
        Label(self.root,text="Output",anchor="center").grid(row=1, column=2)

        button1 = Button(self.root, text="Load File", justify="center", padx="50", command="load_file")
        button1.grid(row=0, column=1)
        button2 = Button(self.root, text="Process", justify="center", padx="50", command="process_file")
        button2.grid(row=0, column=2)

    def load_file():

        pass

    def process_file():
        pass

main()