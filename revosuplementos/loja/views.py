from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Reserva, Matricula
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from django.urls import reverse
from django.db import transaction


def home(request):
    produtos = Produto.objects.all()  # 🔥 remove o campo inexistente
    return render(request, 'loja/home.html', {'produtos': produtos})


def reservar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == 'GET':
        return render(request, 'loja/reservar.html', {'produto': produto})

    if request.method == 'POST':
        try:
            quantidade = int(request.POST.get('quantidade', 1))
        except ValueError:
            messages.error(request, 'Quantidade inválida.')
            return redirect('home')

        if quantidade < 1:
            messages.error(request, 'Quantidade inválida.')
            return redirect('home')

        if quantidade > produto.estoque:
            messages.error(request, 'Quantidade indisponível em estoque.')
            return redirect('home')

        with transaction.atomic():
            produto.estoque -= quantidade
            produto.save()

            Reserva.objects.create(
                nome=request.POST.get('nome'),
                telefone=request.POST.get('telefone'),
                produto=produto,
                quantidade=quantidade,
                expira_em=timezone.now() + timedelta(minutes=30)
            )

        messages.success(request, 'Reserva criada com sucesso.')
        return redirect(reverse('home') + '?reserva=sucesso')


def matricula(request):
    if request.method == 'POST':
        Matricula.objects.create(
            nome=request.POST.get('nome'),
            email=request.POST.get('email'),
            telefone=request.POST.get('telefone'),
            plano=request.POST.get('plano')
        )
    return redirect('home')
