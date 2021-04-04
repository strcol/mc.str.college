import json
import time

import flask


class Application:
    def __init__(self, **kwargs):
        self.classes = {}

        for key, value in kwargs.items():
            self.classes[key] = value
            setattr(self, key, value)

        self.db = self.database.connect()[
            self.config.get('DATABASE_NAME')
        ]

    def _check_field(self, fields, name, max_length):
        return name in fields and len(fields[name]) <= max_length

    def handler(self, request):
        try:
            if request.path == 'submit':
                data = json.loads(list(request.data.keys())[0])
                if self._check_field(data, 'school', 32) and \
                        self._check_field(data, 'fullname', 64) and \
                        self._check_field(data, 'phone', 16) and \
                        self._check_field(data, 'email', 64) and \
                        self._check_field(data, 'group', 16) and \
                        self._check_field(data, 'nickname', 16):
                    self.db.users.insert_one({
                        'timestamp': str(int(time.time() * 1000)),
                        'ip': request.ip,
                        'school': str(data['school']),
                        'fullname': str(data['fullname']),
                        'phone': str(data['phone']),
                        'email': str(data['email']),
                        'group': str(data['group']),
                        'nickname': str(data['nickname'])
                    })
                    return json.dumps({'status': 1})
                return json.dumps({'status': 0})
        except Exception:
            return json.dumps({'status': 0})
        return flask.redirect(self.config.get('WEBSITE_URL'), code=301)

    def error(self, request, cause=None):
        if cause == 'NO_DATABASE_CONNECTION':
            return 'NO_DATABASE_CONNECTION'
