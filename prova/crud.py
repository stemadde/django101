from typing import Optional
from django.contrib.auth.models import User
from django.db.models import QuerySet
from prova.models import BlogPostComment
from prova.models import BlogPost


def get_blog_posts(user: User) -> QuerySet:
    return BlogPost.objects.filter(user=user)


def get_blog_post(user:User, post_id: int) -> Optional[BlogPost]:
    return get_blog_posts(user).filter(id=post_id).first()


def create_blog_post(title: str, text: str, user: User, color: str) -> BlogPost:
    return BlogPost.objects.create(title=title, text=text, user=user, color=color)


def delete_blog_post(user: User, post_id: int) -> int:
    """
    :param user: User object
    :param post_id:
    :return: Status code -> 204 = ok, 404 = error
    """
    # ugly except but meh, don't know what .delete() throws
    try:
        BlogPost.objects.filter(user=user, id=post_id).first().delete()
        return 204
    except AttributeError:
        return 404
    except ValueError:
        return 404


def updated_blog_post(user: User, post_id: int, **kwargs) -> Optional[BlogPost]:
    bp = BlogPost.objects.filter(user=user, id=post_id).first()
    if bp:
        for key, value in kwargs.items():
            setattr(bp, key, value)
        bp.save()
        return bp

#CRUD for comments


def get_all_comments(post_id: int) -> Optional[dict]:
    commentsQueryset = BlogPostComment.objects.filter(
        blogpost=post_id
    )
    returnDict = {}
    for comment in commentsQueryset:
        returnDict[comment.pk] = comment
    return returnDict


def get_all_comment(post_id:int, commentId: int) ->Optional[BlogPostComment]:
    return BlogPostComment.objects.filter(
        blogpost=post_id,
        id=commentId
    ).first()


def get_comments(user:User, post_id: int) -> Optional[dict]:
    commentsQueryset = BlogPostComment.objects.filter(
        blogpost=post_id,
        user=user
    )
    returnDict = {}
    for comment in commentsQueryset:
        returnDict[comment.pk] = comment
    return returnDict


def get_comment(user:User, post_id:int, commentId: int) ->Optional[BlogPostComment]:
    return BlogPostComment.objects.filter(
        blogpost=post_id,
        id=commentId,
        user=user
    ).first()


def create_comment(blog_post : int, subtitle : str, text : str) -> BlogPostComment:
    return BlogPostComment.objects.create(blog_post=blog_post, subtitle=subtitle, text=text)


def delete_comment(user : User, post_id : int, commentId : int):
    try:
        BlogPostComment.objects.filter(user=user, blogpost=post_id, id=commentId).first().delete()
        return 204
    except AttributeError:
        return 404
    except ValueError:
        return 404


def update_comment(user : User, post_id: int, commentId: int, **kwargs) -> Optional[BlogPostComment]:
    bpc = get_comment(user,post_id,commentId)
    if bpc:
        for key, value in kwargs.items():
            setattr(bpc, key, value)
        return bpc.save()

#ALL IS TO BE TESTED
