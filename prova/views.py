from django.http import HttpResponse
from django.shortcuts import render
from prova.crud import get_blog_posts


def test_view(request):
    if request.user.is_authenticated:
        return render(request, 'prova/test.html', {
            'title': 'Pippo',
            'blog_posts': get_blog_posts(request.user),
        })
    else:
        return HttpResponse('Accedi per visualizzare il contenuto')
