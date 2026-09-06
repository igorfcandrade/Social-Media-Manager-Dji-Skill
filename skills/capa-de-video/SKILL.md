---
name: capa-de-video
description: "Desenha a capa e o primeiro fotograma de um vídeo curto — Reel ou Short — no mesmo rácio confirmado para o vídeo. Produz texto, composição, zonas seguras, texto alternativo e instruções de captação; em alternativa, um pedido de imagem pronto para um gerador autorizado. Shorts podem ser quadrados ou verticais; TikTok fica LOOK INTO. Usa esta skill sempre que o assunto for a imagem de entrada, capa, primeiro fotograma, thumbnail ou miniatura de vídeo curto. Não faz miniaturas de YouTube longo."
---

# Capa de vídeo curto

## Gate de revisão

Antes de executar, correr `../social-media-manager/scripts/verificar_revisao.py`, resolvido relativamente a este ficheiro. Sem terminal, ler os blocos `Calendário` de `05-estado-das-plataformas.md` e `09-estado-da-vigilancia.md`. Se uma data chegou, passou ou é inválida, avisar uma vez por conversa; a primeira linha deve ser exatamente `Skill necessita de revisão`. Continuar com as limitações declaradas. O aviso não autoriza pesquisa, acesso a contas nem atualização.

## Contrato de contexto

Aplicar `../social-media-manager/references/contexto-do-caso.md`. O contexto pode chegar na mensagem, em anexos, em fontes ligadas ou em documentos com qualquer nome e formato. Neste ficheiro, «perfil» significa a fonte de contexto disponível; referências a números de secção servem apenas para o modelo opcional incluído no pacote. Não exigir esse modelo, não o copiar automaticamente e não tratar website, checkout, equipa ou ferramenta como pré-requisito. Pedir apenas a informação que muda materialmente esta tarefa.

Skill de execução para vídeo curto, no rácio do vídeo. Reels usam normalmente 9:16; Shorts podem ser quadrados ou verticais (PLAT-017). Não faz miniaturas de YouTube longo e não usa regras atuais de TikTok, que está `LOOK INTO`.

O julgamento — o que é um gancho, o que as plataformas premeiam, a lista de acessibilidade — vive em `../social-media-manager/references/04-criacao-de-conteudo.md` e `../social-media-manager/references/05-plataformas.md`. Se a decisão usar um ID PLAT, ler o registo em `../social-media-manager/references/05-estado-das-plataformas.md`. Ler o que for preciso, não repetir aqui.

## Porque é que isto não é uma miniatura de YouTube

Numa miniatura de YouTube longo há uma imagem, num sítio só, com um formato estável, e o espectador decide olhando para ela. Em vídeo curto vertical há **duas superfícies diferentes com funções diferentes**, e a maior parte do trabalho falha por tratá-las como uma:

| | O que é | Onde decide |
|---|---|---|
| **Primeiro fotograma** | O que aparece quando o vídeo começa a correr sozinho no feed | Feed de Reels, Para Ti, Shorts — o utilizador **não escolheu** ver isto |
| **Capa** | A imagem que representa o vídeo parado | Grelha do perfil, separador de Reels, resultados de pesquisa — o utilizador **está a escolher** |

O primeiro fotograma joga contra o polegar em movimento e tem 3 camadas simultâneas com o áudio e o texto (é o gancho — `../social-media-manager/references/04-criacao-de-conteudo.md`). A capa joga contra as outras oito imagens da grelha e é onde se constrói a identidade do perfil. **São dois trabalhos, e uma boa capa raramente é um bom primeiro fotograma.**

## Arranque imediato

Se o vídeo ou o guião já vierem na mensagem, usá-los e saltar para o Passo 2. Não resumir a skill.

## Passo 0. Contexto do caso

Ler o contexto do caso disponível, qualquer que seja o nome ou formato. Interessam a secção 5 (voz, grafias fixas, palavras proibidas), a 4 (plataformas), a 6 (o que se pode afirmar) e a 8 (quem aparece em câmara, meios de produção). Se existir uma fonte canónica de identidade visual, **ela ganha** sobre qualquer sugestão de cor daqui.

Sem destino, voz, alegações e capacidade de produção suficientes, pedir apenas esses dados ou
entregar uma estrutura com lacunas explícitas. Não criar contexto automaticamente.

Se a paleta e a tipografia não estiverem no contexto, perguntar antes de propor um único hex. Com
autorização, devolver a decisão à fonte canónica de identidade visual; sem escrita disponível,
entregar o bloco copiável. Cores, tipografia e nomes de produto não se adivinham.

## Passo 1. Contexto do vídeo

**Perguntar pelo meio interativo disponível**, saltando o que já for conhecido:

```json
[
  {"question": "O vídeo já existe?", "header": "Estado", "multiSelect": false,
   "options": [
     {"label": "Já gravado", "description": "Escolhe-se um fotograma real do vídeo"},
     {"label": "Guião pronto, por gravar", "description": "Planeia-se o plano a captar de propósito"},
     {"label": "Nem guião", "description": "Chamar antes `guiao-video-curto`"}
   ]},
  {"question": "Onde vai sair?", "header": "Destino", "multiSelect": true,
   "options": [
     {"label": "Instagram Reels", "description": "Grelha do perfil + feed"},
     {"label": "TikTok", "description": "LOOK INTO — não produzir segundo regras atuais nesta versão"},
     {"label": "YouTube Shorts", "description": "Quadrado ou vertical; confirmar capa e recorte na conta; PLAT-017"},
     {"label": "Facebook Reels", "description": "Separador de Reels da Página"}
   ]},
  {"question": "Que função tem esta peça na grelha?", "header": "Função", "multiSelect": false,
   "options": [
     {"label": "Descoberta", "description": "Tem de parar quem não conhece a marca"},
     {"label": "Referência", "description": "Alguém vai voltar a esta para reencontrar"},
     {"label": "Identidade", "description": "Mantém a grelha coerente, não precisa de gritar"}
   ]}
]
```

### Vários destinos ao mesmo tempo

**Um destino, uma peça.** Cada superfície tem o seu rácio e as suas zonas seguras; a mesma tela recortada perde a composição em todas menos numa.

- Sai **uma peça por destino**, cada uma **no seu rácio**, com as zonas seguras dessa superfície e o contraste recalculado se a cor mudar.
- O **texto alternativo é por peça**, não um para o conjunto.
- ⚠️ **Destinos que não estejam na secção 4 do perfil não se produzem.** Perguntar porquê primeiro.
- Se o mesmo desenho servir dois rácios sem redesenho, dizê-lo explicitamente — é a exceção, não o pressuposto.

## Passo 2. Escrever o texto da capa

Regras que valem para todos os destinos: ◐

- **3 a 5 palavras.** Seis é o limite absoluto. Não é uma frase — é uma etiqueta.
- **Nomeia algo concreto**, não uma categoria. "Bolo de 3 andares em 40 minutos" pára; "dicas de pastelaria" não.
- **Cumprível.** Uma capa que promete mais do que o vídeo entrega compra a paragem e perde a retenção, que é o sinal que decide a distribuição. É o mesmo mecanismo do gancho, e a mesma consequência.
- **Legível ao sol, num ecrã pequeno, dentro de uma grelha de nove.** Testar encolhendo a imagem até ao tamanho de uma célula de grelha e apertando os olhos. Se não se lê, não existe.
- **Contraste** ⬤ mínimo 4,5:1 para texto normal e 3:1 para texto grande (18pt normal ou 14pt negrito), WCAG 2.2 AA. São limiares, não arredondáveis.
- **Sem informação essencial só na cor.**
- Grafias fixas e palavras proibidas: do perfil, secção 5.

⚠️ Preços, prazos e condições **não vão para a capa** a partir desta skill. Vêm do perfil ou de um humano. Uma capa fica meses na grelha e um preço errado dura o mesmo tempo.

## Passo 3. Composição e zonas seguras

**A armadilha central:** a mesma imagem é cortada de maneiras diferentes em cada sítio onde aparece. O ficheiro segue o rácio confirmado do vídeo — por exemplo, 9:16 (1080×1920) num Reel vertical — mas grelhas e pré-visualizações podem recortá-lo.

Por isso a regra é de método, não de números: **compor o essencial no centro vertical da imagem e verificar o recorte na aplicação real, no dia, antes de publicar** — nem no editor, nem de memória, nem a partir de uma lista de dimensões copiada de um blogue.

- Manter texto e rosto **fora das margens** — topo, base e a faixa lateral direita, onde vivem os botões, o nome de utilizador, a legenda e a barra de progresso.
- O recorte da grelha é **mais largo do que 9:16**, logo **corta topo e base, não os lados**. Isto é geometria, não é spec, e não muda. O que tem de sobreviver fica na **faixa central vertical**.
- ◐ A célula da grelha do Instagram já foi quadrada e hoje é vertical. O rácio exato **não se cita daqui nem de um blogue** — abre-se o perfil e olha-se. Enquanto não estiver verificado, compor para o quadrado central é a margem segura, por ser a mais apertada das hipóteses.
- **Rosto ou mãos, se a marca os usa.** Um plano de produto parado numa grelha de vídeo lê-se como fotografia e perde a expectativa de movimento.
- **Um elemento focal além do texto**: o objeto, o antes-e-depois, um número grande.
- **Duas cores dominam.** A primária da marca mais um acento de contraste.

**Coerência de grelha:** a decisão que mais rende não é uma capa boa — é **a mesma família de capas repetida**. Mesma posição de texto, mesma tipografia, mesma paleta, mesmo tratamento de cor. É o que faz um perfil ser reconhecido de relance, e custa zero.

## Passo 4. O primeiro fotograma

Trabalho separado, e não se resolve escolhendo a capa. O primeiro fotograma é o **segundo zero do gancho** e obedece à camada "o que se vê" do módulo 04.

- **Movimento ou pessoa já a falar**, não um plano estático de abertura. Um logótipo, um genérico ou uma contagem no primeiro segundo gasta o único segundo que decide tudo.
- **Sem texto por cima do texto da plataforma**: verificar na aplicação.
- Evitar uma abertura que seja apenas um cartão de texto parado: perde o movimento do gancho e é menos acessível como vídeo. O Instagram incluiu Reels maioritariamente texto numa lista publicada em 2023; essa afirmação está registada como histórica em PLAT-011 e não se apresenta como peso atual sem nova verificação.
- Coerente com a capa: quem tocou por causa da capa tem de reconhecer o que abriu. Capa e primeiro fotograma diferentes são aceitáveis; **contraditórios, não**.

## Passo 5. Produzir a imagem — manual primeiro, gerador se existir

### 5A. Caminho predefinido: um fotograma real

A melhor capa de um vídeo curto é quase sempre **um plano real do próprio vídeo**, gravado de propósito. Entregar a instrução de captação:

> Antes de gravar o vídeo, gravar 3 segundos extra de um plano de capa: [enquadramento], [expressão ou gesto], [fundo], [luz]. Fica como fotograma isolado e serve de capa.

Ou, se o vídeo já existe, indicar **o segundo exato** do fotograma a extrair e o texto a sobrepor, com posição.

Isto não é o caminho pobre: é o caminho que garante que a capa corresponde ao vídeo, que não precisa de rótulo de IA, e que sai igual à peça.

### 5B. Caminho opcional: pedido de imagem para um gerador

Só quando não há fotograma utilizável — e verificando antes se há alguma ferramenta de geração disponível no ambiente. **Nunca é requisito.** Entregar o pedido num bloco de código, pronto a colar:

```
Capa para vídeo curto, [rácio e tela de produção confirmados].

Composição:
- [sujeito] em [posição], ocupando [%] do enquadramento
- Expressão / gesto: [...]
- O essencial na faixa central vertical da imagem: o recorte da grelha corta topo e base

Texto:
- "[3 a 5 palavras]" em tipografia sem serifa, grande e cheia
- Cor do texto: [hex] · contorno/sombra: [hex] para garantir contraste
- Posição: [área], fora das margens superior, inferior e lateral direita

Paleta: primária [hex] · acento [hex] · fundo [hex, com tratamento]
Elemento de apoio: [objeto / número / seta]

Restrições:
- Legível reduzido ao tamanho de uma célula de grelha de perfil
- Contraste mínimo 4,5:1 entre texto e fundo
- Sem marcas de água, sem elementos de interface de nenhuma aplicação
- Sem texto nas margens
```

⚠️ **Regras que não se contornam:** ⬤ a Meta aplica o rótulo "AI Info" a conteúdo detetado ou declarado. TikTok está `LOOK INTO`. Uma capa que mostra um produto que não corresponde ao produto real **é publicidade enganosa, não estilo** — não se faz, com ou sem rótulo. Rosto de pessoa real: só a partir de fotografia real dessa pessoa, com autorização.

## Passo 6. Formato de saída

```
CAPA — [vídeo]
Destino: [plataformas] · ficheiro [rácio e tela de produção confirmados]

TEXTO DA CAPA
"[3 a 5 palavras]"  — cumpre: [o que o vídeo entrega mesmo]

COMPOSIÇÃO
Sujeito: ... · Posição do texto: ... · Elemento focal: ...
Paleta: primária [hex] · acento [hex]
Zona segura: essencial no quadrado central; margens livres

PRIMEIRO FOTOGRAMA
Segundo 0: [o que se vê] / [o que está escrito no ecrã]

COMO PRODUZIR
[instrução de captação — ou o pedido de imagem, se não houver fotograma]

ACESSIBILIDADE
Texto alternativo: [função e conteúdo essencial, sem começar por "imagem de"]
Legendas do vídeo: revistas à mão — nomes, números e termos do negócio saem errados nas automáticas
Informação essencial que está na capa: repetida também na legenda visível do post

VERIFICAR NA APP ANTES DE PUBLICAR
[ ] recorte da grelha  [ ] nada por baixo dos botões  [ ] legível reduzido
[ ] contraste medido, não estimado  [ ] rótulo de IA, se aplicável
```

## Passo 7. Passo seguinte

> Queres que eu escreva o guião do vídeo? Chamo `guiao-video-curto`. Ou variações do texto da capa: `gerar-ganchos`.

## Regras

- **Português europeu** em tudo, incluindo o texto da capa.
- **Usar o rácio do vídeo.** 9:16 é a escolha normal de um Reel vertical; um Short também pode ser quadrado (PLAT-017). Não transformar “thumbnail” numa dimensão universal.
- **Capa e primeiro fotograma são dois trabalhos.** Entregar sempre os dois.
- **Nunca escrever preços, prazos ou condições** na capa a partir desta skill.
- **Nunca prometer na capa o que o vídeo não entrega.**
- Nenhuma ferramenta de geração de imagem é obrigatória. O caminho manual — fotograma real captado de propósito — é o predefinido e é o melhor.
- Imagem gerada por IA que seja realista: rotulada, e nunca a representar produto, resultado ou pessoa que não correspondam ao real.
- Texto alternativo em todas as capas, legendas do vídeo revistas à mão, e a informação essencial da capa repetida na legenda visível. As três vêm do módulo 04 e nenhuma é opcional.
- **Nenhuma cor se inventa.** Sem paleta no perfil nem fonte canónica de identidade visual, pergunta-se — não se propõe um hex plausível.
- As dimensões de recorte das grelhas mudam: **verificar na aplicação, não citar de memória nem de blogues.**
- Recomendar sempre a mesma família visual de capas ao longo do tempo. A coerência da grelha rende mais do que qualquer capa isolada.
- Não resumir esta skill. Executá-la.
