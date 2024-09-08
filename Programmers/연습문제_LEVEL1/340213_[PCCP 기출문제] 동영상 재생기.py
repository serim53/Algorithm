def convertToSeconds(time):
    m, s = time.split(':')
    m, s = int(m), int(s)
    return 60 * m + s

def solution(video_len, pos, op_start, op_end, commands):
    video_len, pos, op_start, op_end = convertToSeconds(video_len), convertToSeconds(pos), convertToSeconds(op_start), convertToSeconds(op_end)
    if op_start <= pos <= op_end:
            pos = op_end
    for command in commands:
        if command == 'prev':
            pos -= 10
            if pos < 0:
                pos = 0
        else:
            pos += 10
            if pos > video_len:
                 pos = video_len
        if op_start <= pos <= op_end:
                pos = op_end
    return "{:02d}".format(pos // 60) + ":" + "{:02d}".format(pos % 60)
