# Generated by Django 4.2 on 2023-05-10 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebLib', '0005_alter_book_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]
