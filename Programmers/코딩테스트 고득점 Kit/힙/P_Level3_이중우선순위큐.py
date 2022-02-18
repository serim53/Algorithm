def solution(operations):
    heap = []
    for ope in operations:
        command, value = ope.split()[0], int(ope.split()[1])
        if command == 'I':
            heap.append(value)
        elif command == 'D' and len(heap) != 0:
            if value < 0:
                heap.pop(heap.index(min(heap)))
            else:
                heap.pop(heap.index(max(heap)))

    if len(heap) == 0:
        return [0, 0]
    else:
        return [max(heap), min(heap)]