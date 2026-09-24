from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    marca = serializers.CharField(required=True, max_length=50)
    marca = filters.CharFilter(field_name="marca", lookup_expr="iexact")


    def __str__(self):
        return f"{self.nome} - R$ {self.preco}"
