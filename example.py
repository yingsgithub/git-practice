number_list = [1, 1, 3, 3, 3, 7, 8, 2, 1, 3]
frenquence_count={}
for num in number_list:
    if num in frenquence_count:
        frenquence_count[num] += 1
    else:
        frenquence_count[num] = 1
print(frenquence_count)