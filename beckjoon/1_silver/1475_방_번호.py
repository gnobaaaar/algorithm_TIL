n = input() #다솜이 방번호를 string으로
card=[0]*10 #0~9까지 번호
card_6n9 = 0

for i in n:
    if(i=='6' or i=='9'): #6,9 동일취급
        card_6n9 += 1
    else:
        card[int(i)] += 1

#6, 9 개수 결정
if(card_6n9 % 2 == 0):
    card_6n9 = card_6n9//2
else:
    card_6n9 = card_6n9//2 + 1

card[6] = card_6n9

#card에 있는 것들 중 최대값이 세트의 개수
print(max(card))