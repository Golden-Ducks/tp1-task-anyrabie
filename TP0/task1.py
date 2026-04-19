with open("task1.txt","r", encoding='utf-8') as f:
    text = f.read()
    
    #Removing punctuation
    punctuation = [',',':','(',')','.','!','?','-',';','"']
    for p in punctuation:
        if p in text:
            text = text.replace(p,'')
            
    #Romoving numbers
    for i in range(10):
        if str(i) in text:
            text = text.replace(str(i),'')
            
    #Removing symbols like @, #, $
    list_sym = ['@','#','$','%','&','*','/','\\','|','<','>','^','~']
    for s in list_sym:
        if s in text:
            text = text.replace(s,'')
            
    #Converting all words to lowercase
    text = text.lower()
    
    #Removing extra spaces
    text = ' '.join(text.split())
    
print(text)