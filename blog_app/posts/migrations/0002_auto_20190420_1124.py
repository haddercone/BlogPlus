# Generated by Django 2.2 on 2019-04-20 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auther',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_text', models.TextField()),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Auther')),
            ],
        ),
    ]