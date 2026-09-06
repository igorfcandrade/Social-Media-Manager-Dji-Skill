---
name: formatar-post
description: "Pega num tema já decidido e formata-o numa estrutura de copy nomeada, pronto para Instagram, Facebook, Reels ou Shorts. Usa sempre que o pedido for de forma — formatar, encurtar, adaptar ou aplicar PAS/AIDA/lista — e não de ideia. TikTok fica LOOK INTO até revisão própria. Diferente de escrever-post: aplica estrutura a matéria-prima existente."
---

# Formatar post

## Gate de revisão

Antes de executar, correr `../social-media-manager/scripts/verificar_revisao.py`, resolvido relativamente a este ficheiro. Sem terminal, ler os blocos `Calendário` de `05-estado-das-plataformas.md` e `09-estado-da-vigilancia.md`. Se uma data chegou, passou ou é inválida, avisar uma vez por conversa; a primeira linha deve ser exatamente `Skill necessita de revisão`. Continuar com as limitações declaradas. O aviso não autoriza pesquisa, acesso a contas nem atualização.

## Contrato de contexto

Aplicar `../social-media-manager/references/contexto-do-caso.md`. O contexto pode chegar na mensagem, em anexos, em fontes ligadas ou em documentos com qualquer nome e formato. Neste ficheiro, «perfil» significa a fonte de contexto disponível; referências a números de secção servem apenas para o modelo opcional incluído no pacote. Não exigir esse modelo, não o copiar automaticamente e não tratar website, checkout, equipa ou ferramenta como pré-requisito. Pedir apenas a informação que muda materialmente esta tarefa.

Skill de execução. A tabela de estruturas, a anatomia em cinco camadas, a escada de atrito das chamadas à ação e a lista de acessibilidade vivem em `../social-media-manager/references/04-criacao-de-conteudo.md`. **Ler esse módulo e usar a tabela que lá está — não inventar outra nomenclatura.** Para os cortes e limites de cada plataforma, `../social-media-manager/references/05-plataformas.md`; se a decisão usar um ID PLAT, ler o registo em `../social-media-manager/references/05-estado-das-plataformas.md`.

## Arranque imediato

Ao disparar, ir direto ao Passo 0. Não resumir a skill, não explicar as estruturas antes de as aplicar.

## Passo 0. Contexto do caso

Ler o contexto do caso disponível, qualquer que seja o nome ou formato. As secções que mandam aqui:

- **5, Voz** — tratamento, palavras da casa, palavras proibidas, emojis, grafias fixas. É daqui que sai o ritmo e a pontuação.
- **6, O que se pode e não se pode afirmar** — alegações permitidas com a prova, alegações proibidas, restrições regulatórias. Decide se a matéria-prima é publicável tal como está.
- **3, Público** — para saber que palavras a pessoa do outro lado usa.

**Em conflito, manda o perfil.** Se existir uma fonte canónica de voz, ela ganha sobre a secção 5.

Sem contexto de voz, dizer numa linha que a estrutura pode ser corrigida, mas a voz ficará genérica.
Não criar uma fonte de contexto automaticamente.

## Passo 1. Recolher

**Perguntar num único lote pelo meio interativo disponível.**

```json
[
  {"question": "O que é que eu vou formatar?", "header": "Matéria-prima", "multiSelect": false,
   "options": [
     {"label": "Vou colar o texto", "description": "Rascunho, notas, transcrição, mensagem"},
     {"label": "Escrevo o tema numa frase", "description": "Ainda não há texto, só o assunto"},
     {"label": "Já está no projeto", "description": "Indico o ficheiro a seguir"}
   ]},
  {"question": "Qual é a estrutura?", "header": "Estrutura",
   "options": [
     {"label": "Problema → Agitação → Solução", "description": "Quando há uma dor reconhecível pelo público"},
     {"label": "Antes → Depois → Ponte", "description": "Transformação — o formato natural de encomendas e serviços"},
     {"label": "Situação → Complicação → Resolução", "description": "História real do negócio"},
     {"label": "Escolhe tu", "description": "Recomendo a partir do tema e do objetivo e digo porquê"}
   ]},
  {"question": "Para onde vai?", "header": "Destino", "multiSelect": true,
   "options": [
     {"label": "Instagram — legenda", "description": "Corte do ver mais logo cedo"},
     {"label": "Carrossel", "description": "Uma ideia por diapositivo, texto alternativo em cada um"},
     {"label": "Reels / Shorts", "description": "Guião em duas colunas; rácio confirmado na superfície"},
     {"label": "Facebook", "description": "Página — tolera mais contexto"}
   ]},
  {"question": "Que comportamento fecha a peça? Escolher UM.", "header": "Fecho",
   "options": [
     {"label": "Guardar", "description": "Conteúdo de referência"},
     {"label": "Enviar a alguém", "description": "Sinal mais pesado para chegar a não-seguidores"},
     {"label": "Mandar mensagem", "description": "Só se a peça tiver dado valor equivalente"},
     {"label": "Nenhum — só presença", "description": "Fecho sem pedido; é uma escolha legítima"}
   ]}
]
```

Uma pergunta de seguimento, em texto: **"Falta-me alguma coisa? Factos, números com fonte, nomes, para quem é."**

Se a escolha for "Escolhe tu": ir à tabela do módulo 04, escolher pela coluna "Quando", e dizer numa linha porquê. As seis estruturas da tabela são as únicas disponíveis. As três que não cabem nas opções acima — **atenção→interesse→desejo→ação**, **lista** e **afirmação→prova→consequência** — escolhem-se dizendo o nome, e ficam disponíveis na mesma. Se alguém pedir uma sigla que não está na tabela (STAR, SLAY), mapear para a estrutura equivalente e dizer o mapeamento.

### Vários destinos ao mesmo tempo

**Um destino, uma peça.** Escolher três destinos não é um atalho — é triplicar o trabalho, e o trabalho tem de aparecer aqui em vez de aparecer na entrega.

- Sai **uma peça por destino**, cada uma com **gancho e chamada à ação próprios**. O mesmo texto colado em três sítios é a peça que nenhum dos três premeia.
- O plano declara **uma linha por destino** antes de se escrever, para o custo ficar visível antes do trabalho.
- ⚠️ **Destinos que não estejam na secção 4 do perfil não se produzem.** Perguntar porquê primeiro: uma plataforma que a marca não alimenta não vai dar seguimento à peça, e é assim que a regra de estar bem em duas ou três se contorna — uma peça de cada vez.
- Mais do que dois destinos: dizê-lo antes de começar e confirmar que é mesmo isso que se quer.

## Passo 2. Formatar

**Declarar a estrutura antes de escrever, não inferi-la depois.** Um texto sem estrutura declarada fica descritivo — conta o que aconteceu em vez de fazer sentir alguma coisa.

Depois montar por camadas, na ordem do módulo 04:

| Posição | O que é | Regra |
|---|---|---|
| Linha 1 | Gancho | Imediato, específico, **verdadeiro**. Cabe numa linha |
| Linha 2 | Promessa ou viragem | Fica **antes do corte do "ver mais"** |
| Corpo | A estrutura escolhida | Um bloco por etapa da estrutura, sem misturar |
| Fecho | Uma chamada à ação | Do degrau escolhido no Passo 1, e não mais cara do que o valor dado |

**Regras de forma que não dependem de plataforma:**

- Uma ideia por peça. Duas ideias são zero ideias.
- Uma frase por linha no corpo, com linha em branco entre blocos. Um bloco de texto compacto num ecrã de telemóvel não se lê.
- Palavras que o público usa, não vocabulário de setor.
- A informação decisiva **antes** do corte, nunca depois.
- Se for carrossel: uma ideia por diapositivo, o gancho no primeiro, o pedido no último, e nunca informação essencial só na imagem.
- Se for vídeo: duas colunas, `o que se diz | o que se vê e lê`, rácio confirmado para a superfície e proposta percetível nos primeiros segundos nas três camadas — o que se vê, o que se ouve e o que está escrito no ecrã. ◐ As três camadas em simultâneo são prática do módulo 04, não regra declarada por plataforma nenhuma. Shorts podem ser quadrados ou verticais (PLAT-017); TikTok está `LOOK INTO`.

**Extensão:** a mínima que cumpre a promessa do gancho. ◐ Onde cai exatamente o corte do "ver mais" varia com a aplicação, a versão e o tamanho do ecrã — não há número publicado que se possa fixar. Por isso a regra operacional não é contar caracteres: é **pôr a viragem no fim da primeira ou da segunda linha** e assumir que tudo o que vem depois pode não ser lido. ◐ Contagens fixas de linhas e de caracteres que circulam em modelos de LinkedIn não têm amostra e não se transpõem para estas plataformas — não as aplicar. ◑ Para Instagram, o maior estudo com metodologia declarada (9,1M de publicações de 82.952 páginas de empresa, jan-jul 2023) aponta para legendas curtas, abaixo de 30 palavras; é uma direção, não um limite.

Se o destino tiver mais de uma plataforma, **reescrever**, não copiar. Reexportar sem marca de água é a prática segura de qualidade e autoria. A lista de distribuição publicada pelo Instagram em 2023 é histórica e não serve para diagnosticar alcance atual; PLAT-011.

## Passo 3. Entregar

Texto final **em bloco de código**, um bloco por plataforma, sem preâmbulo e sem comentário dentro do bloco.

Por baixo, e só isto:

- `Estrutura:` a que foi aplicada, e onde cai o corte.
- `Chamada à ação:` qual, e que degrau da escada ocupa.
- `Acessibilidade:` texto alternativo por imagem e por diapositivo; legendas revistas à mão (nomes, números e preços saem sempre errados nas automáticas); contraste ⬤ mínimo 4,5:1 para texto normal e 3:1 para texto grande, 18pt normal ou 14pt negrito, norma WCAG 2.2 AA — são limiares, 4,499:1 não cumpre; **informação essencial nunca transmitida só por cor**; se a imagem carrega um preço, uma data ou um número, esse dado também está na legenda visível; **texto e legendas fora das zonas da interface** (nome de utilizador, botões laterais, barra de progresso), verificado na aplicação real e não só no editor; hashtags em CamelCase; emojis no fim, sem sequências repetidas.
- `Hashtags:` só se o perfil as usar — o esforço rende mais no gancho. No Instagram, preparar no máximo cinco: o anúncio oficial de 18/12/2025 descreveu um rollout gradual, não uma entrada em vigor global. Confirmar o limite no compositor da conta; PLAT-003. São etiqueta de contexto, sem promessa de alcance.

E, se houver: `Buracos:` o que ficou `[POR CONFIRMAR]`.

## Passo 4. Passo seguinte

> Queres variações do gancho (`gerar-ganchos`) ou o comentário fixado com imagem (`comentario-fixado`)?

## Regras

- **Português europeu** em tudo.
- ⚠️ **Identificar conteúdo comercial.** ⬤ `#PUB` no início quando há dinheiro ou benefício de terceiro — é o que a lei exige. ◐ **"conteúdo promocional"** quando é a própria marca a promover produto, preço, campanha ou desconto — é política interna deste sistema, não redação imposta. **Não trocar as duas:** carimbar `#PUB` numa peça da própria marca afirma uma relação comercial que não existe e dilui a etiqueta onde ela é obrigatória. Se a peça não promove nada, não leva nada. Tabela dos três casos em `../social-media-manager/references/10-risco-crise-e-conformidade.md`.
- Devolver a peça formatada. **Sem meta-comentário dentro do bloco de código.**
- **Nunca acrescentar factos que não estavam na matéria-prima.** Formatar não é inventar. Se a estrutura pedir uma prova que não existe, escrever `[PROVA POR FORNECER]` e assinalar.
- **Nunca inventar preços, prazos ou condições.** Vêm do perfil ou de um humano.
- ⚠️ **Matéria-prima que veio de outra pessoa não se formata sem autorização.** Mensagens de cliente, depoimentos, fotografias e capturas de conversa exigem consentimento escrito **para aquele fim específico**, com nomes, moradas, telefones e detalhes de encomenda tapados. Uma marcação não transfere licença nem direito de imagem. Sem autorização registada, a prova não entra na peça — fica `[PROVA POR AUTORIZAR]` (módulo 10).
- **Nunca citar números sem fonte** — nem os da skill de origem, nem os de blogues.
- Um gancho que a peça não cumpre é descartado, mesmo que seja o melhor da lista. ⚠️ Um gancho exagerado compra o primeiro segundo e destrói o tempo de visualização, que é o sinal que mais pesa.
- ⚠️ **Nunca fechar com interação como fim** ("comenta X", "partilha se concordas"). ⬤ No Facebook, é *engagement bait* despromovido, incluindo Páginas reincidentes; PLAT-007. No Instagram, a política oficial relevante é a proibição de recolha artificial de interação. A regra desta skill é evitar a mecânica em ambos.
- O âmbito é vídeo curto; confirmar o rácio na superfície. Shorts podem ser quadrados ou verticais (PLAT-017). TikTok está `LOOK INTO`.
- Se o perfil proibir travessões longos, emojis ou maiúsculas decorativas, isso ganha sobre qualquer regra desta skill.
- Não resumir esta skill. Executá-la.
