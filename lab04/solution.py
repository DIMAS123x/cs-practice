def winner(names, scores):
    best = 0
    for i in range(1,len(scores)):
        if scores[i] > scores[best]:
             best = i

    return names[best]
