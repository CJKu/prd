# Generated by Django 4.2 on 2023-04-17 15:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ('card', '0002_publiccardinfo_privatecardinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='LinkModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='MemoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memo', models.CharField(max_length=250)),
                ('update_timestamp', models.DateTimeField(auto_now_add=True)),
                ('order', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PhoneModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=250)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.RemoveField(
            model_name='privatecardinfo',
            name='group',
        ),
        migrations.RemoveField(
            model_name='privatecardinfo',
            name='memo',
        ),
        migrations.RemoveField(
            model_name='privatecardinfo',
            name='status',
        ),
        migrations.AddField(
            model_name='publiccardinfo',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phonemodel',
            name='card_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card.publiccardinfo'),
        ),
        migrations.AddField(
            model_name='memomodel',
            name='card_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card.privatecardinfo'),
        ),
        migrations.AddField(
            model_name='linkmodel',
            name='card_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card.publiccardinfo'),
        ),
        migrations.AddField(
            model_name='emailmodel',
            name='card_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card.publiccardinfo'),
        ),
    ]
