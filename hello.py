def app(env, start_respone):
    args = env['QUERY_STRING']
    args.replace("&", "\n")
    start_respone("200_OK", [("Content-Type", "text/plain")])
    return iter([args])