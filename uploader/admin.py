from django.contrib import admin

from bms.apps.element.models import *
from bms.apps.base.admin import CasModelAdmin
from bms.apps.element.forms import AudioForm, VideoForm, GIFPictureForm,\
    EmotionForm


class PictureAdmin(CasModelAdmin):

    list_display = ('url', 'provider', 'create_time', 'source', 'in_use')
    list_per_page = 100

admin.site.register(Picture, PictureAdmin)


class EmoticonAdmin(CasModelAdmin):

    list_display = ('url', 'provider', 'create_time', 'source', 'in_use')
    list_per_page = 100
    form = EmotionForm
    
admin.site.register(Emoticon, EmoticonAdmin)


class GIFPictureAdmin(CasModelAdmin):

    list_display = ('title', 'url', 'provider', 'create_time', 'in_use')
    list_per_page = 100
    form = GIFPictureForm
    
admin.site.register(GIFPicture, GIFPictureAdmin)


class AudioAdmin(CasModelAdmin):

    list_display = ('title', 'url', 'provider', 'create_time', 'length', 'in_use')
    list_per_page = 100
    form = AudioForm
    
admin.site.register(Audio, AudioAdmin)


class VideoAdmin(CasModelAdmin):

    list_display = ('title', 'url', 'provider', 'create_time', 'length', 'in_use')
    list_per_page = 100
    form = VideoForm
    
admin.site.register(Video, VideoAdmin)


