---
name: carrossel
description: "Constrói um carrossel de vários slides para Instagram ou Facebook — capa, corpo, fecho — a partir de conteúdo existente, com resumo aprovado antes de produzir, contraste verificado e texto alternativo por slide. Usa esta skill SEMPRE que o trabalho for conteúdo de vários cartões (ex.: \"faz-me um carrossel\", \"transforma este artigo em carrossel\", \"quero vários slides sobre isto\", \"um post com várias imagens\", \"explica isto em cartões\", \"isto dá um carrossel?\", \"tenho um guia para publicar\", \"quero um post que as pessoas guardem\"). O carrossel é o formato dos guardados: dispara sempre que o objetivo for referência, profundidade ou algo a que alguém volte, mesmo que a palavra \"carrossel\" não apareça."
---

# Carrossel

## Gate de revisão

Antes de executar, correr `../social-media-manager/scripts/verificar_revisao.py`, resolvido relativamente a este ficheiro. Sem terminal, ler os blocos `Calendário` de `05-estado-das-plataformas.md` e `09-estado-da-vigilancia.md`. Se uma data chegou, passou ou é inválida, avisar uma vez por conversa; a primeira linha deve ser exatamente `Skill necessita de revisão`. Continuar com as limitações declaradas. O aviso não autoriza pesquisa, acesso a contas nem atualização.

Skill de execução. O julgamento — formato por função, escrita para ser guardado, acessibilidade — vive em `../social-media-manager/references/04-criacao-de-conteudo.md`. Ler o que for preciso, não repetir aqui.

## Porque é que o carrossel é o formato dos guardados

◑ No Instagram, os Reels obtêm mais alcance e os carrosséis mais taxa de interação; **carrosséis são o formato dos guardados** (`references/04-criacao-de-conteudo.md`). Isto não é um detalhe de contexto — é a instrução de desenho:

- ◑ O guardado é uma **decisão com custo**, ao contrário do gosto. Alguém guarda porque tenciona **voltar**.
- Logo, o carrossel tem de ser **utilizável mais tarde e fora do contexto**: uma lista de verificação, um método, uma comparação, um guia de escolha, uma sequência de passos.
- Um carrossel de opinião ou de história raramente é guardado. Se o conteúdo é uma história, o formato é vídeo curto ou post de texto — **dizer isso e não fazer o carrossel**.
- **O último slide tem de continuar a servir sozinho.** Quem volta em janeiro ao slide 8 tem de perceber o que ele diz sem reler os sete anteriores.

## Arranque imediato

Se o conteúdo já vier na mensagem, usá-lo e saltar para o Passo 2. Não resumir a skill.

## Passo 0. Perfil de marca

Ler `PERFIL-SOCIAL.md` (ou `MARCA.md`, `CLAUDE.md`, `MEMORY.md`, uma pasta `Social Media/`). Interessam a secção 5 (voz, grafias fixas, palavras proibidas), a 4 (plataformas), a 6 (o que se pode afirmar) e a 7 (pilares — o carrossel tem de caber num).

**Em conflito entre o perfil e esta skill, manda o perfil.** Se o projeto tiver skill própria de tema visual ou de voz, **essa ganha** sobre qualquer cor ou regra daqui.

Sem perfil, criá-lo a partir de `../social-media-manager/assets/PERFIL-MARCA-modelo.md`, em conversa com quem sabe, e **parar até existir**. Os campos por responder ficam `POR DEFINIR` — nunca preenchidos por adivinhação, e nada que dependa deles se afirma no carrossel.

## Passo 1. Conteúdo e parâmetros

Se não houver conteúdo:

> Cola o conteúdo do carrossel. Um post, uma secção de newsletter, um método, notas ou pontos soltos servem todos.

Depois, **AskUserQuestion**:

```json
[
  {"question": "O que é que alguém vai guardar aqui?", "header": "Função", "multiSelect": false,
   "options": [
     {"label": "Lista de verificação", "description": "Passos a cumprir, um a um"},
     {"label": "Método ou enquadramento", "description": "Uma forma de pensar o problema"},
     {"label": "Comparação", "description": "Isto contra aquilo, com critério"},
     {"label": "Guia de escolha", "description": "Ajuda a decidir entre opções"},
     {"label": "Nenhuma das anteriores", "description": "Provavelmente não devia ser carrossel — eu digo porquê e proponho o formato certo"}
   ]},
  {"question": "Estilo visual?", "header": "Estilo", "multiSelect": false,
   "options": [
     {"label": "Marca", "description": "Cores e tipografia do perfil"},
     {"label": "Escrevo as cores", "description": "Vou colar os códigos hex"},
     {"label": "Propõe tu", "description": "Escolhe paleta e tipografia pelo conteúdo"}
   ]},
  {"question": "Quantos slides?", "header": "Slides", "multiSelect": false,
   "options": [
     {"label": "6", "description": "Leitura rápida"},
     {"label": "8", "description": "Comprimento habitual"},
     {"label": "10", "description": "Aprofundado"}
   ]}
]
```

Se a resposta à primeira pergunta for "Nenhuma das anteriores", **parar aqui**: dizer porque é que este conteúdo não é guardável e encaminhar — história para `guiao-video-curto`, opinião ou notícia para `escrever-post`, uma frase só para `post-de-citacao`, informação densa que cabe numa imagem para `infografico`.

## Passo 2. Resumo slide a slide

Produzir o resumo em texto, para aprovação. Estrutura fixa:

| Slide | Função | Regra |
|---|---|---|
| **1 — capa** | Gancho. A promessa do que se leva daqui. | Concreto, cumprível, 5 a 8 palavras. Visualmente distinto do corpo. |
| **2** | Nomear o problema ou o âmbito fechado. | Diz a quem serve e a quem não serve. |
| **3 a N-1 — corpo** | **Uma ideia por slide.** | Título até 8 palavras · corpo até 15 palavras · elemento visual. |
| **N — fecho** | Resumo utilizável + **uma** chamada à ação. | Visualmente distinto. |

Regras do resumo:

- ⚠️ **Cada slide tem de dar razão para deslizar para o seguinte.** Um slide que não avança nada é onde a leitura pára — e a leitura até ao fim é o sinal que o formato tem para dar.
- **Uma ideia e uma chamada à ação por peça.** Duas ideias são zero ideias.
- A chamada à ação não pode custar mais do que aquilo que o carrossel acabou de dar. Se o carrossel entregou valor prático, "guarda para quando precisares" é proporcional; pedir uma compra não é.
- ⚠️ Nunca "marca três amigos" nem "partilha para ganhar": ⬤ o Facebook despromove *engagement bait* e Páginas reincidentes; PLAT-007. O Instagram proíbe recolher artificialmente interação. A política desta skill é não construir a peça sobre essa mecânica (`references/10-risco-crise-e-conformidade.md`).
- O gancho da capa tem de ser cumprido pelo corpo. Se não for, corrige-se **a capa**, não o corpo.

Depois:

> Este é o resumo, slide a slide. Diz o que mudar, ou diz "avança" quando estiver bem.

**Esperar aprovação explícita.** Não produzir imagens antes disso — refazer texto no resumo custa segundos, refazer dez imagens custa uma tarde.

## Passo 3. Produzir — HTML primeiro, gerador se existir

### 3A. Caminho predefinido: HTML/CSS

Funciona sem nada instalado e é o caminho que garante **consistência entre slides**, que é onde os geradores de imagem falham mais: cada geração é independente e a tipografia, as margens e a cor derivam de slide para slide.

Um ficheiro HTML único com **N secções do tamanho do slide**, empilhadas, CSS embutido e partilhado. A capa e o fecho variam na cor de fundo; tudo o resto é rigorosamente igual.

- **Dimensão, pela plataforma de destino da secção 4 do perfil:**
  - ◐ **Instagram — 1080×1350 (4:5).** É o rácio mais alto que o feed aceita sem cortar, e é o predefinido desta skill.
  - ◐ **Facebook — 1080×1080 (1:1).** O carrossel do Facebook alinha todos os cartões pelo rácio do primeiro e corta ao centro o que não encaixar, pelo que 4:5 chega lá recortado. Se a peça é para os dois sítios, ou se exporta em dois tamanhos, ou se assume o 1:1 e diz-se isso.
  - **Todos os slides do mesmo carrossel com rácio idêntico**, em qualquer plataforma. Rácios misturados são cortados.
  - ⚠️ São práticas correntes, não um número oficial datado: **confirmar na aplicação antes de exportar um lote grande** — as dimensões de feed mudam sem aviso.
- **Contraste** ⬤ mínimo 4,5:1 para texto normal e 3:1 para texto grande (18pt normal ou 14pt negrito), WCAG 2.2 AA. Calcular os rácios e escrevê-los na saída. Abaixo do limiar, muda-se a cor.
- **Nada essencial só por cor.**
- Margem interior mínima de 40 px, e o essencial afastado das bordas — ◐ a grelha do perfil pré-visualiza a publicação num rácio mais estreito do que o do feed, e corta.
- Indicador de progresso discreto ("3/8") em posição fixa.
- Tipografia grande: o critério é ler-se em ecrã pequeno.

Gravar e indicar, com o caminho do ficheiro:

> Abre o ficheiro no navegador. Para exportar cada slide: no menu de programador, "capturar imagem do nó" sobre cada secção; ou imprimir para PDF com a página definida ao tamanho do slide e sem margens, e depois separar as páginas. São os [N] ficheiros do carrossel, por ordem.

### 3B. Caminho opcional: pedidos para um gerador de imagem

Só se houver ferramenta disponível — e, se não houver, entregar na mesma os pedidos escritos, prontos a colar em qualquer gerador. **Nunca parar por falta de chave de API.** Dizer o que se perde: consistência entre slides e acentuação correta em português.

Um pedido por slide, cada um em bloco próprio e numerado, **com o bloco de estilo rigorosamente idêntico em todos**:

```
Slide [N] de [M] de um carrossel. Imagem [1080x1350 px (4:5) / 1080x1080 px (1:1)], igual em todos os slides.

Estilo (idêntico em todos os slides do conjunto):
- Fundo [hex] · texto [hex] · acento [hex]
- Tipografia: [título sem serifa, negrito] / [corpo sem serifa]
- Estética: [plana, alto contraste, sem gradientes, sem 3D]
- Margem interior generosa; indicador "[N]/[M]" no canto inferior

Função deste slide: [capa / corpo / fecho]

Conteúdo:
- Título: "[até 8 palavras]"
- Corpo: "[até 15 palavras]"
- Elemento visual: [ícone, número, bloco de cor, diagrama]

Restrições:
- Texto em português europeu, acentuação exatamente como escrita acima
- Contraste do texto sobre o fundo no mínimo 4,5:1
- Sem marcas de água, sem logótipos inventados, sem elementos de interface
```

⚠️ ⬤ O **artigo 50.º do AI Act**, em vigor desde 2 de agosto de 2026, obriga quem publica profissionalmente a identificar *deepfakes* e certos textos de interesse público; as plataformas podem exigir rótulos mais amplos. ◐ Este sistema identifica conteúdo realista ou materialmente alterado por IA quando houver dúvida. **Imagem de produto que não corresponde ao produto real é publicidade enganosa**, não estilo. Ver `references/10-risco-crise-e-conformidade.md`.

## Passo 4. Saída

```
CARROSSEL — [assunto]
Destino: [plataformas] · [N] slides · [dimensão e rácio] · via: [HTML / pedidos]
O que se guarda aqui: [lista de verificação / método / comparação / guia]

SLIDE 1 (capa)   "[gancho]"            alt: [...]
SLIDE 2          "[título]" / "[corpo]"  alt: [...]
...
SLIDE N (fecho)  "[resumo]" + CTA: [uma]  alt: [...]

CONTRASTE  [hex] sobre [hex] = [X,X]:1 ✓
FICHEIRO   [caminho] — ou os pedidos, nos blocos acima

LEGENDA DO POST
[texto da publicação — chamar `escrever-post` se for preciso trabalhá-lo]
```

## Regras

- **Português europeu** em tudo, incluindo o texto dos slides.
- ⚠️ **Identificar conteúdo comercial.** ⬤ `#PUB` no início quando há dinheiro ou benefício de terceiro — é o que a lei exige. ◐ **"conteúdo promocional"** quando é a própria marca a promover produto, preço, campanha ou desconto — é política interna deste sistema, não redação imposta. **Não trocar as duas:** carimbar `#PUB` numa peça da própria marca afirma uma relação comercial que não existe e dilui a etiqueta onde ela é obrigatória. Se a peça não promove nada, não leva nada. Tabela dos três casos em `../social-media-manager/references/10-risco-crise-e-conformidade.md`.
- **Texto alternativo em cada slide**, não um para o conjunto. É obrigatório e é a primeira coisa a desaparecer com pressa.
- **Informação essencial que está na imagem — uma data, um número, um passo — repete-se na legenda visível.** A imagem não pode ser o único sítio onde ela existe.
- **Um rácio só, igual em todos os slides**, escolhido pela plataforma de destino: 4:5 no Instagram, 1:1 no Facebook. Nunca misturar dentro do mesmo carrossel.
- Capa e fecho visualmente distintos do corpo; o corpo rigorosamente consistente.
- Máximo 15 palavras de corpo por slide.
- **Esperar aprovação do resumo antes de produzir.** Sem exceções.
- Se o conteúdo não é guardável, dizê-lo e propor outro formato em vez de fazer o carrossel na mesma.
- Caminho HTML predefinido, funciona sem nada instalado. Nenhum gerador é requisito.
- Contraste calculado e escrito na saída.
- **Nunca escrever preços, prazos ou condições** a partir desta skill; **nunca inventar números ou fontes** para encher slides. Um número sem amostra conhecida não entra num slide.
- **Fotografia, testemunho ou frase de cliente só com autorização escrita** para este fim, e imagem de banco só depois de verificar que a licença cobre uso comercial (`references/10-risco-crise-e-conformidade.md`).
- Sem engagement bait no slide de fecho.
- Não usar travessões longos na saída.
- Não resumir esta skill. Executá-la.
