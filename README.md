# Portfólio profissional – Rodrigo Machado Schuler

Site estático (HTML, CSS e JavaScript puros, sem framework) com landing page e currículo completo, em **português e
inglês**, com **tema claro/escuro** e **PDF** para download. Publicado automaticamente no **GitHub Pages**.

## Estrutura

```
.
├── .github/workflows/static.yml   # deploy automático (GitHub Actions → Pages)
├── index.html                     # landing page
├── curriculo.html                 # currículo completo (imprimível / PDF)
├── styles.css                     # estilos compartilhados + tema claro/escuro
├── curriculo.css                  # estilos do currículo + impressão A4
├── app.js                         # alternância de tema e idioma (salva no localStorage)
├── favicon.svg
├── robots.txt
├── curriculo-rodrigo-schuler-pt.pdf
├── curriculo-rodrigo-schuler-en.pdf
└── tools/
    ├── gerar_site.py              # gera index.html e curriculo.html a partir dos dados
    └── gerar_pdfs.py              # gera os PDFs (Playwright + Chromium)
```

## Como publicar (primeira vez)

1. Crie um repositório no GitHub (por exemplo `curriculum`, ou `<seu-usuario>.github.io` para a URL na raiz).
2. Envie estes arquivos para a branch `main`:
   ```bash
   git init -b main
   git add .
   git commit -m "feat: site do currículo"
   git remote add origin https://github.com/<seu-usuario>/<repositorio>.git
   git push -u origin main
   ```
3. No GitHub: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
4. Aguarde o workflow **Deploy site no GitHub Pages** (aba **Actions**) ficar verde. A URL aparece no resumo da
   execução e em **Settings → Pages**: `https://<seu-usuario>.github.io/<repositorio>/`.

A partir daí, **todo `push` na `main` republica o site** em cerca de 1 minuto.

## Como atualizar o conteúdo

O conteúdo (textos em PT e EN) fica no topo de `tools/gerar_site.py`. Cada texto é um par `(português, inglês)`.

```bash
# 1. edite os dados em tools/gerar_site.py
python tools/gerar_site.py          # regenera index.html e curriculo.html

# 2. (opcional) regenere os PDFs
pip install playwright && playwright install chromium
python tools/gerar_pdfs.py

# 3. publique
git add . && git commit -m "docs: atualiza currículo" && git push
```

Para ver localmente: `python -m http.server 8000` e abra <http://localhost:8000>.
Dica: `?lang=en` e `?theme=dark` na URL forçam idioma e tema (ex.: `curriculo.html?lang=en`).

## Privacidade

O site é público e indexável e exibe celular/WhatsApp, e-mail e LinkedIn (não exibe endereço nem idade).
Para alterar ou remover contatos, edite `TELEFONE`, `EMAIL`, `LINKEDIN` e a função `contato_linha()` (e a seção
`#contato` em `build_index()`) em `tools/gerar_site.py`.
Para evitar que buscadores indexem o site, troque o conteúdo de `robots.txt` por:

```
User-agent: *
Disallow: /
```

e adicione `<meta name="robots" content="noindex">` no `<head>` (em `head()` de `tools/gerar_site.py`).

## Domínio próprio (opcional)

1. Crie um arquivo `CNAME` na raiz com o domínio (ex.: `www.seudominio.com.br`).
2. No provedor de DNS, crie um registro `CNAME` apontando `www` para `<seu-usuario>.github.io`
   (para o domínio raiz, use os registros `A`/`AAAA` indicados na documentação do GitHub Pages).
3. Em **Settings → Pages**, informe o domínio e marque **Enforce HTTPS**.

## Formatação do código

`.editorconfig` e `.prettierrc` padronizam o estilo (2 espaços, UTF-8, `LF`, aspas simples, 120 colunas).
Para formatar: `npx prettier --write "*.{css,js,md}" ".github/**/*.yml"`.
