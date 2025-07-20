from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, ContactForm, NewsForm, ProfilForm, CommentForm
from django.views.generic import View
from django.contrib import messages
from django.db.models import Q
# Create your views here.
def home(request):
    categories = Category.objects.all()
    first_news = []
    for category in categories:
        category_first_post = News.objects.filter(category=category).order_by('-id').first()
        first_news.append(category_first_post)
    first_news = first_news[-5:]
    news = News.objects.all().order_by('-id')

    return render(request, 'home.html', {
        'categories': categories,
        'first_news': first_news,
        'news': news
    })

def category_list(request):
    query_n = request.GET.get('n', '')
    query_p = request.GET.get('p', '')
    if query_n and query_p:
        a = Category.objects.filter(
            Q(name__icontains=query_n) & Q(price=query_p)
        )
    elif query_n:
        a = Category.objects.filter(
            Q(name__icontains=query_n)
        )
    else:
        a = Category.objects.all()
    categories = Category.objects.all()
    return render(request,'category-list.html', {'categories': categories, 'a': a})




@login_required(login_url='login')
def category(request, pk):
    category = Category.objects.get(id=pk)
    news = News.objects.filter(category=category).order_by('-id')
    print(news)
    return render(request, 'category.html',{'news':news})




def new_detail(request, pk):
    post = get_object_or_404(News, id=pk)
    comments = Comment.objects.filter(news=post).order_by('-id')[:3]
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = post
            comment.user = request.user
            comment.save()
            messages.success(request, "Izoh muvaffaqiyatli qo‘shildi")
            return redirect('detail', pk=post.id)

    return render(request, 'detal.html', {
        'post': post,
        'comments': comments,
        'form': form
    })




class Post_create(View):
    def get(self, request):
        form = CategoryForm()
        return render(request, 'create_post.html',{'form':form})

    def post(self, request):
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('category_list')
        return render(request, 'create_post.html',{'form':form})
    

@login_required(login_url = 'login')
def profile(resquest):
    user = User.objects.get(username=resquest.user.username)
    return render(resquest, 'profile.html', {'user':user})

def user(request):
    return render(request, 'user.html')



@login_required(login_url='login')  
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            messages.success(request, "Xabaringiz muvaffaqiyatli yuborildi!")
            return redirect('contact')  
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})




@login_required
def update_post(request, pk):
    post = get_object_or_404(News, id=pk)


    if post.user != request.user:
        messages.error(request, "Siz bu postni o'zgartira olmaysiz!")
        return redirect('home') 

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post muvaffaqiyatli yangilandi!")
            return redirect('detail', pk=post.id)
    else:
        form = NewsForm(instance=post)

    return render(request, 'update_post.html', {'form': form})



@login_required
def del_post(request, pk):
    post = get_object_or_404(News, id=pk)


    if post.user != request.user:
        messages.error(request, "Siz bu postni o'chira olmaysiz!")
        return redirect('home') 
    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post muvaffaqiyatli o'chirildi!")
        return redirect('home')
    
    return render(request, 'del_post.html', {'post': post})


@login_required

def new_comment(request, pk):
    post = get_object_or_404(News, pk=pk)
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.tech = post
            comment.save()
            messages.success(request, "Izoh muvaffaqiyatli qo‘shildi.")
            return redirect('detail', pk=pk)

    return render(request, 'detal.html', {'post': post, 'form': form})



@login_required
def profile_update(request):
    if request.method == 'POST':
        form = ProfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profil muvaffaqiyatli yangilandi!")
            return redirect('profile') 
    else:
        form = ProfilForm(instance=request.user)

    return render(request, 'profile_update.html', {'form': form})



@login_required
def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk, user=request.user)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Kommentariya tahrirlandi.")
            return redirect('detail', pk=comment.news.pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'edit_commit.html', {'form': form})


@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk, user=request.user)

    if request.method == 'POST':
        post_id = comment.news.pk
        comment.delete()
        messages.success(request, "Kommentariya o‘chirildi.")
        return redirect('detail', pk=post_id)

    return render(request, 'delete_confirm.html', {'comment': comment})

