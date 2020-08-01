def to_pig_latin(sentence):
    i = 0
    while i < (len(sentence)-1): #length of sentence changes!!! use while
        if sentence[i] in {'a','e','i','o','u'} and (i == 0 or sentence[i-1] ==' '):
            while sentence[i] != ' ' and i < (len(sentence)-1):
                i +=1
            if i == len(sentence) -1:
                sentence = sentence[:i+1] + 'way' + sentence[i+2:]
            else:
                sentence = sentence[:i] + 'way ' + sentence[i+1:]
        elif sentence[i] not in {'a','e','i','o','u'} and (i == 0 or sentence[i-1] ==' '):
            x =''
            while (sentence[i] != ' ' and sentence[i] not in {'a','e','i','o','u'}) and i < (len(sentence)-1):
                x += sentence[i]
                sentence = sentence = sentence[:i] + '' + sentence[i+1:]
            while sentence[i] != ' '  and i < (len(sentence)-1):
                i += 1
            if i == len(sentence) -1:
                sentence = sentence[:i+1] + 'a' + x + 'ay' + sentence[i+2:]
            else:
                sentence = sentence[:i] + 'a' + x + 'ay '+ sentence[i+1:]
        i +=1#length of sentence changes!!!!
    return sentence
def to_english(e):
    sentence = e.split(" ")
    english = ""
    for word in sentence:
      #If word ends with way,Remove  
        if word[:len(word) - 4:-1] == 'yaw':
            english += word[:len(word) - 3] + " " 
        else: #Remove the ay at the end and return the cons.
            noay = word[:len(word) - 2]
            firstcons = noay.split("a")[-1]
            removedcons = noay[:len(noay) - (len(firstcons)+1)]
            english += firstcons + removedcons + " "
    return english