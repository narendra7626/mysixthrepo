# Generated by Django 3.0.3 on 2021-04-18 05:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20210417_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=264)),
                ('title', models.TextField()),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approve_comments', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='myapp.Post')),
            ],
        ),
    ]