# [비기너 Day 2] 평균 구하기
# 정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

def solution(arr):
    answer = 0
    answer = sum(arr) / len(arr)
    return answer



# [미들러 Day 2] x만큼 간격이 있는 n 개의 숫자
# 함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 
# 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(i * x)        
    return answer