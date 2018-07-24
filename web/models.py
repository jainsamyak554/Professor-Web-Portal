from django.db import models


# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

from django.core.urlresolvers import reverse_lazy

class Info(models.Model):

    Name = models.CharField(max_length=250, help_text="Enter Name")
    Designation = models.CharField(max_length=300)
    Dept = models.ForeignKey(Department, on_delete=models.CASCADE,blank=True,null=True)
    Phone = models.CharField(max_length=20)
    webmail = models.EmailField(max_length=100,blank=True,null=True)
    room = models.CharField(max_length=100)
    residence = models.CharField(max_length=250)
    photo = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.Name
    def get_absolute_url(self):
        return reverse_lazy('web:aboutview',args = [str(self.Dept.id),str(self.id)])


class continuingphdstudents(models.Model):
    continuingphdstudents = models.ForeignKey(Info, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class completephdstudents(models.Model):
    completephdstudents = models.ForeignKey(Info, on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class continuingmtstudents(models.Model):
    continuingmtstudents = models.ForeignKey(Info, on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class continuingbtstudents(models.Model):
    continuingbtstudents = models.ForeignKey(Info, on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class completemtstudents(models.Model):
    completemtstudents = models.ForeignKey(Info, on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class completebtstudents(models.Model):
    completeBTstudents = models.ForeignKey(Info, on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class publication(models.Model):
    publication = models.ForeignKey(Info, on_delete=models.CASCADE,blank=True,null=True)
    publication_details = models.CharField(max_length=1000,blank=True,null=True)

    def get_absolute_url(self):
        return reverse_lazy('web:publicationview', args=[str(self.publication.Dept.id), str(self.publication.id)])

class recognition(models.Model):
    recgonition = models.ForeignKey(Info, on_delete=models.CASCADE,blank=True,null=True)
    recgonition_details = models.CharField(max_length=1000,blank=True,null=True)

    def get_absolute_url(self):
        return reverse_lazy('web:recognitionview' ,args = [ str(self.recgonition.Dept.id),str(self.recgonition.id)])

class project(models.Model):
    project = models.ForeignKey(Info, on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=100)
    pi = models.CharField(max_length=10)
    agency = models.CharField(max_length=10)
    startyear = models.IntegerField()
    endyear = models.IntegerField()

    def get_absolute_url(self):
        return reverse_lazy('web:projectview' ,args = [ str(self.project.Dept.id),str(self.project.id)])

class teaching(models.Model):
    teaching = models.ForeignKey(Info, on_delete=models.CASCADE,blank=True,null=True)
    year = models.CharField(max_length=10)
    odd='odd'
    even='even'
    SEMESTERS= (
        (odd, 'odd'),
        (even, 'even')
    )
    sem= models.CharField(
        max_length=4, choices=SEMESTERS, default=odd,
    )
    course = models.CharField(max_length=500)


    def get_absolute_url(self):
        return reverse_lazy('web:teachingview' ,args = [ str(self.teaching.Dept.id),str(self.teaching.id)])
















































