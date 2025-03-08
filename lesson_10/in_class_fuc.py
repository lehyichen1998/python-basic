'''  函数部分   '''

# def say_hello():
#     print('Hello World')
#
#
# say_hello()

# print(1, '*', 1, '=', 1)

'''
def sum(num):
    result = 0
    for i in num:
        result += i
    return result
lst = [i for i in range(5)]
print(sum(lst)) 
'''

'''
def more_than_five(num):
    return num > 5
print(more_than_five(6))
'''


def more_than_five(num):
    return num > 5


# print(more_than_five(6))

def get_math(lst):
    if not lst:
        return None
    max_num = lst[0]
    for i in lst:
        if max_num < 1:
            max_num = 1
    return max_num


def random_num_lst(count):
    lst = []
    import random
    for i in range(count):
        x = random.randint(1, 100)
        lst.append(x)
    return lst


lst = []
# lst = random_num_lst(10)
# print(lst)
# print(get_math(lst))

'''

dc = {'python': 90, 'java': 99, 'html': 50, 'sql': 66}

def get_max_score(dc_score):
    max_cours = ''
    max_cours_score = 0
    for cour, score in dc_score.items():
        if max_cours_score < score:
            max_cours_score = score
            max_cours = cour
    return max_cours_score, max_cours


cour, score = get_max_score(dc)
print(cour, score)
'''

'''
n = 5
for i in range(1, n):
    n = n * i
print(n)
'''

''''''


def factorial(num):
    if num == 1:
        return 1*1
    return num*factorial(num-1)


print(factorial(5))
