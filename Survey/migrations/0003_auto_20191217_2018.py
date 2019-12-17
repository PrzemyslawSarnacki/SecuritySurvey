# Generated by Django 2.2 on 2019-12-17 19:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Survey', '0002_auto_20191217_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='objecttype',
            name='object_data',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='Survey.ObjectData'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='privateobject',
            name='object_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Survey.ObjectType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publicobject',
            name='object_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Survey.ObjectType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicetype',
            name='object_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Survey.ObjectType'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='objectdata',
            name='fence',
            field=models.CharField(choices=[('1', 'Brak')], max_length=255),
        ),
        migrations.AlterField(
            model_name='objectdata',
            name='landform',
            field=models.CharField(choices=[('1', 'Równy teren')], max_length=255),
        ),
        migrations.AlterField(
            model_name='objectdata',
            name='neighboring_buildings',
            field=models.CharField(choices=[('1', 'Bloki usługowe')], max_length=255),
        ),
    ]
