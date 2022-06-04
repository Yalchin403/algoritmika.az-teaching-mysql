import os
import json
from pprint import pprint

# f = open(os.path.join('text-files', 'test.txt'), 'r')
# #  default mode is reading
# print(f.read())

# f.close()

# with open(os.path.join('text-files', 'test.txt'), 'r') as f:
#     print(f.read())

# with open(os.path.join('text-files', 'test.txt'), 'r') as f:
#     # f.seek(2)
#     print(f.readlines())

# t = 1, 3  # int 1 3 
# f = (1, 3)

# print(type(t), type(f))


# l = []

# for i in range(1, 11):
#     l.append(i)

# print(l)

# l = (i for i in range(1, 11))  # generator

# print(type(l))

# def func():
#     # do smth

#     for i in range(1, 10):
#         yield i


# d = {}

# print(dir(d))


# with open('yalchin403.json', 'r') as f:
   

#     json_content = json.load(f)
#     print(json_content, '\n', type(json_content))


    # writing to json

# with open('test.json', 'w') as f:
#     temp_dict = {
#         'name': "Yalchin",
#         'age': 99
#     }

    # json.dumps(temp_dict, f)

with open('yalchin403.json', 'r') as f:

    json_content = json.load(f)
    pprint(json_content)    
