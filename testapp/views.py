from django.shortcuts import render,redirect

# Create your views here.
def home_view(request):
    return render(request,'testapp/base.html')


from testapp.models import *
def contact_view(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        msg=request.POST.get('msg')
        store=Contact(name=name,email=email,msg=msg)
        store.save()
        return redirect('/thanks')
    return render(request,'testapp/contact.html')


def skill_view(request):
    return render(request,'testapp/skills.html')


def thank_view(request):
    return render(request,'testapp/thanks.html')



def about_view(request):
    return render(request,'testapp/about.html')