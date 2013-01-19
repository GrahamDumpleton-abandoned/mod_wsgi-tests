"""

>>> import _testfuncs
>>> connection = _testfuncs.connection()
>>> messages = _testfuncs.messages()
>>> connection.putrequest('GET', '/content_length-1c.wsgi')
>>> connection.endheaders()
>>> response = connection.getresponse()
>>> response.status
200
>>> response.getheader('Content-Length')
'24'
>>> response.read(12)
'Hello World!'
>>> messages[-1] # doctest: +ELLIPSIS
'[debug] ... Content length mismatch, expected 24, response generated 12: ...'

"""

def application(environ, start_response):
    status = '200 OK' 
    output = 'Hello World!'

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(2*len(output)))]
    start_response(status, response_headers)

    return [output]
