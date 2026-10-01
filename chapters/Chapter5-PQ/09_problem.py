# 9. Can you change the values inside a list which is contained in set S?
S = {8, 7, 12, "Harry", [1,2]}



# Answer: We can't change the values inside a list because the list can't be included into sets.Python sets only allow immutable (unchangeable) types as elements. But a list is mutable, so Python throws an error when you try to include a list inside a set.

# TypeError: unhashable type: 'list'
