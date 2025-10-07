# Como Gerar o PDF da Justificativa

## Opções para Converter Markdown para PDF

### Opção 1: VS Code com extensão

1. Instale a extensão "Markdown PDF" no VS Code
2. Abra o arquivo `JUSTIFICATIVA_TCP.md`
3. Pressione `Ctrl+Shift+P` e digite "Markdown PDF: Export (pdf)"
4. O PDF será gerado na mesma pasta

### Opção 2: Usando Pandoc (Recomendado)

1. Instale o Pandoc: https://pandoc.org/installing.html

2. No terminal, execute:
```bash
pandoc JUSTIFICATIVA_TCP.md -o JUSTIFICATIVA_TCP.pdf --pdf-engine=xelatex
```

### Opção 3: Ferramentas Online

1. Acesse: https://www.markdowntopdf.com/
2. Cole o conteúdo do arquivo `JUSTIFICATIVA_TCP.md`
3. Clique em "Convert" e faça download

### Opção 4: Imprimir como PDF

1. Abra o arquivo `JUSTIFICATIVA_TCP.md` no VS Code
2. Pressione `Ctrl+Shift+V` para visualizar o preview
3. Clique com botão direito e selecione "Abrir no navegador"
4. Use `Ctrl+P` e selecione "Salvar como PDF"

## Arquivo Gerado

O PDF deve conter toda a justificativa técnica do uso do protocolo TCP na aplicação de chat.
