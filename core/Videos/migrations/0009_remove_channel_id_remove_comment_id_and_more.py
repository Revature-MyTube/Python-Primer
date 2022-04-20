# Generated by Django 4.0.3 on 2022-04-15 19:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Videos', '0008_remove_video_file_remove_video_thumbnail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, serialize=False),
        ),
        migrations.AddField(
            model_name='playlist',
            name='duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='playlist',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='channel',
            name='playlists',
            field=models.ManyToManyField(blank=True, related_name='channel_playlists', to='Videos.playlist'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, serialize=False),
        ),
        migrations.AlterField(
            model_name='channel',
            name='videos',
            field=models.ManyToManyField(blank=True, related_name='channel_videos', to='Videos.video'),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='channel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='Videos.channel'),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, serialize=False ),
        ),
        migrations.AlterField(
            model_name='video',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, serialize=False),
        ),
    ]
