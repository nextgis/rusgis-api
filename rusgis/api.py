import os
import json

from pyramid.view import view_config
from pyramid.response import FileResponse
from pyramid.httpexceptions import HTTPForbidden


def path(fname):
    return os.path.join(os.path.dirname(__file__), 'static/api', fname)


@view_config(route_name='api.version', request_method='GET')
def version(request):
    return FileResponse(path('version.json'))


@view_config(route_name='resource.forbidden', request_method='GET')
def forbidden(request):
    response = HTTPForbidden()
    response.content_type = 'application/json'
    with open(path('forbidden.json')) as msg:
        response.text = msg.read()
    return response


@view_config(route_name='resource.item', request_method='GET')
def get_resource(request):
    comp = request.matchdict['comp']
    layer = request.matchdict['layer']
    return FileResponse(path('resource#%s:%s.json' % (comp, layer)))


@view_config(route_name='resource.collection', request_method='GET')
def get_resources(request):
    return FileResponse(path('resources.json'))


@view_config(route_name='resource.diff', request_method='GET')
def get_resource_diff(request):
    return FileResponse(path('diff.json'))


@view_config(route_name='feature.item', request_method='GET')
def get_feature(request):
    return FileResponse(path('feature.json'))


@view_config(route_name='feature.item', request_method='PUT',
             renderer='json')
def put_feature(request):
    return {'id': 7}


@view_config(route_name='feature.item', request_method='DELETE',
             renderer='json')
def delete_feature(request):
    return json.dumps(None)


@view_config(route_name='feature.collection', request_method='GET')
def get_features(request):
    return FileResponse(path('features.json'))


@view_config(route_name='feature.collection', request_method='POST',
             renderer='json')
def post_features(request):
    return {'id': 7}


@view_config(route_name='feature.collection', request_method='DELETE',
             renderer='json')
def delete_features(request):
    return json.dumps(None)


@view_config(route_name='attachment.item', request_method='GET')
def get_attachment(request):
    return FileResponse(path('image.png'))


@view_config(route_name='attachment.item', request_method='PUT',
             renderer='json')
def put_attachment(request):
    return {'id': 8}


@view_config(route_name='attachment.item', request_method='DELETE',
             renderer='json')
def delete_attachment(request):
    return json.dumps(None)


@view_config(route_name='attachment.collection', request_method='POST',
             renderer='json')
def post_attachments(request):
    return {'id': 8}


@view_config(route_name='attachment.collection', request_method='DELETE',
             renderer='json')
def delete_attachments(request):
    return json.dumps(None)


@view_config(route_name='tile', request_method='GET')
def get_tile(request):
    return FileResponse(path('tile.png'))


@view_config(route_name='basemaps', request_method='GET')
def get_basemaps(request):
    return FileResponse(path('basemaps.json'))


@view_config(route_name='geocoder', request_method='GET')
def get_geocoder(request):
    return FileResponse(path('geocoder.json'))


@view_config(route_name='alerts', request_method='GET')
def get_alerts(request):
    return FileResponse(path('alerts.json'))


@view_config(route_name='tracks', request_method='POST',
             renderer='json')
def post_tracks(request):
    return json.dumps(None)


@view_config(route_name='userinfo', request_method='GET')
def get_userinfo(request):
    return FileResponse(path('userinfo.json'))


@view_config(route_name='keycloak', request_method='GET')
def get_keycloak(request):
    return FileResponse(path('keycloak.json'))
