# python code to check the dfa input for errors
import Main

def dfaerrchecking(trans):
    trans=open(trans, 'r').read().splitlines()
    
    alphabet=trans[0].split(',')
    for line in trans[1:]:
        alpha_count=len(alphabet)
        #splits every character separated by comma
        charac=line.split(',')
        length=len(charac)-1

        #checks if the number of alphabet is equal
        if(alpha_count+1)!=length:
            return False
        else:
            return True