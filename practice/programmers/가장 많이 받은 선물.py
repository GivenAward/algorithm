def solution(k, m, score):
    return sum(sorted(score)[len(score) % m :: m]) * m
    answer = 0
    score.sort(reverse=True)
    for i in range(0, len(score), m):
        box = score[i : i + m]
        if len(box) < m:
            return answer
        answer += min(box) * len(box)
    return answer


print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))
print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))
