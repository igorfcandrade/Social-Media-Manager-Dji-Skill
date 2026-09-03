# 9 — Tendências, concorrência e parcerias

Saber o que se passa sem perseguir tudo, e aprender com quem está à volta sem copiar.

**Última verificação de fontes:** 30/08/2026.

**Cadência:** vigilância leve semanal · recap manual mensal e incremental · descoberta alargada de novas fontes de dois em dois meses · registo competitivo mensal, sempre no mesmo dia · revisão do conjunto competitivo semestral.

**Delegabilidade:** ✓ Alta. A recolha, a comparação e o registo são delegáveis. A decisão de entrar numa tendência é humana, porque envolve identidade, oportunidade e risco reputacional.

## Tendência, sinal e previsão não são a mesma coisa

- **Sinal observado:** há evidência datada de que um assunto, formato ou comportamento está a crescer numa fonte concreta.
- **Tendência confirmada:** o sinal persiste ou aparece em mais do que uma fonte relevante para o público e a geografia da marca.
- **Previsão:** alguém estima o que acontecerá depois. Serve para descobrir hipóteses, não para as declarar verdadeiras.

◐ Relatórios de previsões, listas de tendências anuais e observações de outros mercados entram na fase de **descoberta**. Só passam a recomendação depois de serem observados em Portugal ou nos dados da própria conta.

## O critério para entrar

Uma tendência só entra se sobreviver a **três** perguntas:

1. **Soa à marca?** Uma marca que comunica com calma não adota humor barulhento só porque está na moda.
2. **Ainda estará relevante quando o conteúdo estiver pronto?** Chegar tarde é pior do que ignorar.
3. **Há risco de contexto?** Confirmar a origem do áudio, do formato, da frase ou da piada antes de os associar à marca.

◑ A janela pode ser curta e o público nota a falta de adequação: num inquérito a **4.044 consumidores que seguiam pelo menos cinco marcas**, cerca de um terço considerou constrangedor uma marca aderir a tendências virais e 27% disse que uma tendência só funcionava nas primeiras 24 a 48 horas. É **autodeclaração de atitude**, não comportamento observado, e não prova uma janela universal. [Sprout Social, 2025](https://investors.sproutsocial.com/news/news-details/2025/The-Days-of-Trend-Chasing-Are-Over-New-Research-from-Sprout-Social-Reveals-a-Third-of-Consumers-Think-Jumping-on-Viral-Trends-is-Embarrassing-for-Brands/)

◐ Tendências de nicho e mudanças duradouras de formato tendem a merecer uma avaliação diferente de uma piada do momento. **Para um negócio pequeno, recusar a maioria das tendências é um resultado válido.**

**A exceção que vale investigar:** uma mecânica que se está a estabelecer e serve um pilar existente. Nesse caso, adota-se a mecânica com calma; não se copia a execução alheia.

## Registo mínimo de cada sinal

Sem este registo, “está a dar” é apenas uma impressão:

| Campo | O que escrever |
|---|---|
| Candidato | Assunto, formato, comportamento ou áudio |
| Observado em | Fonte e ligação direta |
| Data e geografia | Quando foi observado e que mercado representa |
| Trajetória | A subir, estável ou a cair; ou `não verificável` |
| O que prova | O sinal que a fonte permite concluir |
| O que não prova | Volume absoluto, intenção de compra, adequação à marca ou outra limitação |
| Decisão | Observar · testar · adotar · recusar |
| Validade | Data em que se volta a verificar ou se arquiva |

◐ **Triangulação útil:** cruzar pelo menos um sinal externo com dados da própria conta, pesquisa do público ou observação numa segunda fonte. Duas páginas a repetir a mesma notícia não são duas fontes independentes.

## Memória e recap manual

A vigilância tem duas camadas, como o resto do sistema:

| Camada | Estado corrente | Histórico |
|---|---|---|
| **Ofício — fontes e ferramentas da skill** | `09-estado-da-vigilancia.md` | `recaps-tendencias/AAAA-MM-DD.md` |
| **Marca — sinais do nicho e decisões** | `Social Media/tendencias/ESTADO.md` | `Social Media/tendencias/recaps/AAAA-MM-DD.md` |

Se o estado da marca não existir, criar a partir de `../assets/ESTADO-TENDENCIAS-modelo.md`. O estado corrente diz **o que se sabe agora**; cada recap guarda o snapshot que permite provar o que mudou.

### O lembrete não é uma automatização

Em cada utilização da skill governante, ler apenas o bloco `Calendário` dos estados disponíveis:

- se a data ainda não chegou, não dizer nada;
- se chegou ou passou, informar uma vez por conversa: `Recap mensal devido desde DD/MM/AAAA; último concluído em DD/MM/AAAA`;
- **não pesquisar, não escrever o recap e não atualizar datas** sem pedido explícito do utilizador;
- o pedido de uma pesquisa avulsa não autoriza nem conta como recap.

O recap só fica concluído quando o ficheiro datado é gravado, o estado corrente é atualizado e as próximas datas ficam registadas. Num ambiente sem escrita, entregar um rascunho e declarar que o recap continua pendente.

### Recap mensal normal — incremental para poupar tokens

1. Ler o estado corrente e **apenas o recap imediatamente anterior**; não carregar todo o histórico.
2. Verificar as fontes ativas, os itens cuja data de revisão venceu e as observações pendentes. Não repetir uma pesquisa geral já fechada.
3. Comparar pelos IDs estáveis e classificar cada linha: `novo`, `reforçado`, `sem alteração`, `enfraquecido`, `expirado`, `refutado` ou `retirado`.
4. Mostrar primeiro as diferenças, incluindo fonte, data e impacto na decisão. `Sem alteração` aparece num resumo, não ocupa uma explicação longa.
5. Resolver as observações pendentes; nada altera silenciosamente o conhecimento corrente entre recaps.
6. Guardar o snapshot depois do recap, atualizar `Último recap concluído` e marcar o próximo para **um mês de calendário depois**. Se o dia não existir nesse mês, usar o último dia.

### De dois em dois meses — descoberta de fontes

Quando `Próxima descoberta alargada de fontes` estiver vencida, o recap autorizado acrescenta uma procura limitada de fontes que ainda não façam parte do sistema. Avaliar cada candidata por:

- autoridade e proximidade ao facto;
- metodologia, amostra, geografia e atualidade;
- utilidade que acrescente às fontes já existentes;
- acesso sustentável, custo e conflitos de interesse;
- limite: o que permite e o que não permite concluir.

Registar candidatas **aceites e rejeitadas**, com a razão. Não acrescentar uma fonte apenas para aumentar a lista. Depois, marcar a próxima descoberta para dois meses de calendário mais tarde.

### Comparação obrigatória entre recaps

Cada recap começa com:

| ID | Antes | Agora | Tipo de alteração | Prova e data | Impacto / decisão |
|---|---|---|---|---|---|

Se for o primeiro recap, declarar `linha de base — sem comparador`. O responsável humano lê e decide sobre entradas com risco reputacional. O nome vem do perfil da marca do projeto; se não estiver registado, perguntar antes de tratar qualquer entrada como aprovada.

## Vigilância sem ruído

Fontes por ordem de fiabilidade:

1. **Anúncios oficiais das plataformas** — blogues de produto, páginas de ajuda e salas de imprensa. É a única categoria que este sistema aceita como fonte primária sobre uma funcionalidade.
2. **Dados da própria conta** — mostram o que mudou naquele público, embora não expliquem porquê.
3. **Relatórios com metodologia declarada** — ler amostra, geografia, período e financiador.
4. **Contas de referência** — dão hipóteses de formato, nunca explicações de algoritmo.

O que **não** vale como prova: notícias de algoritmo em blogues que citam outros blogues, capturas sem ligação ou listas de previsões sem método.

**Registo de alterações de plataforma:** o método está em `05-plataformas.md`, o estado corrente em `05-estado-das-plataformas.md` e os snapshots em `recaps-plataformas/AAAA-MM-DD.md`. Cada mudança separa anúncio, entrada em vigor, rollout e verificação, com fonte, âmbito, confiança e implicação prática — ou a nota `sem ação`. A interface de uma ferramenta pode mudar sem que a estratégia tenha de mudar.

## Onde olhar — e o que cada fonte não prova

### TikTok Creative Center — LOOK INTO

Fora da cobertura atual. Não usar disponibilidade, filtros, tendências, áudio ou geografia como informação corrente. Uma revisão futura exige autorização e fontes oficiais relidas.

### Google Trends

⬤ Mostra uma amostra anonimizada e agregada das pesquisas Google, normalizada por localização e período numa escala relativa de **0 a 100**. O valor não é volume absoluto; `0` pode significar dados insuficientes. A própria Google avisa que não é uma sondagem e deve ser apenas um sinal entre outros. [Perguntas frequentes do Google Trends](https://support.google.com/trends/answer/4365533?hl=pt)

**Serve para:** comparar sazonalidade, termos e geografia. **Não serve para:** afirmar quantas pessoas pesquisaram, medir intenção de compra ou tratar diferenças pequenas como precisão estatística.

### Biblioteca de Anúncios da Meta

⬤ Permite pesquisar anúncios ativos nas plataformas Meta. Para anúncios apresentados na União Europeia, o arquivo inclui também anúncios que correram no último ano; informação nova e alterações podem demorar até cerca de 24 horas a aparecer. [Biblioteca de Anúncios da Meta](https://www.facebook.com/ads/library/)

**Serve para:** ver mensagens, formatos, ofertas e duração observável. **Não prova:** orçamento, segmentação completa, rentabilidade ou vendas do concorrente.

### Instagram — por verificar na conta

⬤ Em 2023, a Meta anunciou uma área dedicada a áudio e assuntos em tendência no Reels. [Meta, anúncio da funcionalidade](https://about.fb.com/news/2023/04/instagram-reels-trending-audio-and-gifts-updates/) A disponibilidade atual pode variar por conta e região, e a documentação pública não dá uma matriz por país. **Não assumir disponibilidade em Portugal:** verificar na própria conta e registar `não disponível` se for o caso.

### Pesquisa dentro das plataformas ◐

Sugestões automáticas são pistas de linguagem e de procura, não uma escala pública de popularidade. Podem ser filtradas ou personalizadas. Usá-las para descobrir perguntas e sinónimos; nunca para afirmar volume.

### Avaliações e comentários públicos ◐

Queixas repetidas ajudam a descobrir objeções e lacunas. **Resumir padrões em palavras próprias**; não republicar nomes, fotografias, capturas ou detalhes pessoais. Um comentário isolado não representa o mercado.

### Dados da própria conta

São a confirmação mais próxima do público real da marca. Comparar grupos de peças e períodos equivalentes; uma publicação isolada não confirma uma tendência.

## Análise de concorrência: o método

Escolher **8 a 12 contas comparáveis** e registar **sempre no mesmo dia do mês**:

1. Número de seguidores, com data
2. Número de publicações no período
3. Divisão por formato
4. Interações visíveis nas últimas 9 publicações comparáveis
5. Taxa de interação **estimada**: interações médias visíveis ÷ seguidores
6. As 3 publicações com melhor resultado visível e uma hipótese sobre a razão
7. Notas: posicionamento, campanhas, promoções, preços e mudanças observáveis

Os números acima são **escolhas operacionais para manter uma série gerível**, não referências de indústria. Se forem alterados, registar a quebra de método.

**Regras da série:**

- manter a lista fixa durante um ciclo comparável — por defeito, seis meses;
- recolher no mesmo dia ou janela mensal;
- incluir 2 ou 3 contas mais desenvolvidas e pelo menos uma de fora do setor com público semelhante;
- não misturar plataformas na mesma taxa;
- guardar capturas ou ligações só para investigação interna, respeitando direitos e dados pessoais.

## O que não se vê de fora

**Alcance, impressões, guardados, envios, tráfego e vendas são normalmente invisíveis.** Os gostos podem estar ocultos, as publicações têm idades diferentes e “interações ÷ seguidores” usa um denominador que não é o alcance real.

Consequência: **a taxa pública é uma estimativa metodológica, não uma medida de sucesso do negócio.** Usar a concorrência para ideias, lacunas e cadência; julgar a própria conta pelos seus dados e resultados.

Uma conta com números visíveis fracos pode vender por mensagem privada; uma conta com números fortes pode não converter. Não há forma pública de decidir entre as duas.

## Análise de lacunas

Perguntas mais úteis do que “quem teve mais gostos?”:

- Que perguntas do público ninguém responde?
- Que objeção toda a gente evita?
- Que formato não aparece — por falta de competência, por risco ou porque já falhou?
- Que posição está livre? Se todos falam de preço, pode sobrar qualidade; se todos falam de qualidade, pode sobrar conveniência.

◐ Em negócios pequenos, uma lacuna recorrente é responder às perguntas práticas que parecem pouco vistosas: prazos, cuidados, critérios de escolha e o que pode correr mal. Confirmar sempre no perfil, nas mensagens e na pesquisa real; não assumir que a lacuna existe.

## Parcerias e criadores

**Escolher por adequação, não por seguidores.** Verificar:

- sobreposição entre audiência e público da marca, incluindo geografia;
- qualidade e natureza dos comentários, sem tratar uma ferramenta de “audiência falsa” como prova definitiva;
- conflitos com concorrentes, histórico de segurança de marca e coerência de valores;
- identidade e propriedade da conta antes de enviar produto, dinheiro ou acessos;
- capacidade de atribuir resultado por código, ligação UTM ou pergunta de origem.

**Combinar por escrito:** entregáveis, calendário, plataformas, aprovação, identificação publicitária, direitos de utilização, território, duração, alterações, arquivo e condições de retirada. Autoria, direito de imagem e licença de música são direitos diferentes.

**A divulgação é obrigação, não cortesia** — ver `10-risco-crise-e-conformidade.md`.

## Modos de falha

- Confundir previsão com tendência observada.
- Declarar Portugal quando o filtro usado era global ou não estava visível.
- Tratar a escala 0–100 do Google Trends como volume de pesquisas.
- Prometer uma funcionalidade que só existe noutra região ou conta.
- Perseguir tendências fora de janela ou fora de personagem.
- Usar um áudio ou formato sem confirmar origem e licença.
- Mudar a amostra ou a fórmula a meio da série competitiva.
- Comparar taxas entre plataformas ou julgar vendas por interações públicas.
- Copiar a execução de uma conta maior em vez de testar a mecânica.
- Reagir a cada notícia de algoritmo com uma revisão de estratégia.
- Escolher parceiros pelo número de seguidores ou contratar sem acordo escrito.
- Confundir vigilância com distração.

## Do perfil de marca

Conjunto competitivo e data de fixação · posicionamento · público e perguntas · pilares · o que a marca não faz · tempo de produção · geografia · orçamento e critérios para parcerias.
