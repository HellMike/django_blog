from django.shortcuts import render

posts = [
    {
        'author': 'SemenEV',
        'title': 'Post 1',
        'content': 'First post content',
        'date_posted': 'March 15, 2007'
    },
    {
        'author': 'VladimirKS',
        'title': 'Post 6',
        'content': 'Sixth post content',
        'date_posted': 'July 25, 2009'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
