# Generated by Django 1.11 on 2018-10-13 07:29


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0005_entry_head_sha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='type',
            field=models.IntegerField(choices=[(0, b'Ten Single Votes'), (1, b'Select Many'), (2, b'Instant-Runoff'), (3, b'Poll')], help_text=b'Instant-runoff is the type for challenge theme polls.'),
        ),
    ]
