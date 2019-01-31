from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Lancamentos(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    # data = models.DateTimeField()
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.descricao