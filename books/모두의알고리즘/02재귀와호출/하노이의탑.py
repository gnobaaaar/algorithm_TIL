def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:
        print(from_pos, '->', to_pos)
        return

    hanoi(n-1, from_pos, aux_pos, to_pos)
    print(from_pos, '->', to_pos)
    hanoi(n-1, aux_pos, to_pos, from_pos)

print("n = 1")
hanoi(1, 1, 3, 2)  # 원반 한 개를 1번 기둥에서 3번 기둥으로 이동(2번을 보조 기둥으로)
print("n = 2")
hanoi(2, 1, 3, 2)  # 원반 두 개를 1번 기둥에서 3번 기둥으로 이동(2번을 보조 기둥으로)
print("n = 3")
hanoi(3, 1, 3, 2) # 원반 세 개를 1번 기둥에서 3번 기둥으로 이동(2번을 보조 기둥으로)