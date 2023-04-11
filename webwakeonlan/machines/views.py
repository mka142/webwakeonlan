from django.shortcuts import render, redirect, get_object_or_404
from .forms import MachineForm
from .models import Machine

# Create your views here.


def list_machines(request):
    machines = Machine.objects.all()
    return render(request, "machines/list_machines.html", {"machines": machines})


def new_machine(request):
    if request.method == "POST":
        form = MachineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_machines")
    else:
        return render(request, "machines/new_machine.html", {"form": MachineForm()})


def edit_machine(request, pk):
    machine = get_object_or_404(Machine, pk=pk)
    if request.method == "POST":
        form = MachineForm(request.POST, instance=machine)
        if form.is_valid():
            form.save()
            return redirect("list_machines")
    else:
        return render(
            request,
            "machines/edit_machine.html",
            {"form": MachineForm(instance=machine), "machine": machine},
        )


def delete_machine(request, pk):
    machine = get_object_or_404(Machine, pk=pk)
    if request.method == "POST":
        machine.delete()
        return redirect("list_machines")
    else:
        return render(request, "machines/delete_machine.html", {"machine": machine})


def awake_machine(request, pk):
    machine = get_object_or_404(Machine, pk=pk)

    machine.awake()
    return redirect("list_machines")
