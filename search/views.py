from django.shortcuts import render

from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.views.generic import ListView

from shop.models import Item, Item_variation


class SearchListView(ListView):
    """
    Display a Items filtered by the search query.
    """
    model = Item
    template_name = 'search/item_list.html'
    paginate_by = 10

    def get_queryset(self, **kwargs):
        qs = Item.objects.all()
        keywords = self.request.GET.get('q')
        if keywords:
            query = SearchQuery(keywords)
            # vector = SearchVector('title', 'content')
            vector = SearchVector('title')
            qs = qs.annotate(search=vector).filter(search=query)
            # qs = qs.annotate(rank=SearchRank(vector, query)).order_by('-rank')

        return qs