"""

>>> import _testfuncs
>>> connection = _testfuncs.connection()
>>> messages = _testfuncs.messages()
>>> connection.putrequest('GET', '/content_length-1b.wsgi')
>>> connection.endheaders()
>>> response = connection.getresponse()
>>> response.status
200
>>> response.getheader('Content-Length')
'24'
>>> response.read(12)
'Hello World!'
>>> messages[-1]
'[error] RuntimeError: ERROR'

"""

def application(environ, start_response):
    status = '200 OK' 
    output = 'Hello World!'

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(2*len(output)))]
    start_response(status, response_headers)

    yield output

    raise RuntimeError("ERROR")

    yield output
