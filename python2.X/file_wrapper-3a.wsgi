import os
import string

def application(environ, start_response):
    status = '200 OK'

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-length', str(len(string.ascii_lowercase)/2))]
    start_response(status, response_headers)

    filelike = open('/tmp/filetest.txt', 'w+')
    filelike.write(string.ascii_lowercase)
    filelike.close()

    filelike = open('/tmp/filetest.txt', 'r')

    return environ['wsgi.file_wrapper'](filelike)
