def most_common_value(number_list):
    """ returns the most common element of the list
    """
    num_dic={}
    for nums in number_list:
        if nums in num_dic:
            num_dic[nums]+=1
        else:
            num_dic[nums]=1

    most_often=0
    for nums in num_dic:
        if num_dic[nums]> most_often:
            most_often=num_dic[nums]
            common_key=nums
    return common_key
nums = [1, 1, 3, 3, 3, 7, 8, 2, 1, 3]
print(f"Most common value = {most_common_value(nums)}")  
answer= most_common_value(nums) 

# if __name__ == "__main__":
#     nums = [1, 1, 3, 3, 3, 7, 8, 2, 1, 3]
#     print(f"Most common value = {most_common_value(nums)}")
