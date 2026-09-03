---
name: construir-voz
description: "Extrai a voz e o público de uma marca a partir de textos reais que ela já escreveu, mais uma entrevista curta, e escreve o resultado nas secções 3 (Público) e 5 (Voz) do perfil de marca do projeto. Usa esta skill SEMPRE que o trabalho depender de saber como a marca soa e ainda não houver perfil preenchido — e também quando o pedido for vago (ex.: \"aprende a minha voz\", \"como é que devo escrever?\", \"quero que soe a mim\", \"define o tom da marca\", \"o texto não soa a nós\", \"monta o meu sistema de conteúdo\", \"vamos começar as redes do zero\", \"treina nos meus textos\", \"tenho aqui uns posts antigos, vê o estilo\"). Dispara também quando alguém colar um punhado de textos antigos no início de um projeto sem dizer para que são. Não cria ficheiros de voz paralelos: escreve no perfil."
---

# Construir voz

## Gate de revisão

Antes de executar, correr `../social-media-manager/scripts/verificar_revisao.py`, resolvido relativamente a este ficheiro. Sem terminal, ler os blocos `Calendário` de `05-estado-das-plataformas.md` e `09-estado-da-vigilancia.md`. Se uma data chegou, passou ou é inválida, avisar uma vez por conversa; a primeira linha deve ser exatamente `Skill necessita de revisão`. Continuar com as limitações declaradas. O aviso não autoriza pesquisa, acesso a contas nem atualização.

Skill de execução. O julgamento sobre o que é uma boa voz vive em `../social-media-manager/references/02-voz-e-mensagem.md` — ler esse módulo antes de começar e não repetir aqui o que ele já diz.

## Arranque imediato

No momento em que esta skill é carregada ou disparada, executar o Passo 0 e depois o Passo 1. A tua próxima mensagem é trabalho, não descrição de trabalho.

**Não fazer:** resumir a skill · explicar que ficheiros vai produzir · perguntar se o utilizador quer avançar · confirmar a instalação · oferecer opções do tipo "queres que corra isto agora?".

## Passo 0. Encontrar (ou criar) o perfil de marca

1. Procurar no projeto: `PERFIL-SOCIAL.md`, `MARCA.md`, `MEMORY.md`, `CLAUDE.md`, pasta `Social Media/`.
2. **Se existir**, ler as secções 1, 3, 5 e 6 antes de perguntar seja o que for. Não voltar a perguntar o que já lá está preenchido — dizer ao utilizador o que foi aproveitado.
3. **Se não existir**, copiar `../social-media-manager/assets/PERFIL-MARCA-modelo.md` para `PERFIL-SOCIAL.md` na raiz do projeto e dizê-lo numa linha. Esta skill preenche as secções **3 (Público)** e **5 (Voz)**; as restantes ficam `POR DEFINIR`.
4. Se o projeto já tiver uma skill própria de voz, **ela ganha**. Perguntar antes de escrever por cima.
5. Se as secções 3 ou 5 já estiverem preenchidas (e não `POR DEFINIR`), **não escrever por cima sem perguntar**. Mostrar o que lá está e perguntar se se refaz, se se acrescenta, ou se se para aqui.

## Passo 1. Entrevista

**Caminho preferido:** a ferramenta **AskUserQuestion**, que apresenta as opções para o utilizador escolher em vez de as escrever. O limite de perguntas por chamada é da ferramenta, não desta skill — se couberem quatro, são duas chamadas; se couberem menos, mais chamadas.

**Caminho manual, se a ferramenta não estiver disponível** (e este caminho tem de chegar ao fim sozinho): fazer as mesmas perguntas em conversa, numeradas, **um lote de cada vez**, com as opções escritas como lista e a indicação de que se pode responder pelo número ou por palavras próprias. O conteúdo das perguntas é o mesmo; muda só a forma de as apresentar. Nada nesta skill depende de a ferramenta existir.

### Lote 1 (a tua primeira ação, sem texto antes)

```json
[
  {"question": "Quem fala nas redes desta marca?", "header": "Quem fala",
   "options": [
     {"label": "Uma pessoa concreta", "description": "Assina com nome próprio e aparece"},
     {"label": "A marca", "description": "Fala no singular, mas sem pessoa identificada"},
     {"label": "A equipa", "description": "Nós, com várias mãos a escrever"},
     {"label": "Depende do canal", "description": "Pessoa nuns sítios, marca noutros"}
   ]},
  {"question": "Para quem se escreve, em comportamento e não em demografia?", "header": "Público",
   "options": [
     {"label": "Cliente final local", "description": "Compra perto de casa, decide depressa"},
     {"label": "Cliente por encomenda", "description": "Planeia com semanas ou meses"},
     {"label": "Outra empresa", "description": "Decide em grupo, com orçamento"},
     {"label": "Escrevo eu", "description": "Vou descrever à mão"}
   ]},
  {"question": "Que tratamento se usa com quem lê?", "header": "Tratamento",
   "options": [
     {"label": "Informal (tu)", "description": "Próximo, direto"},
     {"label": "Formal (o cliente, 3.ª pessoa)", "description": "Distância cortês, sem interpelar por tu"},
     {"label": "Impessoal", "description": "Evita interpelar diretamente"},
     {"label": "Ainda não decidido", "description": "Quero decidir com base nos textos"}
   ]},
  {"question": "O que é que esta marca diz que os concorrentes não dizem?", "header": "Posição",
   "options": [
     {"label": "Mostra o processo", "description": "O trabalho por trás, sem embelezar"},
     {"label": "Diz preços e prazos", "description": "Transparência onde os outros escondem"},
     {"label": "Recusa trabalho", "description": "Diz que não a coisas que não faz bem"},
     {"label": "Escrevo eu", "description": "Tenho outra coisa em mente"}
   ]}
]
```

### Lote 2 (logo a seguir às respostas, sem comentário no meio)

```json
[
  {"question": "O que se quer que fique na cabeça de quem vê a conta?", "header": "Promessa",
   "options": [
     {"label": "Sabem o que fazem", "description": "Competência visível"},
     {"label": "É gente de confiança", "description": "Cumprem o que dizem"},
     {"label": "Isto é bonito / bom", "description": "O produto fala por si"},
     {"label": "Escrevo eu", "description": "Tenho outra formulação"}
   ]},
  {"question": "Sobre o que é que esta marca nunca fala?", "header": "Fora de limites",
   "multiSelect": true,
   "options": [
     {"label": "Política e religião", "description": "Nunca, em nenhum formato"},
     {"label": "Vida pessoal", "description": "Só o negócio"},
     {"label": "Concorrência", "description": "Não se nomeia nem se compara"},
     {"label": "Preços em público", "description": "Só por mensagem"}
   ]},
  {"question": "Que perguntas chegam sempre por mensagem?", "header": "Perguntas",
   "multiSelect": true,
   "options": [
     {"label": "Quanto custa", "description": "Preço, orçamento, mínimos"},
     {"label": "Para quando", "description": "Prazos e disponibilidade"},
     {"label": "Fazem X?", "description": "Âmbito e personalização"},
     {"label": "Entregam onde?", "description": "Área servida, envio, recolha"}
   ]}
]
```

Se alguma resposta vier vazia, voltar a perguntar essa uma vez, em conversa, e seguir.

## Passo 2. Os três montes (o núcleo desta skill)

Adaptado de `02-voz-e-mensagem.md`. Este passo vale mais do que a entrevista inteira: quase nenhuma marca precisa de inventar uma voz — já tem uma escrita algures.

Dizer isto, tal e qual:

> Agora preciso de textos que já escreveste. **10 a 20**, e não têm de ser publicações: mensagens a clientes, descrições de produto, respostas a orçamentos, um email, uma legenda antiga. Quanto mais reais e menos "trabalhados", melhor. Cola-os aqui, um por mensagem ou todos de uma vez.
>
> Se tiveres poucos, diz-me — trabalha-se com o que há, mas a voz sai mais frouxa e eu vou marcá-lo no perfil como provisória.
>
> Antes de colares: **tira nomes, moradas, contactos e números de encomenda de clientes**. Estes textos vão ficar guardados no ficheiro de perfil do projeto, e o que interessa é como escreves, não quem é a pessoa do outro lado.

Se vierem dados pessoais de clientes na mesma, **substituí-los por marcadores** (`[nome]`, `[morada]`) antes de escrever seja o que for no perfil. Um texto de cliente com nome só se guarda ou publica com consentimento para esse fim — ver `10-risco-crise-e-conformidade.md`.

Depois de os receber, **separá-los em três montes** e mostrar a separação ao utilizador para ele corrigir:

| Monte | Critério |
|---|---|
| **Soa certo** | Publicava isto hoje sem mudar nada |
| **Soa errado** | Isto não somos nós |
| **Indiferente** | Funcional, não diz nada sobre a voz |

Se o utilizador não souber separar, fazer a separação como proposta e pedir só que confirme ou troque.

## Passo 3. Perguntar porquê

Para cada texto do monte "soa certo" e do monte "soa errado", perguntar **porquê**, em conversa e sem formulários. As respostas *são* a voz. Insistir onde a resposta for um adjetivo: "mais informal" não é regra; "não começamos por 'Olá!' porque parece atendimento telefónico de empresa grande" é.

Parar quando as razões começarem a repetir-se e a última pergunta não trouxer regra nova. Não há um número certo de razões — o critério é a saturação, não a contagem.

## Passo 4. Analisar os textos

Padrões que atravessam vários textos, nunca tiques de um só.

**Sinais de presença** — comprimento médio de frase · ritmo de parágrafo · como abre · como fecha · pessoa gramatical e tratamento · vocabulário da casa e expressões repetidas · emojis (quais, quantos, onde) · grafias fixas · como pede uma ação.

**Sinais de ausência** (a parte mais valiosa, preservada da origem) — o que **não** aparece em nenhum texto: pontuação ausente (ex.: travessão em 0 de 14 textos) · tipos de abertura que nunca usa · tons que nunca atinge · construções que evita · palavras de setor que nunca escreve. Cada item tem de ser justificado com a contagem: "ausente em 14 de 14". Nada de listas genéricas de palavras proibidas.

**Marcas de outra variante** — assinalar qualquer traço de português do Brasil encontrado nos originais (gerúndio de ação em curso, "você" como tratamento corrente, "mídia", "equipe", "planejamento", "tela", "usuário") e registá-lo como proibição explícita no perfil.

**Contradições** — se dois textos aprovados se contradizem, escrever a contradição no perfil em vez de a alisar.

## Passo 5. Escrever no perfil

Editar `PERFIL-SOCIAL.md` (ou o ficheiro equivalente do projeto). **Não criar `about-me.md` nem `voice.md`.**

**Secção 3 — Público:** quem é em comportamento · o que já pergunta com frequência (usar as respostas do Lote 2) · objeções que aparecem sempre · o que a concorrência diz e nós não.

**Secção 5 — Voz:** língua e variante (português europeu, com as marcas proibidas listadas) · quem fala · tratamento · três adjetivos, cada um seguido da regra observável que o torna verificável · palavras e expressões da casa · palavras proibidas · emojis · grafias fixas · **3 a 5 exemplos aprovados colados na íntegra** · **2 ou 3 rejeitados, cada um com a razão dada no Passo 3** · uma subsecção **"O que esta voz nunca faz"** com os sinais de ausência e as contagens.

Sobre **emojis**: registar não só quais e quantos, mas **onde**. O módulo `04-criacao-de-conteudo.md` fixa a regra de acessibilidade — emojis no fim, sem sequências repetidas, porque cada um é lido em voz alta por um leitor de ecrã. Se os textos originais os usarem a meio da frase ou em sequência, escrever isso no perfil como observação **e** escrever a regra de acessibilidade ao lado, para quem escrever a seguir saber qual é qual.

Acrescentar no topo da secção 5 uma linha de proveniência: `Derivada de N textos reais em AAAA-MM-DD · monte "soa certo": N · rever anualmente, e sempre que mude quem escreve ou o posicionamento.`

O prazo é o do módulo `02-voz-e-mensagem.md` ("define-se uma vez, revê-se anualmente"). Se a voz tiver ficado marcada como provisória por falta de textos, escrever também a data em que se volta a olhar para ela com material novo.

Se algo não se conseguir determinar dos textos, escrever `POR DEFINIR` e acrescentar à lista de campos por definir no fim do ficheiro. **Nunca preencher por adivinhação.**

Se aparecerem alegações que a marca faz sem prova, não as escrever na secção 5 — levantá-las como pergunta para a secção 6, seguindo `02-voz-e-mensagem.md`.

## Passo 6. Confirmar e entregar

Mostrar as duas secções escritas, em bloco de código, para o utilizador poder corrigir de imediato. **A voz não fica fechada aqui:** o módulo `02-voz-e-mensagem.md` diz que aplicar uma voz é delegável mas defini-la não — a versão escrita é uma proposta derivada dos textos até quem é dono do negócio a confirmar. Dizê-lo em voz alta e esperar pela correção antes de a tratar como definitiva.

> As secções **3 (Público)** e **5 (Voz)** do `PERFIL-SOCIAL.md` estão preenchidas. A partir de agora, qualquer texto que eu escrever neste projeto sai daqui — e em caso de conflito entre esta skill e o perfil, manda o perfil.
>
> A seguir podes dizer:
> - "faz o calendário do mês" — planeamento editorial
> - "escreve um post" / "escreve um reel" — peças concretas
> - "otimiza o perfil" — bio, destaques, fixados, fotografia e capa
> - "constrói a voz da newsletter" — se houver newsletter
>
> Ficam por preencher as secções 1, 2, 4 e 6 a 12 do perfil. Diz-me quando quiseres tratar delas.

## Regras

- Ao disparar, ir direto ao Passo 0. Sem resumo, sem preâmbulo.
- Alvo de **10 a 20 textos** — é o número do módulo `02-voz-e-mensagem.md`. Abaixo disso trabalha-se na mesma, mas escreve-se no perfil que a voz é provisória e porquê.
- ◐ Prática, sem estudo por trás: com **menos de meia dúzia de textos** um padrão não se distingue de um tique de um texto só. Não é um limiar medido — é o ponto a partir do qual não se deve afirmar que uma regra é da casa. Abaixo dele, escrever as observações como hipóteses e não como regras.
- Nenhuma ferramenta é obrigatória. Se `AskUserQuestion` não existir, a entrevista faz-se em conversa e a skill chega ao fim na mesma.
- Não guardar dados pessoais de clientes nos exemplos colados no perfil.
- Trabalhar só do que está nos textos. Não inventar padrões nem fontes.
- Português europeu em tudo o que se escreve, incluindo as perguntas.
- Colar os exemplos aprovados em bloco de código, para o utilizador copiar sem perder quebras de linha.
- Nenhum número entra no perfil sem origem. Contagens dos próprios textos são aceitáveis e escrevem-se como tal ("14 de 14").
- Nada de listas de palavras proibidas trazidas de fora: só o que os textos evitam de facto.
- Preços, prazos e alegações não se derivam de textos antigos — confirmam-se com quem sabe.
