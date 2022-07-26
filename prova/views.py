from django.http import HttpResponse
from django.shortcuts import render
from prova import crud


def test_view(request):
    if request.user.is_authenticated:
        blog_posts = crud.get_blog_posts(request.user)
        return render(request, 'prova/test.html', {
            'title': 'Pippo',
            'blog_posts': blog_posts,
        })
    else:
        return HttpResponse('Accedi per visualizzare il contenuto')
