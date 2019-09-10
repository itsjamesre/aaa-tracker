# Generated by Django 2.2.5 on 2019-09-10 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='component',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='test_tracker.Component'),
        ),
        migrations.AddField(
            model_name='test',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='test_tracker.Status'),
        ),
        migrations.AddField(
            model_name='test',
            name='test_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='test_tracker.TestType'),
        ),
        migrations.AddField(
            model_name='test',
            name='variable',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='test_tracker.Variable'),
        ),
        migrations.AddField(
            model_name='test',
            name='winner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='test_tracker.Winner'),
        ),
    ]
