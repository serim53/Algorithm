import copy
def move(r, c, nr, nc, h, w, num):
    for i in range(r, r + h):
        for j in range(c, c + w):
            area[i][j] = 0
    for i in range(nr, nr + h):
        for j in range(nc, nc + w):
            area[i][j] = num
    infos[num] = [nr, nc, h, w]

def find_blocks_to_move(nr, nc, h, w, num):
    global flag
    blocks = []
    for i in range(nr, nr + h):
        for j in range(nc, nc + w):
            if 0 > i or i >= l or 0 > j or j >= l:
                flag = True
                return
            if area[i][j] > 0 and area[i][j] != num and area[i][j] not in blocks:
                blocks.append(area[i][j])
            if graph[i][j] == 2:
                flag = True
                return
    flag = False
    return blocks

def get_damage(num_block):
    r, c, h, w = infos[num_block]
    nums = 0
    for i in range(r, r + h):
        for j in range(c, c + w):
            if graph[i][j] == 1:
                nums += 1
    strength[num_block] -= nums
    if strength[num_block] <= 0:
        for i in range(r, r + h):
            for j in range(c, c+ w):
                area[i][j] = 0
        strength.pop(num_block)
        infos.pop(num_block)


# l : 체스판 크기, n : 기사 수, q : 명령어 수
l, n, q = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(l)]
area = [[0] * l for _ in range(l)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
infos = {}
strength = {}
origin_strength = {}
result = 0
for i in range(1, n + 1):
    # (r, c)가 좌측 상단 꼭짓점, h * w 직사각형, k 체력
    r, c, h, w, k = map(int, input().split())
    infos[i] = [r - 1, c - 1, h, w]
    strength[i] = k
    origin_strength[i] = k
    for j in range(r - 1, r - 1 + h):
        for k in range(c - 1, c - 1 + w):
            area[j][k] = i

for _ in range(q):
    i, d = map(int, input().split())
    if i in infos.keys():
        flag = False    # 벽이 존재함
        r, c, h, w = infos[i]
        nr, nc = r + dx[d], c + dy[d]
        if 0 > nr or nr >= l or 0 > nc or nc >= l:
            continue
        blocks = find_blocks_to_move(nr, nc, h, w, i)
        # if blocks:
        #     blocks = set(blocks)
        if flag:  # 벽이 존재하는 경우 명령 실행 X
            continue
        # 연쇄 작용 X
        if not blocks:
            move(r, c, nr, nc, h, w, i)
        # 연쇄 작용 O
        else:
            temp_blocks = copy.deepcopy(blocks)
            # temp_blocks = blocks
            while temp_blocks and not flag:
                temp = []
                for block in temp_blocks:
                    r, c, h, w = infos[block]
                    nr, nc = r + dx[d], c + dy[d]
                    if 0 > nr or nr >= l or 0 > nc or nc >= l:
                        flag = True
                        break
                    blocks_to_move = find_blocks_to_move(nr, nc, h, w, block)
                    if blocks_to_move:
                        for b in blocks_to_move:
                            if b not in temp:
                                temp.append(b)
                temp_blocks = copy.deepcopy(temp)
                for b in temp_blocks:
                    blocks.append(b)
            if flag:
                continue
            if not temp_blocks:
                for block in blocks:
                    r, c, h, w = infos[block]
                    move(r, c, r + dx[d], c + dy[d], h, w, block)
                for block in blocks:
                    get_damage(block)
                r, c, h, w = infos[i]
                move(r, c, r + dx[d], c + dy[d], h, w, i)
result = 0
for num in strength.keys():
    result += (origin_strength[num] - strength[num])
print(result)