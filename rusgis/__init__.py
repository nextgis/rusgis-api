from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('login', '/login') #0
    config.add_route('api.version', '/api') #1
    config.add_route('resource.collection', '/api/v1/resources') #2, #24
    config.add_route('resource.item', '/api/v1/resources/{comp}/{layer}') #3, #4
    config.add_route('resource.forbidden', '/api/v1/resources/test/vector2/features') #23
    config.add_route('feature.collection', '/api/v1/resources/{comp}/{layer}/features') #5, #8, #12
    config.add_route('feature.item', '/api/v1/resources/{comp}/{layer}/features/{fid}') #6, #9, #13
    config.add_route('attachment.item', '/api/v1/resources/{comp}/{layer}/features/{fid}/attachments/{aid}') #7, #11, #15
    config.add_route('attachment.collection', '/api/v1/resources/{comp}/{layer}/features/{fid}/attachments') #10, #14
    config.add_route('tile', '/api/v1/resources/{comp}/{layer}/tiles/{x}/{y}/{z}') #16, #25
    config.add_route('basemaps', '/api/v1/basemaps') #17
    config.add_route('geocoder', '/api/v1/geocoder') #18
    config.add_route('alerts', '/api/v1/alerts') #19
    config.add_route('resource.diff', '/api/v1/resources/{comp}/{layer}/diff') #20
    config.add_route('tracks', '/api/v1/tracks') #21
    config.add_route('userinfo', '/api/v1/userinfo') #22
    config.add_route('keycloak', '/api/v1/keycloak') #26

    config.scan()
    return config.make_wsgi_app()
