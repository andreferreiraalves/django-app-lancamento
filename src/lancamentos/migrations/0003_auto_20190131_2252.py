# Generated by Django 2.1.5 on 2019-01-31 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lancamentos', '0002_auto_20190131_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='lancamento',
            name='data',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='descricao',
            field=models.CharField(max_length=100, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='lancamento',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lancamentos.Categoria', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='lancamento',
            name='descricao',
            field=models.CharField(max_length=100, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='lancamento',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Valor'),
        ),
    ]
