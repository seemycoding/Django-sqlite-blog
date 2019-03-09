from django.shortcuts import render
from django.http import HttpResponse
from blog.forms import registrationForm, loginForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from blog.models import AddPost
from django.contrib.auth import logout as log
from django.contrib.auth.decorators import login_required


# Create your views here.
def Home(request):
    return render(request, 'blog/home.htm')


def about(request):
    return render(request, 'blog/about.htm')


def blog(request):
    if request.method == "POST":
        if request.session.has_key('username'):
            name = request.session['username']
            request.session.set_expiry(300)
            posts = AddPost.objects.all()
            return render(request, 'blog/blog.htm', {'Name': name, 'nav': 'Nav', 'Posts': posts})
    else:
        if request.session.has_key('username'):
            name = request.session['username']
            request.session.set_expiry(300)
            posts = AddPost.objects.all()
            return render(request, 'blog/blog.htm', {'Name': name, 'nav': 'Nav', 'Posts': posts})
        return render(request, 'blog/login.htm', {'form': loginForm})


def login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        regiform = registrationForm()
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

        user = authenticate(username=email, password=password)
        if user is not None:
            auth_login(request, user)
            request.session['username'] = email
            return render(request, 'blog/blog.htm', {'Name': email, 'nav': 'Nav'})
        else:
            return render(request, 'blog/registration.htm', {'form': regiform})

    else:
        form = loginForm()
        return render(request, 'blog/login.htm', {'form': form})


def register(request):
    if request.method == 'POST':
        form = registrationForm(request.POST)
        loginForm = loginForm()
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(
                username=email, email=email, password=password)
            user.save()
            request.session['username'] = email
            return render(request, 'blog/login.htm', {'form': loginForm})

    else:
        form = registrationForm()
        return render(request, 'blog/register.htm', {'form': form})


@login_required(login_url='login')
def add(request):
    if request.method == 'POST':
        Title = request.POST.get('title')
        Category = request.POST.get('category')
        Body = request.POST.get('body')
        post = AddPost(titile=Title, category=Category, body=Body)
        instance = post
        instance.user = request.user
        instance.save()
        return render(request, 'blog/viewpost.htm')
    else:
        return render(request, 'blog/add.htm')


@login_required(login_url='login')
def viewpost(request):
    post = AddPost.objects.filter(user=request.user.id)
    return render(request, 'blog/viewpost.htm', {'posts': post})


@login_required(login_url='login')
def logout(request):
    log(request)
    return render(request, 'blog/login.htm', {'form': loginForm})

@login_required(login_url='login')
def details(request,idd):
    print(idd)
    detailedpost=AddPost.objects.filter(id=idd)
    print(detailedpost)
    return render(request,'blog/details.htm',{'posts': detailedpost})