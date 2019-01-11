# Generated by Django 2.1.3 on 2018-12-10 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dtenapp', '0002_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_attend', models.CharField(default='SOME STRING', max_length=100)),
                ('attend_serial_no', models.CharField(default='SOME STRING', max_length=100)),
                ('department', models.CharField(default='SOME STRING', max_length=100)),
                ('division', models.CharField(default='SOME STRING', max_length=100)),
                ('Subject', models.CharField(default='SOME STRING', max_length=100)),
                ('batch', models.CharField(default='SOME STRING', max_length=100)),
                ('date', models.CharField(default='SOME STRING', max_length=100)),
                ('time', models.CharField(default='SOME STRING', max_length=100)),
                ('present_list', models.CharField(default='SOME STRING', max_length=100)),
                ('absent_list', models.CharField(default='SOME STRING', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_batch', models.CharField(default='SOME STRING', max_length=100)),
                ('department', models.CharField(default='SOME STRING', max_length=100)),
                ('division', models.CharField(default='SOME STRING', max_length=100)),
                ('name', models.CharField(default='SOME STRING', max_length=100)),
                ('start_roll_no', models.CharField(default='SOME STRING', max_length=100)),
                ('end_roll_no', models.CharField(default='SOME STRING', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_division', models.CharField(default='SOME STRING', max_length=100)),
                ('department', models.CharField(default='SOME STRING', max_length=100)),
                ('name', models.CharField(default='SOME STRING', max_length=100)),
                ('enrol_key', models.CharField(default='SOME STRING', max_length=100)),
                ('creator', models.CharField(default='SOME STRING', max_length=100)),
                ('total_students', models.CharField(default='SOME STRING', max_length=100)),
                ('division_dict', models.CharField(default='SOME STRING', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_subject', models.CharField(default='SOME STRING', max_length=100)),
                ('department', models.CharField(default='SOME STRING', max_length=100)),
                ('division', models.CharField(default='SOME STRING', max_length=100)),
                ('name', models.CharField(default='SOME STRING', max_length=100)),
                ('type_of_subject', models.CharField(default='SOME STRING', max_length=100)),
                ('batch', models.CharField(default='SOME STRING', max_length=100)),
                ('total_l_or_p', models.CharField(default='SOME STRING', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='department',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='person',
            name='division',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='person',
            name='id_person',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='person',
            name='mailid',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='person',
            name='profession',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='college',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='surname',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='college',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='division',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='profession',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
    ]
