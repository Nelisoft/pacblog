from django.shortcuts import render, get_object_or_404,redirect
from .models import Post,Category
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PostForm
from django.core.paginator import Paginator
# from django
# Create your views here.

def Home(request):
    featured = Post.objects.filter(featured=True,status='approved').order_by('-id')[:1]
    trending = Post.objects.filter(trending=True, status='approved').order_by('-id')[:4]
    post = Post.objects.filter(status='approved').order_by('-id')
    paginator = Paginator(post,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # user = u
    context ={
        'featureds':featured,
        'trending':trending,
        'page_obj':page_obj
    }
    return render(request, 'core/index.html' ,context)


def PostDetails(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context={
        'post':post
    }
    return render(request, 'core/single-blog.html', context)
def About(request):
    return render(request, 'core/about.html')

@login_required
def Create_Post(request):
    form = PostForm
    categories = Category.objects.all()
    context={
        "form":form, 
         "categories": categories
    }
    if request.method =="POST":
        form = form(request.POST, request.FILES )
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
        print(messages.error)
    return render(request, "core/create.html",context)


@login_required
def Update_Post(request,pk):
    post = get_object_or_404(Post,pk=pk, author = request.user)
 
    categories = Category.objects.all()
    context = {
        "post":post,
        "categories":categories
    }
    if request.method =="POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('home')
        
    else:
        form = PostForm(instance=post)
        

    return render(request, 'core/update.html', context)




@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)  # only author can delete

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('home')  # or wherever your list view is

    return render(request, 'core/delete_post.html', {'post': post})
