"""

>>> import _testfuncs
>>> connection = _testfuncs.connection()
>>> messages = _testfuncs.messages()
>>> connection.putrequest('GET', '/exceptions-1g.wsgi')
>>> connection.endheaders()
>>> response = connection.getresponse()
>>> response.status
500
>>> messages[-5] # doctest: +ELLIPSIS
"[error] ... Exception occurred processing WSGI script ..."

>>> messages[-1]
'[error] TypeError: byte string value expected, value of type unicode found'

"""

def application(environ, start_response):
    status = '200 OK' 
    output = u'Hello World!'

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    write = start_response(status, response_headers)

    write(output)
