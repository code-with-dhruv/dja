from django.shortcuts import render
from DjangoCrud.models import Posts
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from bson import ObjectId

@csrf_exempt

def add_post(request):
    post=Posts(StudentName=request.POST.get("StudentName"),Age=request.POST.get("Age"),DoB=request.POST.get("DoB"),Grade=request.POST.get("Grade"))
    post.save()
    return HttpResponse("Inserted")
def update_post(request,id):
    pass
def delete_post(request,id):
    pass
def read_post(request,id):
    post=Posts.objects.get(_id=ObjectId(id))
    stringval="studentName"+post.StudentName+"AGE:"+post.Age +"DOB"+ post.DoB +"GRADE:"+ post.Grade
    return stringval
