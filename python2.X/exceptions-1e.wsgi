"""

>>> import _testfuncs
>>> connection = _testfuncs.connection()
>>> messages = _testfuncs.messages()
>>> connection.putrequest('GET', '/exceptions-1e.wsgi')
>>> connection.endheaders()
>>> response = connection.getresponse()
>>> response.status
200
>>> response.getheader('Content-Length')
'12'
>>> response.read()
'Hello World!'
>>> messages[-5] # doctest: +ELLIPSIS
"[error] ... Exception occurred processing WSGI script ..."

>>> messages[-1]
'[error] RuntimeError: ERROR'

"""

class Iterable:
    def __init__(self, output):
        self.__output = output
    def __iter__(self):
        yield self.__output
    def close(self):
        raise RuntimeError('ERROR')

def application(environ, start_response):
    status = '200 OK' 
    output = 'Hello World!'

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return Iterable(output)
