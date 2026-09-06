---
name: gerar-ganchos
description: "Gera 8 variações de gancho para Instagram, Reels, Facebook ou Shorts, com técnica nomeada e, em vídeo, nas camadas visual, sonora e escrita. Testa imediato, específico e verdadeiro. Usa sempre que pedirem ganchos, hooks, primeira linha, título ou correção dos primeiros segundos. TikTok fica LOOK INTO até revisão própria."
---

# Gerar ganchos

## Gate de revisão

Antes de executar, correr `../social-media-manager/scripts/verificar_revisao.py`, resolvido relativamente a este ficheiro. Sem terminal, ler os blocos `Calendário` de `05-estado-das-plataformas.md` e `09-estado-da-vigilancia.md`. Se uma data chegou, passou ou é inválida, avisar uma vez por conversa; a primeira linha deve ser exatamente `Skill necessita de revisão`. Continuar com as limitações declaradas. O aviso não autoriza pesquisa, acesso a contas nem atualização.

## Contrato de contexto

Aplicar `../social-media-manager/references/contexto-do-caso.md`. O contexto pode chegar na mensagem, em anexos, em fontes ligadas ou em documentos com qualquer nome e formato. Neste ficheiro, «perfil» significa a fonte de contexto disponível; referências a números de secção servem apenas para o modelo opcional incluído no pacote. Não exigir esse modelo, não o copiar automaticamente e não tratar website, checkout, equipa ou ferramenta como pré-requisito. Pedir apenas a informação que muda materialmente esta tarefa.

Skill de execução. A biblioteca de técnicas, as três camadas e os três critérios de teste vivem em `../social-media-manager/references/04-criacao-de-conteudo.md`. **Ler esse módulo e usar as técnicas que lá estão.** Para o que cada plataforma declara premiar nos primeiros segundos, `../social-media-manager/references/05-plataformas.md`.

## O conflito com a prática do isco, resolvido

A prática corrente ensina a escrever ganchos curtos construídos sobre "princípios de *clickbait*": tensão, lacuna de curiosidade, riscos inflacionados, números impressionantes. **Esta skill não faz isso, e a razão é mecânica e não moral.**

◐ Um gancho precisa de tornar a proposta percetível cedo e de ser cumprido pelo corpo. Os sinais e pesos concretos variam por superfície; TikTok está `LOOK INTO`, portanto esta skill não lhe atribui regras atuais de distribuição.

Um gancho que promete mais do que o corpo entrega **compra o primeiro segundo e perde os dez seguintes**. Otimiza a métrica visível — a paragem — e é castigado pela métrica que decide a distribuição: o tempo de visualização e o reenvio. ◐ Numa conta pequena o custo é plausivelmente maior, porque a mesma pessoa aprende a passar à frente da conta inteira — é mecanismo defensável, não um efeito medido.

**Consequência operacional, sem exceções:** todo o gancho é testado contra os três critérios do módulo 04 — **imediato**, **específico**, **verdadeiro** — e **tudo o que falhe no terceiro é descartado, por muito bom que seja nos outros dois**. Não se entrega um gancho que a peça não cumpre, nem sequer marcado como opção. A tensão faz-se com o que é mesmo verdade: um facto concreto do negócio é quase sempre mais interessante do que uma promessa inflacionada, e tem a vantagem de sobreviver ao corpo.

> Os números de retenção associados a estas técnicas que circulam em blogues não têm estudo público. Usar as técnicas, ignorar as percentagens.

## Arranque imediato

Se o tema já vier na mensagem, usá-lo e saltar para o Passo 2 — mas **o formato e a régua nunca se saltam**, porque o Passo 3 e o Passo 4 dependem deles. Se vierem implícitos no material (um guião é Reels, um post colado traz a promessa no corpo), deduzi-los e **escrever a dedução em cima do bloco**, para poder ser corrigida. Se não der para deduzir, perguntar só o que falta. Não resumir a skill, não explicar o que é um bom gancho antes de os escrever.

## Passo 1. Tema e o que é verdade

Ler o perfil de marca do projeto (o contexto do caso disponível na mensagem, anexos, fontes ligadas ou documentos do projeto):

- **secção 5, Voz** — tratamento, palavras da casa, palavras proibidas, emojis;
- **secção 6, O que se pode e não se pode afirmar** — alegações permitidas com a prova que as sustenta, alegações proibidas, restrições regulatórias do setor. **É a secção que decide se um gancho é publicável**, e a que mais se salta;
- **secção 7, Pilares** — âmbito e contra-âmbito.

Sem voz disponível, avançar apenas se a pessoa aceitar uma versão genérica e dizê-lo numa linha.
Não criar contexto automaticamente nem inventar factos para tapar a falta.

**Em conflito entre o perfil e esta skill, manda o perfil.**

Se faltar o tema, pedir as três escolhas num único lote pelo meio interativo disponível.

```json
[
  {"question": "Sobre o que são os ganchos?", "header": "Tema", "multiSelect": false,
   "options": [
     {"label": "Escrevo o tema", "description": "Uma frase a seguir"},
     {"label": "Colo o post inteiro", "description": "Já há corpo — os ganchos têm de o cumprir"},
     {"label": "Aconteceu isto", "description": "Um episódio real, a matéria-prima mais forte"}
   ]},
  {"question": "Para que formato?", "header": "Formato",
   "options": [
     {"label": "Reels / Shorts", "description": "Primeiros segundos, três camadas; formato confirmado na superfície"},
     {"label": "Legenda de Instagram", "description": "Primeira linha, antes do corte do ver mais"},
     {"label": "Capa de carrossel", "description": "Texto no primeiro diapositivo"},
     {"label": "Facebook", "description": "Primeira linha da publicação"}
   ]},
  {"question": "O que é que o corpo cumpre mesmo?", "header": "Promessa",
   "options": [
     {"label": "Ensina a fazer algo", "description": "Valor prático"},
     {"label": "Conta o que correu mal", "description": "Erro real, com o custo"},
     {"label": "Mostra um resultado", "description": "Antes e depois com prova visual"},
     {"label": "Desmonta uma ideia feita", "description": "Contrário ao senso comum, e defensável"}
   ]}
]
```

A resposta a esta última é a **régua**. Nenhum gancho entregue pode prometer mais do que ela.

## Passo 2. Escrever 8 variações

Uma técnica diferente por variação, da lista do módulo 04: lacuna de curiosidade · quebra de padrão · afirmação contrária ao senso comum · aviso de erro ("perdi X porque fiz Y") · lista numerada com âmbito fechado · *cold open* (mostrar o resultado antes do processo) · pergunta de auto-identificação · prova visual e antes-e-depois · âmbito temporal ("como fiz X em Y tempo").

Cada gancho é escrito **nas três camadas**, porque é o erro mais comum ter gancho só na voz e ecrã sem informação — e aí perde-se toda a gente que está em silêncio.

- **Vê** — o primeiro plano, em linguagem de execução.
- **Ouve** — a frase dita, curta o suficiente para caber em 3 segundos.
- **Lê** — o texto no ecrã. Não é a transcrição da frase dita: acrescenta ou concretiza.

Para legenda ou capa de carrossel, a camada "vê" é a imagem e a camada "lê" é o texto — as duas continuam obrigatórias.

**A camada "lê" é saída visual, e leva a acessibilidade com ela** (`04-criacao-de-conteudo.md`): ⬤ contraste mínimo de **4,5:1** para texto normal e **3:1** para texto grande (18pt normal, 14pt negrito), norma WCAG 2.2 AA — 4,499:1 não cumpre; e o texto fica **fora das zonas da interface** (nome de utilizador, botões laterais, barra de progresso), verificado na aplicação real. Um gancho escrito a branco fino sobre fotografia clara não existe ao sol.

**Preferências de escrita:** algarismos em vez de números por extenso · nomear coisas concretas em vez de categorias · sem enchimento · sem pergunta retórica que não se responde a seguir. Cada palavra tem de justificar o lugar.

## Passo 3. Testar e cortar

Para cada um dos 8, três marcas:

| Critério | Passa quando |
|---|---|
| **Imediato** ◐ | Cabe em cerca de 3 segundos ou numa linha, sem preparação |
| **Específico** | Nomeia algo concreto — não uma categoria, não um adjetivo |
| **Verdadeiro** | O corpo cumpre-o, tal como está escrito |

**Descartar e substituir tudo o que falhe em "verdadeiro".** Entregar 8 aprovados, não 8 gerados. Se para chegar a 8 verdadeiros for preciso escrever 14, escrevem-se 14 — a qualidade de um gancho vem de escolher entre muitos, e essa é exatamente a parte do trabalho que é barata para a máquina e cara para uma pessoa.

Se o tema não der 8 ganchos verdadeiros, entregar os que der e dizer qual é o facto que falta para desbloquear os outros.

## Passo 4. Formato de saída

```
GANCHOS — [tema] · [formato]
Régua: o corpo cumpre [promessa do Passo 1]

1. [técnica]
   Vê:    ...
   Ouve:  ...
   Lê:    ...
   ✓ imediato · ✓ específico · ✓ verdadeiro

2. [técnica]
   ...
```

Depois do bloco, duas linhas: **qual recomendo e porquê** (uma frase, ligada ao objetivo da peça), e **quais descartei por falharem em "verdadeiro"**, com a promessa que cada um fazia a mais. Esta segunda linha é a parte mais útil da entrega e não se omite.

## Passo 5. Passo seguinte

> Queres que eu construa um destes numa peça inteira? Diz o número e eu chamo `formatar-post`.

## Regras

- **Português europeu** em tudo.
- **Um gancho que a peça não cumpre nunca é entregue**, nem como alternativa, nem com aviso. Esta é a regra que substitui o "clickbait" da prática corrente.
- **Nunca inventar números, resultados, poupanças, prazos ou casos de cliente** para tornar um gancho mais forte. Vêm do perfil ou de um humano. Um número inventado num gancho é publicidade enganosa, não estilo.
- Nomes de terceiros só quando a relação é real e verificável. "Roubar autoridade" com uma marca com que não se trabalhou é falso. Uma frase de cliente só entra num gancho **com consentimento escrito para esse fim** (`10-risco-crise-e-conformidade.md`).
- **Nada de interação como fim no gancho.** ⬤ No Facebook, "marca três amigos", "partilha para ganhar" e afins entram no *engagement bait* despromovido, incluindo Páginas reincidentes; PLAT-007. No Instagram, a regra oficial proíbe recolher artificialmente interação. Uma pergunta de auto-identificação a que o corpo responde é legítima.
- **Setor regulado** — saúde, finanças, alimentar, imobiliário, jurídico, álcool, jogo, produtos para crianças: aqui **o gancho mais eficaz pode ser simplesmente ilegal**. Trabalhar dentro da lista de alegações permitidas da secção 6 do perfil e marcar para validação humana qualquer gancho que faça uma alegação nova.
- Se a camada "vê" for uma imagem realista gerada ou materialmente alterada por IA, anotar a verificação do rótulo da plataforma e do artigo 50.º do AI Act e passar para as skills visuais. A lei cobre *deepfakes* e certos textos de interesse público; a política interna pode ser mais ampla. Variantes de gancho apenas em texto comercial corrente não são automaticamente abrangidas.
- Sem enchimento, sem ressalvas defensivas, sem "neste post vou falar sobre". ⚠️ Enterrar o gancho gasta os únicos segundos que decidem tudo.
- As percentagens de retenção que circulam por técnica **não têm estudo público** — não repetir nenhuma.
- Se o perfil proibir emojis, maiúsculas decorativas ou travessões, isso ganha.
- Não resumir esta skill. Executá-la.
