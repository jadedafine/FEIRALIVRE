from rest_framework import viewsets
from rest_framework.response import Response
from app.models import Verduras, Frutas, Entrega, Pagamento, Item
from app.api.serializers import VerdurasSerializer, FrutasSerializer, EntregaSerializer, PagamentoSerializer, ItemSerializer

class CalculoMetrica:
    @staticmethod
    def calcular_metrica(queryset):
        return queryset.count() * 10 + 5

class Mixin_metrica:
    def get_metrica(self, queryset):
        return CalculoMetrica.calcular_metrica(queryset)

class VerdurasViewSet(viewsets.ModelViewSet, Mixin_metrica):
    queryset = Verduras.objects.all()
    serializer_class = VerdurasSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        metrica = self.get_metrica(self.queryset)
        return Response({'message': 'Verdura cadastrada!', 'metrica': metrica})

class FrutasViewSet(viewsets.ModelViewSet):
    queryset = Frutas.objects.all()
    serializer_class = FrutasSerializer

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        for fruta in self.queryset:
            fruta.disponibilidadeDoProduto -= 1
            fruta.save()
        return response

class EntregaViewSet(viewsets.ModelViewSet):
    queryset = Entrega.objects.all()
    serializer_class = EntregaSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        entrega_info = [{'nome_cliente': entrega.nomeDoCliente, 'endereco': entrega.enderecoEntrega} for entrega in self.queryset]
        response.data = entrega_info
        return response

class PagamentoViewSet(viewsets.ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        return Response({'message': 'Pagamento excluído!'})

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        item_data = response.data
        item_data['quantidade'] *= 2
        return Response(item_data)