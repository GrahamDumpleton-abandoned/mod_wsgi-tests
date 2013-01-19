import os
import string

def application(environ, start_response):
    status = '200 OK'
    
    response_headers = [('Content-type', 'text/plain'),]
    start_response(status, response_headers)
    
    filelike1 = open('/tmp/filetest-a.txt', 'w+')
    filelike1.write(string.ascii_lowercase)
    filelike1.flush()
    filelike1.seek(0, os.SEEK_SET)

    file_wrapper1 = environ['wsgi.file_wrapper'](filelike1)

    filelike2 = open('/tmp/filetest-b.txt', 'w+')
    filelike2.write(string.ascii_uppercase)
    filelike2.flush()
    filelike2.seek(0, os.SEEK_SET)

    file_wrapper2 = environ['wsgi.file_wrapper'](filelike2)

    return file_wrapper1

