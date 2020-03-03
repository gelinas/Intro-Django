# Generated by Django 3.0.3 on 2020-03-03 18:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_app', '0002_auto_20200303_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalNote',
            fields=[
                ('note_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='my_app.Note')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('my_app.note',),
        ),
    ]
