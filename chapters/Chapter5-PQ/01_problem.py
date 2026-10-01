# 1. Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

words = {
   "Seb" : "Apple",
   "Aam" : "Mango",
   "kela": "Banana"
}

word = input("Enter the words which you want to meaning of: ")

print(words, type(words))
print(words[word])