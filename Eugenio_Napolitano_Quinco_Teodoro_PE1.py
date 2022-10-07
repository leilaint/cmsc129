#open the transition file
trans=open('transitions.dfa', 'r').read().splitlines()

#alphabet=[]
alphabet=trans[0].split(',')
print('Alphabets: ', alphabet)

fin_state=[]
start_state=''
transitions={}

#reads every line until end starting from the 2nd line
for line in trans[1:]:
    alpha_count=len(alphabet)
    #splits every character separated by comma
    charac=line.split(',')
    length=len(charac)

    #checks if the number of alphabet is equal to
    if(alpha_count+1)==length:
        continue
    else:
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

#opens the input string file
with open(r"strings.in", 'r') as inputstrings:
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

        if err==False:
            #checks if the last state is the same as the final state
            if current_state in fin_state:
                print(line, ' ===> VALID')
            else:
                print(line, ' ===> INVALID')
            
