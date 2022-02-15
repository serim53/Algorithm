def solution(genres, plays):
    answer = []
    # 장르별 횟수 key : 장르, value : 횟수
    lists = {}
    # 노래 리스트 key : 고유번호, value : 장르, 횟수
    dict = {}

    index = 0
    for genre, play in zip(genres, plays):
        dict[index] = [genre, play]
        index += 1
        if genre not in lists:
            lists[genre] = play
        else:
            lists[genre] = lists.get(genre) + play

    # 장르별 횟수를 횟수가 큰 순으로 정렬
    lists = sorted(lists.items(), key=lambda  x: x[1], reverse=True)

    # 노래 리스트를 횟수가 큰 순으로 정렬
    dict = sorted(dict.items(), key=lambda x: x[1][1], reverse=True)

    for list in lists:
        num = 0
        for d in dict:
            if d[1][0] == list[0]:
                answer.append(d[0])
                num += 1
                if num == 2:
                    break


    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))