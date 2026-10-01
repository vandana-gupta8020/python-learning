# 2. Write a program to fill in a letter template given below with name and date. 

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
        '''
        
print(letter.replace("<|Name|>", "Vandana"))
print(letter.replace("<|Date|>", "Feb,13"))
print(letter.replace("<|Name|>", "Vandana").replace("<|Date|>", "Feb,13"))         # Chaining process
