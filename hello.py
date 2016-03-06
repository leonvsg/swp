def app(env, start_responce):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    body = '\r\n'.join(env['QUERY_STRING'].split('&'))
    start_responce(status, headers)
    return body