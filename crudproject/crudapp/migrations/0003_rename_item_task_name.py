# Generated by Django 4.2.2 on 2023-06-09 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0002_alter_task_desc_alter_task_slno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='item',
            new_name='name',
        ),
    ]
