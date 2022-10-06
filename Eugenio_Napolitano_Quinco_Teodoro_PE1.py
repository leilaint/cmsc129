trans=open('transitions.dfa', 'r').read().splitlines()

#alphabet=[]
alphabet=trans[0].split(',')
print('Alphabets: ', alphabet)

fin_state=[]
start_state=''
transitions={}

#reads every line until end starting from the 2nd line
for line in trans[1:]:
    #splits every character separated by comma
    charac=line.split(',')

    #determines the final and start state 
    if charac[0] == '+':
        fin_state.append(charac[1])
    elif charac[0] == '-':
        start_state=charac[1]
    
    for i in range(0, len(alphabet)):
        #if i==0 then add item in dictionary
        if i==0:
            transitions[charac[1]] = {alphabet[i]: charac[i+2]}
        #else, update the item in the dictionary
        else:
            transitions[charac[1]].update({alphabet[i]: charac[i+2]})


#opens the input string file
with open(r"strings.in", 'r') as inputstrings:
    #gets the length
    x = len(inputstrings.readlines())
    
    #goes back to first line of the files
    line=inputstrings.seek(0)

    #will check per line
    for i in range(0, x):
        current_state = start_state
        line = inputstrings.readline()

        for per in line:
            if(per!='\n'):
                current_state=transitions[current_state][per]
    
        #checks if the last state is the same as the final state
        if current_state in fin_state:
            print('VALID')
        else:
            print('INVALID')
