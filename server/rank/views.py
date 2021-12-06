from django.shortcuts import render
from rank.models import Ranking
from rank.helper import JsonDictionary
from django.http import JsonResponse

# Create your views here.
def intro(request):
    return render(request, 'rank/rank_intro.html')

def rank_list(request):
    data = request.GET
    ranks = Ranking.objects.order_by('-score')[:10]
    ranks = JsonDictionary.RanksToDictionary(ranks)
    
    return JsonResponse(ranks, json_dumps_params={'ensure_ascii': False},
                        content_type=u"application/json; charset=utf-8", status=200)

def saverank(request, getuserName, getscore):
    Ranking.objects.create(userName=getuserName, score=getscore)
    
    return rank_list(request)