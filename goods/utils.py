from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.db.models import Q

from goods.models import Products


def q_search(query: str):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    # поиск в sqlite3
    # keywords = [w for w in query.split() if len(w) > 2]
    # q_objects = Q()
    # for token in keywords:
    #     q_objects |= Q(description__icontains=token)
    #     q_objects |= Q(name__icontains=token)
    #
    # return Products.objects.filter(q_objects)

    vector = SearchVector("name", "description")
    query = SearchQuery(query)
    return Products.objects.annotate(rank=SearchRank(vector, query)).order_by("-rank")
