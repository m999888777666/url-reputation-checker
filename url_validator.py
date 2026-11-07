import urllib.parse
def yeah(url):
    
    control=url.startswith(("http://","https://"))

    if not control:
        url="https://"+url
    is_it_meaningful=False
    parsed_url=urllib.parse.urlparse(url)
    domain_part=parsed_url.netloc
    #is_it_meaningful
    tatsız=["@","!","#","?"]

    if "." in domain_part:
        if not any(m in domain_part for m in tatsız):
                if not domain_part.startswith("-"):
                        if not domain_part.endswith("-"):
                            is_it_meaningful=True
                        else:
                            is_it_meaningful=False
                            return None
                else:
                    is_it_meaningful=False  
                    return None
        else:
            is_it_meaningful=False
            return None
    else:
            is_it_meaningful=False
            return None
    if is_it_meaningful:
        return domain_part
