import wikipedia

def scrape(termino, oraciones=1):
    resultado = wikipedia.summary(termino, sentences=oraciones)
    return resultado