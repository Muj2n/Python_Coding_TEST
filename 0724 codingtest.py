# https://school.programmers.co.kr/learn/courses/30/lessons/12916
# 대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 
# 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

# 예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.

# 제한사항
# 문자열 s의 길이 : 50 이하의 자연수
# 문자열 s는 알파벳으로만 이루어져 있습니다.

def solution(s):
    count_p = 0
    count_y = 0
    s = s.lower()
    for i in range(len(s)):
        if s[i] == 'p':
            count_p += 1
        elif s[i] == 'y':
            count_y += 1
    return count_p == count_y

def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')

# https://school.programmers.co.kr/learn/courses/30/lessons/12915
# 문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 
# 예를 들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.

# 제한 조건
# strings는 길이 1 이상, 50이하인 배열입니다.
# strings의 원소는 소문자 알파벳으로 이루어져 있습니다.
# strings의 원소는 길이 1 이상, 100이하인 문자열입니다.
# 모든 strings의 원소의 길이는 n보다 큽니다.
# 인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.

def solution(strings, n):
    # 인덱스 n번째 문자를 기준으로 정렬하고, 같은 경우 원래 문자열 사전 순으로 정렬
    sorted_strings = sorted(strings, key=lambda x: (x[n], x))
    return sorted_strings

# sorted
# 숫자 리스트의 절대값 기준 정렬:
# 숫자들의 절대값을 기준으로 정렬하고 싶을 때 lambda x: abs(x)를 사용합니다
words = ["apple", "banana", "cherry", "date"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)  # 출력: ['date', 'apple', 'banana', 'cherry']

# 문자열 리스트의 길이 기준 정렬:
# 문자열의 길이를 기준으로 정렬하려면 lambda x: len(x)를 사용합니다
words = ["apple", "banana", "cherry", "date"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)  # 출력: ['date', 'apple', 'banana', 'cherry']


# count():
# 문자열에서 특정 문자의 개수를 세는 메서드.
# 예: s.count('a')

# sum():
# 숫자형 데이터를 가진 리스트나 다른 iterable의 합을 계산하는 함수.
# 예: sum([1, 2, 3, 4])

# max():
# iterable에서 최대값을 찾는 함수.
# 예: max([1, 2, 3, 4])

# min():
# iterable에서 최소값을 찾는 함수.
# 예: min([1, 2, 3, 4])

# len():
# iterable의 길이를 반환하는 함수.
# 예: len([1, 2, 3, 4])

# sorted():
# iterable을 정렬하여 새로운 리스트를 반환하는 함수.
# 예: sorted([3, 1, 4, 1, 5]) (기본은 오름차순 정렬)
# 키워드 인자 reverse=True를 사용하면 내림차순으로 정렬 가능.

# sort():
# 리스트 자체를 정렬하는 메서드로, sorted()와 달리 리스트를 직접 변경합니다.
# 예: a = [3, 1, 4]; a.sort()

# map():
# 함수와 iterable을 인자로 받아, 각 요소에 함수를 적용한 결과를 담은 map 객체를 반환합니다.
# 예: map(int, ['1', '2', '3']) (모든 요소를 정수로 변환)

# filter():
# 함수와 iterable을 인자로 받아, 함수의 조건을 만족하는 요소들만 반환하는 filter 객체를 반환합니다.
# 예: filter(lambda x: x > 0, [-1, 0, 1, 2])

# reduce() (from functools):
# iterable의 모든 요소를 누적적으로 함수에 적용하여 단일 값을 반환합니다.
# 예: reduce(lambda x, y: x + y, [1, 2, 3, 4])

# enumerate():
# iterable의 요소와 인덱스를 튜플로 반환하는 함수.
# 예: enumerate(['a', 'b', 'c']) -> [(0, 'a'), (1, 'b'), (2, 'c')]

# zip():
# 두 개 이상의 iterable의 요소들을 병렬로 묶어 튜플로 반환하는 함수.
# 예: zip([1, 2, 3], ['a', 'b', 'c']) -> [(1, 'a'), (2, 'b'), (3, 'c')]

# all():
# iterable의 모든 요소가 참(True)인지 확인하는 함수. 빈 iterable에 대해서는 True를 반환.
# 예: all([True, True, False]) -> False

# any():
# iterable 중 하나라도 참(True)인지 확인하는 함수. 빈 iterable에 대해서는 False를 반환.
# 예: any([False, False, True]) -> True

# set():
# iterable에서 중복을 제거하고 집합(set) 자료형으로 변환하는 함수.
# 예: set([1, 2, 2, 3]) -> {1, 2, 3}

# dict():
# 키-값 쌍으로 구성된 데이터를 사전(dictionary) 자료형으로 변환하는 함수.
# 예: dict([('a', 1), ('b', 2)]) -> {'a': 1, 'b': 2}

# sorted() with key:
# key 인자를 사용하여 정렬 기준을 커스터마이즈할 수 있습니다.
# 예: sorted(['apple', 'banana', 'cherry'], key=len) -> ['apple', 'cherry', 'banana'] (문자열 길이로 정렬)

# reversed():
# iterable의 요소를 역순으로 반환하는 함수. 원래 리스트를 변경하지 않고 역순으로 된 반복자를 반환.
# 예: list(reversed([1, 2, 3])) -> [3, 2, 1]

# list():
# iterable을 리스트 자료형으로 변환하는 함수.
# 예: list(range(5)) -> [0, 1, 2, 3, 4]

# str.split():
# 문자열을 특정 구분자로 분리하여 리스트로 반환하는 메서드.
# 예: 'a b c'.split() -> ['a', 'b', 'c']

# str.join():
# 리스트와 같은 iterable의 요소들을 문자열로 결합하는 메서드.
# 예: '-'.join(['a', 'b', 'c']) -> 'a-b-c'

# str.replace():
# 문자열 내의 특정 부분을 다른 문자열로 바꾸는 메서드.
# 예: 'hello world'.replace('world', 'Python') -> 'hello Python'