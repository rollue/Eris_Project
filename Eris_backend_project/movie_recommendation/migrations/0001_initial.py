# Generated by Django 2.1.7 on 2019-04-03 10:28

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('created_at', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ActorMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_recommendation.Actor')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessPartnerMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(default='man', max_length=16)),
                ('age', models.IntegerField()),
                ('nickname', models.CharField(max_length=64)),
                ('created_at', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField(default=None)),
                ('created_at', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_recommendation.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('genre', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=256)),
                ('rate', models.FloatField(default=None)),
                ('running_time', models.IntegerField(default=0, help_text='영화 시간, 분을 기준으로')),
                ('created_at', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True)),
                ('director', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessPartner',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_owner',
            field=models.ManyToManyField(through='movie_recommendation.BusinessPartnerMovie', to='movie_recommendation.BusinessPartner'),
        ),
        migrations.AddField(
            model_name='customermovie',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_recommendation.Movie'),
        ),
        migrations.AddField(
            model_name='customer',
            name='associated_bp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_recommendation.BusinessPartner'),
        ),
        migrations.AddField(
            model_name='customer',
            name='movie',
            field=models.ManyToManyField(through='movie_recommendation.CustomerMovie', to='movie_recommendation.Movie'),
        ),
        migrations.AddField(
            model_name='businesspartnermovie',
            name='businessPartner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_recommendation.BusinessPartner'),
        ),
        migrations.AddField(
            model_name='businesspartnermovie',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_recommendation.Movie'),
        ),
        migrations.AddField(
            model_name='actormovie',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_recommendation.Movie'),
        ),
        migrations.AddField(
            model_name='actor',
            name='movie',
            field=models.ManyToManyField(through='movie_recommendation.ActorMovie', to='movie_recommendation.Movie'),
        ),
    ]
