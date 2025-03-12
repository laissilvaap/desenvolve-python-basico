# Lista de URLs
urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

# Usando fatiamento para criar a lista de domínios
dominios = [url[4:-4] for url in urls]
#url[4:] retira o www.
#url[:-4] retira o .com
print(dominios)  # Saída: ['google', 'gmail', 'github', 'reddit', 'yahoo']
