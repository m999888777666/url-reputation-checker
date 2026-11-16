import url_validator
import socket
def resolve_dns(ham_domain):

    #ham_domain=input("domain gir: ") ---> main.pyde sorulacak..;)
    clean_domain=url_validator.yeah(ham_domain)

    try:
        if clean_domain:
            print("domain name is valid and exist.")
            domain_ip=socket.gethostbyname(clean_domain)
            #print(f"{clean_domain} domainine ait \
            #   ip adresi: {domain_ip}")
            return domain_ip
        else:
            return None

    except socket.gaierror:
        return None