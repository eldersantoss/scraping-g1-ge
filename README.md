# Scraping G1 e GE
Webscraping das notícias das páginas g1.globo.com e ge.globo.com utilizando os pacotes requests, re (regex) e flask para servir resultados através de API.
## Como executar:

Acesse a pasta raiz da aplicação e execute os seguintes passos:

**1. Instale as dependências:**

```bash
pip install -r requirements.py
```

**2. Crie a variável de ambiente `FLASK_APP` de acordo com seu interpretador de comandos:**

_Bash_

```bash
export FLASK_APP=app
```

_PowerShell_

```powershell
$env:FLASK_APP = "app"
```

**3. Execute a aplicação:**

```bash
flask run
```

## Observações

- Ao fazer a requisição GET nos endereços g1.globo.com e ge.globo.com, o conteúdo do html retornado, por algum motivo que não tive tempo hábil pra descobrir, não contém todas as notícias que estão presentes na página.

- As notícias cujo campo "resume" contém uma string vazia não possuem resumo no site.
