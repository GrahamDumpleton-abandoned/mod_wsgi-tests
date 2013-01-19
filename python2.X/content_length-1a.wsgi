"""

>>> import _testfuncs
>>> connection = _testfuncs.connection()
>>> messages = _testfuncs.messages()
>>> connection.putrequest('GET', '/content_length-1a.wsgi')
>>> connection.endheaders()
>>> response = connection.getresponse()
>>> response.status
200
>>> response.getheader('Content-Length')
'12'
>>> response.read()
'Hello World!'
>>> messages[-1] # doctest: +ELLIPSIS
'[debug] ... Content length mismatch, expected 12, response generated 24: ...'

"""

def application(environ, start_response):
    status = '200 OK' 
    output = 'Hello World!'

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output, output]
