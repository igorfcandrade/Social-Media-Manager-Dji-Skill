# 5 — Plataformas e algoritmos

Como cada superfície decide o que mostra a quem, o que está **declarado** pelas próprias empresas, e o que é folclore.

**Cadência:** verificação de conformidade antes de publicar · leitura por formato semanal · auditoria de perfis mensal · revisão do mix de plataformas e da tabela de specs trimestral.

**Delegabilidade:** ✓ Alta, com uma condição: esta área envelhece mais depressa do que qualquer memória. **Nunca responder de memória sobre algoritmos** — quase de certeza cita-se uma regra revogada. Exigir sempre fonte datada e nível de confiança.

> ⚠️ Este módulo explica o método e guarda contexto. O estado atual dos factos voláteis vive em `05-estado-das-plataformas.md`. Uma data de publicação não é automaticamente a data efetiva, e nenhuma revisão interna prevê a próxima mudança da plataforma. A cobertura validada inclui Instagram, Facebook, Graph API, Google Business Profile, WhatsApp, YouTube e Pinterest. TikTok, Threads e X estão `LOOK INTO` e não fornecem regras atuais.

## Três verdades estruturais

1. **Nenhuma plataforma grande deve ser tratada como se tivesse "um algoritmo".** Na Meta, existem sistemas separados para Feed, Reels, Stories, Pesquisa e outras experiências, com modelos e sinais dinâmicos. ⬤ [Meta AI, system cards, 29/06/2023](https://ai.meta.com/blog/how-ai-powers-experiences-facebook-instagram-system-cards/) · PLAT-001.
2. **Alcance conectado e recomendado são problemas diferentes.** Os volumes e a influência da dimensão da conta mudam por superfície e ao longo do tempo; não usar uma percentagem global como regra. Separar as métricas e validar na conta.
3. **A pesquisa dentro das apps é uma superfície própria.** Não assumir que hashtags, nomes, legendas ou transcrições têm os mesmos campos ou pesos em todas as plataformas.

## Grelha de diagnóstico: as quatro etapas

Quando algo não funciona, usar como grelha de diagnóstico as quatro etapas que a Meta publica para os seus sistemas de ranking. É uma forma de pensar o problema, não prova de que todas as plataformas implementem o mesmo processo. ⬤ [Meta, ranking e conteúdo](https://transparency.meta.com/features/ranking-and-content/) · PLAT-001.

```
1. inventário elegível  →  2. sinais  →  3. previsões  →  4. pontuação
```

Perguntar em que etapa falhou, porque a resposta é diferente em cada uma:

- **Etapa 1 — elegibilidade.** Verificar diretrizes, direitos, originalidade e qualidade técnica. Marca de água, republicação e baixa resolução são hipóteses de diagnóstico, não causas atuais universais; no Instagram, consultar PLAT-002 e o snapshot histórico PLAT-011.
- **Etapa 2 — sinais.** A conta não tem histórico com aquela audiência. Resolve-se com tempo e consistência, não com escrita.
- **Etapa 3 — previsões.** O conteúdo não gera o comportamento que a plataforma tenta prever. **É a única etapa que se resolve escrevendo melhor.**

Culpar o algoritmo por um problema de retenção nos primeiros segundos, de oferta pouco clara ou de audiência mal definida faz errar o diagnóstico e a correção.

## Alcance conectado vs. não-conectado

A separação mais útil de toda a área: chegar a quem já segue e chegar a quem não segue são distribuídos por sistemas diferentes, respondem a sinais diferentes e servem objetivos diferentes.

**Separar as duas métricas em todos os relatórios e nunca somar.** Uma queda no total pode esconder uma subida no que importa — ou o contrário.

- Objetivo de aquisição → alcance não-conectado, e o que o desbloqueia (envios, partilhas, retenção).
- Objetivo de retenção ou conversão → alcance conectado, e guardados, respostas e cliques.

## Escada de sinais

Hierarquia prática, do gesto mais barato ao mais caro para quem vê. Quanto mais caro o gesto, mais peso costuma ter na distribuição a não-seguidores:

```
ver (retenção, dwell time) → reagir → aprofundar (comentar, guardar) → propagar (enviar, partilhar)
```

Escolher, para cada peça, **qual o degrau** que se está a tentar provocar. Uma peça desenhada para ser guardada tem estrutura diferente de uma desenhada para ser enviada a um amigo.

---

## Instagram

◐ O explicador oficial de 2023 descrevia sistemas próprios por superfície e os seguintes grupos de sinais. É um snapshot histórico cuja fonte não foi relida nesta revisão, não uma tabela atual de pesos. [Instagram, Ranking Explained, 31/05/2023](https://about.instagram.com/blog/announcements/instagram-ranking-explained) · PLAT-011.

| Superfície | Grupos de sinais descritos em 2023 |
|---|---|
| Feed | Atividade do utilizador, informação do post, informação de quem publica, **histórico de interação entre os dois** |
| Stories | Histórico de visualização e de interação, proximidade da relação |
| Explorar | Informação do post; o explicador dizia que a popularidade era mais relevante aqui; atividade no Explorar; histórico com quem publica |
| Reels | Atividade, histórico com quem publica, informação do reel **incluindo o áudio** |

**Leitura do snapshot de 2023:** Feed e Stories davam mais contexto à relação prévia; Explorar e Reels davam mais contexto ao interesse no conteúdo. Serve para distinguir superfícies, não para afirmar pesos atuais nem prometer vantagem a uma conta pequena.

Tempo de visualização, gostos por alcance e envios por alcance são métricas úteis para comparar grupos de peças na própria conta. **Não existe neste sistema uma fonte atual que lhes atribua pesos universais.** O número de que “um envio vale 3 a 5 vezes um gosto” não tem origem oficial conhecida e não se usa.

◐ Em 2023, o Instagram declarou que procurava tornar menos visíveis Reels de baixa resolução, com marca de água, sem som, com bordas, maioritariamente texto ou já publicados no Instagram. [Instagram, Ranking Explained, 31/05/2023](https://about.instagram.com/blog/announcements/instagram-ranking-explained) · PLAT-011. A fonte não foi relida nesta revisão; tratar a lista como histórica até nova verificação. Reexportar limpo e legível continua a ser boa prática independente.

◐ **Originalidade:** a orientação publicada em 30/04/2026 abrange Reels, fotografias e carrosséis. Contas que publiquem sobretudo conteúdo não original podem ficar fora das recomendações; alterações cosméticas não contam como contribuição criativa, e a recuperação é descrita por maioria de conteúdo recente original numa janela móvel de 30 dias. [Instagram for Creators, 30/04/2026](https://creators.instagram.com/blog/rewarding-original-creators-on-instagram) · PLAT-002. A fonte não foi relida nesta revisão nem declara uma data global de entrada em vigor; confirmar o Estado da conta.

◐ **Hashtags:** a conta oficial Instagram for Creators anunciou em 18/12/2025 um rollout gradual para até cinco hashtags na legenda de posts e Reels. [Anúncio oficial no Threads](https://www.threads.com/@creators/post/DSalXGPCWM4) · PLAT-003. A publicação não foi relida nesta revisão. Cinco é um máximo seguro para produção; o limite efetivo confirma-se no compositor da conta e a data do anúncio não é uma data global de entrada em vigor.

◐ **Pesquisa:** o explicador de 2021 dizia que o texto pesquisado era o sinal principal e o comparava com nomes de utilizador, biografias, legendas, hashtags e locais; atividade e popularidade entravam depois. [Instagram, Pesquisa, 25/08/2021](https://about.instagram.com/blog/announcements/break-down-how-instagram-search-works) · PLAT-004. É uma descrição histórica oficial cuja fonte não foi relida nesta revisão, não uma especificação atual de pesos. Usar linguagem clara é defensável; prometer que um campo “pesa mais” hoje exige fonte mais recente.

## Facebook

⬤ A Meta documenta sistemas separados e uma sequência de inventário, sinais, previsões e pontuação. Entre as previsões publicadas estão interação e valor percebido. [Meta, ranking e conteúdo](https://transparency.meta.com/features/ranking-and-content/) · PLAT-001.

> A previsão de conversa justifica testar perguntas genuínas; não prova que uma pergunta supere sempre um anúncio nem autoriza engagement bait.

⬤ **Engagement bait:** a Meta anunciou em 2017 a despromoção de pedidos artificiais de votos, reações, partilhas, marcações e comentários; a reincidência pode afetar a Página. Pedidos genuínos de ajuda, conselho ou recomendação foram excluídos. [Meta, 18/12/2017](https://about.fb.com/news/2017/12/news-feed-fyi-fighting-engagement-bait-on-facebook/) · PLAT-007.
> “Marca três amigos” e “comenta EU QUERO” correspondem aos padrões que a fonte manda despromover. O risco pode acumular-se ao nível da Página.

Ocultar, escolher “Não tenho interesse” e outros controlos dão feedback aos sistemas de recomendação. Não transformar esta conclusão numa “taxa de salto” universal sem definição e fonte atuais. [Meta AI, system cards](https://ai.meta.com/blog/how-ai-powers-experiences-facebook-instagram-system-cards/) · PLAT-001.

⬤ **Observação datada:** em 07/10/2025, a Meta disse que o motor então atualizado estava a mostrar **50% mais Reels de criadores publicados naquele dia**. A fonte não dá linha de base, janela de medição nem causalidade. [Meta, Reels no Facebook](https://about.fb.com/news/2025/10/finding-sharing-reels-facebook-just-got-easier-more-fun/) · PLAT-005. Não é uma regra atual de horário nem, por si só, razão para alterar o calendário.

⬤ **Originalidade:** em março de 2026, a Meta clarificou que reagir apenas com expressões faciais, juntar clips, narrar o que já está no ecrã ou fazer alterações menores sem contributo substancial pode ser classificado como não original. Pode haver despromoção e, com reincidência, perda de recomendação ou monetização. [Meta, originalidade no Facebook](https://about.fb.com/news/2026/03/rewarding-original-creators-on-facebook/) · PLAT-006.

⬤ No feed do Facebook nos EUA, cerca de **97,9% das visualizações não incluíam ligação para fora** no Q4 de 2024. [Meta, Widely Viewed Content Report](https://transparency.meta.com/reports/widely-viewed-content-report/).
> ⚠️ **Isto mede a composição do que foi visto, não supressão de links.** Não prova que a plataforma penalize ligações nem, por si só, decide onde pôr o esforço.
> O rácio de "30 vezes mais alcance em Grupos do que em Páginas" **não tem metodologia publicada por ninguém**. A direção é plausível; o número é folclore.

## TikTok

**LOOK INTO.** Fora da cobertura atual. Não usar este módulo para afirmar algoritmo, pesquisa, limites, formatos ou funcionalidades atuais do TikTok. Uma revisão futura exige autorização e fontes oficiais datadas.

## YouTube

⬤ **Pesquisa:** a documentação atual organiza os sinais em relevância, engagement e qualidade. Para relevância, o YouTube compara a pesquisa com título, tags, descrição e conteúdo do vídeo. [YouTube Search](https://support.google.com/youtube/answer/16090438?hl=en) · PLAT-016.

⬤ **Recomendações:** são personalizadas por pessoa e superfície. A orientação para criadores agrupa o desempenho em *appeal*, *engagement* e *satisfaction*; não publica pesos universais. [YouTube, desempenho de conteúdo](https://support.google.com/youtube/answer/16559650?hl=en) · PLAT-016.

⬤ **Tags:** continuam a existir, mas têm papel mínimo e são sobretudo úteis para grafias incorretas. Título, miniatura, promessa cumprida e satisfação recebem prioridade; não dizer que as tags desapareceram. [YouTube, desempenho de conteúdo](https://support.google.com/youtube/answer/16559650?hl=en) · PLAT-016.

⬤ **Shorts até três minutos:** vídeos quadrados ou verticais carregados desde 15/10/2024 em canais normais são classificados como Shorts. Em Official Artist Channels, a data é 08/12/2025. 9:16 é uma opção, não uma condição técnica. [YouTube, Shorts de três minutos](https://support.google.com/youtube/answer/15424877?hl=en-GB) · PLAT-017.

## Pinterest

⬤ **Distribuição:** um Pin pode começar a gerar engagement horas, dias, meses ou anos depois. A distribuição pode aumentar ou diminuir; não existe na documentação atual uma janela fixa de 7 a 30 dias. [Pinterest, desempenho e distribuição](https://help.pinterest.com/en/business/article/pin-performance-and-distribution) · PLAT-018.

⬤ **Metadados e especificações orgânicas:** título até 100 caracteres e descrição até 800, usada para relevância. Vídeo orgânico aceita 4 segundos a 5 minutos e vários rácios entre 1:2 e 9:16; 9:16 é recomendado para ecrã inteiro, não obrigatório. [Pinterest, especificações de Pins](https://help.pinterest.com/en/article/review-pin-specs) · PLAT-019.

1000×1500, “primeiros 40 caracteres visíveis” e 15 minutos não são tratados como limites universais de conteúdo orgânico. Separar sempre criação orgânica, anúncios e formatos compráveis.

## Threads e X

**LOOK INTO.** Threads e X estão fora da cobertura atual. Não usar este módulo para afirmar ranking, links, pesos, limites ou funcionalidades. Uma revisão futura exige autorização e fontes oficiais datadas.

## Google Business Profile

⬤ **Elegibilidade e nome:** é preciso contacto presencial com clientes durante o horário declarado; negócios apenas online não são elegíveis. Usar o nome real e categorias específicas, sem palavras-chave acrescentadas. [Google, elegibilidade](https://support.google.com/business/answer/13763036?hl=en) e [representação](https://support.google.com/business/answer/3038177?hl=en) · PLAT-012.

⬤ **Ranking local:** a Google declara relevância, distância e proeminência/popularidade, sem publicar pesos fixos nem uma ordem universal. Informação completa e exata, horários, avaliações e fotografias ajudam a representar o negócio. [Google, resultados locais](https://support.google.com/business/answer/7091?hl=en) · PLAT-013.

⬤ **Posts:** servem para comunicar novidades, ofertas, eventos e produtos. A documentação consultada não os declara fator de ranking; ausência de declaração também não prova efeito nulo. [Google, Posts](https://support.google.com/business/answer/7342169?hl=en) · PLAT-013.

O Google Business Messages terminou em 31/07/2024. Isso não autoriza afirmar que outras funcionalidades, como Perguntas e Respostas, foram retiradas sem uma fonte atual própria.

## WhatsApp

⬤ **Superfícies diferentes:** conversas, Estados e Canais não têm a mesma lógica. O separador Atualizações inclui Estados e Canais, e anúncios em Estados e Canais promovidos foram anunciados com rollout regional; por isso, “não tem feed nem descoberta” deixou de ser uma descrição universal. [Meta, Atualizações do WhatsApp](https://about.fb.com/news/2025/06/helping-you-find-more-channels-businesses-on-whatsapp/) · PLAT-014.

⬤ **Envios diferentes:** listas tradicionais, Business Broadcasts, Canais e Business Platform são produtos distintos. O limite de 256 e a condição de número guardado pertencem às listas tradicionais e não se aplicam universalmente; Business Broadcasts é pago e limitado a utilizadores elegíveis em países selecionados. [WhatsApp, listas](https://faq.whatsapp.com/861663048350950/?cms_platform=android&locale=pt_BR) e [Business Broadcasts](https://whatsappbusiness.com/products/business-app-features/) · PLAT-015.

Antes de recomendar volumes ou automatização, identificar o produto, o país, a conta, o consentimento e a forma de saída. Não usar escalões, preços ou fórmulas da API de memória.

---

## Hashtags: usar sem inventar alcance

Hashtags podem dar contexto, apoiar pesquisa e agregar uma campanha. **A skill não lhes atribui um aumento de alcance universal nem um número “ótimo”.** No Instagram, produzir até cinco é compatível com o rollout oficial conhecido, mas o limite efetivo confirma-se na conta (PLAT-003). Noutras plataformas, consultar a documentação e o registo atual antes de dar limites ou efeitos como certos.

O tempo de produção deve ir primeiro para clareza do tema, gancho e utilidade; hashtags entram depois, apenas quando ajudam a classificar ou encontrar a peça.

## Mapa de indexação

Antes de escrever, saber onde é que aquela plataforma vai buscar as palavras. Escrever para o campo errado é trabalho perdido.

| Plataforma | O que é indexado |
|---|---|
| Instagram | O explicador de 2021 listava nome de utilizador, nome de exibição, bio, legendas, hashtags e locais; confirmar atualidade (PLAT-004) |
| Facebook | Não há neste registo um mapa público, atual e estável de campos com pesos; desambiguar o pedido e verificar (PLAT-008) |
| TikTok | `LOOK INTO` — não existe mapa validado nesta cobertura |
| YouTube | Título, tags, descrição e conteúdo do vídeo; tags com papel mínimo (PLAT-016) |
| Pinterest | Título e descrição do Pin, com contexto do quadro e destino (PLAT-019) |
| Google Business Profile | A Google não publica pesos por campo; manter informação completa, exata e representativa (PLAT-012 e PLAT-013) |

Fazer a pesquisa de palavras **dentro da própria plataforma** (barra de pesquisa, sugestões automáticas, pesquisas relacionadas), não em ferramentas de SEO web.

## Lista de conformidade antes de publicar

- [ ] Sem marca de água de outra aplicação
- [ ] Sem bordas; resolução adequada; com som
- [ ] Não é republicação de conteúdo já publicado
- [ ] Contribuição criativa real, se o material tem origem em terceiros
- [ ] Hashtags dentro do limite confirmado na plataforma ou conta
- [ ] Sem engagement bait explícito
- [ ] Texto alternativo e legendas
- [ ] Rácio e duração corretos para a superfície pretendida
- [ ] Rótulo de IA, se aplicável

## Testar sem enganar-se

Uma variável de cada vez · métrica de decisão e janela definidas **antes** · repetições suficientes.

Usar mecanismos nativos quando existem e estão disponíveis na conta. Trial Reels são mostrados primeiro a não seguidores e a fonte oficial compara o desempenho com trials anteriores; por isso, **comparar trial com trial, não trial com uma publicação normal**. [Meta, Trial Reels](https://about.fb.com/news/2024/12/trial-reels-try-content-non-followers-first-see-what-perfoms-best/) · PLAT-010.

## Registo de alterações

O ficheiro vivo é `05-estado-das-plataformas.md`; os snapshots ficam em `recaps-plataformas/AAAA-MM-DD.md`. Cada mudança separa publicação, entrada em vigor, rollout e verificação, com fonte primária, âmbito, confiança e implicação prática — **ou a nota explícita de que não há implicação nenhuma**.

A maior parte das entradas deve terminar em "sem ação". O valor do registo está em travar a reação impulsiva a cada notícia de algoritmo, e em ter uma resposta com fonte quando alguém perguntar.

## Modos de falha

- Responder de memória sobre algoritmos e citar uma regra revogada.
- Exportar o mesmo ficheiro entre plataformas com marca de água — má prática de qualidade e autoria; qualquer efeito atual na distribuição confirma-se por plataforma (PLAT-011 é histórico).
- Tratar o anúncio de cinco hashtags como uma data global fixa, sem confirmar o limite da conta.
- Usar engagement bait num Facebook onde a despromoção está declarada desde 2017 e penaliza a Página.
- Copiar "as melhores horas para publicar" de estudos globais em vez de olhar para os dados da própria conta.
- Confundir alteração de métrica com alteração de desempenho.
- Somar alcance conectado e não-conectado num número único.
- Estar em cinco plataformas com o mesmo conteúdo cortado.
- Ignorar o Google Business Profile num negócio elegível que atende clientes presencialmente.
- Manter checklists que mandam ativar o Google Business Messages, encerrado em 31/07/2024.
- Tratar conversas, Estados, Canais, listas tradicionais e Business Broadcasts como se fossem a mesma superfície do WhatsApp.
- Repetir folclore: "30x mais alcance em Grupos", "um envio vale 3-5 gostos".
- Reagir a cada notícia de mudança com uma revisão de estratégia.
- Perseguir viralidade num negócio que serve um raio de vinte quilómetros.

## Do perfil de marca

Plataformas escolhidas e recusadas · quem alimenta cada uma · área geográfica · captar procura existente ou criar procura · formatos sustentáveis · quem aparece em câmara · restrições regulatórias · língua e mercado.
