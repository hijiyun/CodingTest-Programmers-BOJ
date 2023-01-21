def solution(common):
    answer = 0
    num = common[-1] - common[-2]
    if common[1] + num == common[2] and common[0] + num == common[1]:
        answer = common[-1] + num
    else:
        num = common[-1] // common[-2]
        answer = common[-1] * num
        
    return answer