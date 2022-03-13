def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        tmp = []
        for j in range(len(arr1[0])):
            tmp.append(arr1[i][j] + arr2[i][j])
        answer.append(tmp)

    return answer

# better answer
# def sumMatrix(A,B):
#     answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
#     return answer
#
# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))

# def sumMatrix(A,B):
#     return [list(map(sum, zip(*x))) for x in zip(A, B)]
#
# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))