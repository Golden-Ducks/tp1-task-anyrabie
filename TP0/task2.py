import string

with open('task2.txt','r', encoding='utf-8') as f:
    text = f.read()
    
    #Lowering the text
    text  = text.lower()
    
    #Removing punctuation
    for p in text:
        if p in string.punctuation:
            text = text.replace(p,'')
    
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
    for s in text:
        if s.isdigit():
            text = text.replace(s, digits[s])
    
    #Removing extra spaces
    text = ' '.join(text.split())
    
    #Expanding contractions
    common_contractions = {
        "can’t": "cannot",
        "won’t": "will not",
        "i’m": "i am",
        "he’s": "he is",
        "she’s": "she is",
        "it’s": "it is",
        "we’re": "we are", 
        "they’re": "they are",
        "i’ve": "i have",
        "i’ll": "i will",
        "don’t": "do not",
        "doesn’t": "does not",
    }
    
    for contraction, exp_contraction in common_contractions.items():
        if contraction in text:
            print(f"Expanding contraction: {contraction} to {exp_contraction}")
            text = text.replace(contraction, exp_contraction)
        else:
            print(f"No contraction found for: {contraction}")
            
    #print(text)
    
    #Creating new file to save the normalised text
    with open('normalised_text.txt','w', encoding='utf-8') as f:
        f.write(text)
