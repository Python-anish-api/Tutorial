# Generated by Django 5.0.3 on 2024-03-25 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('code', models.TextField()),
                ('linenos', models.BooleanField(default=False)),
                ('language', models.CharField(choices=[('python', 'Python'), ('javascript', 'JavaScript'), ('java', 'Java'), ('ruby', 'Ruby')], default='python', max_length=100)),
                ('style', models.CharField(choices=[('friendly', 'Friendly'), ('bw', 'Black and White'), ('colorful', 'Colorful')], default='friendly', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
