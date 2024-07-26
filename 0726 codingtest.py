# https://school.programmers.co.kr/learn/courses/30/lessons/42577
# 문제 설명
# 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
# 전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

# 구조대 : 119
# 박준영 : 97 674 223
# 지영석 : 11 9552 4421
# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

# 제한 사항
# phone_book의 길이는 1 이상 1,000,000 이하입니다.
# 각 전화번호의 길이는 1 이상 20 이하입니다.
# 같은 전화번호가 중복해서 들어있지 않습니다.

def solution(phone_book):
    phone_book.sort()  # 사전순 정렬
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False  # 접두어가 발견되면 False
    return True  # 접두어가 없으면 True


# https://school.programmers.co.kr/learn/courses/30/lessons/42576
# 문제 설명
# 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
# completion의 길이는 participant의 길이보다 1 작습니다.
# 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
# 참가자 중에는 동명이인이 있을 수 있습니다.

def solution(participant, completion):
    answer = ''
    
    for i in completion:
        participant.remove(i)
        
    return participant[0]
# 해당 풀이는 시간 복잡도의 문제로 인해 오류가 난다.

def solution(participant, completion):
    participant_dict = {}
    
    # 참가자 명단에서 이름을 카운트
    for person in participant:
        if person in participant_dict:
            participant_dict[person] += 1
        else:
            participant_dict[person] = 1
    
    # 완주자 명단에서 이름 카운트를 줄임
    for person in completion:
        if person in participant_dict:
            participant_dict[person] -= 1
    
    # 완주하지 못한 사람 찾기
    for person, count in participant_dict.items():
        if count > 0:
            return person
# 이 문제는 딕셔너리를 이용하여 효율적으로 해결할 수 있습니다. 각 선수의 이름을 키로 하고, 
# 해당 이름의 출현 횟수를 값으로 저장하는 딕셔너리를 사용할 수 있습니다. 이 접근 방식은 동명이인이 있는 경우에도 문제를 해결할 수 있게 해줍니다.

# 참가자 딕셔너리 생성: participant 리스트를 순회하면서 각 선수의 이름을 딕셔너리에 추가하고, 그 이름이 나타난 횟수를 카운트합니다.

# 완주자 카운트 감소: completion 리스트를 순회하면서 각 선수의 이름을 딕셔너리에서 찾아 값을 1씩 감소시킵니다.

# 완주하지 못한 선수 찾기: 딕셔너리를 순회하며 값이 0이 아닌 첫 번째 키(선수 이름)를 찾습니다. 이 키가 완주하지 못한 선수를 의미합니다.
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


# Counter(participant)는 participant 리스트의 각 이름을 키로 하고, 해당 이름의 출현 횟수를 값으로 가지는 Counter 객체를 만듭니다. Counter(completion)도 마찬가지로 완주자의 이름과 출현 횟수를 담은 Counter 객체를 만듭니다.
# 두 Counter 객체에서 빼기 연산을 수행하면, participant에 있는 모든 이름의 출현 횟수에서 completion에 있는 이름의 출현 횟수를 뺀 결과를 얻습니다. 이 결과는 participant에 있지만 completion에 없거나 participant에서 더 많이 출현한 이름만 남게 됩니다. 이 문제에서는 완주하지 못한 선수의 이름이 됩니다.
# 위 단계에서 남은 Counter 객체는 단 한 명의 선수만 포함하게 됩니다. list(answer.keys())는 남은 선수의 이름을 리스트로 만듭니다. 여기서 첫 번째 요소, 즉 list(answer.keys())[0]가 완주하지 못한 선수의 이름입니다.