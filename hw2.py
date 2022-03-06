def reverse(sentence, reverse_word):
#return "invalis input" if sentence and reverse_word not a strings    
    if not(type(reverse_word)==str and type(sentence)==str):
        return("invalid input")        
    idx = sentence.find(reverse_word)
    if idx != -1: # if reverse_word found in sentence
#concatenation of sentence the new variable by index 
        new_sentence = sentence[0:idx]+sentence[idx:idx+len(reverse_word)][::-1]+sentence[idx+len(reverse_word):]
        return new_sentence
    else:
        return("The word was not found")

