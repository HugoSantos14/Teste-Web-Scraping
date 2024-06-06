import os
import requests
from bs4 import BeautifulSoup

os.system("cls")
"""
## Requests

- A biblioteca requests permite o envio de requisições HTTP utilizando Python.
- A requisição retorna uma `Response` (Resposta) com o status e conteudo solicitado.

### Session

Uma _Session_ permite:

    - Utilizar parametros e cookies em múltiplas requisições.
    - Estabelecer e manter uma conexão ativa com o site.

A _Session_ é utilizada da seguinte forma:
"""

session = requests.Session()

"""### Headers

Os _Headers_ permitem fornecer informações sobre o contexto da solicitação.

Por exemplo:

    O 'User-Agent' permite informar o sistema operacional, fornecedor e versão de quem está enviando a requisição.

 A nossa _Session_ tem um valor definido por padrão.
"""

# print(session.headers)

"""#### Atualizando Headers

 **Para atualizar os _Headers_ da nossa _Session_, vamos utilizar o site**: [What is my user agent?](https://www.whatismybrowser.com/detect/what-is-my-user-agent/)
"""

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
}

session.headers.update(headers)

# print(session.headers)

"""### Exemplo: GET com a biblioteca Requests"""

url = 'https://example.com'

response = session.get(url)

# print("Status HTTP:", response.status_code, end= "\n\n")
# print(response.text)

"""### Exemplo: POST com a biblioteca Requests"""

url = 'https://httpbin.org/anything'

data = {
    'Exemplo': 'Post',
    'Workshop': 'Web Scraping'
}

response = session.post(url, json=data)

# print("Status HTTP:", response.status_code, end= "\n\n")

# print(response.json())

"""### Compreendendo os Códigos de Status HTTP

Os códigos de status HTTP são emitidos pelo servidor em resposta a uma solicitação feita ao servidor.

Aqui estão os códigos de status mais comuns e seus significados:

1. **1xx: Informativo**
    - **100 Continue:** O servidor recebeu a solicitação inicial e o cliente deve continuar com a solicitação.
    - **101 Switching Protocols:** O servidor aceita a solicitação do cliente para alterar o protocolo.
    
    <br>

2. **2xx: Sucesso**
    - **200 OK:** A solicitação foi bem-sucedida e o servidor retornou os dados solicitados.
    - **201 Created:** A solicitação foi bem-sucedida e um novo recurso foi criado.
    - **204 No Content:** A solicitação foi bem-sucedida, mas não há conteúdo para enviar na resposta.
    
    <br>

3. **3xx: Redirecionamento**
    - **301 Moved Permanently:** O recurso solicitado foi movido permanentemente para uma nova URL.
    - **302 Found:** O recurso solicitado foi encontrado em uma URL diferente temporariamente.
    - **304 Not Modified:** O recurso não foi modificado desde a última solicitação.
    
    <br>

4. **4xx: Erro do Cliente**
    - **400 Bad Request:** A solicitação não pôde ser entendida pelo servidor devido à sintaxe incorreta.
    - **401 Unauthorized:** A solicitação requer autenticação do usuário.
    - **403 Forbidden:** O servidor entendeu a solicitação, mas se recusa a autorizá-la.
    - **404 Not Found:** O servidor não encontrou o recurso solicitado.
    
    <br>

5. **5xx: Erro do Servidor**
    - **500 Internal Server Error:** O servidor encontrou uma condição inesperada que o impediu de atender à solicitação.
    - **502 Bad Gateway:** O servidor recebeu uma resposta inválida do servidor upstream.
    - **503 Service Unavailable:** O servidor está indisponível no momento (por sobrecarga ou manutenção).

Esses códigos de status ajudam a identificar o estado da solicitação HTTP e fornecem informações úteis para depuração e solução de problemas.

"""

url = 'https://httpbin.org/anything'

data = {
    'Exemplo': 'Post',
    'Workshop': 'Web Scraping'
}

response = session.post(url, json=data)

if(response.status_code != 200):
    print(f"Falha, Status: {response.status_code}")

"""
## BeautifulSoup

- BeautifulSoup é uma biblioteca de Python para analisar documentos HTML e XML.
- A biblioteca cria caminhos que auxiliam a extração dos dados.
"""

url = 'https://example.com'

response = session.get(url)

if(response.status_code == 200):
    soup = BeautifulSoup(response.text, 'html.parser')

"""### Encontrando o titulo da página"""

titulo_da_pagina = soup.title

# print("Titulo da Página:", titulo_da_pagina)
print("Titulo da Página:", titulo_da_pagina.text)

"""### Encontrando o texto da página

#### Find
"""

texto_da_pagina = soup.find('p')

print(texto_da_pagina.text)

"""#### FindAll"""

texto_da_pagina_2 = soup.findAll('p')

# print(texto_da_pagina_2)

# for texto in texto_da_pagina_2:
#    print(texto)
#    print('-----')

"""#### Selecionando uma propriedade"""

texto_com_link = texto_da_pagina_2[1]
tag_a = texto_com_link.find('a')
tag_a_url = tag_a.get('href')

# print("Texto com link: ", texto_com_link)
# print("Tag <a>: ", tag_a)
print(f"URL: {tag_a_url}\n\n")

"""<p style="font-family: 'Meiryo UI'; font-size: 30px; padding: 12px; text-align: center; color: #ffffff; border-radius: 15px;  font-weight: bold; background-color: #007040;">Prática #1</p>

## Prática #1

Você foi contratado pela Zintendo, uma empresa renomada no mundo dos jogos. A sua chefe, Nelda, lhe informa que, para acessar os dados do servidor, você precisa fornecer o IP da sua máquina.

Para descobrir o IP da máquina, escreva um código que faz Web Scraping do site [Meu IP](https://www.meuip.com.br/) e retorna o IP da sua máquina.

**Uma ajudinha:**

1. Envie uma requisição GET para a 'url_meuip'
2. Verifique o status da requisição
3. Utilize o BeautifulSoup para analisar o HTML
4. No exemplo anterior, o texto estava na tag 'p', em que tag se encontra o IP?
"""

print("PRÁTICA #1:\n")
url_meuip = "https://www.meuip.com.br/"

response = session.get(url_meuip)
if(response.status_code == 200):
    # print('Ok!')
    soup = BeautifulSoup(response.text, 'html.parser')
    meu_ip = soup.find('h3')
    print(f"{meu_ip.text}\n\n")

print("PRÁTICA #2:\n")
"""<p style="font-family: 'Meiryo UI'; font-size: 30px; padding: 12px; text-align: center; color: #ffffff; border-radius: 15px;  font-weight: bold; background-color: #007040;">Prática #2</p>

## Prática #2

Localizada no centro histórico da cidade do Porto, a Livraria Lello é um marco artístico e cultural com mais de 100 anos de história.

Existe um rumor que a escritora dos livros de Harry Potter se inspirou na livraria. Apesar de algumas semelhanças, essa informação foi desmentida em 2020. No entanto, a Livraria Lello continua a atrair inúmeros turistas e fãs da saga, que a visitam em busca de sua atmosfera encantadora.

<br>

<img src="https://i0.wp.com/turismo.eurodicas.com.br/wp-content/uploads/2018/07/interior-da-livraria-lello.jpg?w=1200&ssl=1" />

<br>

Vamos imaginar que o rumor ainda é verdadeiro. Ao preparar um café, o proprietário da livraria acidentalmente soltou uma magia, sujando todos os livros de Harry Potter. Que tragédia!

**Sua tarefa hoje é auxiliar o proprietário a comprar novos livros**.

<br>

<img src="https://a-static.mlcdn.com.br/450x450/box-livros-harry-potter-tradicional-j-k-rowling/magazineluiza/236789300/7a83cac4fe23aed6be68865ec175b4a7.jpg" />

<br>

Antes de comprar novos livros, é necessário entender que a Livraria Lello precisa ter **lucro** ao vender estes livros, ou seja, você vai construir um sistema que:

- **Monitorar o preço dos livros**.
- **Compra o livro quando o preço estiver em promoção**.

### Limitações e definição de um alvo

Infelizmente, precisamos informar ao proprietário que, para evitar problemas com a rede da universidade, teremos que escolher apenas um livro desta vez.

Ele é uma boa pessoa, entendeu o problema e ainda sugeriu os seguintes links:

[Harry Potter e a Pedra Filosofal](https://leitura.com.br/harry-potter-e-a-pedra-filosofal-L999-9788532511010) <br>
[Harry Potter e a Câmara Secreta](https://leitura.com.br/harry-potter-e-a-camara-secreta-L999-9788532511669?search=harry%20potter%20camara) <br>
[Harry Potter e o Prisineiro de Azkaban](https://leitura.com.br/harry-potter-e-o-prisioneiro-de-azkaban-L999-9788532512062) <br>
[Harry Potter e o Cálice de Fogo](https://leitura.com.br/harry-potter-e-o-calice-de-fogo-L999-9788532512529) <br>
[Harry Potter e o Enigma do Príncipe](https://leitura.com.br/harry-potter-e-o-enigma-do-principe-L999-9788532519474) <br>
[Harry Potter e as Relíquias da Morte](https://leitura.com.br/harry-potter-e-as-reliquias-da-morte-L037-9788532522610) <br>

Escolha um dos livros e insira o link abaixo!
"""

url_livro_alvo = 'https://leitura.com.br/harry-potter-e-a-pedra-filosofal-L999-9788532511010'

"""### Carregando Informações

Vamos fazer Web Scraping na página do livro para obter as seguintes informações:

- O titulo
- A imagem
- O preço
- O product_id

**Mais uma ajudinha:**

1. Atualize o cabeçalho da _Session_
2. Utilize o método GET da _Session_ para obter o código HTML do livro
3. Utilize os métodos Find/FindAll para encontrar cada uma das informações
4. A 'imagem' é a URL da Imagem, você pode encontrar a URL na propriedade 'src'
"""

session = requests.Session()
session.headers.update(headers)

response = session.get(url_livro_alvo)

if(response.status_code == 200):
    soup = BeautifulSoup(response.text, 'html.parser')

PRECO = soup.findAll('h2')[1].text
TITULO = soup.title.text
IMAGEM = soup.find('img', {'title': TITULO}).get('src')
PRODUCT_ID = soup.findAll('td')[1].text

print(f'Nome do Produto: {TITULO}')
print(f'Preço do Produto: {PRECO}')
print(f'Identificador do Produto: {PRODUCT_ID}')
print(f'URL da Imagem: {IMAGEM}')

"""### Comprando o Produto

**O produto está em promoção e com um valor muito abaixo que o mercado, já está para esgotar, corra!!!**

<img src="https://thumbs.dreamstime.com/b/girl-running-shopping-cart-to-shop-supermarket-store-boutique-black-friday-vector-illustration-cartoon-crazy-241043020.jpg" />

**Vamos fazer um código para automatizar esse processo!**
"""

url = ''

data = {}
headers = {}

session = None