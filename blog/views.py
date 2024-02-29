from django.shortcuts import render, redirect
from .models import Post, Contact, Comments


def home(request):
    posts = Post.objects.all()
    d = {
        'posts': posts
    }
    return render(request, 'index.html', context=d)


def blog(request):
    data = request.GET
    cat = data.get('cat', None)
    if cat:
        posts = Post.objects.filter(is_published=True, category_id=cat)
    else:
        posts = Post.objects.filter(is_published=True)
    d = {
        'posts': posts, 'blog': 'active'

    }
    return render(request, 'blog.html', context=d)


def blog_detail(request, pk):
    if request.method == 'POST':
        data = request.POST

        comment = Comments.objects.create(post_id=pk, name=data["name"], email=data["email"], message=data["message"])
        comment.save()
        return redirect(f'/blog/{pk}/')
    blog = Post.objects.filter(id=pk).first()
    comments = Comments.objects.filter(post_id=pk)
    d = {'blog': blog, 'comments': comments,'comments_count':len(comments)}
    return render(request, 'blog_single.html', context=d)


def about(request):
    return render(request, 'about.html')


def cantact(request):
    if request.method == 'POST':
        data = request.POST
        obj = Contact.objects.create(full_name=data['name'], email=data['email'], subject=data['subject'],
                                     message=data['message'])
        obj.save()
        return redirect('/contact')
    return render(request, 'contact.html')

# Create your views here.
