from django.shortcuts import render
from django.views.generic import View
from library.forms import BookCreateForm
from library.models import Book

# Create your views here.

class BookCreateView(View):
    def get(self,request,*args,**kwargs):
        form=BookCreateForm()

        return render(request,"book_add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        
        form=BookCreateForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Book.objects.create(**form.cleaned_data)
            
            print("To dos created")
            return render(request,"book_add.html",{"form":form})
            

        else:
            return render(request,"book_add.html",{"form":form})
        
class BookListView(View):
    def get(self,request,*args,**kwargs):
        
        qs=Book.objects.all()
        return render(request,"book_list.html",{"books":qs})
    

class BookDetailView(View):
    def get(self,request,*args,**kwargs):
        
        id=kwargs.get("id")
        print(kwargs)
        qs=Book.objects.get(id=id)
        return render(request,"book_details.html",{"books":qs})   