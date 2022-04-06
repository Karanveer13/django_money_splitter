# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-04-06 11:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('splitter', '0002_auto_20220323_0623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense_Splitter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owes', models.IntegerField()),
                ('e_splitter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Expense_Group_Friend', to='splitter.Group_Friend')),
            ],
        ),
        migrations.AlterField(
            model_name='expense',
            name='splitters',
            field=models.ManyToManyField(related_name='Expense_splitters', through='splitter.Expense_Splitter', to='splitter.Group_Friend'),
        ),
        migrations.AlterField(
            model_name='expense_total',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Expense_total_receiver', to='splitter.Group_Friend'),
        ),
        migrations.AlterField(
            model_name='expense_total',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Expense_total_sender', to='splitter.Group_Friend'),
        ),
        migrations.AddField(
            model_name='expense_splitter',
            name='expense',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Expense_name', to='splitter.Expense'),
        ),
        migrations.AlterUniqueTogether(
            name='expense_splitter',
            unique_together=set([('expense', 'e_splitter')]),
        ),
    ]
