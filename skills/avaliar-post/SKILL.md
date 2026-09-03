---
name: avaliar-post
description: "Avalia um rascunho de post, legenda ou guião de Reel/Short antes de publicar, comparando-o com dados disponíveis da própria conta e o perfil de marca. Devolve pontuação honesta, correções concretas e avisa quando a amostra não permite concluir. Usa sempre que pedirem avaliação, crítica, nota, revisão ou feedback a conteúdo. TikTok fica LOOK INTO até revisão própria."
---

# Avaliar post

## Gate de revisão

Antes de executar, correr `../social-media-manager/scripts/verificar_revisao.py`, resolvido relativamente a este ficheiro. Sem terminal, ler os blocos `Calendário` de `05-estado-das-plataformas.md` e `09-estado-da-vigilancia.md`. Se uma data chegou, passou ou é inválida, avisar uma vez por conversa; a primeira linha deve ser exatamente `Skill necessita de revisão`. Continuar com as limitações declaradas. O aviso não autoriza pesquisa, acesso a contas nem atualização.

Skill de execução. O critério vive nos módulos: anatomia da peça, ganchos, extensão e acessibilidade em `../social-media-manager/references/04-criacao-de-conteudo.md`; leitura de dados, regressão à média e regra dos três em `../social-media-manager/references/07-analise-e-relatorio.md`; benchmarks com amostra em `../social-media-manager/references/11-numeros-de-referencia.md`. **Ler o que for preciso e não o repetir aqui.**

## Arranque imediato

Ao disparar, ir direto ao Passo 0. Não resumir a skill, não explicar o método de pontuação, não perguntar se se avança.

## Passo 0. Perfil de marca — bloqueante

Procurar no projeto: `PERFIL-SOCIAL.md`, `MARCA.md`, `MEMORY.md`, `CLAUDE.md`, pasta `Social Media/`.

- **Se existir**, lê-lo primeiro. Interessam as secções 3 (Público), 5 (Voz), 6 (Alegações), 7 (Pilares), 11 (Aprendizagens) e 12 (fórmula de taxa escolhida). Dizer numa linha o que foi aproveitado.
- **Se não existir**, copiá-lo de `../social-media-manager/assets/PERFIL-MARCA-modelo.md` para `PERFIL-SOCIAL.md` e **parar até estarem preenchidas as secções 5 e 7**. Sem voz definida, a pontuação de voz é adivinhação com ar de rigor.
  - **Exceção declarada:** se a pessoa não quiser preencher o perfil agora, avaliar na mesma os outros quatro critérios e escrever `Voz — · sem perfil de voz definido` em vez de uma nota. Nunca pontuar voz por adivinhação, e nunca inferir a voz do próprio rascunho — isso é dar nota ao texto contra ele mesmo.
- **Em conflito entre esta skill e o perfil, manda o perfil.** Se o projeto tiver skill própria de voz, essa ganha.

## Passo 1. Obter o rascunho

Se já foi colado na mesma mensagem, usar. Caso contrário:

> Cola o rascunho que queres avaliar, e diz-me para que plataforma é.

Esperar. Não avaliar um texto imaginado.

## Passo 2. Escolher a fonte de dados

**Dependências externas são opcionais.** Nada aqui exige API, chave ou ferramenta instalada, em passo nenhum. Se **AskUserQuestion** não estiver disponível, fazer as mesmas duas perguntas em texto corrido, numeradas, num turno só — o resto da skill corre igual.

```json
[
  {"question": "Com que histórico queres que eu compare este rascunho?", "header": "Dados", "multiSelect": false,
   "options": [
     {"label": "Tenho a exportação", "description": "Ficheiro de Insights do Instagram/Facebook ou introdução manual. TikTok está LOOK INTO. CSV ou XLSX."},
     {"label": "Escrevo os números à mão", "description": "Digo-te as peças recentes com alcance e interações. Quantas mais, melhor — e digo-te na entrega o que essa amostra permite concluir."},
     {"label": "Já exportei antes", "description": "Procura em Social Media/dados/ ou na pasta do projeto o que já lá está."},
     {"label": "Sem histórico", "description": "Avalia só contra o perfil de marca e o ofício. Perde-se a comparação com o que já funcionou — e digo-o na entrega."}
   ]},
  {"question": "Que comportamento é que esta peça tem de provocar?", "header": "Objetivo", "multiSelect": false,
   "options": [
     {"label": "Guardar", "description": "Conteúdo de referência a que se volta"},
     {"label": "Enviar a alguém", "description": "O sinal mais forte para chegar a quem não segue"},
     {"label": "Comentar ou perguntar", "description": "Abrir conversa, tipicamente para venda por mensagem"},
     {"label": "Ir ao link ou pedir orçamento", "description": "Ação fora da plataforma — o degrau mais caro"}
   ]}
]
```

**Números não chegam — é preciso o texto.** A exportação dá métricas; para detetar tipo de gancho, extensão e chamada à ação das peças antigas é preciso o **conteúdo** delas. Se a exportação escolhida não trouxer uma coluna com a legenda, pedir os textos das peças que ficaram acima da mediana. Sem eles, a comparação com o histórico limita-se a formato e tema — e a entrega tem de o dizer.

**Onde se vai buscar cada exportação** (dizer só se perguntarem; os caminhos de interface mudam sem aviso, confirmar no ecrã real):
- Instagram — Meta Business Suite → Insights → intervalo de datas → Exportar. ⬤ As métricas **de conta** do Instagram só estão disponíveis até **90 dias** para trás (documentação da API); as de peça duram mais. O que não se exportar, perde-se.
- Facebook — mesmo caminho. ◐ A janela do Facebook **não é a mesma do Instagram** e não tem número declarado que eu possa citar: exportar o intervalo mais longo que a interface aceitar e registar as datas efetivas no ficheiro.
- TikTok — `LOOK INTO`; não dar instruções atuais de exportação ou retenção nesta versão.
- Se o ficheiro guardado for visivelmente mais antigo do que o rascunho a avaliar, dizê-lo e propor exportar de novo. ◐ Não há prazo de validade publicado — a regra é comparar o rascunho com um período que ainda descreva a conta de hoje.

## Passo 3. Construir o perfil de referência — e testar se ele existe

Antes de pontuar, **verificar se há base para pontuar**. Esta é a parte da skill que mais vale.

1. Contar quantas peças há e que alcance mediano têm. **Mediana, nunca média** — a distribuição em social é enviesada por virais.
2. Aplicar o **teste de amostra** abaixo. Se falhar, a pontuação sai na mesma mas **rotulada como juízo de ofício, não como leitura de dados**.
3. Se passar, agrupar as peças por **tema e formato** (não uma a uma) e registar o padrão de cada grupo: extensão mediana, tipo de gancho, formato, chamada à ação, comportamento pedido.
4. Marcar como padrão **só o que se repete três vezes ou mais** — regra dos três do módulo 07. Uma observação é nota, duas são hipótese.

### Teste de amostra — obrigatório, e dito em voz alta

| Situação | O que se pode dizer |
|---|---|
| Menos de 8 a 12 semanas de dados **por formato** | ◑ Ainda não há base própria. Só ofício. É a única quantidade ancorada numa fonte: módulo 11, *o que uma conta pequena deve concluir*. |
| Poucas peças dentro do mesmo formato | Nenhuma comparação entre peças é conclusiva. ⚠️ **Não fixar um limiar de alcance.** Os números que circulam ("500 impressões por variante") são regras práticas sem origem estatística e estão na lista de folclore do módulo 11. Descrever a amostra em vez de a aprovar ou reprovar contra um número inventado. |
| Padrão observado 1 ou 2 vezes | ◐ Nota ou hipótese — **não** muda o plano. |
| Padrão observado 3+ vezes | ◐ Hipótese de trabalho. Pode fundamentar uma correção. Regra dos três, módulo 07 — prática defensável, não método estatístico. |
| Série que atravessa 21 de abril de 2025 | ⬤ O Instagram substituiu impressões e reproduções por **visualizações**. Série partida — declarar. |

Escrever isto na entrega, com o número real. Uma frase do género *"isto são 340 pessoas de alcance mediano em 7 posts: não dá para concluir nada, o que se segue é juízo de ofício"* é mais útil do que qualquer pontuação.

**Comparar formato com formato.** Um rascunho de Reel compara-se com Reels, não com imagens únicas: ⬤ as métricas mudaram de nome e de definição entre formatos, e ⬤ o alcance da Meta não é aditivo — somar alcance de várias peças não desduplica pessoas e o resultado não significa nada.

⚠️ **Nunca comparar a taxa desta conta com um benchmark cuja metodologia não se verificou** (módulo 11). E ⬤ o alcance da Meta é amostrado, não contado — variações pequenas entre semanas podem ser ruído.

## Passo 4. Pontuar

Cinco critérios, 1 a 10 cada, total sobre 50. **A escala é um instrumento desta skill para ordenar prioridades de correção, não uma medição.** Não a apresentar como se fosse um dado, nem comparar totais entre avaliações feitas com bases de dados diferentes.

1. **Gancho** — imediato, específico e **cumprível**. Um gancho que promete mais do que o corpo entrega compra o primeiro segundo e destrói a retenção, que é o sinal que mais pesa. Critérios em `references/04`. Com histórico, 8+ exige que o tipo de gancho coincida com um padrão confirmado três vezes; **sem histórico**, 8+ exige execução manifestamente boa nos três critérios e a nota sai marcada como juízo de ofício.
2. **Voz** — contra a secção 5 do perfil: tratamento, adjetivos de tom, palavras da casa, palavras proibidas, grafias fixas, emojis. Comparar com os exemplos aprovados, que valem mais do que os adjetivos.
3. **Substância** — há facto, história, prova ou passo concreto? Ou é texto plausível e vazio? Sem matéria-prima real fornecida por um humano, este critério não passa de 5.
4. **Estrutura e formato** — uma ideia só, uma chamada à ação só, legível no telemóvel, a viragem antes do corte do "ver mais". Vídeo curto: rácio confirmado para a superfície, guião em duas colunas e compreensão sem depender do som. Shorts podem ser quadrados ou verticais (PLAT-017); TikTok está `LOOK INTO`. **Testar contra o comportamento escolhido no Passo 2:** a peça pede esse degrau e só esse, e a escada de atrito do módulo 04 diz que o que a peça deu chega para o pedir? Uma peça excelente que pede o degrau errado leva nota baixa aqui.
5. **Pronto a publicar** — lista de riscos, cada um a abater a nota por si só:
   - preço, prazo, disponibilidade ou condição **não confirmados por um humano**;
   - alegação sujeita a regulação, ou que a marca não consiga provar (módulo 10, secção 6 do perfil);
   - conteúdo de terceiros sem **autorização escrita** — uma marcação não transfere licença nem direito de imagem;
   - testemunho, fotografia ou caso de cliente sem consentimento **para este fim concreto** (RGPD, módulo 10);
   - música: ⚠️ numa conta de empresa, um áudio em tendência pode não estar coberto por licença comercial, e a licença da Meta Sound Collection **não** acompanha o vídeo para outras plataformas; TikTok está `LOOK INTO` e o YouTube exige confirmação própria (módulo 10);
   - imagem, vídeo ou áudio realista gerado ou alterado por IA **sem cumprir a política atual da plataforma** — ⬤ a Meta aplica "AI Info"; TikTok está `LOOK INTO`; e nunca depoimentos, casos ou resultados inventados, com ou sem rótulo (módulo 04);
   - **acessibilidade**, item a item e não como impressão geral: texto alternativo escrito (e por slide, num carrossel), legendas revistas **manualmente**, ⬤ contraste mínimo 4,5:1 para texto normal e 3:1 para texto grande pela WCAG 2.2 AA, informação essencial que não vive só na cor nem só na imagem, hashtags em CamelCase;
   - isco de interação ⬤ — o Facebook declara despromover publicações que pedem explicitamente gostos, partilhas, comentários ou votos; PLAT-007. O Instagram proíbe recolher artificialmente interação. ⚠️ Distinguir de uma pergunta genuína ou de uma sondagem: o problema é pedir a reação pela reação.

**Ser duro.** Um avaliador generoso não serve para nada. 8+ exige o que está escrito em cada critério — não simpatia.

## Passo 5. Entregar

Em bloco de código, compacto:

```
AVALIAÇÃO — [plataforma] · [data]

Fonte de dados:   [exportação IG/Facebook / manual / nenhuma; TikTok: LOOK INTO]
Peças analisadas: [n]   Alcance mediano: [n]
Base:             [LEITURA DE DADOS | JUÍZO DE OFÍCIO — amostra insuficiente]
Comportamento:    [o degrau escolhido no Passo 2]

Gancho              [x]/10   [tipo detetado]
Voz                 [x]/10
Substância          [x]/10
Estrutura/formato   [x]/10
Pronto a publicar   [x]/10
--------------------------------
TOTAL               [xx]/50
(escala interna para ordenar correções, não uma medição)

VEREDICTO: [uma frase]
```

Se a voz não pôde ser pontuada por não haver perfil, escrever `—` nessa linha e `TOTAL [xx]/40`. Não inflacionar o total com uma nota inventada.

Depois do bloco:

- **O que a amostra permite dizer** — a frase honesta do Passo 3, com o número.
- **Comparação com o histórico** — só padrões vistos 3+ vezes, com a contagem ao lado. Nunca "os teus melhores posts são assim" a partir de dois casos.
- **Três correções**, cada uma com a base declarada: `[3 de 4 peças acima da mediana abriam com um número; esta abre com pergunta]` ou, sem dados, `[ofício, módulo 04]`. Não "melhora o gancho".
- **Buracos** — o que ficou `[POR CONFIRMAR]` e quem confirma.

Terminar:

> Queres que reescreva a parte mais fraca, ou publicas assim?

## Regras

- **Português europeu.** Sem gerúndio de ação em curso, sem "você", sem vocabulário do Brasil.
- **Nunca decidir com um post.** Nem o rascunho nem o histórico. Grupos, sempre.
- **Nunca citar um número sem amostra.** Se não estiver no perfil nem no módulo 11, não entra. E manter a marcação ⬤ / ◑ / ◐ em tudo o que se cite a partir dos módulos.
- **Nunca comparar métricas diferentes com o mesmo nome** — nem entre formatos, nem entre plataformas, nem através de 21 de abril de 2025.
- **Sem histórico não se inventa histórico.** Dizer que se está a avaliar por ofício é a resposta certa, não uma falha.
- **Não usar a exportação de outra conta como referência.** Comparar-se com uma conta grande de outro setor não é análise.
- **Nunca aconselhar apagar um post por desempenho** — apagar é apagar o dado que faltava.
- Preços, prazos, alegações reguladas e conteúdo de terceiros **não passam sem humano**.
- Se a mesma correção sair três vezes em avaliações diferentes, registar na secção 11 do perfil. É aprendizagem, não repetição.
- Não resumir esta skill ao utilizador. Executá-la.
