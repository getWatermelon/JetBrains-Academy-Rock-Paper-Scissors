numbers = [1234, 5678, 90]
# save this list in `file_with_list.txt`
with open('file_with_list.txt', 'w') as file_:
    print(numbers, end='', file=file_)
