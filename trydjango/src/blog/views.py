from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
    )



from .models import Article

# Create your views here.
# def article_detail_view(request,id):
#     obj = get_object_or_404(Article, id=id)
#     context = {
#         'objects':obj
#     }
#     return render(request, "blog/article_detail.html",context)

class ArticleListView(ListView):
    # template_name = 'blog/article_list.html'
    queryset = Article.objects.all()    


class ArticleDetailView(DetailView):
    # template_name = 'blog/article_detail.html'
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article,id=id_)