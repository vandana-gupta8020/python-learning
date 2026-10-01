# 7. Write a python function to remove a given word from a list ad strip it at the same time.


# def rem(l, word):
#     for item in l:
#         l.remove(word)
#         return l

# l = ["Harry", "Carry", "Cherry", "Merry", "jerry", "rry"]

# print(rem(l, "rry"))


def rem(l, word):
    n =[]
    for item in l:
        if not (item ==word):
            n.append(item.strip(word))
        
    return n

l = ["Harry", "Carry", "Cherry", "Merry", "jerry", "rry"]

print(rem(l, "rry"))