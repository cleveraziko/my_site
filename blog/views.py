from django.shortcuts import render
from datetime import  date
# Create your views here.

all_posts =[
    {
        'slug': "hikeinmountains",
        'author':'Azamat ',
        "date": date(2021, 7, 15),
        'title': 'Mountain haiking',
        'content': """
             Fuga esse voluptatem perspiciatis. Ex eligendi aperiam molestiae fugit dicta esse nam itaque, iure facilis vel placeat reprehenderit, laudantium saepe beatae, doloremque nulla. Dignissimos doloremque magni est suscipit omnis veritatis?
   
             Fuga esse voluptatem perspiciatis. Ex eligendi aperiam molestiae fugit dicta esse nam itaque, iure facilis vel placeat reprehenderit, laudantium saepe beatae, doloremque nulla. Dignissimos doloremque magni est suscipit omnis veritatis?
    
             Fuga esse voluptatem perspiciatis. Ex eligendi aperiam molestiae fugit dicta esse nam itaque, iure facilis vel placeat reprehenderit, laudantium saepe beatae, doloremque nulla. Dignissimos doloremque magni est suscipit omnis veritatis?
        """
    },
    {
        'slug': "hike-in-mountains",
        'author':'Azamat ',
        "date": date(2021, 7, 15),
        'title': 'Mountain haiking',
        'content': """
             Fuga esse voluptatem perspiciatis. Ex eligendi aperiam molestiae fugit dicta esse nam itaque, iure facilis vel placeat reprehenderit, laudantium saepe beatae, doloremque nulla. Dignissimos doloremque magni est suscipit omnis veritatis?
   
             Fuga esse voluptatem perspiciatis. Ex eligendi aperiam molestiae fugit dicta esse nam itaque, iure facilis vel placeat reprehenderit, laudantium saepe beatae, doloremque nulla. Dignissimos doloremque magni est suscipit omnis veritatis?
    
             Fuga esse voluptatem perspiciatis. Ex eligendi aperiam molestiae fugit dicta esse nam itaque, iure facilis vel placeat reprehenderit, laudantium saepe beatae, doloremque nulla. Dignissimos doloremque magni est suscipit omnis veritatis?
        """   
    },
    {
        'slug': "hike-in-mountains",
        'author':'Azamat ',
        "date": date(2021, 7, 15),
        'title': 'Mountain haiking',
        'content': """
             Fuga esse voluptatem perspiciatis. Ex eligendi aperiam molestiae fugit dicta esse nam itaque, iure facilis vel placeat reprehenderit, laudantium saepe beatae, doloremque nulla. Dignissimos doloremque magni est suscipit omnis veritatis?
   
             Fuga esse voluptatem perspiciatis. Ex eligendi aperiam molestiae fugit dicta esse nam itaque, iure facilis vel placeat reprehenderit, laudantium saepe beatae, doloremque nulla. Dignissimos doloremque magni est suscipit omnis veritatis?
    
             Fuga esse voluptatem perspiciatis. Ex eligendi aperiam molestiae fugit dicta esse nam itaque, iure facilis vel placeat reprehenderit, laudantium saepe beatae, doloremque nulla. Dignissimos doloremque magni est suscipit omnis veritatis?
        """
    }
]


def get_date(post):
    return post['date']



def starting_page(request):
    sorted_posts = sorted(all_posts,key=get_date)
    latest_posts = sorted_posts[-3:] 
    return render(request,'blog/index.html',{"posts":latest_posts})



def posts(request):
    return render(request, "blog/all-posts.html",{
        "all_posts": all_posts
    })


def post_detail(request,slug):
    post_id = next(post for post in all_posts if post['slug']== slug)
    return render(request,"blog/post-detail.html",{
        "post": post_id  
    })