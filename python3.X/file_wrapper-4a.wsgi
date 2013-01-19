import os
import string

def application(environ, start_response):
    status = '200 OK' 
    
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    
    filelike = open('/tmp/filetest.txt', 'w+')
    filelike.write(string.ascii_lowercase)
    filelike.flush()
    
    filelike.seek(len(string.ascii_lowercase)/2, os.SEEK_SET)

    return environ['wsgi.file_wrapper'](filelike)
