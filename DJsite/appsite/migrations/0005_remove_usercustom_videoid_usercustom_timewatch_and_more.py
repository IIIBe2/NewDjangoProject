# Generated by Django 4.2.5 on 2023-09-25 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appsite', '0004_alter_usercustom_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercustom',
            name='VideoID',
        ),
        migrations.AddField(
            model_name='usercustom',
            name='TimeWatch',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usercustom',
            name='lessonID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appsite.lesson'),
        ),
        migrations.DeleteModel(
            name='VideoWatchPASS',
        ),
    ]
