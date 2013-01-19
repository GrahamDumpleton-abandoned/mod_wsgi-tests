"""

>>> import _testfuncs
>>> connection = _testfuncs.connection()
>>> messages = _testfuncs.messages()
>>> connection.putrequest('GET', '/exceptions-1a.wsgi')
>>> connection.endheaders()
>>> response = connection.getresponse()
>>> response.status
500
>>> messages[-5] # doctest: +ELLIPSIS
"[error] ... Exception occurred processing WSGI script ..."

>>> messages[-1]
'[error] RuntimeError: ERROR'

"""

def application(environ, start_response):
    raise RuntimeError("ERROR")
