from rest_framework import serializers
from app.models import Verduras, Frutas, Entrega, Pagamento, Item

class VerdurasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verduras
        fields = ['nomeDoProduto', 'valorUnidade', 'disponibilidadeDoProduto']

class FrutasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frutas
        fields = ['nomeDoProduto', 'valorUnidade', 'disponibilidadeDoProduto']

class EntregaSerializer(serializers.ModelSerializer):
    pagamento = serializers.PrimaryKeyRelatedField(queryset=Pagamento.objects.all())
    class Meta:
        model = Entrega
        fields = ['nomeDoCliente', 'enderecoEntrega', 'dataEntrega',  'pagamento']

class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = ['metodoPagamento', 'valor']

class ItemSerializer(serializers.ModelSerializer):
    entregaDoItem = serializers.PrimaryKeyRelatedField(queryset=Entrega.objects.all())
    class Meta:
        model = Item
        fields = ['nomeDoItem', 'quantidade', 'valorUnidadeItem', 'entregaDoItem']