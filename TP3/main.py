
# Online Python - IDE, Editor, Compiler, Interpreter
import math

DFs = {
    'luna':1,
    'eat':1,
    'food':2,
    'dog':1,
    'love':1,
    'ai':1,
    'massive':1
}

N = 3
def IDF(word):
    
    return math.log((N+1)/(DFs[word]+1)) + 1
    
for token,_ in DFs.items():
    print(f"IDF({token}) = {IDF(token)}")
        
    
