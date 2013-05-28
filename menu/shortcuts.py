import json

from django.http import HttpResponse

from bms.apps.lib.util import json_date_dumps


def render_json_ok(message=None, status=1):
    data = json.dumps({'status': status, 'message': message})
    return HttpResponse(data, content_type='application/json')


def render_json_error(e):
    data = json.dumps({'error': str(e)})
    return HttpResponse(data, content_type='application/json')


def render_json(data):
    if not isinstance(data, basestring):
        try:
            data = json_date_dumps(data)
        except Exception as e:
            return render_json_error(str(e))
    return HttpResponse(data, content_type='application/json')
