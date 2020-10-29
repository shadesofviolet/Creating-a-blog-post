from django.shortcuts import render

# Create your views here.
#whatever view we added to our blog.urls path, we will write it here.

def post_list(request):
    return render(request, 'blog/post_list.html',{})

#def post_list: accepts requests and returns it by calling the function render- which puts together our template 'blog/post_list.html'