def RanksToDictionary(ranks):
    output = {}
    output['rank'] = [{
        'userName' : rank.userName,
        'score' : rank.score,
    } for rank in ranks]
    return output