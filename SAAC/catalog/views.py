from django.shortcuts import render
from .models import Batch, Student
from django.views import generic



''' from . import face
return id of present Students
increase the attendance of the present Students
'''
class StudentListView(generic.ListView):
    model = Student
    context_object_name = 'Students'
    template_name = 'students/my_arbitrary_template_name_list.html'

class StudentDetailView(generic.DetailView):
    model = Student

def index(request):
    batches = Batch.objects.all()
    studlist = Student.objects.all()

    return render(
                    request,
                    'index.html',
                    context = {'Students': studlist, 'batches': batches}
    )
