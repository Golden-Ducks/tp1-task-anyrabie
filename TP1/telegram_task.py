import string
def funt_norm(text):
    #Lowering the text
    text = text.lower()
    
    #Removing punctuation
    for o in string.punctuation: #(string bib is a pure library for python, instead, i used a list of punctuation in task1.py, but here i used the string library to get all the punctuation characters)
        if o in text:
            text = text.replace(o,'')
    
    #Converting digits to words
    digits = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }
    
    for digt, word in digits.items():
        if digt in text:
            text = text.replace(digt, word)
    

    print('Normalized text:', text)
    
D1 = "Today she cooked 4 bourak. Later, she added two chamiyya and 1 pizza."
D2 = "Five pizza were ready, but 3 bourak burned!"
D3 = "We only had 8 chamiyya, no pizza, and one tea."
D4 = "Is 6 too much? I ate nine bourak lol."

funt_norm(D1)
funt_norm(D2)
funt_norm(D3)
funt_norm(D4)
