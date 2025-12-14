from django.core.management.base import BaseCommand
from django.utils import timezone
from loja.models import Reserva

class Command(BaseCommand):
    help = 'Remove reservas expiradas e devolve estoque'

    def handle(self, *args, **kwargs):
        agora = timezone.now()
        reservas = Reserva.objects.filter(
            status='pendente',
            expira_em__lt=agora
        )

        for reserva in reservas:
            produto = reserva.produto
            produto.estoque += reserva.quantidade
            produto.save()
            reserva.delete()

        self.stdout.write('Reservas expiradas processadas.')
