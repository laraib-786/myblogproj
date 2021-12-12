from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .models import Post, Comments

from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def post_create_view(request):
    if request.method=='POST':
        context={}
        title=request.POST['title']
        content=request.POST['content']
        #image=request.FILES['fileupload']
        image=request.POST.get('fileupload', False)
        

        if title and content:
            if image:
                user=request.user
                post=Post.objects.create(title=title,content=content,author=user,image=image)
                id=post.id

                #context['error']='Your post has been successfully created!'
                return post_detail_view(request,id)
            else:
                user=request.user
                post=Post.objects.create(title=title,content=content,author=user)
                id=post.id
                return post_detail_view(request,id)

        else:
            context['error']='Your title and content can not empty'
            return render(request,'posts/create.html',context=context)
    else:
        return render(request,'posts/create.html')
# this is to view one specific blog post

def post_detail_view(request,id):
    posts=Post.objects.filter(id=id).first()
    context={'posts':posts}
    context['total_likes']=posts.total_likes()
    return render(request,'posts/detail.html',context=context)

# this is to view all blog post

def post_list_view(request):
    posts=Post.objects.all()
    context={'posts':posts}
    return render(request,'posts/list.html',context=context)

@login_required
def post_update_view(request,id):
    context={}
    post=Post.objects.filter(id=id).first()
    context['post']=post
    if request.user==post.author:
        if request.method=='POST':
            title=request.POST['title']
            content=request.POST['content']
            if 'fileupload' in request.FILES:
                image=request.FILES['fileupload']
            else:
                image=False
            if title and content:
                if image:
                    post.title=title
                    post.content=content
                    post.image=image
                    post.save()
                    context['error']='Your post has been successfully updated!'
                    return render(request,'posts/update.html',context=context)
                else:
                    post.title=title
                    post.content=content
                  
                    post.save()
                    context['error']='Your post has been successfully updated!'
                    return render(request,'posts/update.html',context=context)

            else:
                context['error']='Your title and content can not empty'
                return render(request,'posts/update.html',context=context)
        else:
            return render(request,'posts/update.html',context=context)
    else:
        return redirect('posts:list')


@login_required
def post_delete_view(request,id):
    #post=Post.objects.filter(id=id)
    post=Post.objects.filter(id=id).first()
    if request.user==post.author:
        if request.method=='POST':
            post.delete()
            return redirect('posts:list')
        else:
            return render(request,'posts/delete.html')
    else:
        return redirect('posts:list')
@login_required
def post_like_view(request,id):
    post=Post.objects.filter(id=id).first()
    post.likes.add(request.user)

    return HttpResponseRedirect(reverse('posts:detail',args=[str(id)]))
    

def post_comments_view(request,id):
    post=Post.objects.filter(id=id).first()
    context={}
    context['posts']=post
    if request.method=='POST':
    
        name=request.POST['title']
        content=request.POST['content']

        if name and content:
            user=request.user
            comment=Comments.objects.create(name=name,content=content,post=post)
            id=post.id

            #context['error']='Your post has been successfully created!'
            return post_detail_view(request,id)
        else:
            context['error']='Your name and content can not empty'
            return render(request,'posts/comment.html',context=context)
    else:
        return render(request,'posts/comment.html',context=context)
