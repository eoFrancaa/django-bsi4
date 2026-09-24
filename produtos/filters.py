from django_filters import rest_framework as filters

from .models import Produto


class ProdutoFilter(filters.FilterSet):
    estoque_minimo = filters.NumberFilter(field_name="estoque", lookup_expr="gte")
    estoque_maximo = filters.NumberFilter(field_name="estoque", lookup_expr="lte")

    class Meta:
        model = Produto
        fields = ("preco_minimo", "preco_maximo")
