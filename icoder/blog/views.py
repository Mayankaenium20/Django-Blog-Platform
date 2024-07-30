from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from blog.models import Post


# Create your views here.
def blogHome(request):
    # return HttpResponse("This is the blogHome!. We will keep all the posts here.")'
    allPosts = Post.objects.all()       #fetches the every blog snos with their content in the form of a query set obj
    context = {
        'allPosts' : allPosts           #html var : py var
    }
    return render(request, 'blog/blogHome.html', context)

def blogPost(request, slug):                    #the slug defined in the local urls.py will be passed here. Hence, the extra arg is passed. 
    # return HttpResponse(f"This is the Blog Post: {slug}")
    # return render(request, 'blog/blogPost.html')
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/blogPost.html', {'post': post})
