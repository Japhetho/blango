# Generated by Django 3.2.12 on 2022-03-31 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20220217_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
    ]
