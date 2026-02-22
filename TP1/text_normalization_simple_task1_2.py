import contractions


def text_normalization(text):
    #Lowercase
    text_norm = text.lower()
    #Removing punctuation
    punctuation = [',',':','(',')','.','!','?','-',';','"']
    for p in punctuation:
        if p in text_norm:
            text_norm = text_norm.replace(p,'')
    #Conerting numbers to words
    digit_ = {
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

    for digit, word in digit_.items():
        text_norm = text_norm.replace(digit, word)

    #Expanding contractions
    text_norm = contractions.fix(text_norm) # Using the contractions library seen in class jsut to test it out, but we can also do it manually like in task2.py
    
    return text_norm

text = "Wow!! This cow ran fast & ate 3 apples."
normalized_text = text_normalization(text)
print('Simple Task 1:',normalized_text)
originaltext = "I'm sure the cow will stop the ducks from fighting soon!!. let's see how it goes. The cow is very fast and can eat 3 apples in a minute."
normalized_original_text = text_normalization(originaltext)
print('Simple Task 2:',normalized_original_text)# this include expanding contractions


