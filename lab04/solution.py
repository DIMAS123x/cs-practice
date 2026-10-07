def winner(names, scores):
    best = 0
    for i in range(1,len(scores)):
        if scores[i] > scores[best]:
             best = i

    return names[best]


def average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores)/len(scores)


def ranking(names, scores):
    res = []
    for i in range(len(names)):
        res.append((scores[i],names[i]))
    res.sort(reverse = True)
    return [name for scores,name in res]
