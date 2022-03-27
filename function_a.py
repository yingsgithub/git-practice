def most_common_value(number_list):
    """ returns the most common element of the list
    """
    frenquence_count = {}
    for num in number_list:
        if not num in frenquence_count:
            frenquence_count[num] = 1
        else:
            frenquence_count[num] += 1
    print(frenquence_count)
    value_with_most_count = []
    max_value = 0
    for key, value in frenquence_count.items():
        if value > max_value:
            max_value = value
            value_with_most_count.append(key)
    return value_with_most_count

nums = [1, 1, 3, 3, 3, 7, 8, 2, 1, 3]
result = most_common_value(nums)
print(result)
# if __name__ == "__main__":
#     nums = [1, 1, 3, 3, 3, 7, 8, 2, 1, 3]
#     print(f"Most common value = {most_common_value(nums)}")
