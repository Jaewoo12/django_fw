from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Post

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
