# flake8: noqa

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_code', models.CharField(help_text='The code of the transfer college', max_length=15, unique=True)),
                ('college_name', models.CharField(help_text='The name of the transfer college', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MTUCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mtu_course_name', models.CharField(help_text='The name of the MTU course', max_length=50)),
                ('mtu_subject', models.CharField(help_text='The subject of the MTU course', max_length=50)),
                ('mtu_credits', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_code', models.CharField(help_text='The abbreviation of the transfer college state', max_length=2, unique=True)),
                ('state_name', models.CharField(help_text='The long name of the transfer college state', max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(help_text='The name of the transfer course', max_length=50)),
                ('course_id', models.CharField(help_text='The id of the transfer course', max_length=15)),
                ('course_credit', models.IntegerField()),
                ('course_number', models.IntegerField()),
                ('MTU_course_crn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mtu_course_crn', to='course_viewer.MTUCourse')),
            ],
        ),
    ]
