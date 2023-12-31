# Generated by Django 4.2.6 on 2023-10-30 23:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drive', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thumbnail',
            name='personalFile',
        ),
        migrations.AddField(
            model_name='file',
            name='is_image',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='thumbnail',
            name='personal_file',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='file_path',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='file',
            name='is_video',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='file',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='drive.folder'),
        ),
        migrations.AlterField(
            model_name='file',
            name='personal_file',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='thumbnail_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='drive.thumbnail'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='folder',
            name='personal_folder',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='thumbnail',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='FileSystem',
        ),
    ]
