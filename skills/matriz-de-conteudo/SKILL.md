---
name: matriz-de-conteudo
description: "Gera um banco ou matriz de ideias ao cruzar pilares, formatos e ângulos concretos. Usa quando pedirem ideias, temas, pilares ou uma matriz sem datas. Produz ideias, não calendário datado, estratégia completa nem texto final."
---

# Matriz de conteúdo

## Gate de revisão

Antes de executar, correr `../social-media-manager/scripts/verificar_revisao.py`, resolvido relativamente a este ficheiro. Sem terminal, ler os blocos `Calendário` de `05-estado-das-plataformas.md` e `09-estado-da-vigilancia.md`. Se uma data chegou, passou ou é inválida, avisar uma vez por conversa; a primeira linha deve ser exatamente `Skill necessita de revisão`. Continuar com as limitações declaradas. O aviso não autoriza pesquisa, acesso a contas nem atualização.

## Contrato de contexto

Aplicar `../social-media-manager/references/contexto-do-caso.md`. O contexto pode chegar na mensagem, em anexos, em fontes ligadas ou em documentos com qualquer nome e formato. Neste ficheiro, «perfil» significa a fonte de contexto disponível; referências a números de secção servem apenas para o modelo opcional incluído no pacote. Não exigir esse modelo, não o copiar automaticamente e não tratar website, checkout, equipa ou ferramenta como pré-requisito. Pedir apenas a informação que muda materialmente esta tarefa.

Skill de execução. O critério — como se escolhem pilares, o contra-âmbito, Hero/Hub/Help, o folclore dos rácios, banco de ideias — vive em `../social-media-manager/references/03-planeamento-e-calendario.md`. **Ler esse módulo antes de gerar seja o que for e não o repetir aqui.** Para o formato de cada peça, `../social-media-manager/references/04-criacao-de-conteudo.md`.

## Arranque imediato

Ao disparar, ir direto ao Passo 0. Não resumir a skill, não explicar a matriz antes de a construir.

## Passo 0. Contexto do caso

Procurar o contexto do caso disponível na mensagem, anexos, fontes ligadas ou documentos do projeto.

- **Se existir**, lê-lo primeiro: secção 1 (Negócio, incluindo **ciclo de decisão**), 3 (Público e as perguntas que já faz), 4 (Plataformas), 6 (o que se pode afirmar), 7 (**Pilares com âmbito e contra-âmbito**), 8 (cadência real), 10 (datas aceites e recusadas), 11 (aprendizagens). Dizer numa linha o que foi aproveitado e **não voltar a perguntar o que já lá está**.
- **Se não existir**, pedir oferta e público. Sem ambos, parar: a matriz daria ideias igualmente
  aplicáveis a um concorrente. Os pilares não bloqueiam; o Passo 1 pode propô-los.
- **Sem ferramentas de ficheiro** (não se consegue ler nem escrever no projeto), a skill não para: perguntar em conversa o conteúdo das secções 1 e 3, trabalhar com as respostas, e entregar no fim o texto do perfil e da matriz para a pessoa colar num ficheiro seu. Nenhum passo desta skill exige chave de API, ferramenta instalada ou serviço pago.
- **Não criar ficheiros de contexto paralelos** — nada de `pilares.md`, `ideias.md` ou equivalente. O que é da marca escreve-se no perfil.
- **Em conflito entre esta skill e o perfil, manda o perfil.**
- ⚠️ Se o negócio for **local com morada física, B2B, de ritmo diário, de comércio eletrónico, de setor regulado ou sem fins lucrativos**, ler `../social-media-manager/references/12-contextos-de-negocio.md` **antes** de gerar. Corrige pressupostos que os módulos gerais assumem e que aqui produziriam colunas inteiras inúteis.

## Passo 1. Os pilares

Se a secção 7 do perfil tiver 3 a 5 pilares com contra-âmbito, usá-los tal como estão e passar ao Passo 2.

Se faltarem ou estiverem vagos, apresentar as opções num único lote pelo meio interativo disponível.

```json
[
  {"question": "De onde saem os pilares?", "header": "Pilares", "multiSelect": false,
   "options": [
     {"label": "Escrevo-os eu", "description": "Tenho 3 a 5 pilares para te dar a seguir"},
     {"label": "Deduz dos dados", "description": "Agrupa os posts dos últimos 90 dias por tema e mostra que aglomerados já existem de facto na conta"},
     {"label": "Propõe tu", "description": "A partir das secções 1, 3 e 6 do perfil, propõe 4 pilares para eu aprovar"}
   ]}
]
```

Se a escolha for **"Deduz dos dados"**, o caminho não depende de ferramenta nenhuma: se houver exportação de conteúdo da conta, usá-la; **se não houver, pedir à pessoa que abra o perfil e liste os últimos 90 dias de publicações — data e assunto em duas palavras, uma por linha.** Agrupar por **tema**, nunca por formato. É trabalho manual de dez minutos e substitui integralmente qualquer API.

**3 a 5, nunca mais.** ◐ O porquê está no módulo 03 e não se repete aqui.

Cada pilar sai escrito com: nome · âmbito · **contra-âmbito** ("este pilar NÃO cobre…") · objetivo de negócio · peso — os campos da tabela da secção 7 do perfil.

**Teste antes de avançar:** se não conseguires listar 15 ideias por pilar sem esforço, o pilar é demasiado estreito ou não é um pilar (módulo 03). Recusar pilares vagos que não geram nada: "inspiração", "novidades", "lifestyle".

Se os pilares forem novos ou alterados, **escrevê-los na secção 7 do perfil** antes de gerar a matriz.

## Passo 2. As colunas

Colunas = formatos e ângulos. Escolher **6 a 8** adequados às plataformas da secção 4 do perfil — ◐ número de trabalho desta skill, não um dado: abaixo de 6 a matriz repete-se, acima de 8 enche-se de células fracas. Ajustável com razão escrita. Conjunto por defeito, com a definição a aplicar em cada célula:

| Coluna | O que é |
|---|---|
| **Como se faz** | Um passo-a-passo ultra-específico. Ensina a fazer uma coisa. |
| **Bastidores** | O processo real, o que ninguém vê, o que correu mal. |
| **Pergunta frequente** | Responde a uma pergunta que chega mesmo por mensagem ou ao balcão. |
| **Objeção** | Enfrenta de frente o que trava a compra — preço, prazo, dúvida. |
| **Contra a corrente** | Contraria o conselho corrente do setor, com fundamento. |
| **Comparação** | X vs Y: dois materiais, duas opções, dois momentos. |
| **Antes e depois** | Transformação concreta, com o intervalo declarado. |
| **Lista** | Erros, cuidados, escolhas, sinais — enumeráveis e guardáveis. |
| **Prova de cliente** | Caso real, com autorização escrita. Nunca sem. |

Para vídeo, estas colunas descrevem a ideia antes do rácio: confirmar a superfície ao produzir. Reels usam normalmente vertical; Shorts podem ser quadrados ou verticais (PLAT-017). TikTok está `LOOK INTO`. O âmbito destas skills é vídeo curto, não uma regra universal contra vídeo horizontal ou longo.

⚠️ **Três colunas têm travão de conformidade** (módulo 10, e módulo 12 para setores regulados):

- **Prova de cliente** e qualquer testemunho — exigem **consentimento escrito para esse fim específico**. Consentimento para uma coisa não serve para outra. Uma ideia desta coluna sai sempre com a nota `[precisa de autorização escrita]`.
- **Antes e depois** — em saúde, estética, nutrição, finanças e outros setores regulados, verificar **caso a caso junto da ordem profissional antes de produzir**. Não há regra genérica segura, e é o tipo de peça que mais se publica sem verificar. Se o setor for regulado, marcar a célula `[verificar antes de produzir]` em vez de a dar por aprovada.
- **Comparação** — comparar com um concorrente identificável é publicidade comparativa e tem regras próprias. Comparar **opções, materiais ou momentos** é seguro; comparar marcas nomeadas não sai sem decisão humana.

## Passo 3. Encher a matriz

Uma célula = **um título concreto e produzível**, não um tema. Bom: *"Porque é que um bolo de três andares precisa de encomenda com `[X dias — secção 1 do perfil]` de antecedência"*. Mau: *"Prazos"*. Repare-se no exemplo: o título é concreto, mas **o prazo fica por confirmar** — nem sequer num exemplo se escreve um número que não veio do perfil.

Regras de preenchimento:
- Cada ideia é específica **àquele pilar E àquela coluna**. Não reciclar a mesma ideia entre linhas.
- Nenhuma ideia pode violar o contra-âmbito do seu pilar.
- Nenhuma ideia pode afirmar o que a secção 6 do perfil proíbe. Preços, prazos e disponibilidade ficam `[POR CONFIRMAR]`.
- Puxar matéria-prima real: as perguntas da secção 3, as objeções, as aprendizagens da secção 11. **A fonte mais rica e mais desperdiçada são as perguntas que já chegam por mensagem, comentário, telefone e balcão.**
- Marcar cada célula com **HERO**, **HUB** ou **HELP**, escrito por extenso — as três palavras começam por H e qualquer abreviatura por inicial é ambígua. Hero: os poucos momentos grandes do ano. Hub: a série recorrente que dá razão para voltar. Help: resposta a pergunta com procura constante.

⚠️ **A maior parte da matriz tem de ser HELP e HUB**, porque são os únicos que se sustentam sem orçamento nem evento (módulo 03). Hero é, por definição, raro: se a matriz de um mês trouxer mais do que um punhado de células Hero, está a planear campanhas em vez de conteúdo sempre-ligado. Dizê-lo. ◐ **Não citar proporções** — o 70/20/10 e as outras que circulam vêm de fontes secundárias que se contradizem e não têm dados públicos por trás.

## Passo 4. Entregar

Tabela markdown, pilares em linhas, colunas em cima, **sem bloco de código** — uma grelha em monoespaçado não se lê. Cada célula: título + `[HERO]`, `[HUB]` ou `[HELP]` por extenso, mais as notas de conformidade do Passo 2 quando se apliquem.

Se a superfície suportar artefacto interativo e a grelha for grande, tabela interativa. Se houver ferramentas de ficheiro, guardar também em `Social Media/matriz-AAAA-MM-DD.md` e dizer o caminho.

Depois da tabela, e só depois:

- **As três ideias mais fortes**, com uma frase cada a dizer porquê — ligadas ao público e ao objetivo de negócio, não ao gosto.
- **Contagem por Hero/Hub/Help** e o aviso se o equilíbrio estiver errado.
- **Quantas cabem na cadência real** da secção 8 do perfil. Uma matriz de 40 ideias para quem publica duas vezes por semana é o plano de cinco meses, não do próximo. **Dizer o número.** ◑ O que os dados associam a resultado é o número de **semanas** com publicação, não o volume por semana.
- **O que fica de fora e porquê** — as ideias recusadas por contra-âmbito ou por alegação proibida.

Terminar:

> Queres que passe alguma destas ao calendário com datas, ou que escreva uma como post? Diz-me a célula por pilar + coluna.

Guardar as ideias não usadas no **banco de ideias** do projeto, com pilar, formato sugerido e origem. A ideia que não se encontra não existe. **Se não houver ferramentas de ficheiro**, entregar essas ideias na resposta, na mesma estrutura, para a pessoa colar onde já guarda as suas — a skill não fica a dever nada por não poder escrever.

**Acessibilidade.** A matriz é texto e não tem contraste nem texto alternativo a verificar. Mas cada célula que for para produção arrasta a camada de acessibilidade da peça — texto alternativo, legendas revistas, contraste mínimo de 4,5:1 — e essa camada é da responsabilidade das skills que produzem (`escrever-post`, `carrossel`, `guiao-video-curto`, `design-grafico`). Dizê-lo ao passar as ideias adiante, para não desaparecer na pressa, que é o que lhe acontece sempre.

## Regras

- **Português europeu.** Sem gerúndio de ação em curso, sem "você", sem vocabulário do Brasil.
- **3 a 5 pilares.** Sem exceções.
- **Nunca inventar preços, prazos, características, casos de cliente ou testemunhos.** Vêm do perfil ou de um humano — nem sequer nos exemplos.
- **Nunca construir a matriz a partir de listas de datas comemorativas** — o resultado é uma sucessão de ocasiões sem fio condutor. E ⚠️ a maioria das listas que circulam é de mercado brasileiro ou norte-americano: para uma marca portuguesa refazem-se com feriados e hábitos locais, pela grelha de cinco perguntas do módulo 03.
- **Não citar rácios de mistura.** 80/20, regra dos terços, 5-3-2, 4-1-1, 70/20/10 — ◐ nenhum tem estudo publicado; a demonstração está no módulo 03 e não se repete aqui. **O rácio real calibra-se pelo ciclo de decisão da secção 1 do perfil**, e os dois erros são simétricos: o feed que é só catálogo, e meses de "conteúdo de valor" sem nunca dizer o que se vende, a quanto e como se compra.
- ⬤ **Nenhuma ideia pode ter como mecânica interação artificial** — "marca três amigos", "partilha para ganhar", "comenta X para receberes". O Facebook declara a despromoção de *engagement bait* e de Páginas reincidentes; PLAT-007. O Instagram proíbe recolher artificialmente gostos, seguidores ou partilhas. A regra desta skill é não construir conteúdo sobre spam, mesmo quando as políticas diferem.
- **Passatempos e sorteios não entram na matriz como ideia solta.** Em Portugal caem no regime das modalidades afins de jogos de fortuna ou azar e podem exigir autorização da câmara municipal. Se aparecer a ideia, marcá-la `[ver módulo 10 antes de planear]` e não a dar por produzível.
- **Ideia que dependa de conteúdo gerado por IA realista** sai com a nota de que a rotulagem é obrigatória (módulo 10).
- Esta skill **não data as peças nem escreve os posts**. Datar é o calendário; escrever é `escrever-post`.
- Não resumir esta skill ao utilizador. Executá-la.
