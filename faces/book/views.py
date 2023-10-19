from book.models import Mybooksread
from .forms import BookForm
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#bookninsert data page
from django.views.generic import TemplateView, ListView
#search bar.....
from django.db.models import Q


class SearchResultsView(ListView):
    model = Mybooksread
    template_name = 'book/booksearch.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Mybooksread.objects.filter(Q(authors__icontains=query))
        return object_list


def show(request, pk):

    show = Mybooksread.objects.get(pk=pk)
    return render(request, 'book/showeach.html', {'show': show})



#paginator
def book_index(request):
    user_list = Mybooksread.objects.all()
    page = request.GET.get('page', 1 )
    count= Mybooksread.objects.all().count()
    context= {'count': count}
    paginator = Paginator(user_list,25)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:

        users = paginator.page(paginator.num_pages)
    return render(request, 'book/user_list.html', { 'users': users ,'count':count})
