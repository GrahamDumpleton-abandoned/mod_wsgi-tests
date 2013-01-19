"""

>>> import _testfuncs
>>> connection = _testfuncs.connection()
>>> connection.putrequest('GET', '/start_response-1e.wsgi')
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
    status = '200 ' 
    output = 'Hello World!'

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]
