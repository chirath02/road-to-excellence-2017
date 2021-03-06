# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.urls import reverse


class Album(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='album_img/')
    genre = models.CharField(max_length=250)

    def get_absolute_url(self):
        print 'pk : ' + str(self.pk)
        print reverse('album_detail', args=(self.pk, ))
        return reverse('album_detail', args=(self.pk, ))

    def __str__(self):
        return self.name


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    artist = models.CharField(max_length=150)

    def __str__(self):
        return self.name
