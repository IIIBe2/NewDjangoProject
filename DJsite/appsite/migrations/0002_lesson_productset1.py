# Generated by Django 4.2.5 on 2023-09-25 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='productSet1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appsite.product'),
        ),
    ]
