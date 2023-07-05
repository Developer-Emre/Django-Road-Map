# Generated by Django 4.1.5 on 2023-07-02 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ogrenci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=50, verbose_name='Adınız')),
                ('soyisim', models.CharField(max_length=50, verbose_name='Soyadınız')),
                ('no', models.IntegerField(verbose_name='Numaranız')),
                ('aciklama', models.TextField(max_length=500, verbose_name='Açıklama')),
            ],
        ),
    ]