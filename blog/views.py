from django.shortcuts import render, redirect
from .models import Post, Contact, Comments
from django.core.paginator import Paginator
import requests

BOT_TOKEN = '6235320770:AAEG9jfSuctcyNQEPrr_IjdZLWoIVM0NYhk'
CHAT_ID = '5046341911'


def home(request):
    posts = Post.objects.filter(is_published=True).order_by('-view_count')[:2]

    d = {
        'posts': posts,
        'home': 'active',

    }
    return render(request, 'index.html', context=d)


def blog(request):
    data = request.GET
    cat = data.get('cat', None)
    page = data.get('page', 1)
    if cat:
        posts = Post.objects.filter(is_published=True, category_id=cat)
        d = {
            'posts': posts,
            'blog': 'active',
        }
        return render(request, 'blog.html', context=d)

    posts = Post.objects.filter(is_published=True)
    page_obj = Paginator(posts, 2)
    d = {
        'blog': 'active',
        'posts': page_obj.get_page(page)
    }

    return render(request, 'blog.html', context=d)


def blog_detail_view(request, pk):
    if request.method == 'POST':
        data = request.POST
        blog = Post.objects.filter(pk=pk).first()
        comment = Comments.objects.create(post_id=pk, name=data["name"], email=data["email"], message=data["message"])
        comment.save()
        blog.comments_count += 1
        blog.save(update_fields=['comments_count'])
        return redirect(f'/blog/{pk}/')
    blog = Post.objects.filter(pk=pk).first()
    blog.view_count += 1
    blog.save(update_fields=['view_count'])
    comments = Comments.objects.filter(post_id=pk)
    return render(request, 'blog_single.html', {'blog': blog, 'comments': comments})


def about(request):
    return render(request, 'about.html', context={'about': 'active'})


def contact(request):
    if request.method == 'POST':
        data = request.POST
        obj = Contact.objects.create(full_name=data['name'], email=data['email'], subject=data['subject'],
                                     message=data['message'])
        obj.save()
        text = f"""
        project: MOOSE
        id: {obj.id}
        name:{obj.full_name}
        subject:{obj.message}
        """
        url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}'
        response = requests.get(url)
        print(response)
        return redirect('/contact')
    return render(request, 'contact.html', context={'contact': 'active'})

# Create your views here.
