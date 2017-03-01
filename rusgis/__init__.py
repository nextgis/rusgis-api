from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('login', '/login')

    config.add_route('api.version', '/api')
    config.add_route('resource.item', '/api/v1/resources/{id}')
    config.add_route('resource.diff', '/api/v1/resources/{id}/diff')
    config.add_route('feature.item', '/api/v1/resources/{id}/features/{fid}')
    config.add_route('feature.collection', '/api/v1/resources/{id}/features')
    config.add_route('attachment.item', '/api/v1/resources/{id}/features/{fid}/attachments/{aid}')
    config.add_route('attachment.collection', '/api/v1/resources/{id}/features/{fid}/attachments')
    config.add_route('tile', '/api/v1/resources/{id}/tiles/{x}/{y}/{z}')
    config.add_route('basemaps', '/api/v1/basemaps')
    config.add_route('geocoder', '/api/v1/geocoder')
    config.add_route('alerts', '/api/v1/alerts')
    config.add_route('tracks', '/api/v1/tracks')

    config.scan()
    return config.make_wsgi_app()
