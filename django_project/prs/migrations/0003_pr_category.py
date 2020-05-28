# Generated by Django 3.0.6 on 2020-05-24 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prs', '0002_auto_20200524_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='pr',
            name='category',
            field=models.CharField(choices=[('constr', 'Construction'), ('consul', 'Consulting'), ('fm', 'Facility Management'), ('ggs', 'General Goods and Sevices'), ('it', 'IT'), ('office', 'Office')], default='Choose Category', max_length=10),
        ),
    ]