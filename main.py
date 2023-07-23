from datetime import datetime
from git import Repo

# Função para calcular a idade
def calcular_idade(data_nascimento):
    data_atual = datetime.now()
    idade = data_atual.year - data_nascimento.year - ((data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day))
    return idade

# Data de nascimento da sua filha (substitua com a data correta)
data_nascimento = datetime(2011, 4, 13)

# Calcula a idade atual
idade = calcular_idade(data_nascimento)

# Texto do README.md com a idade da sua filha
readme_content = f"""
# Olá, pessoal!

Meu nome é Sofia, tenho {idade} anos e estou empolgada em começar minha jornada na programação! Este é o meu espaço aqui no GitHub, onde vou aprender, criar e compartilhar minhas aventuras no mundo da programação.

## Sobre Mim:
Sou uma jovem curiosa e apaixonada por tecnologia. Adoro resolver problemas e criar coisas novas usando a magia do código. Meu pai, [Aristides](https://github.com/AriHenrique), é um incrível engenheiro de dados, e com o apoio e incentivo dele, estou embarcando nessa emocionante jornada de aprendizado.

## O que Aprenderei Aqui:
Neste GitHub, pretendo compartilhar projetos divertidos e desafiadores, desde pequenos jogos até aplicativos interativos. Vou explorar diferentes linguagens de programação, como Python, JavaScript e muito mais. Além disso, pretendo estudar algoritmos e estruturas de dados para me tornar uma programadora cada vez melhor.

## Sobre o GitHub:
O GitHub é uma plataforma incrível que permite compartilhar meus códigos e trabalhar em projetos com outras pessoas. Além disso, ele me ajudará a acompanhar minhas evoluções e a receber feedback valioso de outros desenvolvedores.

## Agradeço o seu Apoio:
Quero agradecer a todos que estão me apoiando nessa jornada. É incrível ter vocês ao meu lado enquanto embarco nesta aventura de aprendizado e crescimento na programação.

Vamos juntos nessa jornada emocionante! Obrigada por visitar o meu GitHub!

Sofia Eduarda da Cruz
"""

repo = Repo(".")
index = repo.index

# Atualiza o conteúdo do arquivo README.md no index
with open('README.md', 'w') as file:
    file.write(readme_content)
