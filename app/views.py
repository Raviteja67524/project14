from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['topic']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('insert_topic is done')
    return render(request,'insert_topic.html')    
        
        
    
def form_webpage(request):

    if request.method=="POST":
        tn=request.POST['topic']
        name=request.POST['name']
        url=request.POST['url']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        W=webpages.objects.get_or_create(topic_name=T,name=name,url=url)[0]
        W.save()
        return HttpResponse('inserted webpages successfull')

    return render(request,'form_webpage.html')



def  form_Access(request):
    if request.method=="POST":
        tn=request.POST['topic']
        name=request.POST['name']
        url=request.POST['url']
        date=request.POST['date']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        W=webpages.objects.get_or_create(topic_name=T,name=name,url=url)[0]
        W.save()
        A=AccessRecords.objects.get_or_create(name=W,date=date)[0]
        A.save()
        return HttpResponse('Insertes AccessRecords successfull')
    return render(request,'form_Access.html')
    
    

