def solution(s):
    answer = ''

    arr_list = list(s)
    index = int(len(arr_list)/2)

    if len(arr_list) % 2 ==0:
        return arr_list[index-1] + arr_list[index]
    else:
        return arr_list[index]



# 더 나은 풀이
def string_middle(str):
    # 함수를 완성하세요
    return str[(len(str)-1)//2:len(str)//2+1]