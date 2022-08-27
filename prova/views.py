import json

from django.http import HttpResponse
from django.shortcuts import render
from prova import crud
from prova.forms import BlogPostForm


def test_view(request, post_id):
    if request.user.is_authenticated:
        if request.method == 'GET':
            blog_posts = crud.get_blog_posts(request.user)
            return render(request, 'prova/test.html', {
                'title': "Blogposts di " + request.user.username,
                'blog_posts': blog_posts,
                'blog_form': BlogPostForm(),
            })
        elif request.method == 'POST':
            body = json.loads(request.body)
            bp = crud.create_blog_post(body['title'], body['text'], request.user, body['color'])
            return HttpResponse(bp)
        elif request.method == 'PUT':
            body = json.loads(request.body)
            bp = crud.updated_blog_post(request.user, post_id, **body)
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


def commentView(request, post_id):
    if request.user.is_authenticated:
        if request.method == 'GET':
            comments = crud.get_all_comments(post_id)
            return render(request, 'prova/comment.html', {
                'title': 'Commenti',
                'comments': comments
            })
        elif request.method == 'POST':
            body = json.loads(request.body)
            comment = crud.create_comment(body['blogpost'], body['subtitle'], body['text'], request.user)
            if comment:
                return HttpResponse(comment)
            else:
                return HttpResponse("Comment not found", status=404)
        elif request.method == 'PUT':
            body = json.loads(request.body)
            post = body['blogpost']
            commentId = body['commentId']
            del body['blogpost']
            del body['commentId']
            comment = crud.update_comment(request.user, post, commentId, **body)
            if comment:
                return HttpResponse(comment)
            else:
                return HttpResponse("Comment not found", status=404)
        elif request.method == 'DELETE':
            return HttpResponse(status=crud.delete_comment(request.user, 1, 1))
    else:
        HttpResponse('Accedi per visualizzare i commenti', status=403)
