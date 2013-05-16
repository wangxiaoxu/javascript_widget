# -*- coding: utf-8 -*-

import json
import logging

from django.db import models

from bms.apps.role.models import Presenter


logger = logging.getLogger(__name__)

class Label(models.Model):

    name = models.CharField(u'标签', max_length=50)

    class Meta:
        verbose_name = u'标签'
        verbose_name_plural = u'标签'
        db_table = 'tree_program_label'
        ordering = ('name',)

    def __unicode__(self):
        return u'%s' % self.name


class Tree(models.Model):
    
    _tree_cache = {}
    
    TYPE_CHOICES = ((1, u'部门'), (2, u'频道'), (3, u'节目'))
    
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', verbose_name=u'父对象')
    name = models.CharField(u'名称', max_length=100)
    description = models.CharField(u'介绍', max_length=200, blank=True)
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    priority = models.PositiveIntegerField(u'优先级', default=0)
    display = models.BooleanField(u'是否显示', default=True)
    type = models.IntegerField(u'树元素的类型', choices=TYPE_CHOICES)
    
    def get_tree(self):
        child_nodes = [n.get_tree() for n in self.children.all()]
        return {
            'type': self.type,
            'parent': self.parent.id if self.parent else -1,
            'name': self.name,
            'id': self.id,
            "desc": self.description,
            'children': child_nodes
        }

    @classmethod
    def get_full_tree(cls):
        if not cls._tree_cache:
            parents = cls.objects.filter(parent__isnull=True)
            cls._tree_cache = [n.get_tree() for n in parents]
        return json.dumps(cls._tree_cache)
    
    
    @classmethod
    def load_menu(cls, parent_id=None):
        if not parent_id:
            trees = cls.objects.filter(parent__isnull=True)
        else:
            tree = cls.objects.get(id = parent_id)
            trees = tree.children.all()
            
        results = [{
                    "parent": tree.parent.id if tree.parent else -1,
                    'name': tree.name,
                    'id': tree.id,
                    "description": tree.description,
                    'have_children': bool(tree.children.all())
                    } for tree in trees]
        return json.dumps(results)
        
    

    @property
    def icon_type(self):
        logger.info(self.__class__.__name__)
        return self.__class__.__name__
        
    class Meta:
        verbose_name = u'树'
        verbose_name_plural = u'树'
        db_table = 'tree'
        ordering = ('name',)

    def __unicode__(self):
        return u'%s' % self.name
    

class Department(Tree):
    
    @property
    def channels(self):
        return Channel.objects.filter(parent=self)
    
    class Meta:
        verbose_name = u'部门'
        verbose_name_plural = u'部门'
        db_table = 'tree_department'
        ordering = ('name',)

    def __unicode__(self):
        return u'%s' % self.name


class Channel(Tree):
    
    @property
    def programs(self):
        return Program.objects.filter(parent=self)
    
    class Meta:
        verbose_name = u'频道'
        verbose_name_plural = u'频道'
        db_table = 'tree_channel'
        ordering = ('name',)

    def __unicode__(self):
        return u'%s' % self.name


class Program(Tree):

    CATEGORY_CHOICES = ((1, u'默认'), (2, u'访谈'), (3, u'直播'), (4, u'播报'))
    TEMPLATE_CHOICES = ((1, u'默认'),)

    category = models.IntegerField(u'类型', choices=CATEGORY_CHOICES, default=1)
    label = models.ForeignKey(Label, verbose_name=u'标签', blank=True, null=True)
    template = models.IntegerField(u'模板', choices=TEMPLATE_CHOICES, default=1)
    presenter = models.ForeignKey(Presenter, verbose_name=u'主持人', blank=True, null=True)
    icon = models.URLField(u'图标')
    key_picture = models.URLField(u'焦点图', blank=True)
    start_time = models.DateTimeField(u'开始时间')
    period = models.IntegerField(u'周期', blank=True, null=True)
    subscribes = models.PositiveIntegerField(u'订阅数', default=0, editable=False)

    class Meta:
        verbose_name = u'节目'
        verbose_name_plural = u'节目'
        db_table = 'tree_program'
        ordering = ('name',)

    def __unicode__(self):
        return u'%s' % self.name


