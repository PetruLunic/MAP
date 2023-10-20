def parse_url(url, params):
    result = url

    if "brand" in params and len(params["brand"]):
        result += ",".join(params["brand"]).lower() + "/"
        params.pop("brand")

    query = []

    for param in params:
        if isinstance(params[param], str):
            query.append(param + "=" + params[param])
        else:
            query.append(param + "=" + "%2C".join(params[param]))

    if len(query):
        result += "?" + "&".join(query)

    return result
