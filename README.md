# Transcrição e Resumo de Áudio do YouTube

Este projeto permite que você baixe o áudio de um vídeo do YouTube, faça a transcrição utilizando o modelo Whisper da OpenAI, e gere um resumo utilizando o modelo GPT-3.5-turbo da OpenAI.

## Funcionalidades

- Baixar o áudio de um vídeo do YouTube
- Transcrever o áudio em texto usando Whisper
- Gerar um resumo detalhado da transcrição utilizando o GPT da OpenAI

## Pré-requisitos

Certifique-se de ter os seguintes itens instalados:

1. **Python 3.8+**
2. **pytubefix** (para download de vídeos do YouTube)
3. **whisper** (modelo Whisper da OpenAI para transcrição)
4. **openai** (para interagir com os modelos GPT)
5. **dotenv** (para gerenciar variáveis de ambiente)

## Instruções de Configuração

### 1. Clone o Repositório

```bash
git clone https://github.com/seu-repositorio.git
cd seu-repositorio
```

### 2. Crie um Ambiente Virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate  # No Windows, use: venv\Scripts\activate
```

### 3. Instale as Dependências

```bash
pip install pytubefix whisper openai python-dotenv
```

### 4. Configure as Chaves da API

1. Crie um arquivo .env no diretório raiz do projeto.
2. No arquivo .env, adicione a sua chave de API da OpenAI:

```makefile
API_KEY=sua-chave-de-api-da-openai
```


