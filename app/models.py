from django.db import models
# bejo que nomes esta sem sentido ou sej primeiro passo ajsurta isso
class Produto(models.Model):
    nomeDoProduto = models.CharField(max_length=100)
    valorUnidade = models.DecimalField(max_digits=6, decimal_places=2)
    disponibilidadeDoProduto = models.IntegerField()
    class Meta:
        abstract = True
    def __str__(self):
        return self.nomeDoProduto
class Verduras(Produto):
    class Meta:
        verbose_name_plural = "Verduras"
    
class Frutas(Produto):
    class Meta:
        verbose_name_plural = "Produtos"

class Entrega(models.Model):
    nomeDoCliente = models.CharField(max_length=255)
    enderecoEntrega = models.TextField()
    dataEntrega = models.DateTimeField()
    pagamento = models.OneToOneField('Pagamento', on_delete=models.CASCADE, related_name='entrega')
    def __str__(self):
        return self.nomeDoCliente

class Pagamento(models.Model):
    metodoPagamento = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self):
        return self.metodoPagamento


class Item(models.Model):
    entregaDoItem = models.ForeignKey(Entrega, on_delete=models.CASCADE, related_name="itens")
    nomeDoItem = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    valorUnidadeItem = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return  f"{self.nomeDoItem}"
