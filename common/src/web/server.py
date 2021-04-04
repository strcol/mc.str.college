import sys

try:
    import flask
except ImportError:
    pass

loaded = 'flask' in sys.modules


class Request:
    def __init__(self, request, path):
        self.ip = request.remote_addr
        self.method = request.method
        if self.method == 'GET':
            self.data = request.args.to_dict()
        else:
            self.data = request.form.to_dict()
        self.cookies = request.cookies.to_dict()
        self.headers = request.headers
        self.url = request.url
        self.path = path
        self.files = request.files
        self._data = request.data
        self.json = request.get_json()
        self.url_cs = self._split_url(self.path)
        self.url_ncs = self._split_url(self.path, False)

    def _split_url(self, path, case_sensitive=True):
        if not path:
            return []
        if path.startswith('/'):
            path = path[1:]
        path = path.lower() if not case_sensitive else path
        if '/' in path:
            return path.split('/')
        else:
            return [path]

    def __str__(self):
        return (f'IP: {self.ip}, Method: {self.method}, Data: {self.data}, ',
                f'Cookies: {self.cookies}, URL: {self.url}')


class WebServer:
    def __init__(self, name, directory='static', debug=False):
        self.name = name
        self.app = flask.Flask(
            self.name, root_path='.', template_folder=directory
        )
        self.app.config['TEMPLATES_AUTO_RELOAD'] = debug
        self.events = []

        @self.app.after_request
        def after_request(response):
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers.add(
                'Access-Control-Allow-Headers', 'Content-Type,Authorization'
            )
            response.headers.add(
                'Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE'
            )
            return response

        @self.app.route('/', methods=['GET', 'POST'])
        @self.app.route('/<path:path>', methods=['GET', 'POST'])
        def event_handler(path=''):
            self.events = sorted(self.events, key=lambda e: e['priority'])
            for event in self.events:
                if flask.request.method not in event['methods']:
                    continue
                if path.lower() not in event['paths'] and \
                        '*' not in event['paths']:
                    continue
                result = event['event'](Request(flask.request, path))
                if result:
                    return result
            return '<h1>404 Not Found</h1>'

    def register_event(self, path, event, method=['GET', 'POST'], priority=1):
        paths = [path] if not isinstance(path, list) else path
        methods = [method] if not isinstance(method, list) else method
        paths = [
            p.lower() if not p.startswith('/') else p.lower()[1:]
            for p in paths
        ]
        self.events.append({
            'priority': priority, 'event': event, 'paths': paths,
            'methods': methods
        })
        return True
