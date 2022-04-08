from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

from .models import GeeksModel
from .forms import GeeksForm


def index(request):
    return render(request, "index.html")


def create_view(request):
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/list")
    context = {'form': form}
    return render(request, "create_view.html", context)


def list_view(request):
    context = {"dataset": GeeksModel.objects.all()}

    return render(request, "list_view.html", context)


def detail_view(request, id):
    context = {"data": GeeksModel.objects.get(id=id)}

    return render(request, "detail_view.html", context)


def update_view(request, id):

    obj = get_object_or_404(GeeksModel, id=id)

    form = GeeksForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/list/")
    context = {"form": form}

    return render(request, "update_view.html", context)


def delete_view(request, id):

    context = {}

    obj = get_object_or_404(GeeksModel, id=id)

    if request.method == "POST":

        obj.delete()

        return HttpResponseRedirect("/")

    return render(request, "delete_view.html", context)
