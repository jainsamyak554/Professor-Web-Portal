from .models import Info,Department ,teaching,publication , completebtstudents,completemtstudents,completephdstudents,continuingbtstudents,continuingmtstudents,continuingphdstudents, recognition, project
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import userform, teachingform,publicationform,projectform,recognitionform,CaptchaForm,publicationform1
from django.views.generic import CreateView, DeleteView, UpdateView
from .crawler import postupdate
# Create your views here.


class infocreate (CreateView):
    model = Info
    fields = '__all__'

class teachingcreate (CreateView):
    model = teaching
    fields = '__all__'

def teachingcreate(request, prof_id):
    info = Info.objects.get(id=prof_id)


    if request.method == 'POST':
        form = teachingform(request.POST)
        if form.is_valid():

            teachings = teaching.objects.create(sem=form.cleaned_data['sem'] , course=form.cleaned_data['course'], year=form.cleaned_data['year'],teaching= info)

            return HttpResponseRedirect(reverse('web:teachingview',args=[str(info.Dept.id),str(info.id)]))
    else:
        form = teachingform()
    return render(request, 'web/teaching_form.html',{'form':form})

def publicationcreate(request, prof_id):
    info = Info.objects.get(id=prof_id)


    if request.method == 'POST':
        form = publicationform(request.POST)
        if form.is_valid():

            publications = publication.objects.create(publication_details=form.cleaned_data['publication_details'] , publication=info)

            return HttpResponseRedirect(reverse('web:publicationview',args=[str(info.Dept.id),str(info.id)]))
    else:
        form = publicationform()
    return render(request, 'web/publication_form.html',{'form':form})

def projectcreate(request, prof_id):
    info = Info.objects.get(id=prof_id)


    if request.method == 'POST':
        form = projectform(request.POST)
        if form.is_valid():

            projects = project.objects.create(title=form.cleaned_data['title'], pi=form.cleaned_data['pi'], agency=form.cleaned_data['agency'], startyear=form.cleaned_data['startyear'], endyear=form.cleaned_data['endyear'] ,project=info )

            return HttpResponseRedirect(reverse('web:projectview',args=[str(info.Dept.id),str(info.id)]))
    else:
        form = projectform()
    return render(request, 'web/project_form.html',{'form':form})

def recognitioncreate(request, prof_id):
    info = Info.objects.get(id=prof_id)


    if request.method == 'POST':
        form = recognitionform(request.POST)
        if form.is_valid():

            recognitions = recognition.objects.create(recgonition_details=form.cleaned_data['recgonition_details'] , recgonition=info)

            return HttpResponseRedirect(reverse('web:recognitionview',args=[str(info.Dept.id),str(info.id)]))
    else:
        form = publicationform()
    return render(request, 'web/recognition_form.html',{'form':form})

class infoupdate(UpdateView):
    model = Info
    fields = ['Designation','Phone','room','residence']


class teachingupdate(UpdateView):
    model = teaching
    fields = ['year','sem','course']

class publicationupdate(UpdateView):
    model = publication
    fields = ['publication_details']

class projectupdate(UpdateView):
    model = project
    exclude = ['project']

class recognitionupdate(UpdateView):
    model = recognition
    fields = ['recgonition_details']

def about(request):
    return (request, 'web/base.html')


# def aboutview(request, prof_id):
#     all_infos = Info.objects.get(id=prof_id)
#     context = {
#         'Infoo': all_infos,
#     }
#     return render(request, 'web/about.html', context)

class aboutview(generic.DetailView):
    model = Info

class publicationview(generic.DetailView):
    model = Info
    template_name = 'web/publications_list.html'

class recognitionview(generic.DetailView):
    model = Info
    template_name = 'web/recg.html'

class projectview(generic.DetailView):
    model = Info
    template_name = 'web/proj.html'

def deptview(request, dept_id):
    dept = Department.objects.get(id=dept_id)
    context = {
        'dept' : dept,
    }
    return render(request, 'web/dept.html', context)


def homeview(request):
    return render(request, 'web/home.html')

class studentview(generic.DetailView):
    model = Info
    template_name = 'web/students.html'

class teachingview(generic.DetailView):
    model = Info
    template_name = 'web/teachings.html'


class userformview( View ):
    form_class = userform
    template_name = 'web/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})


    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            # returns user objects if credentials correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('web:infocreate')

        return render(request, self.template_name, {'form': form})

def publicationcreate1(request, prof_id):
    info = Info.objects.get(id=prof_id)


    if request.method == 'POST':
        form = publicationform1(request.POST)

        if form.is_valid():

            publications = publication.objects.create(publication_details=form.cleaned_data['publication_details'] , publication=info)

            return HttpResponseRedirect(reverse('web:publicationview',args=[str(info.Dept.id),str(info.id)]))
    else:
        form = publicationform1()
    return render(request, 'web/publication_form.html',{'form':form})

def updatepost(request,prof_id):
    info = Info.objects.get(id=prof_id)
    post=[]
    residence=[]
    phone = []
    email= []
    newresidence=""
    newpost=""
    postupdate(post,residence,phone,email)
    print(residence)
    for word in residence:
        newresidence = newresidence+ str(word) + " "
    for word in post:
        newpost = newpost + str(word) + " "
    print(newresidence)
    if post:
        info.Designation = newpost
    if residence:
        info.residence = newresidence
    if phone:
        info.Phone = phone[0]
    if email:
        info.webmail = email[0]
    info.save()
    return render(request,'web/info_detail.html',{'info':info})














