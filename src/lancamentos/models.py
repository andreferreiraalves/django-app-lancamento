from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(verbose_name=('Descrição'), max_length=100)

    def __str__(self):
        return self.descricao

class Lancamento(models.Model):
    descricao = models.CharField(verbose_name=('Descrição'), max_length=100)
    valor = models.DecimalField(verbose_name=('Valor'), max_digits=9, decimal_places=2)
    data = models.DateField(null=True, verbose_name=('Data de Lançamento'))
    categoria = models.ForeignKey(Categoria, verbose_name=('Categoria'), on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.descricao