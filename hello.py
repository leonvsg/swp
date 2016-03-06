bind = "0.0.0.0:8080"
pythonpath = "/home/box/web"

def app(environ, start_response):
    args = environ['QUERY_STRING']
    args.replace("&", "\n")
    start_response("200 OK", [("Content-Type", "text/plain")])
    return [args]