import urllib.parse

url=input("url ismi gir:")
control=url.startswith(("http://","https://"))

if not control:
    url="https://"+url

parsed_url=urllib.parse.urlparse(url)
domain_part=parsed_url.netloc
#is_it_meaningful
tatsız=["@","!","#","?"]

if "." in domain_part:
    if any(m in domain_part for m in tatsız):
            if not domain_part.startswith("-"):
                    if not domain_part.endswith("-"):
                        is_it_meaningful=True
                    else:
                          is_it_meaningful=False
            else:
                is_it_meaningful=False  
    else:
        is_it_meaningful=False
      
else:
        is_it_meaningful=False
        

if is_it_meaningful:
      print("domain anlamlı.")




