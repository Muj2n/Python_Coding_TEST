# https://school.programmers.co.kr/learn/courses/30/lessons/12951
# JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 
# 단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)
# 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

# 제한 조건
# s는 길이 1 이상 200 이하인 문자열입니다.
# s는 알파벳과 숫자, 공백문자(" ")로 이루어져 있습니다.
# 숫자는 단어의 첫 문자로만 나옵니다.
# 숫자로만 이루어진 단어는 없습니다.
# 공백문자가 연속해서 나올 수 있습니다.

def solution(s):
    answer = ''
    for i in range(len(s)):
        if i == 0:
            answer += s[i].upper() # 제일 처음 단어에 대한 대문자
        elif s[i-1] == ' ':
            answer += s[i].upper() # 공백 뒤의 단어에 대한 대문자
        else:
            answer += s[i].lower() # 다른 단어들은 소문자
    return answer

def Jaden_Case(s):
    # 함수를 완성하세요
    return s.title() # 단어의 타이틀에 대해서는 대문자

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Jaden_Case("3people unFollowed me for the last week"))

# https://school.programmers.co.kr/learn/courses/30/lessons/12925
# 문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.

# 제한 조건
# s의 길이는 1 이상 5이하입니다.
# s의 맨앞에는 부호(+, -)가 올 수 있습니다.
# s는 부호와 숫자로만 이루어져있습니다.
# s는 "0"으로 시작하지 않습니다.

def solution(s):
    answer = int(s)
    return answer

def strToInt(str): 
    result = 0
    for idx, number in enumerate(str[::-1]): # 수를 뒤로 뒤집는다.
        if number == '-': # 첫번째수의 양수인지 파악
            result *= -1
        else:
            result += int(number) * (10 ** idx) # enumerate를 이용하여 숫자와 위치 값을 통해서 제곱으로 계산
    return result


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(strToInt("-1234"))