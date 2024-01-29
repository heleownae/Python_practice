# # 방법1. 플래그

# def find_non_completer(list_a, list_b):
#     return_list = []
#     c_check_list = []

#     for _ in list_b:
#         c_check_list.append(0)

#     for i in list_a:
#         check = 0

#         for j in range(len(list_b)):
#             if check == 0 and c_check_list[j] == 0 and i == list_b[j]:
#                 c_check_list[j] = 1
#                 check = 1

#         if check == 0:
#             return_list.append(i)

#     print(return_list)


# # 예시 데이터
# participant = ["mike", "tom", "lisa", "tom", "mike", "tom", "alice"]
# completion = ["tom", "mike", "lisa", "mike"]


# # 실행
# find_non_completer(participant, completion)


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