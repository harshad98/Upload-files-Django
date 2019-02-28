from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import BookForm
from .models import Book

def index(request):
    return render(request,'prax/index.html')

def upload(request):
    context={}
    if request.method =='POST':
        uploaded_file=request.FILES['document']
        fs=FileSystemStorage()
        name=fs.save(uploaded_file.name,uploaded_file)
        context['url']= fs.url(name)
    return render(request,'prax/upload.html',context)

def book_list(request):
    books= Book.objects.all()
    return render(request,'prax/book_list.html',{
        'books':books })


def upload_book(request):
    if request.method=='POST':
        form=BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('book_list')
    else:
         form =BookForm()
    return render(request,'prax/upload_book.html',{
        'form':form
    })

def about(request):
    return render(request,'prax/about.html')

def contact(request):
    return render(request,'prax/contact.html')




