# Generated by Django 5.0.4 on 2024-04-30 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doct', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('profile_picture', models.ImageField(upload_to='profile_pictures/')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('address_line1', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
