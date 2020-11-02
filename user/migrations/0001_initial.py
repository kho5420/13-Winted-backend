# Generated by Django 3.1.3 on 2020-11-04 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('recommend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppliedStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
            options={
                'db_table': 'applied_status',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
            options={
                'db_table': 'likes',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=250)),
                ('password', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('profile_image_url', models.CharField(max_length=200)),
                ('apllied_status', models.ManyToManyField(related_name='applied_status', through='user.AppliedStatus', to='company.Company')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='UserTagFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'user_tag_filters',
            },
        ),
        migrations.CreateModel(
            name='UserDistrictFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.district')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'user_district_filters',
            },
        ),
        migrations.CreateModel(
            name='UserCareerFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.career')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'user_career_filters',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='career_filters',
            field=models.ManyToManyField(related_name='user_career_filters', through='user.UserCareerFilter', to='company.Career'),
        ),
        migrations.AddField(
            model_name='user',
            name='district_filters',
            field=models.ManyToManyField(related_name='user_district_filters', through='user.UserDistrictFilter', to='company.District'),
        ),
        migrations.AddField(
            model_name='user',
            name='likes',
            field=models.ManyToManyField(related_name='likes', through='user.Like', to='company.Company'),
        ),
        migrations.AddField(
            model_name='user',
            name='recommender',
            field=models.ManyToManyField(related_name='recommenders', through='recommend.Recommender', to='user.User'),
        ),
        migrations.AddField(
            model_name='user',
            name='tag_filters',
            field=models.ManyToManyField(related_name='user_tag_filters', through='user.UserTagFilter', to='company.Tag'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
        migrations.AddField(
            model_name='appliedstatus',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]