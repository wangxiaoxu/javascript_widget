# coding: utf-8

from django.db import models

from bms.apps.base.models import BaseModel
from bms.apps.role.models import Provider

SOURCE_CHOICES = ((1, u'上传'), (2, u'微博'), (3, u'其他'))

class Element(BaseModel):

    url = models.URLField(u'地址')
    description = models.CharField(u'描述', max_length=100, blank=True)
    provider = models.ForeignKey(Provider, verbose_name=u'提供者')
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    monopoly = models.BooleanField(u'独家')
    in_use = models.BooleanField(u'使用中')

    class Meta:
        abstract = True


class Picture(Element):
    
    title = models.CharField(u'标题', max_length=100, blank=True)
    source = models.IntegerField(u'来源', choices=SOURCE_CHOICES, default=1, editable=False)

    class Meta:
        verbose_name = u'图片'
        verbose_name_plural = u'图片'
        db_table = 'element_picture'
        ordering = ('-create_time',)

    def __unicode__(self):
        return u'%s' % self.url


class Emoticon(Element):

    title = models.CharField(u'标题', max_length=100, blank=True)
    source = models.IntegerField(u'来源', choices=SOURCE_CHOICES, default=1, editable=False)

    class Meta:
        verbose_name = u'表情图'
        verbose_name_plural = u'表情图'
        db_table = 'element_emoticon'
        ordering = ('-create_time',)

    def __unicode__(self):
        return u'%s' % self.url


class GIFPicture(Element):

    title = models.CharField(u'标题', max_length=100)
    source = models.IntegerField(u'来源', choices=SOURCE_CHOICES, default=1, editable=False)
    clicks = models.PositiveIntegerField(u'点击次数', default=0, editable=False)

    class Meta:
        verbose_name = u'GIF图'
        verbose_name_plural = u'GIF图'
        db_table = 'element_gifpicture'
        ordering = ('-create_time',)

    def __unicode__(self):
        return u'%s' % self.title


class Audio(Element):

    title = models.CharField(u'标题', max_length=100)
    source = models.IntegerField(u'来源', choices=SOURCE_CHOICES, default=1, editable=False)
    length = models.PositiveIntegerField(u'时长', default=0)
    size = models.PositiveIntegerField(u'大小 (KB)', default=0)
    clicks = models.PositiveIntegerField(u'点击次数', default=0, editable=False)

    class Meta:
        verbose_name = u'音频'
        verbose_name_plural = u'音频'
        db_table = 'element_audio'
        ordering = ('-create_time',)

    def __unicode__(self):
        return u'%s' % self.title

    def check(self):
        return ('<script language="javascript" type="text/javascript">'
                'Player("%s");</script>' % self.url)
    check.allow_tags = True


class Video(Element):
    
    vid = models.IntegerField(u'短视频的vid', blank=True, null=True)
    title = models.CharField(u'标题', max_length=100)
    source = models.IntegerField(u'来源', choices=SOURCE_CHOICES, default=3, editable=False)
    cover_image = models.URLField(u'封面图', blank=True)
    length = models.PositiveIntegerField(u'时长', default=0)
    size = models.PositiveIntegerField(u'大小 (KB)', default=0)
    clicks = models.PositiveIntegerField(u'点击次数', default=0, editable=False)

    class Meta:
        verbose_name = u'视频'
        verbose_name_plural = u'视频'
        db_table = 'element_video'
        ordering = ('-create_time',)

    def __unicode__(self):
        return u'%s' % self.title

