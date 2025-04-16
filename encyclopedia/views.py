from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from . import util
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request,name):
    if util.get_entry(name)!=None:
          return render (request,"encyclopedia/entry.html",{
               "entry":util.get_entry(name),
               "title":name,
          })
    else:
        print("HERE",name)
        return render(request,"encyclopedia/error.html")
    
def search(request):
     query=request.GET.get("q")
     if query in util.list_entries():
         return HttpResponseRedirect(reverse("entry",args=[query]))
         
     else:
          nq=query.lower()
          entries=util.list_entries()
          matches=[]
          for e in entries:
               if nq in e.lower():
                    matches.append(e)
          return render(request,"encyclopedia/search.html",{"matches":matches})
     
def new(request):
     if request.method=="POST":
      print("HERERER")
      title=request.POST.get("title")
      if title not in util.list_entries():
                content=request.POST.get("content")
                util.save_entry(title,content)
                return HttpResponseRedirect(reverse("entry",args=[title]))
      else:
            return render(request,"encyclopedia/error.html",{
                "message":"Entry already exists",
            })
     else:
          print("Paji here")
          return render(request ,"encyclopedia/new_page.html")
def rdom(request):
     r=random.choice(util.list_entries())
     return HttpResponseRedirect(reverse("entry",args=[r]))

        
     
          
     
     

