# 4. What will be the length of following set S:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?


print(s)                  # Ouput: {'20', 20}
print(len(s))                  # Ouput: 2