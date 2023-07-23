from datetime import datetime


data_nascimento = datetime(2011, 4, 13)

data_atual = datetime.now()
idade = data_atual.year - data_nascimento.year - ((data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day))

with open('README.md', 'r') as file:
    readme_content = file.read()

readme_content = readme_content.replace('{IDADE}', str(idade))

with open('README.md', 'w') as file:
    file.write(readme_content)
