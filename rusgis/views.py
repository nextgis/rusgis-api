from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound


@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'RusGIS API Backend'}


@view_config(route_name='login', renderer='templates/login.jinja2')
def login(request):
    if 'form.submitted' in request.params:
        return HTTPFound(location=request.route_url('home'))

    return dict(name='Login')
