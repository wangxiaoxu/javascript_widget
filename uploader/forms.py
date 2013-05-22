from django import forms

from bms.apps.element.models import Audio, Video, GIFPicture, Emoticon
from bms.apps.lib.widgets import AudioWidget, VideoWidget, ImageWidget


class AudioForm(forms.ModelForm):
    
    class Meta:
        model = Audio
        widgets = {
            'url': AudioWidget(attrs={'maxlength':'100', 'class':'vTextField'}),
        }
        
    class Media:
        js = ('/static/js/jquery-1.9.1.js', '/static/js/admin/element/audio/form.js',)


class VideoForm(forms.ModelForm):

    class Meta:
        model = Video
        widgets = {
            'url': VideoWidget(attrs={'maxlength':'100', 'class':'vTextField'}),
        }
        
    class Media:
        js = ('/static/js/jquery-1.9.1.js', '/static/js/admin/element/video/form.js',)
        
    
class GIFPictureForm(forms.ModelForm):

    class Meta:
        model = GIFPicture
        widgets = {
            'url': ImageWidget(),
        }
        
    class Media:
        js = ('/static/js/jquery-1.9.1.js', '/static/js/admin/element/gifpicture/form.js',)
        
        
class EmotionForm(forms.ModelForm):

    class Meta:
        model = Emoticon
        widgets = {
            'url': ImageWidget(),
        }
        
    class Media:
        js = ('/static/js/jquery-1.9.1.js', '/static/js/admin/element/emotion/form.js',)
        