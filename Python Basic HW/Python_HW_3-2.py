# 방법 2. 딕셔너리
def find_non_completer(list_a, list_b):
    return_list = []

    participant_dict = {}
    completion_dict = {}

    for i in list_a:
        participant_dict[i] = 0

    for j in list_a:
        completion_dict[j] = 0

    for i in list_a:
        participant_dict[i] += 1

    for j in list_b:
        completion_dict[j] += 1

    for k in list_a:
        if k not in return_list and participant_dict[k] != completion_dict[k]:
            for l in range(participant_dict[k] - completion_dict[k]):
                return_list.append(k)

    print(return_list)


# 예시 데이터
participant = ["mike", "tom", "lisa", "tom", "mike", "tom", "alice"]
completion = ["tom", "mike", "lisa"]


# 실행
find_non_completer(participant, completion)