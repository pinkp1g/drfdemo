# Generated by Django 4.2.11 on 2024-03-24 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='请输入一个正常的人名！', max_length=20, verbose_name='姓名')),
                ('age', models.SmallIntegerField(help_text='请输入一个人的年龄，范围在1-100之间~', verbose_name='年龄')),
                ('sex', models.SmallIntegerField(choices=[(0, '保密'), (1, '男'), (2, '女')], verbose_name='性别')),
                ('classmate', models.CharField(db_column='class', max_length=15, verbose_name='班级')),
                ('description', models.TextField(blank=True, null=True, verbose_name='个性签名')),
            ],
            options={
                'verbose_name': '学生信息',
                'verbose_name_plural': '学生信息',
                'db_table': 'db_student',
            },
        ),
    ]
