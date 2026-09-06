---
name: escrever-post
description: "Escreve o texto de uma publicação social concreta a partir do contexto do caso — gancho, corpo, uma chamada à ação e acessibilidade. Usa para legendas e posts de texto ou imagem única. Não planeia calendários, não cria carrosséis e não escreve guiões completos de vídeo; essas tarefas têm executores próprios."
---

# Escrever post

## Gate de revisão

Antes de executar, correr `../social-media-manager/scripts/verificar_revisao.py`, resolvido relativamente a este ficheiro. Sem terminal, ler os blocos `Calendário` de `05-estado-das-plataformas.md` e `09-estado-da-vigilancia.md`. Se uma data chegou, passou ou é inválida, avisar uma vez por conversa; a primeira linha deve ser exatamente `Skill necessita de revisão`. Continuar com as limitações declaradas. O aviso não autoriza pesquisa, acesso a contas nem atualização.

## Contrato de contexto

Aplicar `../social-media-manager/references/contexto-do-caso.md`. O contexto pode chegar na mensagem, em anexos, em fontes ligadas ou em documentos com qualquer nome e formato. Neste ficheiro, «perfil» significa a fonte de contexto disponível; referências a números de secção servem apenas para o modelo opcional incluído no pacote. Não exigir esse modelo, não o copiar automaticamente e não tratar website, checkout, equipa ou ferramenta como pré-requisito. Pedir apenas a informação que muda materialmente esta tarefa.

Skill de execução. O critério — anatomia em cinco camadas, técnicas de gancho, extensão e o corte do "ver mais", motores de partilha, acessibilidade — vive em `../social-media-manager/references/04-criacao-de-conteudo.md`. **Ler esse módulo antes de escrever e não o repetir aqui.** Para sinais e limites de cada plataforma, `../social-media-manager/references/05-plataformas.md`; se a decisão usar um ID PLAT, ler o registo em `../social-media-manager/references/05-estado-das-plataformas.md`. Para a voz, a secção 5 do perfil de marca.

## Arranque imediato

Ao disparar, ir direto ao Passo 0 e ao Passo 1. Não resumir a skill, não explicar o que faz, não listar os ficheiros que vai ler, não perguntar se se avança.

## Passo 0. Contexto do caso

Localizar e ler, quando existirem, oferta, público, plataformas, voz, alegações, pilares e capacidade
de produção. Não exigir uma estrutura documental. Sem voz ou público suficientes, pedir esses dados;
se a pessoa preferir avançar, declarar que a versão é genérica. Preços, prazos, disponibilidade,
condições e nomes de produto nunca se estimam: usar `[POR CONFIRMAR]` no sítio exato.

## Passo 1. Recolher o que falta

**Perguntar num único lote pelo meio interativo disponível**, saltando o que o contexto já responde.

```json
[
  {"question": "De onde vem o conteúdo desta peça?", "header": "Matéria-prima", "multiSelect": false,
   "options": [
     {"label": "Vou colar notas", "description": "Notas, transcrição, mensagens de cliente, ideias soltas"},
     {"label": "Tenho o tema na cabeça", "description": "Escrevo o tema a seguir numa frase"},
     {"label": "Aconteceu isto hoje", "description": "Um episódio real do negócio — a matéria-prima mais forte"},
     {"label": "Sugere tu", "description": "Propõe 5 temas a partir dos pilares da secção 7 do perfil"}
   ]},
  {"question": "Onde é que isto vai sair?", "header": "Plataforma", "multiSelect": true,
   "options": [
     {"label": "Instagram — feed", "description": "Imagem única ou carrossel"},
     {"label": "Reels / Shorts", "description": "Vídeo curto, guião em duas colunas; rácio confirmado"},
     {"label": "Facebook", "description": "Página — público habitualmente mais velho e local"},
     {"label": "Histórias", "description": "Sequência de 3 a 7 cartões, canal de relação"}
   ]},
  {"question": "Que comportamento é que esta peça tem de provocar? Escolher UM.", "header": "Objetivo",
   "options": [
     {"label": "Ser guardada", "description": "Referência utilizável — pede carrossel"},
     {"label": "Ser enviada a alguém", "description": "◑ Dos sinais que mais pesam para chegar a quem não segue"},
     {"label": "Gerar mensagem", "description": "A venda passa por conversa"},
     {"label": "Chegar a quem não segue", "description": "Descoberta — escolher o formato com base na superfície e no histórico"}
   ]},
  {"question": "Que prova concreta temos para meter aqui?", "header": "Prova",
   "options": [
     {"label": "Um caso real", "description": "Uma encomenda, um cliente, um erro que aconteceu"},
     {"label": "Um número da casa", "description": "Nosso, verificável, não de blogue"},
     {"label": "Uma fotografia ou vídeo", "description": "Material que já existe"},
     {"label": "Nada ainda", "description": "Escrevo à mesma e assinalo o buraco"}
   ]}
]
```

Se a resposta for "Sugere tu": propor 5 temas, cada um com pilar + ângulo numa linha, e pedir ao utilizador para escolher um.

> ⚠️ **Uma peça, um comportamento.** Se pedirem dois objetivos, escolher o mais barato da escada de atrito do módulo 04 e dizer porquê. Tentar todos não consegue nenhum.

### Vários destinos ao mesmo tempo

**Um destino, uma peça.** Escolher três destinos não é um atalho — é triplicar o trabalho, e o trabalho tem de aparecer aqui em vez de aparecer na entrega.

- Sai **uma peça por destino**, cada uma com **gancho e chamada à ação próprios**. O mesmo texto colado em três sítios é a peça que nenhum dos três premeia.
- O plano declara **uma linha por destino** antes de se escrever, para o custo ficar visível antes do trabalho.
- ⚠️ **Destinos que não estejam na secção 4 do perfil não se produzem.** Perguntar porquê primeiro: uma plataforma que a marca não alimenta não vai dar seguimento à peça, e é assim que a regra de estar bem em duas ou três se contorna — uma peça de cada vez.
- Mais do que dois destinos: dizê-lo antes de começar e confirmar que é mesmo isso que se quer.

## Passo 2. Plano antes de escrever

Não saltar. Apresentar em seis linhas, sem enfeite:

```
Pilar:            (secção 7 do perfil)
Comportamento:    (o degrau escolhido)
Estrutura:        (do módulo 04 — declarada ANTES de escrever)
Ângulo:           (uma frase)
Prova:            (o que sustenta o corpo)
Buracos:          (o que falta confirmar com um humano)
```

A estrutura sai da tabela do módulo 04 (problema→agitação→solução, atenção→interesse→desejo→ação, antes→depois→ponte, lista, situação→complicação→resolução, afirmação→prova→consequência). Escolher pelo caso de uso da tabela, não por hábito. Se a estrutura não for óbvia, oferecer três opções, com o gancho de cada uma escrito por extenso — nunca texto de exemplo genérico.

## Passo 3. Escrever camada a camada

Pela ordem do módulo 04, cada camada revista em separado:

1. **Gancho** — escrever **5 a 10** e escolher. Cada um testado contra os três critérios: imediato, específico, verdadeiro. **Descartar tudo o que falhe no terceiro**, por melhor que seja nos outros dois. Para variações a sério, chamar `gerar-ganchos`.
2. **Promessa** — o que quem lê leva daqui, explícito na segunda linha ou nos segundos 3-8 do vídeo.
3. **Corpo** — entrega a promessa, com a prova do Passo 1. Sem prova, o corpo é opinião.
4. **Fecho e chamada à ação** — **uma só**, do degrau escolhido no Passo 1, e nunca mais cara do que aquilo que a peça acabou de dar.
5. **Acessibilidade** — a lista de verificação do módulo 04, entregue sempre, mesmo que não peçam.

**Extensão:** a mínima que cumpre a promessa do gancho, com a viragem do texto imediatamente antes do corte do "ver mais". A resposta **muda com a superfície** e os dados por plataforma estão no módulo 04, secção "Extensão e o corte do ver mais" — ler lá antes de decidir, não decorar daqui. **Não copiar contagens de caracteres de blogues: não têm amostra.**

**Vídeo curto, com o rácio confirmado para a superfície.** Guião em duas colunas — `o que se diz | o que se vê e lê`. A coluna direita garante que a mensagem essencial também existe visualmente. Os blocos de tempo e o ritmo estão no módulo 04, secção "Vídeo curto". Shorts podem ser quadrados ou verticais (PLAT-017); TikTok está `LOOK INTO` e não fornece regras atuais.

> Para um guião completo, com engenharia inversa de referência e blocos de tempo desenvolvidos, **chamar `guiao-video-curto`.** Aqui escreve-se a peça; ali produz-se o guião.

**Se o Passo 1 escolheu mais do que uma plataforma**, cada peça é **readaptada e reexportada** ao formato de destino — nunca o mesmo ficheiro atirado para todo o lado. Reexportar sem marca de água, com boa resolução e leitura nativa é a prática segura. A lista de despromoção publicada pelo Instagram em 2023 está registada como histórica em PLAT-011 do módulo 05; não a usar para diagnosticar o alcance de uma peça atual.

## Passo 4. Entregar

Texto final **em bloco de código**, com as quebras de linha exatamente como devem sair. Nada antes do bloco. **Se o Passo 1 escolheu mais do que um destino, um bloco por destino**, cada um identificado e com o seu próprio gancho e a sua própria chamada à ação — nunca um bloco só a servir todos.

Depois do bloco, e só depois:

- **Visual** — o que fotografar ou filmar, em linguagem de execução (não "uma imagem apelativa"). Para vídeo, a tabela de duas colunas.
- **Acessibilidade** — a lista completa está no módulo 04. Nunca sai sem: texto alternativo escrito por extenso para cada imagem **e para cada diapositivo** do carrossel; legendas revistas à mão (nomes, números e preços saem errados nas automáticas); contraste ⬤ mínimo 4,5:1 para texto normal e 3:1 para texto grande (18pt normal ou 14pt negrito), norma WCAG 2.2 AA — são limiares, 4,499:1 não cumpre; **informação essencial nunca transmitida só por cor**; se a imagem carrega um preço, uma data ou um número, esse dado também está na legenda visível; **texto e legendas fora das zonas da interface** (nome de utilizador, botões laterais, barra de progresso), verificado na aplicação real e não só no editor; hashtags em CamelCase; emojis no fim, sem sequências repetidas.
- **Porquê** — 2 a 3 frases sobre o gancho e a estrutura escolhidos, ligadas ao perfil e ao módulo 04. Não mais.
- **Buracos** — o que ficou `[POR CONFIRMAR]` e quem confirma.

## Passo 5. Iterar

> Como é que isto te soa? Diz-me o que mudar, ou diz "está bom" e eu guardo a versão final.

Máximo de três voltas. Se ao fim de três ainda não servir, o problema é do perfil e não do texto — dizê-lo e propor rever a secção 5.

Ao "está bom": guardar apenas se houver destino canónico, meio de escrita e autorização. Caso
contrário, entregar a versão final copiável. Devolver qualquer aprendizagem nova à fonte canónica
de métricas e aprendizagem, sem inventar caminho.

**Dizer o que se segue**, conforme o que a peça ainda precisa — sem o fazer sem pedirem:

| Falta | Skill |
|---|---|
| A peça visual | `design-grafico` |
| Vários cartões em vez de um | `carrossel` |
| O guião de vídeo desenvolvido | `guiao-video-curto` · capa: `capa-de-video` |
| Mais variações da primeira linha | `gerar-ganchos` |
| A informação que não coube na legenda | `comentario-fixado` |
| Uma pontuação contra o histórico da conta | `avaliar-post` |

## Regras

- **Português europeu.** Sem gerúndio de ação em curso, sem "você" como tratamento, sem vocabulário do Brasil.
- ⚠️ **Identificar conteúdo comercial.** ⬤ `#PUB` no início quando há dinheiro ou benefício de terceiro — é o que a lei exige. ◐ **"conteúdo promocional"** quando é a própria marca a promover produto, preço, campanha ou desconto — é política interna deste sistema, não redação imposta. **Não trocar as duas:** carimbar `#PUB` numa peça da própria marca afirma uma relação comercial que não existe e dilui a etiqueta onde ela é obrigatória. Se a peça não promove nada, não leva nada. Tabela dos três casos em `../social-media-manager/references/10-risco-crise-e-conformidade.md`.
- **Nunca inventar preços, prazos, disponibilidade, características de produto ou depoimentos.** Vêm do perfil ou de um humano.
- **Nunca citar um número sem fonte e sem amostra.** Se o perfil não o tiver e o módulo 11 não o tiver, o número não entra.
- **Uma chamada à ação por peça.**
- ⚠️ **Sem isco de interação.** ⬤ No Facebook, pedidos do tipo "comenta X que eu envio-te o link" entram no *engagement bait* despromovido, incluindo Páginas reincidentes; PLAT-007. No Instagram, a regra oficial proíbe recolher artificialmente interação. Uma chamada à ação específica e útil é diferente de interação como fim.
- **Sem hashtags** a menos que o perfil as use. Investir o esforço no gancho. Se entrarem no Instagram, preparar no máximo cinco: o anúncio oficial de 18/12/2025 descreveu um rollout gradual, não uma entrada em vigor global. Confirmar o limite no compositor da conta; PLAT-003. Usá-las como etiqueta de contexto, sem promessa de alcance.
- ⚠️ **Música em conta de empresa.** Se a peça for vídeo e levar áudio, **não escolher a faixa aqui**. ⬤ A biblioteca musical licenciada da Meta destina-se a uso pessoal e não comercial, e certas contas empresariais têm acesso restrito; a Sound Collection é a via comercial para Facebook e Instagram, não uma licença multiplataforma. TikTok está `LOOK INTO`. Escrever `[ÁUDIO POR VERIFICAR NA PRÓPRIA CONTA]` no guião — módulo 10.
- ⚠️ **Conteúdo gerado por IA.** Aplicar o rótulo exigido pela plataforma. Desde 2 de agosto de 2026, o artigo 50.º do Regulamento de IA obriga quem publica profissionalmente a identificar *deepfakes* e certos textos de interesse público; ◐ na dúvida, este sistema identifica também conteúdo realista ou materialmente alterado por IA. Fotografia de produto que não corresponde ao produto real é publicidade enganosa — módulo 10.
- **Depoimentos, fotografias de clientes e capturas de conversa** exigem consentimento escrito **para aquele fim específico**, com os dados pessoais tapados. Uma marcação não transfere licença. Se não houver autorização registada, a prova não entra na peça.
- **Sem travessão longo** nas peças, se o perfil o disser. A restrição é da voz, não desta skill.
- **Vídeo curto usa o rácio confirmado para a superfície.** Reels usam normalmente vertical; Shorts podem ser quadrados ou verticais (PLAT-017). TikTok está `LOOK INTO`. Se pedirem vídeo longo, encaminhar para outro fluxo sem alegar que as plataformas não o distribuem.
- Afirmações sujeitas a regulação (saúde, alimentar, finanças) e conteúdo de terceiros **não saem sem humano** — módulo 10 e módulo 06.
- Não resumir esta skill ao utilizador. Executá-la.
