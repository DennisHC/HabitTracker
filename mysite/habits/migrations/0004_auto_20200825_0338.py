# Generated by Django 3.1b1 on 2020-08-25 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_auto_20200825_0338'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Habits',
            new_name='Habit',
        ),
        migrations.RenameModel(
            old_name='Tasks',
            new_name='Task',
        ),
    ]