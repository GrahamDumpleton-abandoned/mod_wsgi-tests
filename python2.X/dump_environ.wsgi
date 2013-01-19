"""

>>> import _testfuncs
>>> connection = _testfuncs.connection()
>>> connection.putrequest('GET', '/dump_environ.wsgi')
>>> connection.endheaders()
>>> response = connection.getresponse()
>>> response.status
200

"""

import cStringIO
import os

def application(environ, start_response):
    headers = []
    headers.append(('Content-Type', 'text/plain'))
    write = start_response('200 OK', headers)

    input = environ['wsgi.input']
    output = cStringIO.StringIO()

    print >> output, "PID: %s" % os.getpid()
    print >> output, "UID: %s" % os.getuid()
    print >> output, "GID: %s" % os.getgid()
    print >> output

    keys = sorted(environ.keys())
    for key in keys:
        print >> output, '%s: %s' % (key, repr(environ[key]))
    print >> output

    output.write(input.read(int(environ.get('CONTENT_LENGTH', '0'))))

    return [output.getvalue()]
