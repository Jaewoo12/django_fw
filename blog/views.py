from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.models import User

from .models import Post
from .forms import PostModelform, PostForm

# Post 등록1 : Form 사용
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # form 데이터가 clean한 상태
            print(form.cleaned_data)
            post = Post.objects.create(
                                author=User.objects.get(username=request.user.username),
                                title = form.cleaned_data['title'],
                                text = form.cleaned_data['text'],
                                published_date = timezone.now()
                                )
            return redirect('post_detail',pk=post.pk)
    else:
        # 등록하는 빈 폼 보여주기
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})

# Post 등록2 : ModelForm 사용
def post_new(request):
    if request.method == 'POST':
        # 실제등록 처리하기
        form = PostModelform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # 작성자
            post.author = User.objects.get(username=request.user.username)
            # 글게시날짜
            post.published_date = timezone.now()
            # 실제등록된
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        # 등록하는 빈 폼 보여주기
        form = PostModelform()
    return render(request, 'blog/post_edit.html', {'form':form})

# Post 수정 : ModelForm 사용
def post_edit(request,pk):
        post = get_object_or_404(Post,pk=pk)
        if request.method == 'POST':
            form = PostModelform(request.POST, instance = post)
            if form.is_valid():
                post = form.save(commit=False)
                # 작성자
                post.author = User.objects.get(username=request.user.username)
                # 글게시날짜
                post.published_date = timezone.now()
                # 실제 갱신됨
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostModelform(instance=post)
        return render(request, 'blog/post_edit.html',{'form':form})

# Post 상세정보
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

# Post 목록
def post_list_response(request):
    name = 'Django'
    #return HttpResponse(f'''<h2>Hello {name}!!</h2><p>HTTP METHOD : {request.method}</p>''')
    response = HttpResponse(content_type="text/html")
    response.write(f'<h2>hello {name}!!</h2>')
    response.write(f'<p>HTTP METHOD : {request.method}</p>')
    response.write(f'<p>HTTP contenttype : {request.content_type}</p>')
    return response

# Post 목록2
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',{'posts':posts})

