import io
import os

def application(environ, start_response):
    headers = []
    headers.append(('Content-Type', 'text/plain'))
    write = start_response('200 OK', headers)

    input = environ['wsgi.input']
    output = io.StringIO()

    print("PID: %s" % os.getpid(), file=output)
    print("UID: %s" % os.getuid(), file=output)
    print("GID: %s" % os.getgid(), file=output)
    print(file=output)

    keys = sorted(environ.keys())
    for key in keys:
        print('%s: %s' % (key, repr(environ[key])), file=output)
    print(file=output)

    output.write(input.read(int(environ.get('CONTENT_LENGTH',
                 '0'))).decode('latin-1'))

    return [output.getvalue().encode('latin-1')]
