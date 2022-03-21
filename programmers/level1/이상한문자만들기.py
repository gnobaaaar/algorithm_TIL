def solution(s):
    answer = ''
    count = 0

    for _ in s:
        if _ == ' ':
            answer = answer + ' '
            count = 0
        else:
            if count % 2 == 0 or count == 0:
                answer = answer + _.upper()
                count = count + 1
            else:
                answer = answer + _.lower()
                count = count + 1

    return answer


#다른사람풀이
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))