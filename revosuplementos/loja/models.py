from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.db import transaction

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    preco = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    estoque = models.PositiveIntegerField(default=0)

    imagem = models.ImageField(
        upload_to='produtos/',
        default='produtos/default.png',
        blank=True
    )

    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Reserva(models.Model):

    STATUS_CHOICES = (
        ('pendente', 'pendente'),
        ('deferida', 'deferida'),
        ('cancelada', 'cancelada'),
    )

    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pendente'
    )

    criada_em = models.DateTimeField(auto_now_add=True)
    expira_em = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.expira_em:
            self.expira_em = timezone.now() + timedelta(minutes=30)  # tempo limite
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome} - {self.produto.nome} ({self.status})"

    def cancelar(self):
        if self.status != 'pendente':
            return

        with transaction.atomic():
            self.produto.estoque += self.quantidade
            self.produto.save()

            self.status = 'cancelada'
            self.save()


class Matricula(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    plano = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)

