# Estado das plataformas

> Registo canónico de afirmações voláteis sobre plataformas. Para saber se a revisão programada está em dia, ler apenas o bloco **Calendário**. Para usar uma afirmação, ler o registo completo do respetivo ID e seguir o campo **Implicação**.

## Calendário

- **Estado:** em dia para a cobertura declarada
- **Última revisão concluída:** 2026-09-03
- **Próxima revisão programada:** 2026-10-01
- **Revisões concluídas:** 4 — linha de base · expansão a Google, WhatsApp, YouTube e Pinterest · expansão ao pago · correção dirigida da segmentação Meta
- **Responsável humano:** `POR DEFINIR` — o nome vem do perfil da marca deste projeto, não desta skill
- **Último recap:** recaps-plataformas/2026-09-03.md
- **Cobertura atual:** Meta orgânico — Instagram e Facebook —, governação da Graph API, Google Business Profile, WhatsApp, YouTube e Pinterest; e **mecânica de campanha paga** na Meta, Google Ads e Pinterest — limiares de aprendizagem e medição e, na Meta, segmentação de audiência e exclusões, **não** custos, leilão, benchmarks nem formatos criativos
- **Fora da cobertura atual:** TikTok, Threads e X — `LOOK INTO`; não usar afirmações de plataforma sem uma revisão autorizada

A revisão programada é um controlo interno de qualidade, não a previsão de uma alteração da plataforma. Uma data vencida gera um aviso; não autoriza pesquisa externa, acesso à conta nem alteração de ficheiros. Sempre que uma decisão dependa de um facto mais recente, a verificação no ponto de uso ganha ao calendário.

## As datas não são todas a mesma data

Registar separadamente:

1. **Publicado em** — quando a plataforma anunciou ou documentou.
2. **Efetivo em** — quando a regra entrou em vigor, apenas se a fonte o disser.
3. **Rollout** — intervalo, região, tipo de conta ou elegibilidade, apenas se declarado.
4. **Fonte relida em** — quando o conteúdo da fonte foi efetivamente aberto e relido por este sistema.
5. **Acesso tentado em** — registar apenas quando a releitura falhou ou exigiu autenticação. Uma tentativa não conta como releitura.

Se a fonte não der uma data, escrever **não declarada**. Nunca transformar a data do anúncio em data de entrada em vigor. Alterações de ranking podem ser contínuas e não anunciadas; funcionalidades podem chegar por conta ou região; políticas e versões de API podem ter datas explícitas. Não existe uma data anual fixa para “mudar o algoritmo”.

## Estados permitidos

- **ativo** — orientação oficial atual, dentro do âmbito declarado;
- **anunciado / em rollout** — existe anúncio, mas a disponibilidade não é universalmente confirmada;
- **condicional** — depende de conta, região, elegibilidade ou interface;
- **observação datada** — medição ou comparação válida para aquele anúncio, não regra permanente;
- **histórico / substituído** — continua útil para auditoria, mas já não governa a recomendação atual;
- **por verificar** — a fonte ou a aplicabilidade atual não foi confirmada;
- **limite conhecido** — o inventário confirma que a evidência não suporta uma resposta mais específica;
- **retirado** — a plataforma retirou a regra ou funcionalidade.

Os IDs são estáveis. Não renumerar nem apagar um facto substituído; atualizar o estado e ligar o sucessor.

## Índice

| ID | Plataforma / superfície | Objeto | Estado |
|---|---|---|---|
| PLAT-001 | Meta · Facebook e Instagram | sistemas de ranking | ativo |
| PLAT-002 | Instagram · recomendações | originalidade | ativo; rollout e âmbito territorial não declarados |
| PLAT-003 | Instagram · posts e Reels | limite de hashtags | anunciado / rollout gradual; confirmar na conta |
| PLAT-004 | Instagram · Pesquisa | campos e sinais publicados | histórico oficial; atualidade por verificar |
| PLAT-005 | Facebook · Reels | frescura no próprio dia | observação datada |
| PLAT-006 | Facebook · Feed e Reels | originalidade | ativo |
| PLAT-007 | Facebook · Feed | engagement bait | ativo |
| PLAT-008 | Facebook · Pesquisa | “keywords” | limite conhecido; sem mapa público estável |
| PLAT-009 | Meta · Graph API / Instagram Platform | versões e alterações | ativo; verificar por tarefa |
| PLAT-010 | Instagram · Trial Reels | disponibilidade e comparação | condicional por elegibilidade |
| PLAT-011 | Instagram · Reels | conteúdo tornado menos visível | histórico oficial; atualidade por verificar |
| PLAT-012 | Google Business Profile | elegibilidade e representação | ativo |
| PLAT-013 | Google Business Profile | ranking local e Posts | ativo |
| PLAT-014 | WhatsApp · separador Atualizações | descoberta e publicidade | condicional; confirmar região e conta |
| PLAT-015 | WhatsApp · envios empresariais | listas, Business Broadcasts e Platform | condicional por produto, conta e região |
| PLAT-016 | YouTube · Pesquisa e recomendações | sinais publicados e metadados | ativo |
| PLAT-017 | YouTube · Shorts | classificação de vídeos até três minutos | ativo; data depende do tipo de canal |
| PLAT-018 | Pinterest · distribuição orgânica | longevidade dos Pins | ativo |
| PLAT-019 | Pinterest · Pins orgânicos | especificações e metadados | ativo |
| PLAT-020 | Meta · campanhas pagas | fase de aprendizagem e eventos de otimização | ativo |
| PLAT-021 | Google Ads · licitação inteligente | ausência de limiar de entrada no CPA-alvo | ativo |
| PLAT-022 | Pinterest · campanhas pagas | modo de aprendizagem | ativo |
| PLAT-023 | Google Ads · medição na UE | limiar da modelação de conversões | ativo |
| PLAT-024 | Google Ads · ações locais | disponibilidade das visitas à loja | ativo |
| PLAT-025 | Meta Ads · Marketing API | remoção das exclusões de segmentação detalhada | ativo |
| PLAT-026 | Meta Ads · Advantage+ audience | sugestões, expansão e controlos rígidos | ativo; opções originais/manuais condicionais ao contexto |

## Plataformas em espera

| Plataforma | Estado | Regra operacional |
|---|---|---|
| TikTok | LOOK INTO | Não usar afirmações atuais sobre algoritmo, pesquisa, limites ou funcionalidades sem revisão autorizada |
| Threads | LOOK INTO | Não usar afirmações atuais sobre ranking, links ou funcionalidades sem revisão autorizada |
| X | LOOK INTO | Não usar afirmações atuais sobre ranking, links ou funcionalidades sem revisão autorizada |

## Registos

### PLAT-001 — os sistemas são separados e mudam continuamente

- **Plataforma / superfície:** Facebook e Instagram; Feed, Reels, Stories, Pesquisa e outras superfícies.
- **Tipo de afirmação:** funcionamento estrutural.
- **Afirmação atual:** a Meta não usa um único sistema de IA para decidir tudo o que se vê. Existem sistemas separados por experiência, com múltiplos modelos e milhares de sinais; a própria Meta diz que modelos e sinais são dinâmicos e mudam frequentemente.
- **Volatilidade:** alta nos sinais e modelos; baixa na conclusão de que não existe “um algoritmo” único.
- **Âmbito:** produtos e superfícies descritos pela Meta; geografia não declarada. O resultado continua personalizado por pessoa.
- **Fonte primária:** https://ai.meta.com/blog/how-ai-powers-experiences-facebook-instagram-system-cards/
- **Publicado em:** 2023-06-29.
- **Efetivo em:** não declarada.
- **Rollout:** não aplicável à conclusão estrutural.
- **Fonte relida em:** 2026-09-01.
- **Rever quando:** antes de dar pesos, sinais ou prioridades como atuais; quando as system cards mudarem de versão.
- **Confiança:** ⬤.
- **Estado:** ativo.
- **Implicação:** nunca prometer a próxima data de mudança do “código do Reels” nem responder de memória com uma lista fixa de pesos. Distinguir superfície, pedir o objetivo concreto e verificar a fonte atual se a precisão depender disso.

### PLAT-002 — originalidade nas recomendações do Instagram

- **Plataforma / superfície:** Instagram; recomendações em Feed, Explorar e Reels.
- **Tipo de afirmação:** elegibilidade e distribuição.
- **Afirmação atual:** a orientação publicada em 2026 abrange Reels, fotografias e carrosséis. Contas que publiquem sobretudo conteúdo não original podem deixar de aparecer em recomendações; alterações cosméticas como borda, marca de água, legendas ou crédito não constituem contribuição criativa. A recuperação é descrita por maioria de conteúdo recente considerado original numa janela móvel de 30 dias.
- **Volatilidade:** alta.
- **Âmbito:** âmbito territorial não declarado; aplicação observável no Estado da conta.
- **Fonte primária:** https://creators.instagram.com/blog/rewarding-original-creators-on-instagram
- **Publicado em:** 2026-04-30.
- **Efetivo em:** não declarada.
- **Rollout:** não declarado.
- **Fonte relida em:** não concluída neste ambiente.
- **Acesso tentado em:** 2026-09-01; a página oficial exigiu autenticação.
- **Rever quando:** antes de diagnosticar inelegibilidade, quando a página ou as diretrizes de conteúdo original mudarem, ou quando o Estado da conta divergir.
- **Confiança:** ◐ neste ambiente: origem oficial identificada, mas conteúdo não relido nesta revisão; confirmar na fonte ou no Estado da conta antes de uma decisão real.
- **Estado:** ativo; disponibilidade e aplicação concretas confirmam-se na conta.
- **Implicação:** este registo substitui o limiar de 2024 de “10 ou mais republicações em 30 dias”. Não usar os dois critérios ao mesmo tempo. Quando a decisão afetar uma conta real, ler o Estado da conta e não diagnosticar “shadowban”.

### PLAT-003 — limite de hashtags no Instagram

- **Plataforma / superfície:** Instagram; legenda de posts e Reels.
- **Tipo de afirmação:** limite de produto.
- **Afirmação atual:** a conta oficial Instagram for Creators anunciou que o número permitido seria gradualmente atualizado para até cinco hashtags numa legenda de post ou Reel.
- **Volatilidade:** alta até o rollout estar confirmado em todas as contas relevantes.
- **Âmbito:** por conta; geografia não declarada.
- **Fonte primária:** https://www.threads.com/@creators/post/DSalXGPCWM4
- **Publicado em:** 2025-12-18.
- **Efetivo em:** não declarada.
- **Rollout:** gradual, segundo o anúncio.
- **Fonte relida em:** não concluída neste ambiente.
- **Acesso tentado em:** 2026-09-01; a publicação oficial exigiu sessão iniciada.
- **Rever quando:** antes de afirmar o limite como universal ou quando o compositor da conta aceitar ou rejeitar uma quantidade diferente.
- **Confiança:** ◐ neste ambiente: origem oficial identificada, mas publicação não relida nesta revisão; confirmar no compositor da conta.
- **Estado:** anunciado / em rollout; confirmar na conta.
- **Implicação:** produzir no máximo cinco hashtags é uma escolha segura. Se o utilizador perguntar qual é o limite efetivo da sua conta, pedir confirmação no compositor; não tratar 2025-12-18 como data global de entrada em vigor.

### PLAT-004 — campos e sinais da Pesquisa do Instagram

- **Plataforma / superfície:** Instagram Search.
- **Tipo de afirmação:** indexação e ranking de pesquisa.
- **Afirmação atual:** o explicador oficial de 2021 dizia que o texto pesquisado era o sinal principal e era comparado com nomes de utilizador, biografias, legendas, hashtags e locais; atividade e popularidade entravam depois. É uma descrição histórica oficial, não uma especificação atual de pesos.
- **Volatilidade:** alta.
- **Âmbito:** não declarado.
- **Fonte primária:** https://about.instagram.com/blog/announcements/break-down-how-instagram-search-works
- **Publicado em:** 2021-08-25.
- **Efetivo em:** não declarada.
- **Rollout:** não declarado.
- **Fonte relida em:** não concluída neste ambiente.
- **Acesso tentado em:** 2026-09-01; a fonte devolveu limite de acesso.
- **Rever quando:** antes de otimizar um perfil com uma afirmação atual sobre campos ou pesos; quando houver explicador ou system card mais recente.
- **Confiança:** ◐ nesta revisão: descrição oficial histórica identificada, mas fonte não relida; por verificar como mapa atual.
- **Estado:** histórico oficial; atualidade por verificar.
- **Implicação:** usar linguagem clara e relevante continua a ser prática defensável, mas não afirmar que um campo “pesa X” hoje sem fonte mais recente ou teste na conta.

### PLAT-005 — Facebook mostrou mais Reels do próprio dia

- **Plataforma / superfície:** Facebook Reels.
- **Tipo de afirmação:** observação de produto datada.
- **Afirmação atual:** em outubro de 2025, a Meta disse que o motor então atualizado estava a mostrar 50% mais Reels de criadores publicados naquele dia. A fonte não publica a linha de base, a janela de medição nem um efeito causal de publicar no próprio dia.
- **Volatilidade:** alta.
- **Âmbito:** âmbito territorial da comparação não declarado.
- **Fonte primária:** https://about.fb.com/news/2025/10/finding-sharing-reels-facebook-just-got-easier-more-fun/
- **Publicado em:** 2025-10-07.
- **Efetivo em:** a fonte usa “now”; data técnica não declarada.
- **Rollout:** outras funcionalidades do anúncio estavam em rollout; a comparação do motor não traz calendário próprio.
- **Fonte relida em:** 2026-09-01.
- **Rever quando:** sempre que alguém quiser transformar esta observação numa regra atual de calendário.
- **Confiança:** ⬤ quanto ao que a Meta declarou; não prova causalidade.
- **Estado:** observação datada.
- **Implicação:** não invalida agendamento nem prova que publicar no próprio dia aumenta alcance. Manter capacidade reativa pode ser uma escolha editorial; a vantagem de horário testa-se com dados da conta.

### PLAT-006 — originalidade no Facebook

- **Plataforma / superfície:** Facebook Feed e Reels.
- **Tipo de afirmação:** elegibilidade, distribuição e monetização.
- **Afirmação atual:** a Meta considera original o conteúdo produzido pelo criador ou proprietário da Página/Perfil. Reações faciais sem contributo, junção de clips, narração do que já está no ecrã e pequenas alterações a material alheio podem ser classificados como não originais e despromovidos; reincidência pode afetar recomendação e monetização.
- **Volatilidade:** média.
- **Âmbito:** âmbito territorial não declarado.
- **Fonte primária:** https://about.fb.com/news/2026/03/rewarding-original-creators-on-facebook/
- **Publicado em:** 2026-03-12; a página também apresenta 13 de março em algumas localizações.
- **Efetivo em:** a orientação é descrita como atual; data técnica não declarada.
- **Rollout:** apenas as novas ferramentas de proteção são descritas como em rollout; não confundir com a regra de originalidade.
- **Fonte relida em:** 2026-09-01.
- **Rever quando:** antes de reutilizar conteúdo de terceiros ou quando as diretrizes ligadas mudarem.
- **Confiança:** ⬤.
- **Estado:** ativo.
- **Implicação:** exigir contribuição criativa substancial e direitos de utilização. Não confundir uma alteração cosmética com autoria ou licença.

### PLAT-007 — engagement bait no Facebook

- **Plataforma / superfície:** Facebook Feed e Páginas.
- **Tipo de afirmação:** despromoção.
- **Afirmação atual:** a Meta anunciou despromoção de publicações que procuram artificialmente votos, reações, partilhas, marcações ou comentários; reincidência pode afetar a Página. Pedidos genuínos de ajuda, conselho ou recomendação foram excluídos.
- **Volatilidade:** média.
- **Âmbito:** rollout faseado por idioma; português confirmado em 2018; território não declarado.
- **Fonte primária:** https://about.fb.com/news/2017/12/news-feed-fyi-fighting-engagement-bait-on-facebook/
- **Publicado em:** 2017-12-18.
- **Efetivo em:** inglês nas semanas seguintes ao anúncio; expansão para português anunciada em 2018-04-04.
- **Rollout:** faseado por idioma; não existe uma única data global na fonte.
- **Fonte relida em:** 2026-09-01.
- **Rever quando:** quando a política ou o anúncio oficial forem substituídos.
- **Confiança:** ⬤.
- **Estado:** ativo.
- **Implicação:** evitar chamadas como “marca três amigos” ou “comenta EU QUERO”; uma pergunta genuína ligada ao conteúdo não é automaticamente bait.

### PLAT-008 — “keywords” no Facebook não têm uma data ou mapa único

- **Plataforma / superfície:** Facebook Search; distinguir de anúncios, SEO web, hashtags e campos da Página.
- **Tipo de afirmação:** limite da evidência.
- **Afirmação atual:** a Meta confirma que Facebook Search é um sistema separado, mas as fontes oficiais desta skill não oferecem um mapa público, atual e estável de campos com pesos de “keywords”. A palavra “keywords” é ambígua e não identifica uma alteração concreta.
- **Volatilidade:** alta.
- **Âmbito:** depende da superfície, consulta, pessoa, região e conta.
- **Fonte primária:** https://ai.meta.com/blog/how-ai-powers-experiences-facebook-instagram-system-cards/
- **Publicado em:** 2023-06-29.
- **Efetivo em:** não aplicável ao limite da evidência.
- **Rollout:** não aplicável.
- **Fonte relida em:** 2026-09-01.
- **Rever quando:** sempre que o pedido mencionar “keywords do Facebook” ou surgir documentação oficial de campos de pesquisa.
- **Confiança:** ⬤ quanto à existência de um sistema Search separado; ◐ quanto à ausência encontrada no inventário atual.
- **Estado:** limite conhecido; sem mapa público estável neste registo.
- **Implicação:** perguntar ou inferir pelo contexto se se fala de Pesquisa, descrição da Página, legendas, anúncios ou API. Não inventar “a mudança das keywords” nem atribuir-lhe uma data.

### PLAT-009 — versões e alterações da Graph API

- **Plataforma / superfície:** Meta Graph API e Instagram Platform.
- **Tipo de afirmação:** governação técnica.
- **Afirmação atual:** versões da API têm calendários e períodos de suporte documentados; alterações também aparecem nos changelogs e podem ocorrer fora de um ciclo anual simples. Isto não significa que o ranking orgânico publique o seu código ou a data de cada alteração.
- **Volatilidade:** alta.
- **Âmbito:** por versão, produto, permissão e aplicação.
- **Fontes primárias:** https://developers.facebook.com/docs/graph-api/guides/versioning/ · https://developers.facebook.com/docs/graph-api/changelog/ · https://developers.facebook.com/docs/instagram-platform/changelog/
- **Publicado em:** documentação viva; sem uma única data.
- **Efetivo em:** conforme cada versão ou entrada do changelog.
- **Rollout:** conforme cada entrada; não inferir.
- **Fonte relida em:** não concluída neste ambiente.
- **Acesso tentado em:** 2026-09-01; a documentação devolveu limite de acesso.
- **Rever quando:** em toda tarefa que use a API, antes de implementar ou estimar impacto.
- **Confiança:** ◐ neste ambiente: documentação oficial identificada, mas não relida; a versão e o changelog confirmam-se em cada tarefa.
- **Estado:** ativo; verificar por tarefa.
- **Implicação:** uma tarefa de conteúdo não precisa da API. Uma integração técnica precisa de versão, endpoint, permissões e changelog atuais; não usar o calendário deste ficheiro como substituto.

### PLAT-010 — Trial Reels

- **Plataforma / superfície:** Instagram Reels.
- **Tipo de afirmação:** funcionalidade e método de teste.
- **Afirmação atual:** Trial Reels mostram primeiro o Reel a não seguidores e comparam-no com trials anteriores. A Meta anunciou rollout global para criadores elegíveis; a elegibilidade e a presença do controlo continuam a confirmar-se na própria conta.
- **Volatilidade:** média.
- **Âmbito:** criadores elegíveis; conta concreta.
- **Fonte primária:** https://about.fb.com/news/2024/12/trial-reels-try-content-non-followers-first-see-what-perfoms-best/
- **Publicado em:** 2024-12-10; página atualizada em 2025-06-26.
- **Efetivo em:** rollout iniciado em 2024-12-10.
- **Rollout:** anunciado como global para criadores elegíveis nas semanas seguintes.
- **Fonte relida em:** 2026-09-01.
- **Rever quando:** antes de prometer disponibilidade ou comparar um Trial Reel com uma publicação normal.
- **Confiança:** ⬤.
- **Estado:** condicional por elegibilidade e conta.
- **Implicação:** confirmar o controlo na conta e comparar trial com trial. A fonte oficial não sustenta a afirmação de que Trials têm “quase sempre menos alcance por construção”.

### PLAT-011 — Reels que o Instagram declarou tornar menos visíveis

- **Plataforma / superfície:** Instagram Reels.
- **Tipo de afirmação:** distribuição.
- **Afirmação atual:** o explicador oficial de 2023 dizia que o Instagram procurava tornar menos visíveis Reels de baixa resolução, com marca de água, sem som, com bordas, maioritariamente texto ou já publicados no Instagram.
- **Volatilidade:** alta.
- **Âmbito:** não declarado.
- **Fonte primária:** https://about.instagram.com/blog/announcements/instagram-ranking-explained
- **Publicado em:** 2023-05-31.
- **Efetivo em:** não declarada.
- **Rollout:** não declarado.
- **Fonte relida em:** não concluída neste ambiente.
- **Acesso tentado em:** 2026-09-01; a fonte devolveu limite de acesso.
- **Rever quando:** antes de apresentar a lista como regra atual de ranking; quando houver explicador mais recente.
- **Confiança:** ◐ nesta revisão: descrição oficial histórica identificada, mas fonte não relida; por verificar como lista atual.
- **Estado:** histórico oficial; atualidade por verificar.
- **Implicação:** reexportar sem marcas de água e assegurar legibilidade/qualidade continuam a ser boas práticas independentes. Não atribuir uma queda concreta a esta lista sem dados da conta.

### PLAT-012 — elegibilidade e representação no Google Business Profile

- **Plataforma / superfície:** Google Business Profile; perfis de lojas e negócios de área de serviço.
- **Tipo de afirmação:** elegibilidade e representação do negócio.
- **Afirmação atual:** um negócio elegível tem contacto presencial com clientes durante o horário declarado, numa localização que os clientes visitam ou numa área de serviço. Negócios apenas online não são elegíveis. O nome deve corresponder ao nome usado no mundo real e as categorias devem ser específicas e em número reduzido; informação desnecessária no nome pode levar à suspensão.
- **Volatilidade:** média.
- **Âmbito:** perfis de empresa; existem exceções e regras próprias para categorias especiais descritas nas diretrizes.
- **Fontes primárias:** https://support.google.com/business/answer/13763036?hl=en · https://support.google.com/business/answer/3038177?hl=en
- **Publicado em:** documentação viva; sem uma única data.
- **Efetivo em:** atual na documentação relida.
- **Rollout:** não aplicável às regras gerais; elegibilidade concreta depende do tipo de negócio.
- **Fonte relida em:** 2026-09-01.
- **Rever quando:** ao criar, reivindicar, renomear ou recategorizar um perfil; quando as diretrizes forem atualizadas.
- **Confiança:** ⬤.
- **Estado:** ativo.
- **Implicação:** não assumir que ter uma morada basta, não criar perfil para negócio apenas online e não acrescentar palavras-chave ao nome real. Confirmar o modelo de atendimento e escolher apenas categorias que descrevam o negócio.

### PLAT-013 — ranking local e função dos Posts no Google Business Profile

- **Plataforma / superfície:** resultados locais da Pesquisa Google e Google Maps; Posts do Business Profile.
- **Tipo de afirmação:** ranking e comunicação com clientes.
- **Afirmação atual:** a Google descreve os resultados locais principalmente por relevância, distância e proeminência/popularidade, sem publicar pesos fixos nem uma ordem universal. Informação completa e exata, verificação, horários, avaliações e fotografias ajudam o perfil a representar o negócio. Os Posts servem para partilhar novidades, ofertas, eventos e produtos; a documentação consultada não os declara fator de ranking.
- **Volatilidade:** média nas orientações; alta em pesos ou efeitos não publicados.
- **Âmbito:** resultados locais e Posts de perfis elegíveis.
- **Fontes primárias:** https://support.google.com/business/answer/7091?hl=en · https://support.google.com/business/answer/7342169?hl=en
- **Publicado em:** documentação viva; sem uma única data.
- **Efetivo em:** atual na documentação relida.
- **Rollout:** não declarado; algumas funcionalidades de Posts variam por tipo de perfil.
- **Fonte relida em:** 2026-09-01.
- **Rever quando:** antes de atribuir pesos, prometer melhoria de posição ou recomendar uma funcionalidade concreta de Posts.
- **Confiança:** ⬤ quanto aos três fatores e à função declarada dos Posts; a ausência de um efeito publicado não prova efeito nulo.
- **Estado:** ativo.
- **Implicação:** otimizar primeiro a exatidão e completude do perfil. Usar Posts pela utilidade para o cliente, sem os vender como fator confirmado de ranking, e nunca prometer posição ou data de mudança.

### PLAT-014 — o WhatsApp tem superfícies de descoberta no separador Atualizações

- **Plataforma / superfície:** WhatsApp; separador Atualizações, Estados e Canais.
- **Tipo de afirmação:** descoberta, distribuição e publicidade.
- **Afirmação atual:** o WhatsApp mantém as conversas pessoais separadas, mas o separador Atualizações inclui Estados e Canais. A Meta anunciou anúncios em Estados, Canais promovidos e subscrições de Canais, com introdução gradual por região. Portanto, “o WhatsApp não tem feed nem descoberta” já não é uma descrição universal do produto.
- **Volatilidade:** alta.
- **Âmbito:** separador Atualizações; disponibilidade por região e conta. Não se aplica às conversas pessoais, que a Meta diz não usar para mostrar estes anúncios.
- **Fonte primária:** https://about.fb.com/news/2025/06/helping-you-find-more-channels-businesses-on-whatsapp/
- **Publicado em:** 2025-06-16.
- **Efetivo em:** não existe uma única data global; o anúncio não confirma conclusão universal.
- **Rollout:** anunciado em 2025 como gradual durante vários meses; estado atual por região não verificado nesta fonte.
- **Fonte relida em:** 2026-09-01.
- **Rever quando:** antes de recomendar anúncios, promoção ou descoberta em Estados/Canais; confirmar disponibilidade na conta e região.
- **Confiança:** ⬤ quanto ao anúncio e à separação das conversas; disponibilidade concreta confirma-se na conta.
- **Estado:** condicional; confirmar região e conta.
- **Implicação:** distinguir conversas, Estados e Canais. Não prometer uma superfície publicitária nem dizer que o canal serve apenas retenção sem confirmar a conta e o objetivo.

### PLAT-015 — “difusão no WhatsApp” identifica produtos diferentes

- **Plataforma / superfície:** WhatsApp Business app e WhatsApp Business Platform; listas de difusão, Business Broadcasts, Canais e mensagens da Platform.
- **Tipo de afirmação:** produto, elegibilidade e consentimento.
- **Afirmação atual:** as listas tradicionais da app, os Business Broadcasts e os envios da Business Platform não são o mesmo produto. A ajuda das listas tradicionais continua a indicar receção por contactos que guardaram o número e um máximo de 256 destinatários por lista, mas alguns países recebem limites mensais graduais. Business Broadcasts é uma funcionalidade paga distinta, disponível apenas para utilizadores elegíveis em países selecionados, e pode chegar a pessoas que não guardaram o número. Os serviços empresariais exigem consentimento prévio e respeito por pedidos de saída. A Platform tem regras e limites próprios que devem ser consultados por implementação.
- **Volatilidade:** alta.
- **Âmbito:** varia por país, conta, produto e método de envio.
- **Fontes primárias:** https://faq.whatsapp.com/861663048350950/?cms_platform=android&locale=pt_BR · https://faq.whatsapp.com/1356785542323967/?cms_platform=web · https://whatsappbusiness.com/products/business-app-features/ · https://business.whatsapp.com/policy
- **Publicado em:** documentação viva; Business Broadcasts anunciado e alterado progressivamente.
- **Efetivo em:** conforme o produto e a conta; não existe uma data universal.
- **Rollout:** limites mensais e Business Broadcasts podem ser graduais e regionais.
- **Fonte relida em:** 2026-09-01.
- **Rever quando:** antes de definir volume, preço, elegibilidade, destinatários ou automatização de qualquer envio empresarial.
- **Confiança:** ⬤ quanto à distinção entre produtos e à necessidade de consentimento; limites efetivos confirmam-se na interface e documentação do produto usado.
- **Estado:** condicional por produto, conta e região.
- **Implicação:** perguntar qual produto está a ser usado antes de dar um limite. Não aplicar “256 e número guardado” a todos os envios, nem usar escalões ou fórmulas da API de memória.

### PLAT-016 — Pesquisa e recomendações no YouTube

- **Plataforma / superfície:** YouTube Search, página inicial, Up Next e outras recomendações.
- **Tipo de afirmação:** pesquisa, recomendação e metadados.
- **Afirmação atual:** a Pesquisa considera relevância, engagement e qualidade; para relevância, avalia a correspondência da consulta com título, tags, descrição e conteúdo do vídeo. As recomendações são personalizadas e a orientação atual organiza o desempenho em appeal, engagement e satisfaction, com sinais concretos que variam por superfície e pessoa. As tags continuam disponíveis, mas o YouTube diz que têm papel mínimo e são sobretudo úteis para erros ortográficos.
- **Volatilidade:** média no modelo publicado; alta em sinais e pesos concretos.
- **Âmbito:** pesquisa e recomendações orgânicas do YouTube; personalização por pessoa e superfície.
- **Fontes primárias:** https://support.google.com/youtube/answer/16090438?hl=en · https://support.google.com/youtube/answer/16559650?hl=en
- **Publicado em:** documentação viva; sem uma única data.
- **Efetivo em:** atual na documentação relida.
- **Rollout:** não aplicável ao modelo geral; funcionalidades e sinais podem variar.
- **Fonte relida em:** 2026-09-01.
- **Rever quando:** antes de declarar pesos, diagnosticar distribuição ou afirmar que um campo deixou de existir.
- **Confiança:** ⬤.
- **Estado:** ativo.
- **Implicação:** priorizar título, miniatura, promessa cumprida e satisfação. Usar tags apenas quando ajudam a resolver grafias; não dizer que desapareceram nem transformar uma lista de sinais em pesos universais.

### PLAT-017 — classificação de vídeos como Shorts

- **Plataforma / superfície:** YouTube Shorts; uploads em canais normais e Official Artist Channels.
- **Tipo de afirmação:** classificação de formato.
- **Afirmação atual:** vídeos quadrados ou verticais com até três minutos são classificados como Shorts quando carregados a partir de 15 de outubro de 2024 em canais normais; para Official Artist Channels, a alteração aplica-se a uploads a partir de 8 de dezembro de 2025. Não é uma regra exclusiva de 9:16.
- **Volatilidade:** média.
- **Âmbito:** vídeos quadrados ou verticais até três minutos; a data depende do tipo de canal e existem implicações próprias de direitos para Shorts com mais de um minuto.
- **Fonte primária:** https://support.google.com/youtube/answer/15424877?hl=en-GB
- **Publicado em:** página de ajuda atualizada; datas efetivas declaradas na fonte.
- **Efetivo em:** 2024-10-15 para canais normais; 2025-12-08 para Official Artist Channels.
- **Rollout:** datas distintas por tipo de canal; confirmar outras condições na página atual.
- **Fonte relida em:** 2026-09-01.
- **Rever quando:** antes de classificar um upload, sobretudo em canais de artista ou vídeos com mais de um minuto.
- **Confiança:** ⬤.
- **Estado:** ativo; data depende do tipo de canal.
- **Implicação:** aceitar quadrado e vertical; não impor 9:16 como condição técnica nem usar 2024-10-15 para todos os canais sem distinguir o tipo.

### PLAT-018 — os Pins não têm uma janela fixa de distribuição

- **Plataforma / superfície:** Pinterest; feed inicial, pesquisa e Pins relacionados.
- **Tipo de afirmação:** distribuição orgânica e longevidade.
- **Afirmação atual:** o Pinterest explica que a distribuição pode aumentar ou diminuir ao longo do tempo e que um Pin pode começar a gerar engagement horas, dias, meses ou anos depois de publicado. A documentação atual não sustenta um “boost de frescura” fixo de 7 a 30 dias nem uma janela universal de engagement.
- **Volatilidade:** média.
- **Âmbito:** Pins orgânicos; o desempenho continua dependente da relevância, qualidade e reação da audiência.
- **Fonte primária:** https://help.pinterest.com/en/business/article/pin-performance-and-distribution
- **Publicado em:** documentação viva; sem uma única data.
- **Efetivo em:** atual na documentação relida.
- **Rollout:** não aplicável à orientação geral.
- **Fonte relida em:** 2026-09-01.
- **Rever quando:** antes de atribuir uma janela fixa de alcance ou diagnosticar um Pin apenas pelas primeiras horas.
- **Confiança:** ⬤.
- **Estado:** ativo.
- **Implicação:** avaliar Pins numa janela adequada ao ciclo de pesquisa e planeamento; não declarar morte precoce nem frescura fixa.

### PLAT-019 — especificações e metadados de Pins orgânicos

- **Plataforma / superfície:** Pinterest; Pins de imagem e vídeo orgânicos.
- **Tipo de afirmação:** especificações e indexação.
- **Afirmação atual:** o título pode ter até 100 caracteres e a descrição até 800. O Pinterest usa a descrição para determinar relevância; palavras relevantes também podem viver no título e no contexto do quadro e destino. Vídeo orgânico aceita 4 segundos a 5 minutos e rácios 1:2, 2:3, 3:4, 4:5, 1:1 ou 9:16; 9:16 é recomendado para vídeo de ecrã inteiro, não o único formato aceite.
- **Volatilidade:** média.
- **Âmbito:** criação orgânica; especificações de anúncios e formatos compráveis podem ser diferentes.
- **Fontes primárias:** https://help.pinterest.com/en/article/review-pin-specs · https://help.pinterest.com/en/business/article/pin-performance-and-distribution
- **Publicado em:** documentação viva; sem uma única data.
- **Efetivo em:** atual na documentação relida.
- **Rollout:** não declarado.
- **Fonte relida em:** 2026-09-01.
- **Rever quando:** antes de produzir ficheiros finais ou aplicar um limite de anúncios a conteúdo orgânico.
- **Confiança:** ⬤.
- **Estado:** ativo.
- **Implicação:** usar metadados claros e dimensões aceites; não impor 1000×1500, 9:16, 40 caracteres visíveis ou 15 minutos como regras universais de Pins orgânicos.

### PLAT-020 — fase de aprendizagem e eventos de otimização na Meta

- **Plataforma / superfície:** Meta; conjuntos de anúncios no gestor de anúncios.
- **Tipo de afirmação:** mecânica de entrega e limiar de aprendizagem.
- **Afirmação atual:** são **duas páginas com duas redações**, e a diferença importa.
  - *Sobre a fase de aprendizagem:* um conjunto sai da aprendizagem quando consegue entregar de forma estável, e isso *"usually occurs after **about 50 results** in the week after the ad set's last significant edit"*.
  - *Sobre a aprendizagem limitada:* um conjunto fica limitado quando é *"unlikely to receive **about 50 optimization events** in the week after your last significant edit"*.
  - **As seis causas, textuais:** *"limited by small audience size, low budget, low bid or cost control, high auction overlap, an infrequent optimization event, or other issues such as running too many ads at the same time"*.
  - ⬤ **"Learning limited isn't a penalty"** — é indicação de que o orçamento não está a ser gasto com eficácia, não uma sanção. A própria Meta di-lo, e é o contrário do que a maior parte dos guias sugere.
  - ⬤ **Exceção documentada:** para anúncios de Shops, o limiar é **17 compras através do site e 5 através da Meta** ao fim de 7 dias — não 50.
  - Edições significativas reiniciam a aprendizagem.
- **Volatilidade:** média.
- **Âmbito:** Meta. ⚠️ **Este número não existe noutra plataforma** — ver PLAT-021 e PLAT-022.
- **Fontes primárias:** https://www.facebook.com/business/help/112167992830700 · https://www.facebook.com/business/help/269269737396981
- **Publicado em:** documentação viva; sem uma única data.
- **Efetivo em:** atual na documentação relida.
- **Rollout:** não aplicável.
- **Fonte relida em:** 2026-09-03 — as duas páginas abertas e lidas num navegador com execução de JavaScript. ⚠️ **Nota de método:** a 2026-09-02 a releitura falhou porque a ferramenta usada não executava JavaScript e as páginas devolviam só o título. **Não era a Meta a bloquear; era o instrumento errado.**
- **Rever quando:** ao dimensionar orçamento, ao escolher o evento de otimização, ou antes de transferir a regra para outra plataforma.
- **Confiança:** ⬤.
- **Estado:** ativo.
- **Implicação:** usar como ordem de grandeza para dimensionar orçamento, nunca como interruptor — a Meta escreve "about" nas duas páginas. E **não aplicar fora da Meta**: é a regra mais copiada e menos verificada da área. As cinco correções que a Meta lista mapeiam uma a uma nas causas: juntar conjuntos, alargar audiência, subir orçamento, subir licitação, e **mudar para um evento mais frequente** — esta última é a que mais serve um negócio pequeno.

### PLAT-021 — o CPA-alvo do Google não tem limiar de entrada

- **Plataforma / superfície:** Google Ads; licitação inteligente, CPA-alvo.
- **Tipo de afirmação:** requisito de histórico e método de avaliação.
- **Afirmação atual:** *"Advertisers can start using Target CPA with no conversion history, and Target CPA is effective for campaigns of all sizes."* Para avaliar, a documentação recomenda medir os últimos 30 dias **com pelo menos 30 conversões**. E recomenda **testar em experiência** — *"Save as experiment"* — em vez de alterar a campanha ativa.
- **Volatilidade:** média.
- **Âmbito:** Google Ads. Não se transfere para a Meta, onde o mecanismo de proteção é não mexer.
- **Fontes primárias:** https://support.google.com/google-ads/answer/6268632
- **Publicado em:** documentação viva.
- **Efetivo em:** atual na documentação relida.
- **Rollout:** não aplicável.
- **Fonte relida em:** 2026-09-02.
- **Rever quando:** ao montar uma campanha de pesquisa, ou ao decidir se há histórico suficiente para automatizar a licitação.
- **Confiança:** ⬤.
- **Estado:** ativo.
- **Implicação:** não adiar o CPA-alvo à espera de acumular conversões, e não aplicar aqui o reflexo da Meta de "não mexer" — no Google, a forma correta de testar uma alteração é a experiência, e evitá-la é deixar de testar sem necessidade.

### PLAT-022 — modo de aprendizagem do Pinterest

- **Plataforma / superfície:** Pinterest; campanhas pagas.
- **Tipo de afirmação:** duração da aprendizagem e ausência de limiar publicado.
- **Afirmação atual:** o indicador de modo de aprendizagem desaparece **em média ao fim de duas semanas**, variando com investimento, eventos de conversão e interação com os anúncios. O Pinterest **não publica um número de conversões para sair**: diz que o indicador é removido quando os eventos de conversão estabilizam. Alterações durante o modo de aprendizagem podem reiniciá-lo.
- **Volatilidade:** média.
- **Âmbito:** Pinterest. ⚠️ **As 50 a 200 conversões por semana que o Pinterest publica são outra afirmação** — é o que a *entrega* precisa para aprender a quem mostrar, não um limiar de saída da aprendizagem. Confundi-las é o erro corrente.
- **Fontes primárias:** https://help.pinterest.com/en/business/article/learning-mode · https://help.pinterest.com/en/business/article/conversions-campaigns
- **Publicado em:** documentação viva.
- **Efetivo em:** atual na documentação relida.
- **Rollout:** não aplicável.
- **Fonte relida em:** 2026-09-02.
- **Rever quando:** antes de planear um calendário de alterações a uma campanha de Pinterest.
- **Confiança:** ⬤.
- **Estado:** ativo.
- **Implicação:** não prometer uma data de saída da aprendizagem e não citar as 50-200 conversões como limiar de saída.

### PLAT-023 — limiar da modelação de conversões do Google

- **Plataforma / superfície:** Google Ads; modo de consentimento e modelação de conversões, EEE.
- **Tipo de afirmação:** condição de ativação da modelação.
- **Afirmação atual:** *"You have a daily ad click threshold of 700 ad clicks over a 7 day period, per country and domain grouping."* Cumpridos os critérios, os modelos entram em período de treino antes de as conversões modeladas aparecerem nos relatórios.
- **Volatilidade:** média.
- **Âmbito:** contas com modo de consentimento ou IAB TCF v2.0 corretamente implementados, no EEE.
- **Fontes primárias:** https://support.google.com/google-ads/answer/10548233
- **Publicado em:** documentação viva.
- **Efetivo em:** atual na documentação relida.
- **Rollout:** não aplicável.
- **Fonte relida em:** 2026-09-02.
- **Rever quando:** sempre que alguém afirmar que o modo de consentimento resolve a perda de medição.
- **Confiança:** ⬤.
- **Estado:** ativo.
- **Implicação:** ◐ um negócio pequeno em Portugal raramente faz 100 cliques por dia num único domínio, pelo que **a modelação não liga** e o que se vê é medição observada, com o buraco de quem recusou. Não prometer que o modo de consentimento repõe o que se perdeu.

### PLAT-024 — disponibilidade das visitas à loja no Google Ads

- **Plataforma / superfície:** Google Ads; ações locais e métrica de visitas à loja.
- **Tipo de afirmação:** condições de disponibilidade da métrica.
- **Afirmação atual:** a métrica exige locais verificados no Perfil de Empresa, elementos de localização ativos, país elegível, locais não sensíveis, e *"enough ad clicks or impressions, and your business must have enough foot traffic, to pass our privacy thresholds"*. Sobre os valores, a documentação declara: *"Because every advertiser is different, these numbers vary by advertiser."*
- **Volatilidade:** média.
- **Âmbito:** anunciantes com locais verificados em países elegíveis.
- **Fontes primárias:** https://support.google.com/google-ads/answer/6100636 · https://support.google.com/google-ads/answer/2404182
- **Publicado em:** documentação viva.
- **Efetivo em:** atual na documentação relida.
- **Rollout:** elegibilidade por país e por anunciante.
- **Fonte relida em:** 2026-09-02.
- **Rever quando:** antes de prometer a um cliente que se consegue medir visitas à loja.
- **Confiança:** ⬤.
- **Estado:** ativo.
- **Implicação:** ◐ **não montar o critério de sucesso de um negócio pequeno sobre visitas à loja.** Usar cliques para telefonar e cliques em direções. ⚠️ E não dizer que o Google "não publica" os limiares: o que a documentação diz é que **variam por anunciante** — a formulação anterior deste sistema era uma inferência apresentada como facto.

### PLAT-025 — remoção das exclusões de segmentação detalhada

- **Plataforma / superfície:** Meta Ads; Marketing API e exclusões ao nível do conjunto de anúncios.
- **Tipo de afirmação:** retirada de opção de segmentação e mecanismos de exclusão que permanecem.
- **Afirmação atual:** a Meta retirou as *Detailed Targeting exclusions*. A alteração foi lançada na Marketing API v22.0 em 21 de janeiro de 2025 e passou a todas as versões em 21 de abril de 2025. O campo `exclusions` aceita apenas uma exclusão de empregador, através dos controlos de audiência ao nível da conta. As exclusões de Públicos Personalizados continuam disponíveis através do campo próprio `excluded_custom_audiences`, não como exclusões de segmentação detalhada.
- **Volatilidade:** média; a retirada está concluída, mas os campos e controlos residuais podem mudar.
- **Âmbito:** endpoints da Marketing API para criar, editar, copiar e estimar a entrega de conjuntos de anúncios. A fonte não declara que todo o interface do Gestor de Anúncios tenha mudado numa única data global.
- **Fonte primária:** https://developers.facebook.com/blog/post/2025/01/21/removal-of-detailed-targeting-exclusions/
- **Publicado em:** 2025-01-21.
- **Efetivo em:** 2025-01-21 na Marketing API v22.0; 2025-04-21 em todas as versões.
- **Rollout:** por versão da Marketing API; concluído para todas as versões em 2025-04-21.
- **Fonte relida em:** 2026-09-03.
- **Rever quando:** antes de recomendar exclusões de interesses, implementar segmentação pela Marketing API ou quando os controlos de audiência da conta mudarem.
- **Confiança:** ⬤.
- **Estado:** ativo.
- **Implicação:** não instruir a excluir interesses através de *Detailed Targeting exclusions* nem datar a retirada em março de 2025. Distinguir três mecanismos: segmentação detalhada, exclusão de empregador ao nível da conta e exclusão de Públicos Personalizados pelo campo próprio.

### PLAT-026 — Advantage+ audience usa sugestões e pode expandir

- **Plataforma / superfície:** Meta Ads; Advantage+ audience e opções de audiência no Gestor de Anúncios.
- **Tipo de afirmação:** comportamento da segmentação automatizada e disponibilidade de controlos.
- **Afirmação atual:** em Advantage+ audience, os critérios introduzidos pelo anunciante funcionam como sugestões para orientar a entrega, não como fronteiras rígidas; o sistema pode encontrar pessoas fora dessas sugestões. A Meta mantém controlos rígidos para necessidades como idade mínima e localização. Uma opção para voltar a opções de audiência originais/manuais está documentada num fluxo específico de anúncios de aplicações Meta Horizon, mas isso não prova disponibilidade universal em todos os objetivos, contas ou interfaces.
- **Volatilidade:** alta na disponibilidade e no lugar dos controlos no interface; média no comportamento declarado de expansão além das sugestões.
- **Âmbito:** Advantage+ audience. O anúncio de 2023 começou num grupo selecionado; a documentação de campanha manual de 2025 citada aqui aplica-se a anúncios de aplicações Meta Horizon. Confirmar objetivo, conta, região e interface antes de prometer opções originais/manuais.
- **Fontes primárias:** https://about.fb.com/fr/news/2023/05/lancement-de-lia-sandbox-pour-les-annonceurs-et-expansion-de-meta-advantage-suite/ · https://developers.meta.com/horizon/resources/launch-ad-campaign/
- **Publicado em:** 2023-05-12 para o anúncio de Advantage+ audience; guia Meta Horizon atualizado em 2025-06-23.
- **Efetivo em:** não há uma mudança universal declarada em fevereiro de 2026.
- **Rollout:** teste com grupo selecionado em 2023; disponibilidade atual das opções originais/manuais condicionada ao contexto e confirmada no interface.
- **Fonte relida em:** 2026-09-03.
- **Rever quando:** antes de recomendar interesses como restrição rígida, ou de afirmar que a opção manual existe ou desapareceu numa campanha concreta.
- **Confiança:** ⬤ quanto ao comportamento documentado de Advantage+ audience e aos controlos rígidos anunciados; a disponibilidade de opções originais/manuais é condicional ao âmbito declarado.
- **Estado:** ativo; opções originais/manuais condicionais ao contexto e ao interface.
- **Implicação:** tratar interesses e outros sinais de Advantage+ audience como sugestões, não como garantia de exclusão ou inclusão. Para limites que têm de ser rígidos, usar apenas controlos que o interface apresente como tal; confirmar a campanha concreta. Não atribuir esta arquitetura a uma alteração universal de fevereiro de 2026.

## Como acrescentar ou atualizar um registo

1. Procurar primeiro fonte oficial e guardar a ligação direta.
2. Copiar apenas a afirmação que a fonte realmente suporta.
3. Separar publicação, entrada em vigor, rollout e verificação.
4. Declarar geografia, tipo de conta e elegibilidade; se não estiverem na fonte, escrever **não declarado**.
5. Dizer o que a prova não permite concluir.
6. Definir uma implicação operacional proporcional; **sem ação** é um resultado válido.
7. Atualizar o recap datado, os consumidores do ID e o calendário apenas se a revisão tiver sido realmente concluída.
8. Marcar o registo anterior como substituído; nunca apagá-lo.

## Observações pendentes

| ID | Data | Observação | Fonte | O que falta verificar |
|---|---|---|---|---|
| OBS-PLAT-001 | 2026-09-01 | A publicação oficial sobre cinco hashtags está numa conta social e pode exigir sessão iniciada | https://www.threads.com/@creators/post/DSalXGPCWM4 | Encontrar uma página de ajuda pública e versionada que confirme o limite e o âmbito |
| OBS-PLAT-002 | 2026-09-01 | A página de originalidade do Instagram pode exigir autenticação | https://creators.instagram.com/blog/rewarding-original-creators-on-instagram | Confirmar se passa a existir versão pública estável ou página de ajuda equivalente |
| OBS-PLAT-003 | 2026-09-01 | TikTok, Threads e X permanecem fora da cobertura validada | referências e fontes do módulo 05 | `LOOK INTO` apenas após revisão autorizada; não usar afirmações atuais entretanto |
