sp = ["abccba", "level", "world", "hello", "madam", "ring"]
print(list(filter(lambda x: x == x[::-1], sp)))