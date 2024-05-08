def solution(sizes):
    len_w = []
    len_h = []
    for size in sizes:
        len_w.append(max(size))
        len_h.append(min(size))
    return max(len_w) * max(len_h)