# Portfólio Profissional — Rodrigo Schuler

Documentação do site estático de portfólio e currículo, preparado para publicação com **GitHub Pages**.

> **Antes de publicar:** revise cargos, empresas, datas, descrições, métricas, links e dados de contato. O repositório e o site podem ser públicos; divulgue somente as informações que deseja tornar acessíveis.

## Objetivos

- Apresentar o perfil profissional de forma clara.
- Destacar competências técnicas, liderança e experiência em Tecnologia da Informação.
- Disponibilizar uma página de currículo detalhado.
- Facilitar o compartilhamento do perfil em candidaturas e no LinkedIn.
- Manter o site simples, sem banco de dados ou backend.

## Estrutura do projeto

```text
curriculum/
├── index.html       # Página inicial do portfólio
├── curriculo.html   # Página do currículo detalhado
├── index.css        # Estilos externos da página inicial
└── README.md        # Documentação
```

### `index.html`

Página inicial: resumo profissional, competências em destaque e links para o currículo e canais profissionais.

### `curriculo.html`

Página com o currículo detalhado, incluindo trajetória, experiências e competências. O arquivo pode manter estilos incorporados, conforme a versão atual.

### `index.css`

Folha de estilos externa para cores, tipografia, espaçamentos, layout e adaptação a diferentes telas.

Para carregar o CSS externo, o `<head>` do `index.html` deve conter:

```html
<link rel="stylesheet" href="index.css">
```

Se o HTML ainda tiver um bloco `<style>...</style>` com as regras antigas, confirme que as regras necessárias foram transferidas para `index.css` antes de remover o bloco. Evite estilos duplicados que possam se sobrepor.

## Tecnologias

- **HTML5:** estrutura e conteúdo.
- **CSS3:** apresentação visual e responsividade.
- **Git/GitHub:** versionamento e hospedagem do código.
- **GitHub Pages:** publicação do site estático.

Não é necessário banco de dados nem processo de compilação para a estrutura básica descrita.

## Visualizar localmente

1. Baixe ou clone o repositório.
2. Mantenha os arquivos na estrutura indicada, a menos que atualize os caminhos no código.
3. Abra `index.html` no navegador.
4. Teste os links para o currículo e para os contatos.

Para desenvolvimento, você também pode abrir a pasta no Visual Studio Code e usar a extensão Live Server para atualizar a prévia enquanto edita.

## Publicar com GitHub Pages

### 1. Enviar os arquivos

Coloque `index.html`, `curriculo.html`, `index.css` e `README.md` na raiz do repositório. Depois, registre e envie as alterações. Se o Git remoto já estiver configurado:

```bash
git add index.html curriculo.html index.css README.md
git commit -m "Atualiza o portfólio e sua documentação"
git push
```

Também é possível enviar arquivos diretamente pela interface do GitHub.

### 2. Configurar a publicação

1. Abra o repositório no GitHub.
2. Entre em **Settings → Pages**.
3. Em **Build and deployment**, selecione **Deploy from a branch**, se essa opção estiver disponível.
4. Escolha a branch que contém os arquivos, normalmente `main`.
5. Selecione a pasta `/ (root)`.
6. Salve a configuração.

O GitHub Pages usa `index.html` como página inicial na origem selecionada. A primeira publicação ou uma atualização pode levar alguns minutos.

### 3. Conferir o site

Consulte o endereço publicado na seção **Settings → Pages**. Abra-o e teste tanto a página inicial quanto a página de currículo. O endereço exato depende das configurações do repositório; use o endereço mostrado pelo GitHub.

## Atualizar o conteúdo

1. Edite `index.html` para modificar a página inicial.
2. Edite `curriculo.html` para alterar o currículo detalhado.
3. Edite `index.css` para modificar cores, fontes, espaçamentos e layout.
4. Salve e teste localmente.
5. Faça commit e envie as alterações para a branch configurada.
6. Aguarde a publicação e confira a versão online.

### Boas práticas para o currículo

- Use títulos objetivos e consistentes.
- Destaque resultados e impactos verificáveis, não apenas tarefas.
- Inclua métricas somente quando forem verdadeiras e puderem ser explicadas em entrevista.
- Mantenha cargos, empresas, períodos e descrições coerentes com sua trajetória.
- Adapte palavras-chave às vagas pretendidas sem incluir competências que não correspondam à experiência real.
- Revise ortografia, datas, acentuação e links antes de publicar.

## Testes de responsividade

Após mudanças, teste em:

- Desktop ou notebook.
- Celular em orientação vertical.
- Zoom ampliado do navegador.
- Navegação por teclado e funcionamento dos links.

Verifique se há textos cortados, contraste insuficiente, botões difíceis de usar ou rolagem horizontal indesejada.

## Solução de problemas

### A página inicial não abre

- Confirme que o arquivo se chama exatamente `index.html`.
- Verifique se está na raiz da pasta publicada.
- Confirme a branch e a pasta configuradas em **Settings → Pages**.

### O CSS não é aplicado

- Confirme que `index.css` está no mesmo diretório de `index.html`.
- Verifique se `<link rel="stylesheet" href="index.css">` está dentro do `<head>`.
- Confira a grafia do nome do arquivo, inclusive maiúsculas e minúsculas.
- Atualize a página sem cache.
- Verifique se um bloco `<style>` ou outro seletor está sobrescrevendo as regras.

### O link para o currículo não funciona

- Confirme que `curriculo.html` foi enviado.
- Verifique o atributo `href` do link.
- Se os dois arquivos estão na mesma pasta, use o caminho relativo `curriculo.html`.

### A versão online não foi atualizada

- Confirme que o commit foi enviado à branch publicada.
- Verifique o estado em **Settings → Pages** e, quando aplicável, na aba **Actions**.
- Aguarde alguns minutos e recarregue o site.
- Confira se está acessando o endereço correto.

## Segurança e privacidade

Tudo o que for publicado no repositório ou no site poderá ficar acessível publicamente.

- Nunca publique senhas, tokens, chaves de API ou credenciais.
- Avalie se deseja tornar públicos telefone, e-mail pessoal ou outros dados de contato.
- Não inclua informações confidenciais de empregadores, clientes ou projetos.
- Revise os arquivos antes de cada publicação.

## Checklist de publicação

- [ ] `index.html` está na raiz da origem de publicação.
- [ ] `curriculo.html` abre corretamente.
- [ ] `index.css` está presente e vinculado corretamente.
- [ ] Os links de navegação e contato funcionam.
- [ ] Cargos, empresas, datas e métricas foram revisados.
- [ ] O site foi testado em desktop e celular.
- [ ] Nenhuma informação confidencial foi publicada por engano.
- [ ] GitHub Pages está configurado para a branch e pasta corretas.

## Licença

Este README não concede uma licença de reutilização. Se quiser permitir o uso do código por terceiros, adicione um arquivo `LICENSE` com a licença escolhida. Sem uma licença explícita, não presuma que outras pessoas estejam autorizadas a reutilizar o conteúdo, as imagens ou os dados publicados.

---

Mantenha este README atualizado sempre que a estrutura do projeto ou o processo de publicação mudar.
