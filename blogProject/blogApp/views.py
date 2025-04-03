from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def post_create(request):

    if request.method == 'POST':

        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
        
    else : 
        form = PostForm()

    return render(request, 'create.html', {'form':form})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts' : posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'detail.html', {'post': post})


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'detail.html', {'post': post})


def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # 사용자가 작성한 글이 아닐 경우 접근 제한
    if request.user != post.author:
        return redirect('post_detail', post_id=post.id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'edit.html', {'form': form, 'post': post})


def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # 사용자가 작성한 글이 아닐 경우 접근 제한
    if request.user != post.author:
        return redirect('post_detail', post_id=post.id)

    if request.method == "POST":
        post.delete()
        return redirect('home')

    return render(request, 'delete.html', {'post': post})




