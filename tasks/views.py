from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskModelForm
# Create your views here.

def addTaskView(request):
    queryset = Task.objects.all()
    form = TaskModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TaskModelForm()
    context = {
        "task_list": queryset,
        "form": form
    }
    return render(request, "tasks/task_add.html", context);

def updateTaskView(request, id):
    obj = get_object_or_404(Task, id=id)
    form = TaskModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("../")
    context = {
        "object": obj,
        "form": form
    }
    return render(request, "tasks/task_update.html", context)

def deleteTaskView(request, id):
    obj = get_object_or_404(Task, id=id)
    if request.method=="POST":
        obj.delete()
        return redirect("../")
    context = {
        "object": obj,
    }
    return render(request, "tasks/task_delete.html", context)
