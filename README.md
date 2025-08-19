# Publicador Hugging Face para Render

Este projeto consome uma API da Hugging Face para gerar conteúdo automaticamente com base em um prompt e publica no WordPress via plugin (ou entrega os dados para um plugin já existente).

## Variáveis de ambiente
- `HF_TOKEN`: sua chave de API do Hugging Face

## Rodando no Render
1. Crie um repositório no GitHub e suba os arquivos deste projeto.
2. Vá até [Render.com](https://render.com/), crie um novo serviço de background baseado neste repositório.
3. Configure a variável de ambiente `HF_TOKEN` no painel do Render.
4. O script `main.py` irá buscar conteúdo e gerar automaticamente.

Pronto!