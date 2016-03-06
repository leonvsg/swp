def app(environ, start_response):
    args = environ['QUERY_STRING']
    args.replace("&", "\n")
    start_response("200 OK", [("Content-Type", "text/plain")])
    return args