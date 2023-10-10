from django.shortcuts import render, redirect 
from .models import Clientes
from .forms import ClientesForm
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'home.html')

def listar(request):
    Clientes = Cliente.objects.all().order_by('-nome')
    return render(request, 'listar.html', {'clientes':clientes})

def detalhar(request, id):
    cliente = Clientes.objects.get(id=id)
    return render(request, 'detalhar.html', {'cliente':clientes})

def cadastrar(request):
    if request.method == "POST":
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Cliente cadastrado com sucesso!")
            return redirect("listar")
    else:
         form = ClientesForm()
         return render(request, 'cadastrar.html', {'form': form})
    
def atualizar(request, id):
    cliente = Cliente.objects.get(id=id)
    form = ClienteForm(instance=cliente)
    if request.method == "POST":
        form = ClienteForm(request.POST, request.FILES, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect("atualizar", id=id)
        else:
            return render(request, 'atualizar.html', {'form': form})
    else:
         return render(request, 'atualizar.html', {'form': form})

def deletar(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('listar')