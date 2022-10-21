#this code file is the main logic of the program, it calls on the gui component to be able to execute the program

import GUI

#function to open the transition file and extracr the alphabet, transitions and the start and final states
def open_dfafile(dfa, input):

    trans = dfa
    trans=open(trans, 'r').read().splitlines()
    
    alphabet=trans[0].split(',')
    alpha_count = 0
    charac = ''

    fin_state=[]
    start_state=''
    transitions={}

    #start err checking
    #reads every line until end starting from the 2nd line
    for line in trans[1:]:
        alpha_count=len(alphabet)
        #splits every character separated by comma
        charac=line.split(',')

        #determines the final and start state s
        if charac[0] == '+':
            fin_state.append(charac[1].upper())
        elif charac[0] == '-':
            start_state=charac[1].upper()

        for i in range(0, alpha_count):
            #if i==0 then add item in dictionary
            if i==0:
                transitions[charac[1].upper()] = {alphabet[i]: charac[i+2].upper()}
            #else, update the item in the dictionary
            else:
                transitions[charac[1].upper()].update({alphabet[i]: charac[i+2].upper()})
    
    open_inputstring(start_state, alphabet, transitions, fin_state, input)

#opens the input string file, evaluate each line and produce a result in a .out file
def open_inputstring(start_state, alphabet, transitions, fin_state, filename):
    res = open('strings.out', 'w')

    with open(filename, 'r') as inputstrings:
        #gets the length
        x=len(inputstrings.readlines())
        
        #goes back to first line of the files
        line=inputstrings.seek(0)
        current_state = start_state

        #will check per line
        for i in range(0, x):
            err=False
            line = inputstrings.readline()

            #checks the input per line and produces an error message if the input is not valid to the corresponding dfa table
            for per in line:
                if(per!='\n') :
                    if per in alphabet:
                        current_state=transitions[current_state][per] 
                    else:
                        GUI.messagebox.showerror("Line ", i+1, "containing ", line," has an error!", per,"is not one of the alphabets")
                        err=True
                        break

            if err==False:
                #checks if the last state is the same as the final state
                if current_state in fin_state:
                    res.write('Valid\n')
                else:
                    res.write('Invalid\n')
    res.close()