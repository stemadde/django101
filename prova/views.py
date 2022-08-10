from django.http import HttpResponse
from django.shortcuts import render
from prova import crud
from prova.forms import BlogPostForm


def test_view(request, post_id):
    if request.user.is_authenticated:
        if request.method == 'GET':
            blog_posts = crud.get_blog_posts(request.user)
            return render(request, 'prova/test.html', {
                'title': 'Pippo',
                'blog_posts': blog_posts,
                'blog_form': BlogPostForm(),
            })
        elif request.method == 'POST':
            bp = crud.create_blog_post('Ciao', 'TESTO', request.user, 'FFFFFF')
            return HttpResponse(bp)
        elif request.method == 'PUT':
            bp = crud.updated_blog_post(request.user, post_id, title='Mod', text='Alter', color='CCCCCC')
            if bp:
                return HttpResponse(bp)
            else:
                return HttpResponse('Object not found', status=404)
        elif request.method == 'DELETE':
            code = crud.delete_blog_post(request.user, post_id)
            return HttpResponse(status=code)
        else:
            return HttpResponse('Metodo non consentito', status=405)
    else:
        return HttpResponse('Accedi per visualizzare il contenuto', status=403)
