from django.contrib import admin
from .models import Produto, Reserva, Matricula
from django import forms
from django.shortcuts import render
from django.utils import timezone

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'produto', 'quantidade', 'status', 'expira_em')
    list_filter = ('status', 'produto')
    search_fields = ('nome', 'telefone')
    actions = ['deferir_reserva', 'cancelar_reservas']

    def deferir_reserva(self, request, queryset):
        queryset.update(status='deferida')

    def cancelar_reservas(self, request, queryset):
        for reserva in queryset:
            reserva.cancelar()

        self.message_user(
            request,
            "Reserva(s) cancelada(s) e estoque devolvido com sucesso."
        )

    cancelar_reservas.short_description = "Cancelar reservas selecionadas"

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'ativo')
    actions = ['adicionar_estoque', 'remover_estoque']

    def adicionar_estoque(self, request, queryset):
        if 'aplicar' in request.POST:
            form = AdicionarEstoqueForm(request.POST)

            if form.is_valid():
                quantidade = form.cleaned_data['quantidade']

                for produto in queryset:
                    produto.estoque += quantidade
                    produto.save()

                self.message_user(
                    request,
                    f"Estoque atualizado: +{quantidade} unidades."
                )
                return None

        else:
            form = AdicionarEstoqueForm(
                initial={
                    '_selected_action': queryset.values_list('id', flat=True)
                }
            )

        return render(
            request,
            'admin/adicionar_estoque.html',
            {
                'produtos': queryset,
                'form': form,
                'title': 'Adicionar estoque'
            }
        )

    adicionar_estoque.short_description = "Adicionar unidades no estoque"

    def remover_estoque(self, request, queryset):
        if 'aplicar' in request.POST:
            form = RemoverEstoqueForm(request.POST)

            if form.is_valid():
                quantidade = form.cleaned_data['quantidade']

                for produto in queryset:
                    if produto.estoque >= quantidade:
                        produto.estoque -= quantidade
                        produto.save()
                    else:
                        self.message_user(
                            request,
                            f'❌ Estoque insuficiente para {produto.nome}',
                            level='error'
                        )
                        return None

                self.message_user(
                    request,
                    f'Estoque reduzido em {quantidade} unidades.'
                )
                return None

        else:
            form = RemoverEstoqueForm(
                initial={
                    '_selected_action': queryset.values_list('id', flat=True)
                }
            )

        return render(
            request,
            'admin/remover_estoque.html',
            {
                'produtos': queryset,
                'form': form,
                'title': 'Remover estoque'
            }
        )

    remover_estoque.short_description = "Remover unidades do estoque"

class AdicionarEstoqueForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    quantidade = forms.IntegerField(
        min_value=1,
        label="Quantidade a adicionar"
    )
    
class RemoverEstoqueForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    quantidade = forms.IntegerField(
        min_value=1,
        label="Quantidade a remover"
    )
