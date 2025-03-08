'''
def out():
    a = 1
    print('outside')

    def inner():
        print('inside', a)

    return inner


inners = out()  # 此时inners是out函数对象
inners()
'''

'''
lst = [20, 10]


def average(num):
    lst.append(num)
    result = sum(lst) / len(lst)
    return result


print(average(10))
print(average(20))
lst.clear()
print(average(10))
'''

def safety_average():
    lst = [20, 10]
    def average(num):
        lst.append(num)
        result = sum(lst) / len(lst)
        return result
    return average

new_average = safety_average()
print(new_average(20))