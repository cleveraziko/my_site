from django.shortcuts import render, get_object_or_404
# from datetime import  date
from .models import Post



# def get_date(post):
#     return post['date']



def starting_page(request):
    latest_posts =  Post.objects.all().order_by('-date')[:3]
    return render(request,'blog/index.html',{"posts":latest_posts})



def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html",{
        "all_posts": all_posts
    })


def post_detail(request,slug):
    # post_id = next(post for post in all_posts if post['slug']== slug)
    # post_id = Post.objects.get(slug=slug)
    post_id = get_object_or_404(Post, slug=slug)
    return render(request,"blog/post-detail.html",{
        "post": post_id  
    })
