def solution(friends, gifts):
    answer = 0
    
    # scores = [이름, 준횟수, 받은횟수, 선물지수]
    scores = []
    for friend in friends:
        scores.append([friend, 0, 0, 0])
    
    giver = []
    taker = []
    
    for gift in gifts:
        give, take = gift.split(" ")
        giver.append(give)
        taker.append(take)
        
    # 준 횟수
    for x in giver:
        for s in scores:
            if s[0] == x:
                s[1] += 1
                
    # 받은 횟수
    for y in taker:
        for s in scores:
            if s[0] == y:
                s[2] += 1
                
    # 선물 지수 계산
    for s in scores:
        s[3] = s[1] - s[2]

    # 이름 → 점수 맵
    score_map = {s[0]: s[3] for s in scores}

    # 선물 주고받기 횟수 저장 (A→B 개수)
    give_map = {f: {t: 0 for t in friends} for f in friends}
    for g, t in zip(giver, taker):
        give_map[g][t] += 1

    # 앞으로 받을 선물 카운트
    will_get = {f: 0 for f in friends}

    # 모든 쌍 비교
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            A = friends[i]
            B = friends[j]
            
            AtoB = give_map[A][B]
            BtoA = give_map[B][A]
            
            if AtoB > BtoA:
                will_get[A] += 1
            elif BtoA > AtoB:
                will_get[B] += 1
            else:
                
                if score_map[A] > score_map[B]:
                    will_get[A] += 1
                elif score_map[B] > score_map[A]:
                    will_get[B] += 1

    return max(will_get.values())
