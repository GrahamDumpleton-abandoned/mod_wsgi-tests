"""

>>> import _testfuncs
>>> connection = _testfuncs.connection()
>>> connection.putrequest('GET', '/hello_world.wsgi')
>>> connection.endheaders()
>>> response = connection.getresponse()
>>> response.status
200
>>> response.getheader('Content-Length')
'12'
>>> response.read()
'Hello World!'

"""

def application(environ, start_response):
    status = '200 OK' 
    output = 'Hello World!'

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]
