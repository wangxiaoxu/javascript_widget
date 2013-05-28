#coding: utf-8

import os
import time
import base64
import random
import urllib2
import logging

from django.views.decorators.csrf import csrf_exempt

from bms.settings import IMAGE_ZOOM_URL, UPLOAD_FILE_ROOT, UPLOAD_FILE_URL
from bms.apps.lib.shortcuts import render_json_ok, render_json_error


logger = logging.getLogger(__name__)

@csrf_exempt
def upload_image(request):
    directory = request.POST.get('directory', 'default')
    files = request.FILES.values()
    if files:
        path = 'bms/image/%s/%s_%s%s' % (
                directory, time.strftime('%Y%m%d%H%M%S'), random.randint(0, 100), os.path.splitext(files[0].name)[1])

        if save_file(UPLOAD_FILE_ROOT + path, files[0]):
            url = get_short_url(UPLOAD_FILE_URL + path)
        else:
            logger.error(u'上传文件失败 file: [%s] path: [%s]', files[0].name, path)
            url = ''
    if url:
        return render_json_ok(url)
    else:
        return render_json_error(u'上传图片失败!')

@csrf_exempt
def upload_audio(request):
    directory = request.POST.get('directory', 'default')
    files = request.FILES.values()
    if files:
        path = 'bms/audio/%s/%s_%s%s' % (
                directory, time.strftime('%Y%m%d%H%M%S'), random.randint(0, 100), os.path.splitext(files[0].name)[1])

        if save_file(UPLOAD_FILE_ROOT + path, files[0]):
            url = UPLOAD_FILE_URL + path
        else:
            logger.error(u'上传文件失败 file: [%s] path: [%s]', files[0].name, path)
            url = ''

    if url:
        return render_json_ok(url)
    else:
        return render_json_error(u'上传音频失败!')

def get_short_url(path):
    url = IMAGE_ZOOM_URL + base64.standard_b64encode(path)
    short_url = None
    try:
        u = urllib2.urlopen(url)
        short_url = u.read()
    except Exception as e:
        logger.error(u'获取图片短地址失败！')
    finally:
        u.close()
    return short_url

def save_file(file_name, upload_file):
    try:
        dir = os.path.dirname(file_name)
        if not os.path.exists(dir):
            os.makedirs(dir)
        with open(file_name, 'wb+') as fp:
            for chunk in upload_file.chunks():
                fp.write(chunk)
    except Exception as e:
        logger.error(u'保存文件失败 Exception: [%s]', e)
#        return True # 本地调试忽略龙存
        return False
    return True
