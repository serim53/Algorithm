class Query:
    def __init__(self, cmd, t, x, name, n):
        self.cmd = cmd
        self.t = t
        self.x = x
        self.name = name
        self.n = n

queries = []
names = set()   # 등장한 사람 목록
p_queries = {}  # 각 사람마다 주어진 초밥 명령
entry_time = {} # 각 사람의 입장 시간
position = {}   # 각 사람의 위치
exit_time = {}  # 각 사람의 퇴장 시간

L, Q = map(int, input().split())
for _ in range(Q):
    command = input().split()
    cmd, t, x, n = -1, -1, -1, -1
    name = ""
    cmd = int(command[0])
    if cmd == 100:
        t, x, name = command[1:]
        t, x = map(int, [t, x])
    elif cmd == 200:
        t, x, name, n = command[1:]
        t, x, n = map(int, [t, x, n])
    else:
        t = int(command[1])

    queries.append(Query(cmd, t, x, name, n))

    if cmd == 100:
        if name not in p_queries:
            p_queries[name] = []
        p_queries[name].append(Query(cmd, t, x, name, n))
    elif cmd == 200:
        names.add(name)
        entry_time[name] = t
        position[name] = x

# 각 사람마다 자신의 이름이 적힌 조합을 언제 먹게 되는지를 계산하여 해당 정보를 기존 Query에 추가 (111번 쿼리)
for name in names:
    exit_time[name] = 0 # 마지막으로 먹는 초밥 시간 중 가장 늦은 시간

    for q in p_queries[name]:
        time_to_removed = 0
        # 만약 초밥이 사람이 등장하기 전에 미리 주어진 상황이라면
        if q.t < entry_time[name]:
            t_sushi_x = (q.x + (entry_time[name] - q.t)) % L    # entry_time때의 스시 위치
            additionl_time = (position[name] - t_sushi_x + L) % L   # 몇 초가 더 지나야 만나는지를 계산
            time_to_removed = entry_time[name] + additionl_time
        # 초밥이 사람이 등장한 이후에 주어졌다면
        else:
            # 몇 초가 더 지나야 만나는지를 계산
            additionl_time = (position[name] - q.x + L) % L
            time_to_removed = q.t + additionl_time

        # 초밥이 사라지는 시간 중 가장 늦은 시간을 업데이트
        exit_time[name] = max(exit_time[name], time_to_removed)

        # 초밥이 사라지는 111번 쿼리를 추가
        queries.append(Query(111, time_to_removed, -1, name, -1))

# 사람마다 초밥을 마지막으로 먹은 시간 t를 계산하여 그 사람이 해당 t 때 코드트리 오마카세를 떠났다는 Query를 추가 (222번 쿼리)
for name in names:
    queries.append(Query(222, exit_time[name], -1, name, -1))

# 시간, 명령어 순으로 정렬 / 사진 촬영이 가장 뒤로 오도록
queries.sort(key=lambda q: (q.t, q.cmd))

people_num, sushi_num = 0, 0
for i in range(len(queries)):
    if queries[i].cmd == 100:  # 초밥 추가
        sushi_num += 1
    elif queries[i].cmd == 111:  # 초밥 제거
        sushi_num -= 1
    elif queries[i].cmd == 200:  # 사람 추가
        people_num += 1
    elif queries[i].cmd == 222:  # 사람 제거
        people_num -= 1
    else:  # 사진 촬영
        print(people_num, sushi_num)

# 시간 초과 풀이
# from collections import defaultdict
#
# def delete_customer(name):
#     customer_info[name][1] -= 1
#     if customer_info[name][1] == 0:
#         customer_info.pop(name)
#         sushi_info.pop(name)
#
# def move_sushi():
#     for name in sushi_info.keys():
#         temp = []
#         for i in range(len(sushi_info[name])):
#             new_loc = (sushi_info[name][i] + 1) % l
#             if name in customer_info.keys() and customer_info[name][0] == new_loc:
#                 delete_customer(name)
#                 continue
#             else:
#                 temp.append(new_loc)
#         sushi_info[name] = temp
#
# def make_sushi(loc, name):
#     if name in customer_info.keys() and customer_info[name][0] == loc:
#         delete_customer(name)
#     else:
#         sushi_info[name].append(loc)
#
#
# def customer_in(loc, name, cnt):
#     customer_info[name] = [loc, cnt]
#     if loc in sushi_info[name]:
#         delete_customer(name)
#
# def take_photo():
#     num_customer = len(customer_info.keys())
#     num_sushi = 0
#     for name in sushi_info.keys():
#         num_sushi += len(sushi_info[name])
#     print(num_customer, num_sushi)
#
#
# l, q = map(int, input().split())
# sushi_info = defaultdict(list)
# customer_info = {}
# cur_time = 1
# for _ in range(q):
#     opers = list(input().split())
#     if int(opers[1]) > (cur_time + 1):
#         for _ in range(int(opers[1]) - cur_time - 1):
#             # 초밥 이동하기
#             move_sushi()
#
#     if opers[0] == '100':
#         move_sushi()
#         cur_time = int(opers[1])
#         make_sushi(int(opers[2]), opers[3])
#     elif opers[0] == '200':
#         move_sushi()
#         cur_time = int(opers[1])
#         customer_in(int(opers[2]), opers[3], int(opers[4]))
#     else:
#         move_sushi()
#         cur_time = int(opers[1])
#         take_photo()