def solution(arr):
    answer = []

    if len(arr) == 1:
        return [-1]
    else:
        arr.remove(min(arr))
        answer =arr
        return answer



# 다른사람의 풀이
# def rm_small(mylist):
#     return [i for i in mylist if i > min(mylist)]
#
# def rm_small(mylist):
#     mylist.pop(mylist.index(min(mylist)))
#     return mylist