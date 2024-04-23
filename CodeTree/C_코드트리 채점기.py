import sys
import heapq
from collections import OrderedDict, defaultdict
from typing import Optional

class Task:
    def __init__(self, t, p, url):
        self.domain = url.split("/")[0]
        self.id = url.split("/")[1]
        self.p = p
        self.t = t

    def __lt__(self, other):
        if self.p != other.p:
            return self.p < other.p
        return self.t < other.t

# 채점기 정보 {J_id: Task}
J_dict = OrderedDict()
# 대기 큐 Priority Queue (Task) dict
domain_wait_q = defaultdict(list)
# 대기 큐 안에 있는 url dict {url: T/F}
wait_q_url_dict = defaultdict(bool)
# 도메인 시간 정보 {domain: {start: int, end: int}}
domain_time_dict = defaultdict(dict)
# 현재 채점 중인 도메인 리스트 {domain: T/F}
domain_judging_dict = defaultdict(bool)

def set_j(input_data):
    """
    Step 1
    input_data: [N, u0]
    채점기 세팅
    u0 wait Q에 넣기
    """
    N = int(input_data[0])
    u = input_data[1]
    for i in range(1, N + 1):
        J_dict[i] = None
    heapq.heappush(domain_wait_q[u.split("/")[0]], Task(0, 1, u))
    wait_q_url_dict[u] = True

def insert_task_wait_q(input_data):
    """
    step 2
    input_data = [t, p ,u]
    waitQ에 새로운 task 넣기
    """
    t, p = map(int, input_data[:2])
    u = input_data[2]
    if not wait_q_url_dict[u]:
        heapq.heappush(domain_wait_q[u.split("/")[0]], Task(t, p, u))
        wait_q_url_dict[u] = True

def pop_task_wait_q(t) -> Optional[Task]:
    task_tmp_list = []

    for domain, pq in domain_wait_q.items():
        if not domain_judging_dict[domain] and domain_wait_q[domain]:
            curr_domain_time = domain_time_dict.get(domain, {"start": 0, "gap": 0})
            if curr_domain_time["start"] + 3 * curr_domain_time["gap"] <= t:
                heapq.heappush(task_tmp_list, heapq.heappop(domain_wait_q[domain]))

    if task_tmp_list:
        task = heapq.heappop(task_tmp_list)
        for tmp in task_tmp_list:
            heapq.heappush(domain_wait_q[tmp.domain], tmp)
        return task
    else:
        return None

def try_task(input_data):
    """
    step 3
    input_data = [t]
    """
    t = int(input_data[0])

    j_id = None
    for i, v in J_dict.items():
        if v is None:
            j_id = i
            break

    if j_id is not None:
        task: Optional[Task] = pop_task_wait_q(t)
        if task is not None:
            J_dict[j_id] = task
            domain_judging_dict[task.domain] = True
            domain_time_dict[task.domain]["start"] = t
            wait_q_url_dict[f"{task.domain}/{task.id}"] = False

def end_task(input_data):
    """
    step 4
    input_data = [t J_id]
    """
    t, j_id = map(int, input_data)
    if J_dict[j_id] is not None:
        task = J_dict[j_id]
        J_dict[j_id] = None
        domain_judging_dict[task.domain] = False
        domain_time_dict[task.domain]["gap"] = t - domain_time_dict[task.domain]["start"]

def print_wait_q():
    """
    step5
    """
    answer = 0
    for v in domain_wait_q.values():
        answer += len(v)
    print(answer)

Q = int(sys.stdin.readline())
for _ in range(Q):
    query, *data = sys.stdin.readline().split()

    # 100 N u0
    if int(query) == 100:
        set_j(data)

    # 200 t p u
    elif int(query) == 200:
        insert_task_wait_q(data)

    # 300 t
    elif int(query) == 300:
        try_task(data)

    # 400 t J_id
    elif int(query) == 400:
        end_task(data)

    else:
        # 500 t
        print_wait_q()

# 정답 코드
# from sortedcontainers import SortedSet, SortedDict
# import heapq
# import sys
#
#
# class PriorityQueue:
#     def __init__(self):  # 빈 Priority Queue 하나를 생성합니다.
#         self.items = []
#
#     def push(self, item):  # 우선순위 큐에 데이터를 추가합니다.
#         heapq.heappush(self.items, item)
#
#     def empty(self):  # 우선순위 큐가 비어있으면 True를 반환합니다.
#         return not self.items
#
#     def size(self):  # 우선순위 큐에 있는 데이터 수를 반환합니다.
#         return len(self.items)
#
#     def pop(self):  # 우선순위 큐에 있는 데이터 중 최솟값에 해당하는 데이터를 반환하고 제거합니다.
#         if self.empty():
#             raise Exception("PriorityQueue is empty")
#
#         return heapq.heappop(self.items)
#
#     def top(self):  # 우선순위 큐에 있는 데이터 중 최솟값에 해당하는 데이터를 제거하지 않고 반환합니다.
#         if self.empty():
#             raise Exception("PriorityQueue is empty")
#
#         return self.items[0]
#
#
# MAX_D = 300
# MAX_N = 50000
# INF = sys.maxsize
#
# # 해당 도메인에서 해당 문제ID가 레디큐에 있는지 관리해줍니다.
# is_in_readyq = [SortedSet() for _ in range(MAX_D + 1)]
#
# # 현재 쉬고 있는 채점기들을 관리해줍니다.
# rest_judger = PriorityQueue()
#
# # 각 채점기들이 채점할 때, 도메인의 인덱스를 저장합니다.
# judging_domain = [0 for _ in range(MAX_N + 1)]
#
# # 각 도메인별 start, gap, end(채점이 가능한 최소 시간)을 관리합니다.
# s = [0 for _ in range(MAX_D + 1)]
# g = [0 for _ in range(MAX_D + 1)]
# e = [0 for _ in range(MAX_D + 1)]
#
# # 도메인을 관리하기 위해 cnt를 이용합니다.
# # 도메인 문자열을 int로 변환해주는 map을 관리합니다.
# domainToIdx = SortedDict()
# global cnt
# cnt = 0
#
# # 현재 채점 대기 큐에 있는 task의 개수를 관리합니다.
# global ans
# ans = 0
#
# # 각 도메인별로 priority queue를 만들어
# # 우선순위가 가장 높은 url을 뽑아줍니다.
# url_pq = [PriorityQueue() for _ in range(MAX_D + 1)]
#
#
# # 채점기를 준비합니다.
# def Init(query):
#     global n
#     (empty, n, url) = query
#     n = int(n)
#
#     global cnt
#
#     for i in range(1, n + 1): rest_judger.push(i)
#
#     # url에서 도메인 부분과 숫자 부분을 나누어줍니다.
#     idx = 0
#     for i in range(len(url)):
#         if url[i] == '/': idx = i
#
#     domain = url[:idx]
#     num = int(url[idx + 1:])
#
#     # 만약 도메인이 처음 나온 도메인이라면 domainToIdx에 갱신합니다.
#     if not domain in domainToIdx:
#         cnt += 1
#         domainToIdx[domain] = cnt
#     domain_idx = domainToIdx[domain]
#
#     # 도메인 번호에 맞는 레디큐에 숫자 부분을 넣어줍니다.
#     is_in_readyq[domain_idx].add(num)
#
#     # 새로 들어온 url을 도메인에 맞춰 url_pq에 넣어줍니다.
#     # id, tme, num
#     newUrl = (1, 0, num)
#     url_pq[domain_idx].push(newUrl)
#
#     # 채점 대기 큐에 값이 추가됐으므로 개수를 1 추가합니다.
#     global ans
#     ans += 1
#
#
# # 새로운 url을 입력받아 레디큐에 추가해줍니다.
# def NewUrl(query):
#     (empty, tme, id, url) = query
#     tme = int(tme)
#     id = int(id)
#
#     global cnt
#
#     # url에서 도메인 부분과 숫자 부분을 나누어줍니다.
#     idx = 0
#     for i in range(len(url)):
#         if url[i] == '/':
#             idx = i
#
#     domain = url[:idx]
#     num = int(url[idx + 1:])
#
#     # 만약 도메인이 처음 나온 도메인이라면 domainToIdx에 갱신합니다.
#     if domain not in domainToIdx:
#         cnt += 1
#         domainToIdx[domain] = cnt
#
#     domain_idx = domainToIdx[domain]
#
#     # 만약 숫자 부분이 이미 레디큐에 있으면 중복되므로 넘어갑니다.
#     if num in is_in_readyq[domain_idx]:
#         return
#     # 도메인 번호에 맞는 레디큐에 숫자 부분을 넣어줍니다.
#     is_in_readyq[domain_idx].add(num)
#
#     # 새로 들어온 url을 도메인에 맞춰 url_pq에 넣어줍니다.
#     # id, tme, num
#     newUrl = (id, tme, num)
#     url_pq[domain_idx].push(newUrl)
#
#     # 채점 대기 큐에 값이 추가됐으므로 개수를 1 추가합니다.
#     global ans
#     ans += 1
#
#
# # 다음 도메인을 찾아 assign합니다.
# def Assign(query):
#     (empty, tme) = query
#     tme = int(tme)
#
#     # 쉬고 있는 채점기가 없다면 넘어갑니다.
#     if rest_judger.empty(): return
#
#     # 가장 우선순위가 높은 url을 찾습니다.
#     min_domain = 0
#     minUrl = (INF, 0, 0)
#
#     global cnt
#
#     for i in range(1, cnt + 1):
#         # 만약 현재 채점중이거나, 현재 시간에 이용할 수 없다면 넘어갑니다.
#         if e[i] > tme: continue
#
#         # 만약 i번 도메인에 해당하는 url이 존재한다면
#         # 해당 도메인에서 가장 우선순위가 높은 url을 뽑고 갱신해줍니다.
#         if not url_pq[i].empty():
#             curUrl = url_pq[i].top()
#
#             if minUrl > curUrl:
#                 minUrl = curUrl
#                 min_domain = i
#
#     # 만약 가장 우선순위가 높은 url이 존재하면
#     # 해당 도메인과 쉬고 있는 가장 낮은 번호의 채점기를 연결해줍니다.
#     if min_domain:
#         judger_idx = rest_judger.top()
#         rest_judger.pop()
#
#         # 해당 도메인의 가장 우선순위가 높은 url을 지웁니다.
#         url_pq[min_domain].pop()
#
#         # 도메인의 start, end를 갱신해줍니다.
#         s[min_domain] = tme
#         e[min_domain] = INF
#
#         # judger_idx번 채점기가 채점하고 있는 도메인 번호를 갱신해줍니다.
#         judging_domain[judger_idx] = min_domain
#
#         # 레디큐에서 해당 url의 숫자를 지워줍니다.
#         is_in_readyq[min_domain].remove(minUrl[2])
#
#         # 채점 대기 큐에 값이 지워졌으므로 개수를 1 감소합니다.
#         global ans
#         ans -= 1
#
#
# # 채점 하나를 마무리합니다.
# def Finish(query):
#     (empty, tme, id) = query
#     tme = int(tme)
#     id = int(id)
#
#     # 만약 id번 채점기가 채점 중이 아닐 경우 스킵합니다.
#     if judging_domain[id] == 0: return
#
#     # id번 채점기를 마무리합니다.
#     rest_judger.push(id)
#     domain_idx = judging_domain[id]
#     judging_domain[id] = 0
#
#     # 해당 도메인의 gap, end 값을 갱신해줍니다.
#     g[domain_idx] = tme - s[domain_idx]
#     e[domain_idx] = s[domain_idx] + 3 * g[domain_idx]
#
#
# # 현재 채점 대기 큐에 있는 url의 개수를 출력해줍니다.
# def Check(query):
#     (empty, tme) = query
#     tme = int(tme)
#
#     global ans
#     print(ans)
#
#
# q = int(input())
#
# for _ in range(q):
#     query = input().split()
#
#     if int(query[0]) == 100:
#         # 채점기를 준비합니다.
#         Init(query)
#     if int(query[0]) == 200:
#         # 새로운 url을 입력받아 레디큐에 추가해줍니다.
#         NewUrl(query)
#     if int(query[0]) == 300:
#         # 다음 도메인을 찾아 assign합니다.
#         Assign(query)
#     if int(query[0]) == 400:
#         # 채점 하나를 마무리합니다.
#         Finish(query)
#     if int(query[0]) == 500:
#         # 현재 채점 대기 큐에 있는 url의 개수를 출력해줍니다.
#         Check(query)

# --- 시간 초과
# import heapq
#
# def check_possibility(task_info, time):
#     p, t, u = task_info
#     url = u.split('/')[0]
#     if url in judging_info.keys():
#         return False
#     if url in history.keys():
#         judger, start, end = history[url]
#         if time < start + (end - start) * 3:
#             return False
#     return True
#
# q = int(input())
# judgers = []
# waiting_queue = []  # 채점 우선순위, 시간, url
# waiting_task = []
# judging_info = {}
# judging_judgers = {}
# history = {}
# for _ in range(q):
#     com = list(input().split())
#     num_com = int(com[0])
#     if num_com == 100:  # 채점기 준비
#         n, u = int(com[1]), com[2]
#         for i in range(1, n + 1):
#             heapq.heappush(judgers, i)
#         heapq.heappush(waiting_queue, [1, 0, u])
#         waiting_task.append(u)
#     elif num_com == 200:    # 채점 요청
#         if com[3] not in waiting_task:
#             heapq.heappush(waiting_queue, [int(com[2]), int(com[1]), com[3]])
#             waiting_task.append(com[3])
#     elif num_com == 300:    # 채점 시도
#         if judgers: # 쉬는 채점기가 있다면 채점 시도
#             temp = []   # pop한 task를 잠시 담아둘 리스트
#             while waiting_queue:
#                 task_info = heapq.heappop(waiting_queue)
#                 if check_possibility(task_info, int(com[1])):    # 채점 가능
#                     j = heapq.heappop(judgers)
#                     judging_judgers[j] = task_info[2]
#                     judging_info[task_info[2].split('/')[0]] = [j, int(com[1])]
#                     waiting_task.remove(task_info[2])
#                     break
#                 else:
#                     temp.append(task_info)
#             for t in temp:
#                 heapq.heappush(waiting_queue, t)
#     elif num_com == 400:    # 채점 종료
#         j_id = int(com[2])
#         if j_id in judging_judgers.keys():
#             id = judging_judgers[j_id]  # 문제 url
#             judging_judgers.pop(j_id)
#             info = judging_info.pop(id.split('/')[0])
#             history[id.split('/')[0]] = [j_id, info[1], int(com[1])]
#             heapq.heappush(judgers, j_id)
#     else:   # 채점 대기 큐 조회
#         print(len(waiting_queue))