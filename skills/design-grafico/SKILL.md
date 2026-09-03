---
name: design-grafico
description: "Desenha a peça visual que acompanha um post — decide entre um gráfico construído em HTML/CSS (estrutura, passos, comparação, números) e uma imagem gerada ou fotografada, e entrega a peça pronta com paleta, contraste verificado e texto alternativo. Usa esta skill SEMPRE que o pedido for uma imagem para acompanhar conteúdo (ex.: \"faz-me um gráfico para este post\", \"preciso de uma imagem para isto\", \"cria um visual\", \"que imagem ponho aqui?\", \"desenha-me isto\", \"transforma este texto em imagem\", \"quero uma peça para o Instagram\", \"acabei o post, falta a arte\", \"monta-me um cartão com estes três passos\"). Dispara também logo a seguir a escrever um post, quando falta o visual. Para carrossel de vários slides usar `carrossel`; para infografia densa usar `infografico`; para citações usar `post-de-citacao`; para capa de vídeo usar `capa-de-video`."
---

# Design gráfico de peça social

## Gate de revisão

Antes de executar, correr `../social-media-manager/scripts/verificar_revisao.py`, resolvido relativamente a este ficheiro. Sem terminal, ler os blocos `Calendário` de `05-estado-das-plataformas.md` e `09-estado-da-vigilancia.md`. Se uma data chegou, passou ou é inválida, avisar uma vez por conversa; a primeira linha deve ser exatamente `Skill necessita de revisão`. Continuar com as limitações declaradas. O aviso não autoriza pesquisa, acesso a contas nem atualização.

Skill de execução. O julgamento — que formato serve que objetivo, o sistema visual de cinco decisões, a lista de acessibilidade — vive em `../social-media-manager/references/04-criacao-de-conteudo.md`. Ler o que for preciso, não repetir aqui.

## Arranque imediato

Se o post já vier na mensagem, usá-lo e saltar a procura de ficheiro no Passo 1 — mas **a pergunta do destino faz-se sempre**, porque é dela que sai a dimensão. Não resumir a skill nem explicar as opções antes de começar.

## Passo 0. Perfil de marca

Ler `PERFIL-SOCIAL.md` (ou `MARCA.md`, `MEMORY.md`) na raiz do projeto. Interessam a secção 4 (plataformas), a 5 (voz, grafias fixas, palavras proibidas), a 6 (o que se pode afirmar) e a 8 (meios de produção). Se o projeto tiver skill própria de tema visual ou paleta, **essa ganha** sobre qualquer sugestão de cor daqui.

Se não existir perfil, criá-lo a partir de `../social-media-manager/assets/PERFIL-MARCA-modelo.md`, e **não produzir peça nenhuma até a identidade visual estar escrita**. Cores e tipografia não se adivinham: uma peça com a cor errada é uma peça a refazer, e vinte peças com a cor errada são uma identidade a refazer.

⚠️ **O modelo de perfil não tem campo de paleta nem de tipografia.** Se as cinco decisões visuais não estiverem lá, perguntar ao utilizador — códigos hexadecimais, tipo de letra, família de fundos — e **escrever a resposta no próprio perfil**, na secção 12 (Convenções técnicas), como uma entrada "Convenções visuais". Nunca criar um ficheiro paralelo de tema, paleta ou estilo: o perfil é o único sítio. O que ficar por responder fica marcado `POR DEFINIR` e é uma pergunta em aberto, não uma lacuna a tapar com um azul qualquer.

## Passo 1. Ler o post e escolher o caminho

Se não houver post na mensagem, procurar o ficheiro de post mais recente no projeto. Se não existir:

> Cola o post para o qual queres a peça.

Depois, **AskUserQuestion**:

```json
[
  {"question": "Que tipo de peça serve este post?", "header": "Tipo", "multiSelect": false,
   "options": [
     {"label": "Gráfico em HTML/CSS", "description": "Estrutura, passos, comparação, números. Totalmente editável, exporta-se por captura de ecrã."},
     {"label": "Fotografia real", "description": "Produto, pessoa, processo. Instruções de captação, sem gerador nenhum."},
     {"label": "Imagem gerada", "description": "Ilustração ou cenário que não existe para fotografar. Entrego o pedido escrito."},
     {"label": "Decide tu", "description": "Analisa o conteúdo e escolhe"}
   ]},
  {"question": "Onde vai sair?", "header": "Destino", "multiSelect": true,
   "options": [
     {"label": "Instagram feed", "description": "4:5 vertical — 1080x1350 ◐"},
     {"label": "Stories 9:16", "description": "1080x1920 ◐, com zonas seguras"},
     {"label": "Facebook", "description": "Mesma peça 4:5"},
     {"label": "Pinterest", "description": "2:3 — 1000x1500 ◐ como tela de produção"}
   ]}
]
```

**Sobre estas dimensões, com honestidade:** ◐ 1000×1500 é uma tela de produção 2:3, não um limite universal do Pinterest. A plataforma aceita vários rácios orgânicos; ver PLAT-019. Os 1080×1350 e 1080×1920 também são **prática corrente de produção**, não dimensões universais impostas pela Meta. Servem como tela de trabalho, não como facto de plataforma.

◐ **Aviso que decide o enquadramento:** a grelha do perfil de Instagram recorta as miniaturas em 3:4 desde 2025, independentemente do que se envia. Uma peça 4:5 aparece inteira no feed e **cortada em cima e em baixo na grelha**. Consequência prática: título, logótipo e números vivem na faixa central, nunca junto às arestas superior e inferior. Confirmar na conta real antes de produzir um lote.

Se o destino for a capa ou primeiro fotograma de um vídeo curto, isto não é a skill certa: `capa-de-video`. TikTok está `LOOK INTO`.

**Se "Decide tu":** conteúdo com passos numerados, comparação, enquadramento ou números → Caminho A (HTML/CSS). Produto, pessoa, processo ou lugar que existem mesmo → Caminho B (fotografia). Cenário ou metáfora que não é fotografável → Caminho C (imagem gerada). Na dúvida entre A e B, ganha B: uma fotografia real da coisa vale mais do que um cartão bonito com palavras.

### Vários destinos ao mesmo tempo

**Um destino, uma peça.** Cada superfície tem o seu rácio e as suas zonas seguras; a mesma tela recortada perde a composição em todas menos numa.

- Sai **uma peça por destino**, cada uma **no seu rácio**, com as zonas seguras dessa superfície e o contraste recalculado se a cor mudar.
- O **texto alternativo é por peça**, não um para o conjunto.
- ⚠️ **Destinos que não estejam na secção 4 do perfil não se produzem.** Perguntar porquê primeiro.
- Se o mesmo desenho servir dois rácios sem redesenho, dizê-lo explicitamente — é a exceção, não o pressuposto.

## Passo 2. As cinco decisões visuais

Antes de produzir seja o que for, fixar as cinco decisões do sistema visual (`references/04-criacao-de-conteudo.md`): **luz · família de fundos · enquadramento · paleta e tipografia · tratamento de cor**. São as mesmas em todas as peças da marca — é a repetição que constrói o reconhecimento, não a qualidade de uma peça isolada. Se o perfil já as tiver fixadas, usá-las tal e qual e não propor alternativas.

## Passo 3A. Caminho A — gráfico em HTML/CSS

Um ficheiro HTML único e autossuficiente, com CSS embutido e `meta viewport`. Restrições:

- **Dimensão** conforme o destino, com uma tela de produção fixada no CSS: 1080×1350 (feed), 1080×1920 (histórias), 1000×1500 (Pinterest 2:3). São escolhas de produção; confirmar a superfície real.
- **Fundo** e cores da paleta do perfil. Nada de fotografia de banco de imagens por baixo do texto — e, se alguma vez entrar uma, ⚠️ verificar primeiro a licença comercial: muitas licenças gratuitas excluem uso comercial ou exigem atribuição (`references/10-risco-crise-e-conformidade.md`).
- **Contraste** ⬤ mínimo 4,5:1 para texto normal e 3:1 para texto grande (18pt normal ou 14pt negrito), norma WCAG 2.2 AA. São limiares, não arredondáveis. **Calcular o rácio dos pares de cor usados e escrevê-lo na saída.** Se der abaixo, muda-se a cor — não se publica.
- **Margem interior** ◐ de pelo menos 5% do lado mais curto da tela — cerca de 54 px numa tela de 1080 de largura. É prática de composição, não uma regra de plataforma; o que não é negociável é o ponto seguinte.
- **Zonas seguras da interface.** ◐ Numa peça 9:16 para histórias, a aplicação sobrepõe o nome de utilizador, a barra de progresso e a barra de resposta: manter texto e elementos essenciais dentro da faixa central, folgando à volta de 250 px em cima e em baixo. Os valores que circulam variam entre ~155 e ~250 px conforme a fonte, nenhum publicado pela Meta — usar o mais conservador e **confirmar na aplicação real, não só no editor** (`references/04-criacao-de-conteudo.md`). Numa peça 4:5, aplicar a mesma lógica ao recorte 3:4 da grelha do perfil.
- **Tipografia sem serifa**, grande. O critério é ler-se num telemóvel, não caber tudo.
- **O número de blocos vem do conteúdo**: 3 passos, 3 blocos; 7 dicas, 7 blocos. Se sete blocos não se lêem, o problema é a peça ser um carrossel disfarçado — nesse caso chamar `carrossel`.
- **Informação essencial nunca só na cor.** Ícone, número ou palavra a acompanhar.
- Rodapé com o nome da marca, tirado do perfil. Sem inventar nome de utilizador nem assinatura de marca.

Destilar o post, **nunca copiá-lo inteiro**: ◐ um título curto, na ordem das 5 a 8 palavras, mais os pontos-chave em blocos. O limite verdadeiro é ler-se de relance, não a contagem.

Gravar o ficheiro e dizer onde ficou. Exportar sem instalar nada:

> Abre o ficheiro no navegador, carrega em imprimir e escolhe "guardar como PDF" — ou, no menu de ferramentas de programador, usa a captura do elemento da tela. Qualquer dos dois dá a imagem no tamanho exato, porque a tela está fixada em pixéis no CSS.

Se houver no ambiente uma ferramenta de captura automática, usá-la e entregar o ficheiro de imagem já pronto. É melhoria, nunca requisito: o caminho de cima funciona sem nada instalado.

## Passo 3B. Caminho B — fotografia real

É o caminho predefinido para produto, pessoa, processo e lugar. Entregar uma instrução de captação concreta, não um conceito:

> Plano: [enquadramento e altura de câmara] · Luz: [janela, lado, difusão] · Fundo: [qual da família de fundos] · Sujeito: [o quê, em que posição] · Extras a captar na mesma sessão: [2 ou 3 variantes]

Telemóvel: bloquear foco e exposição, ligar a grelha, limpar a lente, fotografar em sessão agrupada. **O sol direto é o problema, não a solução.**

Se o texto for sobreposto à fotografia, indicar a zona de fundo liso onde vai assentar e o par de cores com o rácio de contraste calculado.

⚠️ **Antes de mandar fotografar pessoas ou material de terceiros:**
- **Pessoas identificáveis** têm direito de imagem além da proteção de dados. Autorização por escrito, registada, e que pode ser retirada.
- **Fotografia de cliente**, mesmo enviada espontaneamente por ele, **não vem com autorização.** Uma marcação não transfere licença. Pedir por escrito.
- **Testemunho com nome ou rosto** exige consentimento **para esse fim específico** — consentimento para uma coisa não serve para outra.
- Não publicar capturas de conversas com dados de clientes visíveis. Tapar tudo o que identifique.

Detalhe em `references/10-risco-crise-e-conformidade.md`. Nenhuma destas autorizações se presume a partir desta skill: ou existe por escrito, ou a peça não usa a pessoa.

## Passo 3C. Caminho C — imagem gerada (opcional, nunca requisito)

Só quando o que se quer mostrar não é fotografável. Verificar primeiro se existe alguma ferramenta de geração no ambiente; **se não existir, entregar na mesma o pedido escrito** num bloco de código, pronto a colar em qualquer gerador que o utilizador tenha. Não parar, não pedir chave de API.

```
Imagem para redes sociais, [1080x1350 / 1080x1920 / 1000x1500] px.

Assunto: [o que se vê]
Composição: [posição do sujeito, o que ocupa o quê]
Paleta: primária [hex] · acento [hex] · fundo [hex]
Tratamento: [luz, textura, estilo — coerente com as cinco decisões da marca]

Texto na imagem:
- "[máximo 8 palavras]" · tipografia sem serifa, grande
- Cor [hex] sobre [hex] — contraste verificado ≥ 4,5:1
- Posição: [área], fora das margens da interface

Restrições:
- Sem marcas de água e sem elementos de interface de nenhuma aplicação
- Sem logótipos inventados
- Legível reduzido ao tamanho de uma pré-visualização de feed
```

⚠️ **Regras que não se contornam:**
- ⬤ A Meta aplica o rótulo "AI Info" a conteúdo detetado ou declarado. TikTok está `LOOK INTO`; confirmar a política atual antes de qualquer utilização nessa plataforma.
- ⬤ O **artigo 50.º do AI Act** está em vigor desde 2 de agosto de 2026 e obriga quem publica profissionalmente a identificar *deepfakes* — conteúdo que cria falsamente aparência de autenticidade — e certos textos de interesse público. ◐ A política conservadora deste sistema é identificar também conteúdo realista ou materialmente alterado por IA quando houver dúvida. Ver `../social-media-manager/references/10-risco-crise-e-conformidade.md`.
- **Fotografia de produto gerada por IA que não corresponde ao produto real é publicidade enganosa, não estilo.** Não se faz, com ou sem rótulo.
- Rosto de pessoa real: só a partir de fotografia real dessa pessoa, com autorização escrita.
- Verificar que a licença do gerador usado **cobre uso comercial**. Vários geradores gratuitos não cobrem, e a peça é para uma marca.
- ⚠️ A rotulagem é obrigação de quem publica, não da skill: dizer ao utilizador, na entrega, que tem de ativar o rótulo de conteúdo gerado por IA no momento de publicar.

## Passo 4. Formato de saída

```
PEÇA — [post]
Destino: [plataformas] · [dimensão] · caminho: [A / B / C]

CONTEÚDO NA IMAGEM
Título: "[5 a 8 palavras]"
Blocos: [...]

SISTEMA VISUAL
Paleta: [hex] · Tipografia: [...] · Fundo: [...] · Tratamento: [...]
Contraste: [cor texto] sobre [cor fundo] = [X,X]:1 ✓ (mínimo 4,5:1)
Zonas seguras: [o que fica fora do recorte 3:4 da grelha / fora da interface das histórias]

COMO PRODUZIR
[caminho do ficheiro HTML / instrução de captação / pedido de imagem]

TEXTO ALTERNATIVO
[função e conteúdo essencial da imagem, sem começar por "imagem de"]

NA LEGENDA VISÍVEL
[a informação essencial que está na imagem, repetida em texto]
```

## Passo 5. Passo seguinte

> Se isto for demasiado conteúdo para uma imagem só, faço-o em carrossel: `carrossel`. Se for uma infografia densa: `infografico`. Se faltar a legenda: `escrever-post`.

## Regras

- **Português europeu** em tudo, incluindo o texto dentro da imagem.
- Ler sempre o post antes de desenhar. A peça recapitula o conteúdo; não ilustra um conceito abstrato.
- **Uma ideia por peça.** Duas ideias são zero ideias.
- Nenhuma ferramenta de geração de imagem é obrigatória. Os caminhos A e B funcionam sem nada instalado, e o C degrada para um pedido escrito.
- Contraste calculado e escrito na saída. Sem isso a peça não sai.
- **Texto alternativo sempre**, em todas as peças. Não é opcional.
- Se a imagem carrega informação essencial — um preço, uma data, um número — essa informação também vai para a legenda visível.
- **Nunca escrever preços, prazos ou condições** a partir desta skill. Vêm do perfil ou de um humano.
- Nunca inventar um número, uma percentagem ou uma fonte para pôr dentro de um gráfico. Números só os que vierem do post ou do perfil.
- **Nunca pôr na peça um pedido explícito de interação** — "marca três amigos", "partilha para ganhar", "comenta para receber". ⬤ No Facebook, a Meta documenta despromoção de *engagement bait* e de Páginas reincidentes; PLAT-007. No Instagram, a proibição relevante é a recolha artificial de interação; não lhe atribuir a penalização específica do Facebook.
- **Nada de pessoas, testemunhos ou conteúdo de terceiros sem autorização escrita.** Vale para fotografia real e para imagem gerada.
- As dimensões desta skill são tela de trabalho ◐, não factos de plataforma. Antes de fixar um lote grande, confirmar o rácio aceite em `references/05-plataformas.md`.
- Não usar travessões longos na saída.
- Não resumir esta skill. Executá-la.
