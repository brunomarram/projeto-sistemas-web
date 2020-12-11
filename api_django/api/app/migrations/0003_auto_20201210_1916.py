# Generated by Django 3.1.4 on 2020-12-10 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201210_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receita',
            name='outras_informacoes',
        ),
        migrations.CreateModel(
            name='InformacoesReceita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('informacao', models.CharField(max_length=250)),
                ('receita', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.receita')),
            ],
        ),
    ]