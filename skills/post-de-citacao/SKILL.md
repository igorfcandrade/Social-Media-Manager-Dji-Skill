---
name: post-de-citacao
description: "Cria um cartão social com uma única frase em imagem, legenda de suporte, contraste verificado e texto alternativo. Usa apenas quando o pedido especifica uma citação, testemunho autorizado ou frase transformada em cartão; não presume este formato para pedidos vagos ou urgentes."
---

# Post de citação

## Gate de revisão

Antes de executar, correr `../social-media-manager/scripts/verificar_revisao.py`, resolvido relativamente a este ficheiro. Sem terminal, ler os blocos `Calendário` de `05-estado-das-plataformas.md` e `09-estado-da-vigilancia.md`. Se uma data chegou, passou ou é inválida, avisar uma vez por conversa; a primeira linha deve ser exatamente `Skill necessita de revisão`. Continuar com as limitações declaradas. O aviso não autoriza pesquisa, acesso a contas nem atualização.

## Contrato de contexto

Aplicar `../social-media-manager/references/contexto-do-caso.md`. O contexto pode chegar na mensagem, em anexos, em fontes ligadas ou em documentos com qualquer nome e formato. Neste ficheiro, «perfil» significa a fonte de contexto disponível; referências a números de secção servem apenas para o modelo opcional incluído no pacote. Não exigir esse modelo, não o copiar automaticamente e não tratar website, checkout, equipa ou ferramenta como pré-requisito. Pedir apenas a informação que muda materialmente esta tarefa.

Skill de execução. O julgamento — escrever para ser reenviado, prova social, acessibilidade — vive em `../social-media-manager/references/04-criacao-de-conteudo.md`. Ler o que for preciso, não repetir aqui.

## Expectativa honesta, dita à cabeça

◐ Um cartão de citação é barato de produzir e por isso é o formato que mais se produz sem método. O que se sabe com segurança:

- ◑ A imagem única tem desempenho em queda face a vídeo curto e carrossel (`references/04-criacao-de-conteudo.md`). Um cartão de citação **não é um formato de descoberta**.
- ◐ Aciona sobretudo **moeda social** — quem partilha diz algo sobre si próprio. É o motor certo para reconhecimento e identidade de marca; é o motor errado para explicar um produto ou gerar pedidos. *(Motor do modelo STEPPS, que é um livro de divulgação com casos e não um conjunto de estudos replicados — `references/04-criacao-de-conteudo.md`.)*
- ◐ Um feed que é só citações é um feed sem provas. Convenção de trabalho: **no máximo, uma peça de citação por cada quatro ou cinco**. É proporção de bom senso, não um dado — os rácios de mistura de conteúdo (80/20, 4-1-1 e afins) têm autoria conhecida e **nenhum estudo por trás** (`references/11-numeros-de-referencia.md`). Ajustar ao que o histórico da própria conta mostrar.
- Os números de alcance associados a este formato que circulam em blogues não têm amostra publicada. Não os repetir.

⚠️ Se o perfil de marca descrever uma voz analítica, seca ou deliberadamente não motivacional, **assinalar o desencontro e perguntar** se este formato serve o posicionamento, antes de produzir seja o que for.

## Arranque imediato

Se a frase ou a legenda já vierem na mensagem, saltar a escrita de opções do Passo 2 e ir direto ao desenho. **Mas confirmar sempre a origem primeiro** (Passo 1): é a única pergunta que não se salta, porque é dela que dependem a autorização e a verificação. Não resumir a skill.

## Passo 0. Contexto do caso

Ler o contexto do caso disponível, qualquer que seja o nome ou formato. Interessam a secção 5 inteira — voz, tratamento, adjetivos do tom, palavras da casa, **palavras proibidas**, exemplos aprovados e rejeitados — mais a 6 (o que se pode afirmar) e a 4 (plataformas). Uma frase de sete palavras é o sítio onde a voz da marca está mais exposta: não há corpo de texto onde esconder um tom errado.

Em conflito, ganha o contexto do caso. Sem voz ou identidade visual suficientes, pedir as decisões
necessárias ou entregar apenas a estrutura com lacunas explícitas. Não criar ficheiros paralelos.

## Passo 1. Origem da frase — decide tudo o resto

⚠️ A origem pergunta-se **sempre**, mesmo quando a frase já vem colada na mensagem. Ter a frase escrita não diz de quem ela é — e é a origem, não a posse do texto, que abre ou fecha os passos de autorização e de verificação. Uma frase colada sem origem declarada é o caminho mais curto para publicar um depoimento de cliente sem autorização.

**Perguntar pelo meio interativo disponível:**

```json
[
  {"question": "De onde vem a frase?", "header": "Origem", "multiSelect": false,
   "options": [
     {"label": "Da marca", "description": "Uma frase nossa. Sem atribuição a ninguém."},
     {"label": "De um cliente", "description": "Palavras reais de cliente. Exige autorização escrita."},
     {"label": "De um autor", "description": "Citação de terceiro. Exige fonte verificada."}
   ]},
  {"question": "Já tens a frase escrita?", "header": "Frase", "multiSelect": false,
   "options": [
     {"label": "Já tenho", "description": "Vou colá-la. Salta a escrita de opções."},
     {"label": "Escreve tu", "description": "Só se a origem for a marca."}
   ]},
  {"question": "Onde vai sair?", "header": "Destino", "multiSelect": true,
   "options": [
     {"label": "Instagram feed", "description": "4:5 — tela 1080x1350"},
     {"label": "Stories", "description": "9:16 — tela 1080x1920"},
     {"label": "Facebook", "description": "Mesma peça 4:5"},
     {"label": "Pinterest", "description": "2:3 — 1000x1500"}
   ]}
]
```

◐ **Sobre estas dimensões:** 1000×1500 é uma tela de produção 2:3, não um limite universal do Pinterest; a plataforma aceita outros rácios orgânicos (PLAT-019). Os 1080×1350 e 1080×1920 também são **prática corrente de produção**, não dimensões universais impostas pela Meta. Servem como tela de trabalho, não como facto de plataforma.

As três origens têm regras diferentes e **não se misturam**:

| Origem | Regra que não se contorna |
|---|---|
| **Da marca** | Sem atribuição nenhuma. Não pôr aspas com nome de pessoa que não a disse. |
| **De cliente** | ⚠️ Palavras **reais**, com autorização **por escrito** — uma marcação não transfere licença nem direito de imagem (`references/04-criacao-de-conteudo.md`). Um depoimento inventado não é um problema de rotulagem: é fraude. Sem autorização registada, **não sai**. |
| **De autor** | Fonte verificada, com obra e ano. **Nunca inventar uma atribuição.** Citações mal atribuídas circulam em massa, e os sites agregadores de citações copiam-se uns aos outros sem fonte primária — **não servem de verificação**. Se não se consegue chegar à obra, não se publica: reescreve-se como frase da marca, sem aspas e sem nome. |

**Depois da origem, o caminho diverge:**

- **Da marca** → Passo 2 (escrever as opções).
- **De um cliente** → **não se escreve nada.** Confirmar por escrito, com quem tem a autorização registada, qual foi a frase textual e onde está o registo. Sem esses dois campos preenchidos, parar aqui e dizê-lo. Depois, Passo 3.
- **De um autor** → verificar obra, autor e ano antes de desenhar seja o que for. Verificada, Passo 3; não verificada, voltar a "Da marca" e reescrever sem aspas.

### Vários destinos ao mesmo tempo

**Um destino, uma peça.** Cada superfície tem o seu rácio e as suas zonas seguras; a mesma tela recortada perde a composição em todas menos numa.

- Sai **uma peça por destino**, cada uma **no seu rácio**, com as zonas seguras dessa superfície e o contraste recalculado se a cor mudar.
- O **texto alternativo é por peça**, não um para o conjunto.
- ⚠️ **Destinos que não estejam na secção 4 do perfil não se produzem.** Perguntar porquê primeiro.
- Se o mesmo desenho servir dois rácios sem redesenho, dizê-lo explicitamente — é a exceção, não o pressuposto.

## Passo 2. Escrever as opções

Se a frase é da marca, devolver **9 opções em 3 famílias de 3**, escolhidas pelos pilares do perfil (secção 7), não por categorias genéricas de motivação. Famílias típicas de um negócio real:

1. **Ofício** — o que se sabe por fazer aquilo há anos.
2. **Cliente** — o que ele sente, dito na linguagem dele.
3. **Posição** — o que a marca defende e que a distingue.

Cada frase tem de:

- ◐ ter **menos de 15 palavras** — restrição de legibilidade da peça, não um dado de desempenho: acima disso o corpo de letra tem de encolher e a frase deixa de se ler no telemóvel. Não há estudo por trás deste limite, e não o apresentar como se houvesse;
- ser **específica**: nomear algo concreto, não uma categoria. Uma frase que servia a qualquer negócio não serve a este;
- **bater nas três primeiras palavras**;
- funcionar sozinha, sem contexto;
- soar à voz do perfil — comparar com os exemplos aprovados e rejeitados da secção 5;
- ⚠️ não conter nenhuma **alegação** que a marca não consiga provar (secção 6). Uma frase bonita sobre resultados é uma alegação, e em setor regulado pode ser ilegal — ver `references/10-risco-crise-e-conformidade.md`.

```
FRASES — para a legenda: [assunto]

1. Ofício
   a. [frase]   b. [frase]   c. [frase]
2. Cliente
   a. [frase]   b. [frase]   c. [frase]
3. Posição
   a. [frase]   b. [frase]   c. [frase]
```

> Qual delas soa mesmo à marca? Responde com o número e a letra (ex.: 2b), ou cola a tua.

## Passo 3. Desenhar o cartão — HTML primeiro

O caminho predefinido é **HTML/CSS**: funciona sem nada instalado, e é o único que garante que a frase sai com a ortografia e a acentuação exatas. Numa peça cuja mensagem inteira é o texto, um erro de acentuação estraga a peça toda — e é o erro mais frequente dos geradores de imagem em português.

Ficheiro HTML único, CSS embutido, na dimensão do destino. Restrições:

- **A frase é o foco.** Centrada, grande, com muito espaço à volta. Nada compete com ela.
- **Duas cores dominam**, da paleta do perfil. Fundo liso ou fotografia com zona lisa por baixo do texto.
- **Contraste** ⬤ mínimo 4,5:1 para texto normal e 3:1 para texto grande (18pt normal ou 14pt negrito), WCAG 2.2 AA. Calcular e escrever o rácio na saída. Texto de baixo contraste sobre fotografia é ilegível ao sol, e é onde este formato falha mais.
- ⚠️ ◐ **Recorte da grelha do perfil.** A grelha do Instagram recorta as miniaturas em 3:4 desde 2025, independentemente do que se envia. Uma peça 4:5 aparece inteira no feed e **perde uma faixa de cada lado na grelha** — numa peça cuja mensagem inteira é uma frase centrada, é exatamente aí que as palavras das pontas se partem. Manter a frase dentro de uma zona segura 3:4 centrada, com margem lateral folgada, e **confirmar na conta real** antes de produzir um lote.
- Atribuição em corpo pequeno **só quando existe** e está verificada.
- Coerência: a mesma família de cartões repetida ao longo do tempo rende mais do que um cartão brilhante isolado.

**Estilos** a propor se o perfil não fixar um: editorial (serifada grande, muito branco, um acento) · cartaz (sem serifa pesada, bloco de cor sólido) · manuscrito (aspeto de caderno, fundo creme) · fotografia da marca com sobreposição.

### Caminho opcional: gerador de imagem

Só se houver ferramenta disponível, e nunca como requisito. Se não houver, entregar na mesma o pedido escrito para o utilizador colar onde quiser:

```
Cartão de citação, [1080x1350 / 1080x1920 / 1000x1500] px, vertical.

Estilo: [editorial / cartaz / manuscrito / fotografia com sobreposição]
Paleta: fundo [hex] · texto [hex] · acento [hex]

Texto, centrado e como elemento focal, exatamente assim:
"[FRASE ESCOLHIDA]"

[Atribuição em corpo pequeno: [nome], [obra, ano] — omitir se não houver]

Restrições:
- Português europeu: acentuação e pontuação exatamente como escritas acima
- Contraste do texto sobre o fundo no mínimo 4,5:1
- Sem marcas de água, sem nomes de conta, sem logótipos inventados
- Sem rostos de pessoas reais
```

⚠️ ⬤ O **artigo 50.º do AI Act**, em vigor desde 2 de agosto de 2026, obriga quem publica profissionalmente a identificar *deepfakes* e certos textos de interesse público; as plataformas podem exigir rótulos mais amplos. ◐ Este sistema identifica conteúdo realista ou materialmente alterado por IA quando houver dúvida. **Nunca gerar o rosto de um cliente para acompanhar um testemunho**, nem uma imagem de produto que não corresponde ao produto real. Ver `references/10-risco-crise-e-conformidade.md`.

## Passo 4. A legenda

O cartão sozinho é uma frase no ar. A legenda é onde a frase ganha prova: **uma história curta, um caso, um número que a marca consegue sustentar**. Sem isso, o post é decoração.

⬤ **A frase transcrita começa a legenda visível.** Não basta pô-la no texto alternativo: a informação essencial de uma imagem tem de estar também na legenda visível (`references/04-criacao-de-conteudo.md`), e aqui a informação essencial é a peça inteira. Serve também a quem vê a imagem cortada na grelha.

Uma chamada à ação só, e barata — o cartão deu pouco, não pode pedir muito. Guardar, ou uma **pergunta genuína** que convide a responder.

⚠️ Uma pergunta genuína não é o mesmo que pedir um comentário. ⬤ No Facebook, a Meta declara a despromoção de *engagement bait* e de Páginas reincidentes; PLAT-007. ⬤ No Instagram, as Diretrizes da Comunidade proíbem recolher artificialmente gostos, seguidores ou partilhas; não se inventa uma penalização idêntica à do Facebook. Pedidos genuínos de opinião, conselho ou experiência são diferentes de interação como fim. Nunca pedir uma compra a partir desta peça.

Para trabalhar a legenda a sério, chamar `escrever-post`.

## Passo 5. Saída

```
POST DE CITAÇÃO
Destino: [plataformas] · [dimensão] · origem: [marca / cliente / autor]

FRASE   "[...]"
ATRIBUIÇÃO  [nome + fonte verificada — ou "nenhuma", que é o caso normal]
AUTORIZAÇÃO  [para frase de cliente: quem autorizou, quando, onde está registado]

CARTÃO
Estilo: [...] · Paleta: [hex] / [hex]
Contraste: [hex] sobre [hex] = [X,X]:1 ✓
Zona segura: [frase dentro do recorte 3:4 da grelha do perfil — sim / não]
Ficheiro: [caminho do HTML] — ou o pedido de imagem, no bloco acima

TEXTO ALTERNATIVO
Cartão com a frase "[frase transcrita]"[, atribuída a [nome]].

LEGENDA
[frase transcrita + texto que a sustenta com prova real + uma chamada à ação barata]

A SEGUIR
[abrir o HTML no telemóvel e confirmar a legibilidade · confirmar o recorte na
conta real · e, se a legenda precisar de trabalho a sério, chamar `escrever-post`]
```

## Regras

- **Português europeu** em tudo, incluindo a frase do cartão.
- ⚠️ **Identificar conteúdo comercial.** ⬤ `#PUB` no início quando há dinheiro ou benefício de terceiro — é o que a lei exige. ◐ **"conteúdo promocional"** quando é a própria marca a promover produto, preço, campanha ou desconto — é política interna deste sistema, não redação imposta. **Não trocar as duas:** carimbar `#PUB` numa peça da própria marca afirma uma relação comercial que não existe e dilui a etiqueta onde ela é obrigatória. Se a peça não promove nada, não leva nada. Tabela dos três casos em `../social-media-manager/references/10-risco-crise-e-conformidade.md`.
- **Nunca inventar uma atribuição.** Sem fonte verificada, não há aspas com nome.
- **Nunca inventar um testemunho de cliente.** É fraude, não é criatividade. Autorização escrita, sempre, e registada na saída.
- ◐ Máximo 15 palavras na frase, por legibilidade — não por desempenho.
- A origem pergunta-se sempre, mesmo com a frase já colada.
- Vertical sempre. Nunca horizontal.
- O caminho HTML é o predefinido e funciona sem nada instalado. Nenhum gerador é requisito.
- Contraste calculado e escrito na saída. **Texto alternativo sempre, com a frase transcrita** — sem isso a peça não existe para quem usa leitor de ecrã, e a mensagem inteira desta peça é texto. **E a frase também na legenda visível.**
- Nunca pedir comentários, marcações ou partilhas como fim: é interação artificial e não entra nesta skill.
- Nenhuma frase pode conter uma alegação que a marca não consiga provar.
- **Nunca escrever preços, prazos ou condições** a partir desta skill.
- Dizer a expectativa honesta do formato sem ser preciso perguntar.
- Não usar travessões longos na saída.
- Não resumir esta skill. Executá-la.
