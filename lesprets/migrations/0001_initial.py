# Generated by Django 3.1 on 2023-01-02 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demande_De_Pret',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('telephone', models.CharField(max_length=100)),
                ('whatsapp', models.CharField(max_length=100)),
                ('pays', models.CharField(max_length=100)),
                ('ville', models.CharField(max_length=1000)),
                ('montant_du_credit', models.CharField(max_length=10000)),
                ('duree_de_remboursement', models.CharField(max_length=10000)),
                ('date_send', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
