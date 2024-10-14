# 1. Find sum of list elements
number = [1,2,3,3,4,5,6,6,7,9]
print("sum of list elements is",sum(number))
# 2. Find largest element in a list
print("largest element in the list is",max(number))
# 3. Remove Duplicates in a list
new_number = list(set(number))
print(new_number)
# 4. Check if all elements in a list are unique
if len(number) == len(set(number)):
    print("All elements in the list are unique")
else:
    print("All elements in the list are not unique")
# 5. Program to reverse list
print("Reverse list is",number[::-1])
# 6. Count number of odd and even numbers in a list
def count_odd_even(list):
    odd_count = sum(1 for x in list if x % 2 != 0)
    even_count = len(list) - odd_count
    return f"Odd numbers count: {odd_count}, Even numbers count: {even_count}"
print(count_odd_even(number))
# 7. Check if a list is a subset of another list
count = [1,2,3,4]
print(set(count).issubset(number))
# 8. Max difference between two consecutive elements in a list
def max_diff_consecutive(list):
    return max(abs(list[i] - list[i + 1]) for i in range(len(list) - 1))
print(max_diff_consecutive(number))
# 9. Merge multiple dictionaries
def merge_dictionaries(dicts):
    merged = {}
    for d in dicts:
        merged.update(d)
    return merged

dict1 = {'a': 2, 'b': 3}
dict2 = {'b': 2, 'c': 4}
dict3 = {'a': 1,'c': 3}
dicts_to_merge = [dict1, dict2,dict3]

merged_result = merge_dictionaries(dicts_to_merge)
print(merged_result)  

# 10. Find words frequency in a sentence
def word_frequency(sentence):
    words = sentence.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency
print(word_frequency("hello world hello"))