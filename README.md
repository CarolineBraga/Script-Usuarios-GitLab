# Script Usuários GitLab

## Conteúdo
- [Script Usuários GitLab](#script-usuarios-gitlab)
  - [Conteúdo](#conteúdo)
  - [Informações gerais](#informações-gerais)
  - [Tecnologias utilizadas](#tecnologias-utilizadas)
  - [Uso](#uso)

## Descrição
O projeto consiste numa automação que extrai do GitLab SaaS o relatório dos usuários de um determinado grupo e o exporta para uma planilha do Google Sheets. O objetivo é melhorar gerenciamento de usuários do GitLab, tanto para gestão de custos, como para organização.

## Tecnologias utilizadas
### Linguagem
- Python 3
### Bibliotecas
- oauth2client.service_account
- gspread
- gitlab
- time
- sys

## Uso
Executar a pipeline do repositório.