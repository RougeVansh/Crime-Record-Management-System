# Generated by Django 3.1.3 on 2022-11-16 07:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crimerecord', '0002_auto_20201109_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criminal',
            name='catname',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimerecord.category'),
        ),
        migrations.AlterField(
            model_name='criminal',
            name='contactno',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='criminal',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='criminal',
            name='policeid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimerecord.police'),
        ),
        migrations.AlterField(
            model_name='criminal',
            name='policestationid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimerecord.policestation'),
        ),
        migrations.AlterField(
            model_name='fir',
            name='address',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='fir',
            name='chargesheetdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fir',
            name='contactno',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='fir',
            name='crimetype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimerecord.category'),
        ),
        migrations.AlterField(
            model_name='fir',
            name='dateoffir',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='fir',
            name='firno',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='fir',
            name='investigationdetail',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='fir',
            name='investigationofficer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='fir',
            name='nameaccused',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='fir',
            name='nameapplicants',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='fir',
            name='parentageapplicant',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='fir',
            name='policestationid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimerecord.policestation'),
        ),
        migrations.AlterField(
            model_name='fir',
            name='purposeoffir',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='fir',
            name='relationaccused',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='fir',
            name='remark',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='fir',
            name='remarkdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fir',
            name='sectionoflaw',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='fir',
            name='status',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='fir',
            name='userid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='police',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='police',
            name='policestationid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimerecord.policestation'),
        ),
        migrations.AlterField(
            model_name='police',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
