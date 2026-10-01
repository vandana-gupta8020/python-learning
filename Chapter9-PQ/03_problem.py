# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13-year old.

"""
This program creates multiplication tables from 2 to 20
and writes each table into a separate file inside a folder named "tables"
"""
# Function to generate a multiplication table for a given number 'n'
def generateTable(n):
    table = ""     # Create an empty string to store the table content
    
    # Loop from 1 to 10 to create the multiplication lines
    for i in range(1, 11):
        # Append each line to the table string using f-string formatting. For example: "2 X 1 = 2"
        table += f"{n} X {i} = {n*i}\n"     # here, '+=' operator takes that new line and adds it to whatever is already stored in table.
        
    # Open (or create) a new text file inside the "tables" folder
    # The file will be named like table_2.txt, table_3.txt, ..., table_20.txt
    # "w" means write mode – it will overwrite the file if it already exists
    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)        # Write the complete table string into the file
            
# Loop through numbers from 2 to 20(inclusive) & call the generateTable function for each number
for i in range(2, 21):
    generateTable(i)        # This creates and saves the multiplication table for number 'i'