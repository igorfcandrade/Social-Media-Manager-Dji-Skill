---
name: capa-de-video
description: "Desenha a capa e o primeiro fotograma de um vídeo curto — Reel ou Short — no rácio confirmado para o vídeo. Decide se a capa precisa de texto, define composição, zonas seguras, acessibilidade e instruções de captação; em alternativa, prepara um pedido para um gerador autorizado. Shorts podem ser quadrados ou verticais; TikTok fica LOOK INTO. Usa esta skill para imagem de entrada, capa, primeiro fotograma, thumbnail ou miniatura de vídeo curto. Não faz miniaturas de YouTube longo."
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

O primeiro fotograma integra o gancho visual; a capa representa o vídeo parado e pode cumprir outra
função na grelha. São duas decisões que podem usar o mesmo fotograma ou imagens diferentes. Testar
reconhecimento e coerência em vez de presumir que têm de divergir.

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

**Uma validação por destino; nova peça apenas quando houver diferença material.** Cada superfície
pode ter rácio, recorte ou zonas de interface diferentes, mas uma mesma capa pode servir mais do
que uma quando sobreviver às verificações.

- Registar rácio, recorte e zonas seguras por destino. Só criar outra peça quando for preciso
  mudar composição, texto, contraste, rácio ou ficheiro.
- O **texto alternativo é por conteúdo/colocação**; pode ser igual quando a imagem e a função são iguais.
- ⚠️ **Destinos que não estejam na secção 4 do perfil não se produzem.** Perguntar porquê primeiro.
- Se o mesmo desenho servir dois destinos, registá-lo e evitar a duplicação.

## Passo 2. Decidir se a capa precisa de texto

Começar pela direção visual do caso. Uma capa sem texto pode ser a escolha certa quando a imagem
identifica a peça, o gesto ou o resultado e a grelha pede fotografia dominante. Texto é uma
ferramenta, não um requisito.

Quando houver texto: ◐

- Usar a menor quantidade de palavras que permita reconhecer a promessa no tamanho real de grelha;
  a direção da marca pode fixar outra regra ou preferir zero palavras.
- **Nomear algo concreto**, não uma categoria, e cumprir no vídeo o que a capa promete.
- Não atribuir à capa um efeito universal de alcance ou retenção; comparar versões em grupos de peças.
- **Legível num ecrã pequeno e na grelha real.** Testar no tamanho e brilho de uso, sem depender de uma avaliação subjetiva isolada.
- **Contraste** ⬤ mínimo 4,5:1 para texto normal e 3:1 para texto grande (18pt normal ou 14pt negrito), WCAG 2.2 AA. São limiares, não arredondáveis.
- **Sem informação essencial só na cor.**
- Grafias fixas e palavras proibidas: do perfil, secção 5.

⚠️ Preços, prazos e condições **não vão para a capa** a partir desta skill. Vêm do perfil ou de um humano. Uma capa fica meses na grelha e um preço errado dura o mesmo tempo.

## Passo 3. Composição e zonas seguras

**A armadilha central:** a mesma imagem é cortada de maneiras diferentes em cada sítio onde aparece. O ficheiro segue o rácio confirmado do vídeo — por exemplo, 9:16 (1080×1920) num Reel vertical — mas grelhas e pré-visualizações podem recortá-lo.

Por isso a regra é de método, não de números: **compor o essencial no centro vertical da imagem e verificar o recorte na aplicação real, no dia, antes de publicar** — nem no editor, nem de memória, nem a partir de uma lista de dimensões copiada de um blogue.

- Manter texto, rosto, mãos e detalhe essencial fora das áreas que a interface cobre; verificar na
  aplicação real, porque margens e recortes podem mudar.
- O rácio da grelha e o sentido do corte confirmam-se no perfil real. Enquanto não forem vistos,
  manter o essencial numa área central flexível e não declarar uma geometria permanente.
- Usar um elemento focal claro, com ou sem texto, e as cores definidas pela direção do caso.

**Coerência de grelha:** repetir decisões suficientes para reconhecimento — tratamento de cor,
paleta, luz, enquadramento ou tipografia — sem obrigar todas as capas à mesma posição de texto. A
direção visual do caso decide o sistema e pode preferir uma maioria de capas sem texto.

## Passo 4. O primeiro fotograma

Trabalho separado, e não se resolve escolhendo a capa. O primeiro fotograma é o **segundo zero do gancho** e obedece à camada "o que se vê" do módulo 04.

- Tornar cedo a ação, o objeto ou a promessa percetíveis. Movimento, gesto, fala ou um plano
  estático forte são opções; testar qual serve o vídeo em vez de impor uma fórmula.
- **Sem texto por cima do texto da plataforma**: verificar na aplicação.
- Um cartão de texto parado pode atrasar a matéria visual; usá-lo apenas quando tiver função. O
  Instagram incluiu Reels maioritariamente texto numa lista publicada em 2023; essa afirmação está
  registada como histórica em PLAT-011 e não se apresenta como peso atual sem nova verificação.
- Coerente com a capa: quem tocou por causa da capa tem de reconhecer o que abriu. Capa e primeiro fotograma diferentes são aceitáveis; **contraditórios, não**.

## Passo 5. Produzir a imagem — manual primeiro, gerador se existir

### 5A. Caminho predefinido: um fotograma real

Um fotograma real do próprio vídeo é uma opção económica e coerente, sobretudo para produto,
pessoa, processo ou lugar reais. Entregar a instrução de captação:

> Antes de gravar o vídeo, gravar 3 segundos extra de um plano de capa: [enquadramento], [expressão ou gesto], [fundo], [luz]. Fica como fotograma isolado e serve de capa.

Ou, se o vídeo já existe, indicar o fotograma a extrair e, se necessário, o texto a sobrepor, com posição.

Este caminho facilita a correspondência com o vídeo e evita fabricar produto ou pessoa. Continua a
exigir verificação do recorte, da nitidez e dos direitos.

### 5B. Caminho opcional: pedido de imagem para um gerador

Só quando não há fotograma utilizável — e verificando antes se há alguma ferramenta de geração disponível no ambiente. **Nunca é requisito.** Entregar o pedido num bloco de código, pronto a colar:

```
Capa para vídeo curto, [rácio e tela de produção confirmados].

Composição:
- [sujeito] em [posição], ocupando [%] do enquadramento
- Expressão / gesto: [...]
- O essencial na faixa central vertical da imagem: o recorte da grelha corta topo e base

Texto, se necessário:
- "[texto curto ou nenhum]" na tipografia definida pelo caso
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
[sem texto — razão visual / "texto curto" — cumpre: o que o vídeo entrega]

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
- Nenhuma ferramenta de geração de imagem é obrigatória. Para conteúdo real, começar por avaliar
  um fotograma real captado de propósito e usar outra solução apenas quando a função da capa o exigir.
- Imagem gerada por IA que seja realista: rotulada, e nunca a representar produto, resultado ou pessoa que não correspondam ao real.
- Texto alternativo em todas as capas, legendas do vídeo revistas à mão, e a informação essencial da capa repetida na legenda visível. As três vêm do módulo 04 e nenhuma é opcional.
- **Nenhuma cor se inventa.** Sem paleta no perfil nem fonte canónica de identidade visual, pergunta-se — não se propõe um hex plausível.
- As dimensões de recorte das grelhas mudam: **verificar na aplicação, não citar de memória nem de blogues.**
- Aplicar a direção visual do caso e avaliar a coerência do conjunto sem impor uma família repetida
  ou texto obrigatório.
- Não resumir esta skill. Executá-la.
