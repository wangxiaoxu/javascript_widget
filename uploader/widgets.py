# coding: utf-8

from django.forms.util import flatatt
from django.forms.widgets import HiddenInput, Input
from django.utils.safestring import mark_safe
from django.utils.encoding import force_unicode

class ImageWidget(HiddenInput):
    """直播间中上传及展示图片的组件"""
    def render(self, name, value, attrs=None):
        if value is None:
            value = 'http://s7.rr.itc.cn/org/F/6Y/Z3Aj2Az.jpg'
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        if value != 'http://s7.rr.itc.cn/org/F/6Y/Z3Aj2Az.jpg':
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = force_unicode(self._format_value(value))
        return mark_safe(u'''
            <p>
            <input %s />
            <a href="javascript:void(0)" id="id_%s_upload" class="button">上传图片</a>
            <br/>
            <img id="id_%s_show" src="%s" style="width:120px;height:80px;margin:10px 0 0 0;">
            </p>
        ''' % (flatatt(final_attrs), name, name, value))
        
    class Media:
        js = ('/static/js/jquery-1.9.1.js', '/static/js/widgets/uploader.js',)
        
        
class AudioWidget(Input):
    """音频上传组件"""
    input_type = 'text'
    
    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        if value != '':
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = force_unicode(self._format_value(value))
        return mark_safe(u'''
            <input %s />
            <a href="javascript:void(0)" id="id_%s_upload" class="button">上传音频</a>
        ''' % (flatatt(final_attrs), name))
        
    class Media:
        js = ('/static/js/jquery-1.9.1.js', '/static/js/widgets/uploader.js',)
        
        
class VideoWidget(Input):
    """音频上传组件"""
    input_type = 'text'
    
    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        if value != '':
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = force_unicode(self._format_value(value))
        return mark_safe(u'''
            <input %s />
            <a href="javascript:void(0)" id="id_%s_upload" class="button">上传视频</a>
        ''' % (flatatt(final_attrs), name))
        
    class Media:
        js = ('/static/js/jquery-1.9.1.js', '/static/js/widgets/uploader.js',)