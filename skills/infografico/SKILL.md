---
name: infografico
description: "Transforma conteúdo denso — um post, uma secção de newsletter, um artigo, notas soltas — numa infografia vertical única, legível no telemóvel, com contraste verificado e texto alternativo. Entrega a peça em HTML/CSS ou, se houver gerador de imagem disponível, um pedido pronto a colar. Usa esta skill SEMPRE que o pedido for condensar informação numa imagem só (ex.: \"faz-me uma infografia\", \"transforma isto num quadro visual\", \"resume este artigo numa imagem\", \"quero aquele estilo de quadro branco desenhado à mão\", \"mete estes dados num visual\", \"infográfico disto\", \"passa este texto a esquema\"). Se a informação não couber numa imagem sem deixar de se ler, esta skill diz isso e passa para `carrossel`."
---

# Infografia

## Gate de revisão

Antes de executar, correr `../social-media-manager/scripts/verificar_revisao.py`, resolvido relativamente a este ficheiro. Sem terminal, ler os blocos `Calendário` de `05-estado-das-plataformas.md` e `09-estado-da-vigilancia.md`. Se uma data chegou, passou ou é inválida, avisar uma vez por conversa; a primeira linha deve ser exatamente `Skill necessita de revisão`. Continuar com as limitações declaradas. O aviso não autoriza pesquisa, acesso a contas nem atualização.

Skill de execução. Uma infografia é **uma imagem única, vertical, que condensa uma estrutura**. Não é um carrossel espalmado nem um post ilustrado.

O julgamento — formato por função, o que se guarda, a lista de acessibilidade — vive em `../social-media-manager/references/04-criacao-de-conteudo.md`. Ler o que for preciso, não repetir aqui.

## Arranque imediato

Se o conteúdo já vier na mensagem, usá-lo e saltar o Passo 1. **O Passo 0 nunca se salta** — sem perfil não se produz nada. Não resumir a skill.

## Passo 0. Perfil de marca

Ler `PERFIL-SOCIAL.md` (ou `MARCA.md`, `MEMORY.md`, `CLAUDE.md`, ou uma pasta `Social Media/`). Interessam a secção 5 (voz, grafias fixas, palavras proibidas), a 4 (plataformas), a 6 (o que se pode afirmar) e a 12 (convenções).

**Em conflito entre o perfil e esta skill, manda o perfil** — ele conhece o negócio, esta skill não. E se o projeto tiver skill própria de tema visual, **essa ganha** sobre qualquer cor sugerida aqui.

Sem perfil, criá-lo a partir de `../social-media-manager/assets/PERFIL-MARCA-modelo.md`, **em conversa com quem sabe** e sem adivinhar: os campos por responder ficam marcados `POR DEFINIR`. **Parar até existir.**

## Passo 1. Obter o conteúdo

Se não vier na mensagem:

> Cola o conteúdo que queres transformar em infografia. Um post, uma secção de newsletter, um artigo, notas de investigação ou pontos soltos servem todos.

## Passo 2. Teste de cabimento — antes de desenhar

Contar os pontos-chave. Este teste decide o formato e evita o erro mais caro desta skill. ◐ Os limiares são uma convenção de legibilidade desta skill, não um número medido — não os citar como dado:

| Pontos-chave | Decisão |
|---|---|
| 3 a 7 | Infografia. Continuar. |
| 8 a 12 | Ou se corta para 7, ou vai para `carrossel`. Perguntar qual. |
| Mais de 12 | **Não é uma infografia.** Chamar `carrossel` e dizer porquê numa linha. |

⚠️ O modo de falha desta skill é encher a imagem. Uma infografia com dezasseis caixas não é densa — é ilegível, e ninguém a guarda. **O limite é a legibilidade num ecrã de telemóvel, não o espaço em branco.**

## Passo 3. Estilo e destino — antes do resumo

O estilo decide-se **antes** de escrever o resumo, porque o resumo já nomeia cores.

**AskUserQuestion**:

```json
[
  {"question": "Que estilo visual?", "header": "Estilo", "multiSelect": false,
   "options": [
     {"label": "Marca", "description": "Cores e tipografia do perfil. Limpo, plano, alto contraste."},
     {"label": "Desenhado à mão", "description": "Aspeto de quadro branco ou caderno, marcadores. Informal, memorável."},
     {"label": "Editorial", "description": "Serifada grande, muito espaço, um acento de cor."}
   ]},
  {"question": "Onde vai sair?", "header": "Destino", "multiSelect": true,
   "options": [
     {"label": "Instagram feed", "description": "1080x1350 (4:5) — ◐ dimensão corrente, confirmar na aplicação"},
     {"label": "Pinterest", "description": "1000x1500 (2:3) — ◐ tela de produção; outros rácios orgânicos também são aceites"},
     {"label": "Stories", "description": "1080x1920 (9:16) — ◐ dimensão corrente"},
     {"label": "Facebook", "description": "A mesma peça 4:5 — ◐ o feed do Facebook aceita vertical até 4:5; acima disso corta"}
   ]}
]
```

⚠️ **As dimensões acima são telas de produção, não limites universais.** No Pinterest, 1000×1500 é uma escolha 2:3 entre vários rácios orgânicos aceites; ver PLAT-019. Antes de exportar, confirmar na própria aplicação, no telemóvel — nunca só no editor.

⚠️ Se o perfil (secção 4) não listar a plataforma, ela não entra na pergunta. As plataformas escolhem-se no perfil, não aqui.

⚠️ O estilo "desenhado à mão" é uma escolha estética, não um atalho de eficácia. Os números de alcance que circulam associados a este estilo não têm amostra publicada — não os repetir. ◐ O que é defensável: um estilo distinto e repetido torna a marca reconhecível de relance.

⚠️ E o estilo não pode comer a acessibilidade: marcador claro sobre fundo branco falha o contraste com frequência. Se o estilo escolhido não atingir o limiar do Passo 5, muda-se a cor, não o limiar.

### Vários destinos ao mesmo tempo

**Um destino, uma peça.** Cada superfície tem o seu rácio e as suas zonas seguras; a mesma tela recortada perde a composição em todas menos numa.

- Sai **uma peça por destino**, cada uma **no seu rácio**, com as zonas seguras dessa superfície e o contraste recalculado se a cor mudar.
- O **texto alternativo é por peça**, não um para o conjunto.
- ⚠️ **Destinos que não estejam na secção 4 do perfil não se produzem.** Perguntar porquê primeiro.
- Se o mesmo desenho servir dois rácios sem redesenho, dizê-lo explicitamente — é a exceção, não o pressuposto.

## Passo 4. Construir o resumo

Produzir o resumo em texto simples, para aprovação:

- **Título** — 6 palavras ou menos, concreto. Nomeia algo, não uma categoria.
- **Subtítulo** — uma linha de contexto, opcional.
- **Estrutura** — escolher **uma**: passos · enquadramento · comparação · números · lista.
- **Pontos-chave** — 3 a 7, cada um com 10 palavras ou menos.
- **Elementos visuais** — setas, caixas, números destacados, ícones. Dizer onde e de que cor, com as cores do estilo já escolhido no Passo 3.
- **Origem de cada número** — se a infografia mostra dados, cada número leva a fonte e a amostra ao lado, no resumo. Um número que não consiga preencher amostra **e** fonte não entra na peça. Ver `../social-media-manager/references/11-numeros-de-referencia.md`.
- **Rodapé** — nome da marca, do perfil. Sem chamada à ação inventada nem interação artificial. ⬤ O Facebook despromove *engagement bait*; PLAT-007. O Instagram proíbe recolher artificialmente interação — ver `../social-media-manager/references/10-risco-crise-e-conformidade.md`.

Depois:

> Este é o resumo. Diz o que queres mudar, ou diz "avança" quando estiver bem.

**Esperar aprovação explícita.** Não passar ao passo seguinte sem ela: corrigir texto no resumo custa segundos, corrigir dentro de uma imagem obriga a gerar tudo de novo.

## Passo 5. Produzir — HTML primeiro, gerador se existir

### 5A. Caminho predefinido: HTML/CSS

Funciona sem nada instalado, é editável, e o texto sai sempre bem escrito — que é o ponto onde os geradores de imagem falham mais, sobretudo em português.

Ficheiro HTML único, CSS embutido, `meta viewport`, na dimensão do destino. Requisitos:

- Título grande no topo, pontos-chave em blocos com número ou ícone.
- Números destacados em corpo muito maior, com etiqueta por baixo.
- **Contraste** ⬤ mínimo 4,5:1 para texto normal e 3:1 para texto grande (18pt normal ou 14pt negrito), WCAG 2.2 AA. São limiares, não arredondáveis: 4,499:1 não cumpre. Calcular o rácio de **todos** os pares texto/fundo usados — corpo, título, números destacados, rodapé — e escrevê-los na saída. Abaixo do limiar, muda-se a cor.
- **Nada essencial transmitido só por cor.**
- Margem interior mínima de 40 px (escolha de desenho desta skill, não uma regra de plataforma).
- Ícones decorativos com `aria-hidden`; o significado vive no texto, não no ícone.
- Teste final: reduzir a imagem a 1/4 e apertar os olhos. O título e os números têm de continuar a ler-se.

Gravar e indicar o caminho. E dizer **como** se exporta, que é onde quem nunca o fez encalha:

> Abre o ficheiro no navegador. Para exportar na dimensão exata, abre as ferramentas de programador (F12), ativa o modo de dispositivo e fixa a janela na dimensão do destino — depois usa a captura de ecrã de tamanho real do próprio navegador, não uma captura do sistema. Em alternativa, imprimir para PDF com a página definida à mesma dimensão e converter a imagem.

### 5B. Caminho opcional: pedido para um gerador de imagem

Só se houver ferramenta disponível — e, se não houver, entregar na mesma o pedido escrito para o utilizador colar onde quiser. **Nunca parar por falta de chave de API.** Dizer com honestidade o que se perde: um gerador erra acentos, cedilhas e palavras longas em português, e cada correção é uma imagem nova; o HTML não erra nenhuma.

```
Infografia vertical única, [1080x1350 / 1000x1500 / 1080x1920] px.

Estilo: [marca / desenhado à mão em quadro branco / editorial]
Paleta: fundo [hex] · texto [hex] · acento [hex]

TÍTULO (topo, grande, negrito):
[título, 6 palavras ou menos]

SUBTÍTULO:
[uma linha]

CORPO ([N] blocos, cada um com número ou ícone):
1. [ponto, 10 palavras ou menos]
2. [...]

[Números a destacar, em corpo grande, com etiqueta por baixo]

RODAPÉ: [nome da marca]

Restrições:
- Texto em português europeu, com acentuação correta, exatamente como escrito acima
- Contraste do texto sobre o fundo no mínimo 4,5:1
- Texto grande e legível quando a imagem é reduzida a um quarto
- Sem marcas de água, sem logótipos inventados, sem elementos de interface
```

⚠️ **Se o resultado for realista ou materialmente alterado por IA**, aplicar o rótulo da plataforma. ⬤ O artigo 50.º do AI Act, em vigor desde 2 de agosto de 2026, obriga quem publica profissionalmente a identificar *deepfakes* e certos textos de interesse público; ◐ na dúvida, este sistema identifica mais amplamente. Ver `../social-media-manager/references/10-risco-crise-e-conformidade.md`. **Produto que não corresponde ao real é publicidade enganosa**, não estilo.

### 5C. Direitos do que entra na peça

Uma infografia raramente é só texto — leva ícones, fotografias, dados de terceiros, às vezes uma frase de cliente. **Verificar ainda no resumo do Passo 4**, antes de haver imagem para corrigir:

- **Ícones e fotografias de bancos de imagens** — confirmar que a licença cobre **uso comercial** e se exige atribuição. Muitas licenças gratuitas não cobrem.
- **Testemunho, frase ou fotografia de cliente** — autorização **por escrito para esse fim específico**, registada. Uma marcação não transfere licença nem direito de imagem.
- **Dados de terceiros** — a fonte fica visível na peça. Um gráfico sem fonte é um boato com eixos.
- **Setor regulado** (saúde, finanças, alimentar, imobiliário, jurídico) — as alegações vêm da secção 6 do perfil e passam por quem responde legalmente. Uma infografia dá às alegações um ar de facto que elas podem não ter.

Ver `../social-media-manager/references/10-risco-crise-e-conformidade.md`.

## Passo 6. Saída

```
INFOGRAFIA — [assunto]
Destino: [plataformas] · [dimensão] · via: [HTML / pedido de imagem]

TÍTULO  "[...]"
ESTRUTURA  [passos / enquadramento / comparação / números / lista]
PONTOS  [1..N]

CONTRASTE  um par por linha: [hex] sobre [hex] = [X,X]:1 ✓ · limiar aplicado [4,5:1 / 3:1]
FICHEIRO  [caminho] — ou o pedido, no bloco acima

TEXTO ALTERNATIVO
[título, estrutura e os pontos, por ordem, em texto corrido. Sem começar por "imagem de".
 Num infográfico o texto alternativo carrega o conteúdo todo, não uma descrição do aspeto.]

NA LEGENDA VISÍVEL
[os números, as fontes e a informação essencial, repetidos em texto]
```

## Passo 7. Iterar e o que vem a seguir

> Se a primeira versão falhar, diz o que ajustar e reescrevo. Correções comuns: menos pontos, título maior, menos cores, outra direção de leitura.

A peça ainda não é uma publicação. Falta a legenda que a acompanha e a chamada à ação — uma só. Para isso, `escrever-post`, que lê o mesmo perfil. Se houver uma pergunta previsível que a infografia não responde, `comentario-fixado`.

## Regras

- **Português europeu** em tudo, incluindo o texto dentro da imagem.
- **Vertical sempre.** Nunca horizontal — perde-se no feed e no Pinterest.
- Máximo 7 pontos. Acima disso é `carrossel`, e diz-se porquê.
- Cada ponto com 10 palavras ou menos.
- **Esperar aprovação do resumo antes de produzir a imagem.** Sem exceções.
- O caminho HTML é o predefinido e funciona sem nada instalado. Nenhum gerador é requisito.
- Contraste calculado e escrito. Texto alternativo sempre — e num infográfico o texto alternativo tem de conter os pontos todos, não uma descrição vaga.
- **Nunca inventar números, percentagens ou fontes** para encher a infografia. Se o conteúdo de origem não traz um número, a infografia não traz. Um número sem amostra conhecida é um boato com casas decimais.
- **Um número só entra na peça se conseguires escrever a amostra e a fonte ao lado dele.** Se não conseguires as duas, não é citável — nem na imagem, nem na legenda.
- Conteúdo de terceiros, testemunhos e imagens de banco só entram com autorização escrita e licença comercial verificada.
- Nunca escrever preços, prazos ou condições a partir desta skill.
- Sem mecânicas de "partilha para ganhar" no rodapé.
- Não usar travessões longos na saída.
- Não resumir esta skill. Executá-la.
