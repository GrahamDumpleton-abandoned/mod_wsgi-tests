"""

>>> import _testfuncs
>>> connection = _testfuncs.connection()
>>> messages = _testfuncs.messages()
>>> connection.putrequest('GET', '/exceptions-1h.wsgi')
>>> connection.endheaders()
>>> response = connection.getresponse()
>>> response.status
500
>>> messages[-2] # doctest: +ELLIPSIS
"[error] ... Exception occurred processing WSGI script ..."

>>> messages[-1]
"[error] TypeError: iter() returned non-iterator of type 'NoneType'"

"""

class Iterable:
    def __init__(self, output):
        self.__output = output
    def __iter__(self):
        return None

def application(environ, start_response):
    status = '200 OK' 
    output = 'Hello World!'

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return Iterable(output)
