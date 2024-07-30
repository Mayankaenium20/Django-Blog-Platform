from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from blog.models import Post
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
import json
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method == 'POST':
        # print("We are using the POST request!")
        name = request.POST['name']             #'name' is the name defined in the contacts page in the html form
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        if not name or not email or len(phone)<10 or not content: 
            messages.error(request, "All fields are necessary!")
        else:
            print(name, email, phone, content, sep = " ")
            contact = Contact(name = name, email = email, phone = phone, content = content)   #values passed to the dataset
            contact.save()                       #done to update the db
            messages.success(request, "Thank you for your message. We will get back to you shortly.")     
                
    return render(request, 'home/contact.html')

def featured_block(request):
    print("Entering featured_block view...")  # Debug statement
    author="Andrew Nguyen"

    post = Post.objects.filter(author__icontains = author)
    print("Query executed.")  # Debug statement

    if post:
        print(f"Author: {post.author}")
        print(f"Title: {post.title}")
        print(f"Content: {post.content[:100]}...")
    else:
        print("No post found for the author!")

    context = {
        "1_post": post
    }

    print("Rendering template with context...")  # Debug statement
    return render(request, "home/home.html", context)

def search(request):

    query = request.GET['query']            #defined in the name and id of the html code under search button to link the views.py function with it.

    if len(query) > 70:
        allPosts = Post.objects.none()
    
    else:
        allPostsTitle = Post.objects.filter(title__icontains = query)
        allPostsContent = Post.objects.filter(content__icontains = query)
        allPostsAuthor = Post.objects.filter(author__icontains = query)

        allPost0 = allPostsTitle.union(allPostsContent)                         #v1.union(v2) is a django feature of combining the
        allPosts = allPost0.union(allPostsAuthor)

    print(allPosts)

    if allPosts.count() == 0:
        messages.warning(request, "No search results found!")
    # allPosts = Post.objects.all()
    params = {'allPosts' : allPosts,
              'Query' : query
              }

    return render(request, 'home/search.html', params)

#modal handling - signup and login
def handleSignup(request):
    if request.method == 'POST':
        # Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        #validation of inputs:
        if not len(username):
            messages.error(request, "Username cannot be empty!")
            return redirect('home')
        
        if pass1 != pass2:
            messages.error(request, "Passwords don't match. Type the password again.")
            return redirect('home')
        
        if not pass1.isalnum():
            messages.error(request, "Username should only contain letters and numbers.")
            return redirect('home')

        #creation of user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your iCoder account has been successfully created!")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found!")
    

def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username = loginusername, password = loginpassword)                 #the var names must be passed as defined parameters as they are a part of the function syntax

        #login validation
        if user is not None:                                                                    #django implcitely performs the authentication process and doesn't need explicity code as such.
            login(request, user)
            messages.success(request, "Logged in! Congrats!")
            return redirect('/')

        else: 
            messages.error(request, "Invalid credentials! Please try again.")
            return redirect('/')

    return HttpResponse(f"username = {loginusername} and pass = {loginpassword}")

def handleLogout(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "Logged out successfully!")
        return redirect('home')
    
    else:
        messages.error(request, "Try logging out again!")
        return redirect('home')
    

#rest api
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer

class UpdateUserView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
     
    def get_object(self):
        return self.request.user

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)