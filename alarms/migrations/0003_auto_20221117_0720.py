# Generated by Django 3.2.13 on 2022-11-17 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alarms', '0002_alter_alarm_subscription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alarm',
            name='is_active',
        ),
        migrations.AlterField(
            model_name='alarm',
            name='d_day',
            field=models.PositiveSmallIntegerField(choices=[(-1, '미설정'), (1, '1일전'), (2, '2일전'), (3, '3일전'), (4, '4일전'), (5, '5일전'), (6, '6일전'), (7, '7일전')], help_text='선택 시, 해당 일자에 메일이 발송됩니다.', null=True, verbose_name='카테고리 종류'),
        ),
    ]