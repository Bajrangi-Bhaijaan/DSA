class Solution:
    def sortSentence(self, s):
        
        splited_string = s[::-1].split() # here first we are reversing the sting and then spliting it, split() function make each word of the string as a separate element of the list.  For example: ['3a', '1sihT', '4ecnetnes', '2si']
        splited_string.sort() # as we are having number in front of each word now, we can sort the list.
        
        res = [] # taking empty list to save the result. 
        
        for word in splited_string: # travering the splited string. 
            res.append(word[1:][::-1]) # here by doing "[1:]" we are eradicating number from the word & by doing "[::-1]" we are reversing back the word, that we reversed at one step of the solution. Here res will have "['This', 'is', 'a', 'sentence']  
        return " ".join(res) # in res we are having list of words, now we want a string with words separated -> "This is a sentence". 