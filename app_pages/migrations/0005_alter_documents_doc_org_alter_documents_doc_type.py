# Generated by Django 4.2.7 on 2023-12-14 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_pages', '0004_alter_documents_doc_org_alter_documents_doc_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='doc_org',
            field=models.CharField(choices=[('5', 'Boshqarma'), ('1', 'Parlament'), ('3', 'Vazirlar mahkamasi'), ('4', 'Xalq talimi vazirligi'), ('2', 'Prezident')], max_length=25, verbose_name='Tashkilot/Organisation'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_type',
            field=models.CharField(choices=[('4', 'Buyruq'), ('5', 'Farmon'), ('1', 'Qonun'), ('3', 'Farmoyish'), ('2', 'Qaror')], max_length=15, verbose_name='Toifa/Type'),
        ),
    ]
