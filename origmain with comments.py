#function to open the transition file
def open_dfafile():
    trans=open('transitions.dfa', 'r').read().splitlines()

    alphabet=trans[0].split(',')
    print('Alphabets: ', alphabet)

    fin_state=[]
    start_state=''
    transitions={}
    current_state=NULL

    #reads every line until end starting from the 2nd line
    for line in trans[1:]:
        alpha_count=len(alphabet)
        #splits every character separated by comma
        charac=line.split(',')
        length=len(charac)-1

        print("charac:", charac)

        #checks if the number of alphabet is equal to
        if(alpha_count+1)!=length:
            print("Error in dfa file")
            exit() 
        
        #determines the final and start state 
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

    for transit in transitions:
        print(transit, "=", transitions[transit])

    #ang naa sa dfa func kay fin_state
    #ang naa sa input func kay current state
    #if current state remains NULL then call input func
    open_inputstring(start_state, alphabet, transitions, fin_state, current_state)
    #else (current state and final state  is not equal to NULL)
    #then ready na siya for processing
    #so call result

#opens the input string file
def open_inputstring(start_state, alphabet, transitions, fin_state):
    with open("strings.in", 'r') as inputstrings:
        #gets the length
        x=len(inputstrings.readlines())
        
        #goes back to first line of the files
        line=inputstrings.seek(0)
        current_state = start_state

        #will check per line
        for i in range(0, x):
            err=False
            line = inputstrings.readline()

            for per in line:
                if(per!='\n') :
                    #KANI KAY FOR CHECKING NI IF ANG NAA SA INPUT STRING KAY KATONG SA ALPHABET LANG
                    #SO DIRA SA ELSE KAY MAG DISPLAY GURU MSG IF 
                    if per in alphabet:
                        current_state=transitions[current_state][per] 
                    else:
                        print("Line ", i+1, "containing ", line," has an error!", per,"is not one of the alphabets")
                        err=True
                        break

            if err==False: #and final state is not null then call result
                result(current_state, fin_state)
            
#function that makes the strings.out file
def result(current_state, fin_state):
    with open('strings.out', 'a+') as res:
         #checks if the last state is the same as the final state
            if current_state in fin_state:
                res.write('Valid\n')
            else:
                res.write('Invalid\n')
    open('string.out', 'w')



#opens the functions for testing
open_dfafile()