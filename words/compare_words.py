from assemb_class import Assembly

potter = Assembly(potter_series)
print(potter)

with open("special_words.txt") as f:
    data = f.readlines()
new_data = list(map(lambda k: k.strip(), data))
print(new_data)
n= 0
for i in new_data:
    if i not in potter.words:
        n += 1
print(n)
