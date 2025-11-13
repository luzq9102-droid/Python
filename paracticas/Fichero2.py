from urllib import request
from urllib.error import URLError

def verContenido(url):
    try:
        f = request.urlopen(url)
    except URLError:
        return f"Error de acceso a {url}"
    else:
        contenido = f.read()
        return contenido
    
def contarPalabras(url):
    contenido = verContenido(url)
    return len(contenido.split())

if __name__=="__main__":
    url ="https://www.abc.com.py/"
    cantPalabras = contarPalabras(url)

print(verContenido(url))
print(f"El recurso tiene {cantPalabras} palabras")