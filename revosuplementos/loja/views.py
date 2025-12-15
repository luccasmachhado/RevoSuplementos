from django.shortcuts import render, redirect
from .models import Produto, Reserva, Matricula
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from django.urls import reverse


def home(request):
    produtos = Produto.objects.filter(ativo=True)
    return render(request, 'loja/home.html', {'produtos': produtos})


from django.utils import timezone
from django.contrib import messages
from datetime import timedelta

def reservar_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)

    if request.method == 'GET':
        return render(request, 'loja/reservar.html', {
            'produto': produto
        })

    if request.method == 'POST':
        quantidade = int(request.POST['quantidade'])

        if quantidade > produto.estoque:
            messages.error(request, 'Quantidade indisponível em estoque.')
            return redirect('home')

        # 🔻 Abate provisório
        produto.estoque -= quantidade
        produto.save()

        Reserva.objects.create(
            nome=request.POST['nome'],
            telefone=request.POST['telefone'],
            produto=produto,
            quantidade=quantidade,
            expira_em=timezone.now() + timedelta(minutes=30)
        )

        messages.success(request, 'Reserva criada. Aguardando confirmação.')
        return redirect(reverse('home') + '?reserva=sucesso')

def matricula(request):
    if request.method == 'POST':
        Matricula.objects.create(
            nome=request.POST['nome'],
            email=request.POST['email'],
            telefone=request.POST['telefone'],
            plano=request.POST['plano']
        )
    return redirect('home')