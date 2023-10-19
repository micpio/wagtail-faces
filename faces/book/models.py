# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

CATEGORIES = (
    ('thriller', 'thriller'),
    ('text_book', 'text book'),
    ('mystery', 'mystery'),
    ('classics', 'classics'),
    ('novel', 'novel'),
    ('sailing', 'sailing'),

        )


class Mybooksread(models.Model):
    book_title = models.CharField(max_length=(50),null=True)
    authors = models.CharField(max_length=(50),null=True)
    comment = models.CharField( max_length=(200),null=True)
    image = models.ImageField(upload_to='media',null=True, blank=True)
    category = models.CharField(max_length=15, choices=CATEGORIES, default='novel')
    def __str__(self):
       return u"%s %s  %s"%( self.book_title,self.authors,self.category,)



    class Meta:
        ordering = ['-authors',]
        db_table= "mybooksread"
