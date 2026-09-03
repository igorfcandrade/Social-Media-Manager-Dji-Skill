# 8 — Promoção paga

Pôr dinheiro atrás de conteúdo. Escrito do ponto de vista de quem gere as redes, não de um especialista de performance a tempo inteiro.

**Cadência:** a decisão de investir é trimestral · a gestão de campanha é semanal · leitura diária só durante a fase de aprendizagem, e mesmo aí sem mexer.

**Delegabilidade:** ◐ Análise e recomendação, sim. **Autonomia para gastar, nunca.** Um assistente estrutura a campanha, lê os resultados e diz o que desligar; quem carrega no botão assume o custo.

> ⚠️ **Este módulo consome o registo de estado das plataformas.** As mecânicas voláteis que governam decisões — aprendizagem, modelação, visitas à loja e alterações de segmentação — estão datadas em `PLAT-020` a `PLAT-026`. Confirmar o registo e a interface da conta antes de gastar: disponibilidade, objetivo e configuração podem mudar sem que uma regra histórica se torne universal.

> ⚠️ Área onde quase todos os números publicados vêm de fornecedores com interesse comercial no que descrevem, ou são material de marketing da própria plataforma relatado por agências. Este módulo separa o que está **declarado na documentação oficial** do que é alegação sem metodologia.

## A decisão anterior a todas

**Não se paga para distribuir conteúdo que ninguém guardou.** Só se promove o que já provou funcionar organicamente. Pagar para acelerar na direção errada é a forma mais rápida de concluir que "as redes não funcionam". ◐

E o inverso também é verdade: ◐ orçamento pequeno mal aplicado é pior do que orçamento zero, porque cria a ilusão de que já se testou.

Três perguntas antes de gastar o primeiro euro:

1. **Há alguma peça orgânica que já produz o comportamento que queremos?** Se não, o problema é de conteúdo ou de oferta, e o dinheiro não o resolve.
2. **O negócio consegue servir a procura que isto vai gerar?** Gerar pedidos que não se conseguem responder queima reputação e dinheiro ao mesmo tempo.
3. **Conseguimos medir o que acontece a seguir?** Se a conversão acontece ao balcão e não há inquérito de origem, vai gastar-se sem saber o resultado — decisão legítima, desde que assumida.

## Impulsionar vs. gestor de anúncios

| | Impulsionar (boost) | Gestor de anúncios |
|---|---|---|
| Onde | Botão no próprio post | Ferramenta separada |
| Objetivos | Poucos, genéricos | Toda a gama |
| Segmentação e controlo | Mínimos | Completos |
| Custo por resultado | ◐ Reportado como pior, **sem nenhuma comparação com metodologia publicada** | — |
| Serve para | Alcance local, dar mais gás a um post que já corre bem | Tudo o que tem de produzir pedidos, vendas ou contactos |

⚠️ **Sobre as diferenças de custo:** circulam comparações de 2 a 3 vezes entre impulsionar e gestor de anúncios, e chegam a citar-se testes concretos com valores ao cêntimo. **Nenhuma dessas comparações tem metodologia publicada** — são testes individuais ou material de fornecedores. A direção é consistente entre fontes; a magnitude não é de confiança. Não citar os números.

**Regra prática defensável:** impulsionar para dar mais alcance a um post que já está a correr bem, com verba pequena e objetivo simples. Para qualquer coisa que tenha de produzir resultado de negócio, abrir o gestor de anúncios.

## Fase de aprendizagem — o que está declarado

⬤ **PLAT-020.** A Meta documenta o conceito de **"aprendizagem limitada"** (*learning limited*): um conjunto entra nesse estado quando é **improvável que receba cerca de 50 eventos de otimização na semana seguinte à última edição significativa**. Fonte relida a 2026-09-03.

⬤ **E a Meta diz uma coisa que quase nenhum guia repete** — PLAT-020: *"Learning limited isn't a penalty"* — é indicação de que o orçamento não está a ser gasto com eficácia, **não uma sanção**. Quem o lê como castigo reage a fugir do estado em vez de corrigir a causa.

⚠️ **Duas redações, e a diferença importa.** A página da fase de aprendizagem fala de **"cerca de 50 resultados"**; a da aprendizagem limitada fala de **"cerca de 50 eventos de otimização"**. É o segundo que serve para dimensionar orçamento. E há uma exceção documentada: em anúncios de Shops o limiar é **17 compras pelo site e 5 pela Meta** ao fim de 7 dias.

⬤ Para sair, o conjunto tem de **acumular cerca de 50 eventos de otimização desde a última edição significativa** — PLAT-020. A Meta escreve *"about"* nas duas páginas: é ordem de grandeza, não interruptor.

⬤ As causas declaradas de aprendizagem limitada são seis — PLAT-020 —, e valem como lista de diagnóstico:

1. audiência demasiado pequena
2. orçamento baixo
3. licitação ou controlo de custo demasiado baixo
4. sobreposição de leilão (a marca a competir consigo própria)
5. **evento de otimização pouco frequente**
6. demasiados anúncios a correr ao mesmo tempo

⬤ **Edições significativas reiniciam a aprendizagem** — PLAT-020. Mexer na criatividade, no orçamento ou na segmentação a meio é o erro mais comum e o mais caro.

**As três consequências que importam mais do que o número:**

- **Menos conjuntos com mais verba** é quase sempre melhor do que muitos conjuntos com verba dividida — resolve as causas 1, 2 e 4 de uma vez.
- **Escolher um evento de otimização que aconteça com frequência suficiente.** Otimizar para uma compra que acontece três vezes por mês não dá sinal nenhum. Otimizar para um passo intermédio mais frequente — mensagem iniciada, contacto, visualização de página-chave — dá. É a causa 5, e é a que mais afeta negócios pequenos.
- **Não mexer.** A tentação de ajustar ao segundo dia é exatamente o que impede a campanha de sair da aprendizagem.

## Segmentação: o que mudou estruturalmente

Duas alterações que reorganizam a forma de trabalhar, e que são mais importantes do que qualquer número de desempenho:

⬤ **PLAT-025 — exclusões de segmentação detalhada.** A Meta anunciou a remoção das *Detailed Targeting exclusions* a 21 de janeiro de 2025: a alteração entrou na Marketing API v22 e passou a todas as versões da API a **21 de abril de 2025**. Não foi uma mudança genérica "desde março". As exclusões por público personalizado mantiveram-se; a exclusão de empregadores passou a controlo ao nível da conta. https://developers.facebook.com/blog/post/2025/01/21/removal-of-detailed-targeting-exclusions/

⬤ **PLAT-026 — sugestões no Advantage+ audience.** Dentro de **Advantage+ audience**, a Meta trata critérios como interesses como sugestões e pode encontrar pessoas fora delas. A Meta apresentou este funcionamento a **12 de maio de 2023**, não como mudança universal em fevereiro de 2026, e preservou controlos rígidos como idade mínima e localização. As opções manuais/originais dependem do tipo de campanha e da interface disponível na conta. https://about.fb.com/fr/news/2023/05/lancement-de-lia-sandbox-pour-les-annonceurs-et-expansion-de-meta-advantage-suite/

◐ **Consequência prática, com âmbito.** Em campanhas que usem Advantage+ audience, não tratar camadas de interesses como fronteiras rígidas: a criatividade e o evento de conversão passam a fornecer uma parte maior do sinal. Isto **não elimina toda a segmentação manual**, não transforma geografia num mero palpite e não prova que o mesmo aconteça em cada objetivo ou conta. Verificar a configuração visível antes de reestruturar a campanha.

⚠️ **Sobre os ganhos de desempenho** atribuídos à segmentação algorítmica (reduções de custo por aquisição, subidas de retorno, saída mais rápida da aprendizagem): são **valores de referência internos da própria plataforma**, relatados por agências, **sem metodologia nem amostra publicadas**. A plataforma tem interesse comercial direto em que se adote a automação. Tratar como direção plausível, nunca como facto — e verificar com a própria conta.

**Onde a segmentação manual ainda vale claramente: geografia.** Num negócio local, restringir à área de serviço é a decisão de maior impacto e a mais barata. Um anúncio que alcança pessoas fora da área de entrega é dinheiro deitado fora, por muito bom que seja o custo por clique.

## Regras europeias que não existem nos guias americanos

⬤ O **Regulamento dos Serviços Digitais (DSA)** proíbe, nas plataformas em linha, duas formas específicas de publicidade baseada em definição de perfis. https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32022R2065

- anúncios baseados em definição de perfis que usem dados pessoais quando a plataforma saiba, com razoável certeza, que o destinatário é menor — não é uma proibição de toda a publicidade vista por menores;
- anúncios baseados em definição de perfis que usem categorias especiais de dados, como convicções políticas ou religiosas, orientação sexual, origem étnica ou saúde.

⬤ O artigo 26.º do DSA impõe **transparência no próprio anúncio** — identificação como publicidade, em nome de quem é apresentado, quem o pagou quando diferente e os principais parâmetros usados. O **repositório público** do artigo 39.º é uma obrigação adicional das plataformas e motores de pesquisa de muito grande dimensão, não de todas as plataformas. https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32022R2065

**Duas consequências práticas:** a criatividade tem de ser reconhecível como publicidade; e, **quando a plataforma mantém um repositório público aplicável**, os anúncios podem ser usados como inteligência competitiva. Na Meta, a Biblioteca mostra todos os anúncios ativos e conserva durante um ano os apresentados na UE. https://www.facebook.com/ads/library/ Ver `09-tendencias-e-concorrencia.md`.

### Política e temas sociais: decisões diferentes por plataforma na UE

⬤ O **Regulamento (UE) 2024/900** sobre transparência e direcionamento da publicidade política (TTPA) é aplicável **desde 10 de outubro de 2025**. Abrange mensagens "suscetíveis e concebidas para influenciar o resultado de uma eleição ou referendo, o comportamento eleitoral ou um processo legislativo ou regulamentar" — e não apenas campanhas de partidos.
https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX%3A32024R0900

Meta e Google reduziram a publicidade aceite, mas com âmbitos e exceções diferentes:

- ⬤ **Meta** — deixou de aceitar anúncios sobre política, eleições e **temas sociais** na UE a partir de **6 de outubro de 2025**. A publicação orgânica sobre os mesmos temas continua permitida; o que desaparece é a possibilidade de a amplificar com dinheiro. https://about.fb.com/news/2025/07/ending-political-electoral-and-social-issue-advertising-in-the-eu/
- ⬤ **Google e YouTube** — deixaram de aceitar publicidade abrangida pela sua política de **conteúdo político da UE**, com atualização em setembro de 2025. A regra inclui o âmbito do TTPA e categorias adicionais enumeradas pela Google; excetua certos anúncios de natureza puramente privada ou comercial e admite, mediante candidatura, algumas comunicações oficiais. Não é uma proibição geral de todo o conteúdo sobre temas sociais. https://support.google.com/adspolicy/answer/16409999
- **TikTok — `LOOK INTO`.** A política atual de publicidade não foi validada nesta cobertura e não governa recomendações.

⚠️ **Generalizar também custa dinheiro.** Na Meta, a saída inclui política, eleições e temas sociais; no Google/YouTube, aplica-se à publicidade que cai na definição política da respetiva política. Verificar a plataforma e a mensagem antes de produzir.

◐ **Quem isto atinge e não devia surpreender: as associações.** Na Meta, uma associação ambiental, de defesa de doentes, de moradores ou de uma causa que queira **impulsionar** uma publicação de sensibilização pode cair na definição de "tema social". No Google/YouTube, o teste é se a mensagem cai na política de publicidade política da UE. O caminho seguro é verificar a classificação antes de produzir; quando não houver via paga, ficam **orgânico, comunidade, parcerias, imprensa e e-mail**. Ver `12-contextos-de-negocio.md`.

### As categorias especiais que continuam a existir

⬤ A nomenclatura atual da Meta distingue **habitação, emprego e produtos e serviços financeiros**; esta última substituiu `CREDIT_ADS`. https://www.facebook.com/ads/library/api/
⬤ A Meta documentou restrições de idade, género e localização para habitação, emprego e a então denominada categoria de crédito, e declarou que as estendeu à UE. https://about.fb.com/news/2022/06/expanding-our-work-on-ads-fairness/ · https://about.fb.com/news/2023/01/an-update-on-our-ads-fairness-efforts/
◐ A consequência operacional pode ser menor precisão geográfica do que numa campanha local comum. Confirmar a categoria atual e os controlos efetivamente disponíveis **antes** de produzir a criatividade; não transformar valores históricos de idade ou raio numa regra universal.

⚠️ **E as categorias que mais provavelmente afetam um negócio português não vêm do DSA — vêm de reguladores nacionais.** Saúde (ERS), crédito e banca (Banco de Portugal), e o princípio da identificabilidade do artigo 8.º do Código da Publicidade aplicam-se a **qualquer peça, paga ou orgânica**. Estão em `10-risco-crise-e-conformidade.md`, e lêem-se antes de produzir, não depois.

⬤ A Meta anunciou rótulos para anúncios criados ou materialmente alterados com as suas ferramentas de IA generativa; isto não equivale a uma declaração manual universal para qualquer anúncio feito com IA. https://about.fb.com/news/2025/02/gen-ai-transparency-metas-ads-products/
⬤ Separadamente, o artigo 50.º do AI Act define deveres próprios de transparência para *deepfakes* e certos textos de interesse público. https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32024R1689 Ver `10-risco-crise-e-conformidade.md` antes de decidir o rótulo.

## O que não se transfere entre plataformas

A secção mais útil deste módulo, porque o raciocínio dos 50 eventos foi copiado para todo o lado sem verificação — e é da Meta.

| Plataforma | O que está documentado | O que NÃO existe |
|---|---|---|
| **Meta** | 50 eventos de otimização por conjunto em 7 dias, desde a última edição significativa — PLAT-020 | — |
| **Google** (licitação inteligente) — PLAT-021 | **Nenhum limiar de entrada** — o CPA-alvo funciona sem histórico de conversões. O número que existe é de **avaliação**: 30 conversões em 30 dias para julgar resultados; ~15 conversões/30 dias como referência de ROAS-alvo em Display | Um limiar para "sair da aprendizagem" |
| **Pinterest** — PLAT-022 | O indicador de modo de aprendizagem desaparece **em média ao fim de duas semanas**. Separadamente, **50 a 200 conversões por semana** é o que a *entrega* precisa para aprender a quem mostrar | Um limiar publicado de saída |

⚠️ **Outras plataformas ficam `LOOK INTO`** e não recebem aqui números de aprendizagem, mínimos nem regras de orçamento. Não preencher a lacuna com a regra da Meta.

**A regra geral que substitui a transferência automática:**

```
Antes de aplicar uma regra numérica noutra plataforma,
procurar essa regra na documentação DESSA plataforma.
Se não estiver lá, ela não existe — existe na Meta.
```

◐ **O que de facto se transfere**, e é pouco: (1) não mexer cedo, embora o motivo e o custo variem; (2) um evento de otimização frequente vale mais do que um evento raro; (3) poucos conjuntos com verba concentrada batem muitos conjuntos com verba dividida; (4) a criatividade decide o teto; (5) a geografia é a restrição manual que continua a valer em todo o lado.

⚠️ **E o mecanismo de proteção não é o mesmo.** Na Meta é *não mexer*, porque uma edição significativa reinicia a aprendizagem. No Google é **testar em experiência** — a documentação desaconselha limites de licitação e recomenda a opção de guardar como experiência em vez de alterar a campanha ativa. Aplicar o reflexo da Meta ao Google é deixar de testar sem necessidade.

## A pesquisa vem antes das redes, e o módulo devia dizê-lo

◐ Redes sociais interrompem; a pesquisa responde. Não é retórica — muda o que se compra. Nas redes paga-se para criar procura em quem não estava a pensar no assunto; na pesquisa paga-se para aparecer a quem já escreveu o problema.

**Para um negócio com morada e com procura existente** — "canalizador Braga", "clínica dentária Aveiro" — **a pesquisa é normalmente o primeiro euro mais bem gasto.** Este módulo chama-se promoção paga, não promoção paga em redes sociais, e assumir que são a mesma coisa é o erro que faz um negócio local gastar no sítio errado.

⬤ O Google declara que **não existe gasto mínimo** para usar Google Ads; o anunciante define o orçamento e pode ajustá-lo. https://business.google.com/us/google-ads/how-ads-work/

**Para um negócio com morada, o que muda a campanha:**

- ⬤ Os **elementos de localização** podem mostrar morada, mapa, distância e um botão de chamada; exigem uma fonte de dados, tipicamente o Perfil de Empresa do Google. https://support.google.com/google-ads/answer/2404182
- ⬤ Se um local estiver marcado como encerrado no Perfil de Empresa, os elementos de localização deixam de aparecer. https://support.google.com/google-ads/answer/2404182
- ⚠️ **Não prometer medição de visitas à loja.** ⬤ **PLAT-024.** A métrica exige locais verificados, elementos ativos, país elegível e "cliques ou impressões suficientes e tráfego pedonal suficiente para passar os nossos limiares de privacidade" — e sobre os valores a documentação declara que **variam por anunciante**. ◐ Tradução honesta: **um negócio pequeno com uma morada quase de certeza não vai ver visitas à loja medidas.** As ações locais que ficam realmente disponíveis são **cliques para telefonar e cliques em direções** — e é com essas que se monta o critério de sucesso.
- ◑ Os **Serviços Locais do Google** não aparecem nas listagens públicas de países que incluem Portugal. Tratar como "verificar antes de prometer ao cliente", não como facto fechado.

◐ **YouTube, para quem gere redes:** é sobretudo alcance barato com criatividade que já existe — as peças verticais feitas para Reels servem em Shorts. O erro caro é comprar formato não saltável com um vídeo pensado para ser saltado.

## Orçamento: o raciocínio que substitui o número

Os valores mínimos que circulam variam de umas dezenas a alguns milhares por mês e **nenhum tem amostra declarada** — são recomendações de agências e de fornecedores. Não os repetir.

O que é defensável é o raciocínio:

```
orçamento mínimo útil = eventos necessários para sair da aprendizagem × custo por evento esperado
```

⚠️ **A fórmula é por plataforma, não universal.** Na Meta, **50 eventos por semana por conjunto** multiplicados pelo custo por evento esperado: se o custo por conversa iniciada for de 2 €, são 100 € por semana por conjunto — abaixo disso o sistema não aprende e o desempenho fica instável. **Noutra plataforma, o número que entra na fórmula é o que ESSA plataforma documenta** — ver a tabela de equivalências acima. Não há um número universal, e usar o da Meta noutro sítio é orçamentar a partir de uma regra que não existe lá.

Se esse valor for incomportável, a resposta correta **não** é gastar menos: é escolher um evento de otimização mais barato e mais frequente, ou não pagar de todo.

E antes de começar: **teto de perda aceitável** definido, e **critério escrito de quando se desliga** — que se escreve assim:

## Quando parar

O critério escreve-se **antes de gastar o primeiro euro**, e tem quatro linhas:

```
Teto de perda:        ..... € no total. Ao atingir, para-se, haja o que houver.
Prazo mínimo:         ..... dias sem tocar — a fase de aprendizagem DESTA
                      plataforma, não a da Meta copiada.
Métrica de decisão:   custo por ..... (o evento mais frequente que ainda
                      importa ao negócio).
Limiar de desligar:   se o custo por ..... passar de ..... €, desliga-se.
                      (..... € = margem por unidade, calculada antes.)
```

◐ **Assinado por quem paga, antes de começar.** O objetivo não é rigor estatístico — é **retirar a decisão do momento em que ela é emocional**.

**Sinais que mandam desligar** ◐, por ordem de fiabilidade:

1. **O custo por resultado ultrapassou a margem** e manteve-se acima dela depois de a aprendizagem ter terminado. É o único sinal que não precisa de interpretação.
2. **O teto de perda foi atingido.** Sem discussão, sem "mais uma semana".
3. **O negócio não está a conseguir responder** ao que a campanha gera. Continuar é comprar má reputação a peso.
4. **O conjunto nunca saiu da aprendizagem** ao fim de duas semanas com verba estável. Não é sinal de que o anúncio é mau: é sinal de que **o evento escolhido é demasiado raro ou a verba demasiado curta**. Parar, mudar de evento, e só depois recomeçar.
5. **A frequência subiu e o custo subiu com ela.** Esgotamento criativo: pausa-se para renovar, não se conclui nada sobre o canal.
6. **Deixou de haver quem olhe para a campanha todas as semanas.** Uma campanha sem dono é uma subscrição, não um investimento.

**Sinais que NÃO mandam desligar** ◐ — e são os que mais vezes o fazem:

- Dois dias maus no início. É exatamente o que a fase de aprendizagem é.
- Alcance ou impressões abaixo do esperado **com o custo por resultado dentro do limiar**.
- Um comentário negativo.
- Comparação com um número de outro setor, outro país ou outra plataforma.

### A honestidade estatística que falta a quase todos os guias

◑ Com orçamentos pequenos **não se atinge significância estatística, e não vale a pena fingir que sim**. Aritmética verificável: para distinguir com 95% de confiança e 80% de poder uma taxa de conversão de 2% de uma de 3%, são precisas cerca de **3.900 observações por variante** — quase 8.000 cliques para comparar duas peças. Um negócio que faz 20 cliques por dia demoraria mais de um ano.

◐ A consequência não é desistir de testar; é **mudar o nome ao que se faz**. Com verba pequena não é um teste com vencedor: é **rotação criativa com registo de padrões**, como no orgânico (`07-analise-e-relatorio.md`). Declara-se um padrão quando ele **se repete três vezes**, não quando ganha uma vez.

> ◐ **E o critério que fecha tudo:** se, depois de a campanha ter parado, ninguém consegue dizer numa frase o que se aprendeu, **o problema não foi a campanha — foi não ter havido pergunta antes de começar.**

## O único benchmark que decide

◐ A economia do próprio negócio:

```
custo por pedido  vs.  margem desse pedido
```

Se o custo por pedido for superior à margem, não há volume que salve a campanha. Calcular **antes**, não depois.

Os valores de referência por indústria variam demasiado e quase nenhum declara a amostra. Num negócio pequeno com poucas conversões, medir por **custo por conversa iniciada** ou por contacto é mais estável do que por venda — há volume suficiente para o número significar alguma coisa.

| Métrica | O que é | Cuidado |
|---|---|---|
| CPM | Custo por mil impressões | Mede o preço do inventário, não a qualidade |
| CTR | Taxa de cliques | CTR alto com má conversão = promessa desalinhada |
| CPC | Custo por clique | Consequência do CTR e do CPM, não uma alavanca |
| **CPA** | **Custo por resultado** | **A métrica que decide** |
| ROAS | Retorno sobre investimento | Só faz sentido com receita rastreável |
| Frequência | Vezes que a mesma pessoa viu | Sinal de esgotamento criativo |

## Teste criativo

É onde está o ganho real. O sistema otimiza a distribuição; a criatividade decide o teto — e isso ganha peso nas configurações Advantage+ em que as sugestões de audiência não funcionam como fronteiras rígidas (PLAT-026).

- **Uma variável de cada vez** — gancho, imagem de abertura, oferta, formato.
- **Volume suficiente por variante** antes de decidir — e com verba pequena esse volume não existe. Ver *A honestidade estatística*, na secção **Quando parar**: são precisas ~3.900 observações por variante para distinguir 2% de 3%. O método honesto é **rotação criativa com padrões replicados**, não teste A/B com vencedor.
- **Vigiar a frequência.** ◐ Sinal útil **quando acompanhado de subida do custo por resultado**; isolado, não decide nada. Não há evidência publicada que o sustente como o sinal mais fiável, e o módulo dizia isso a mais.
- **Não correr demasiados anúncios em simultâneo** — é uma das causas declaradas de aprendizagem limitada.
- Criatividade nativa da plataforma bate criatividade que parece um anúncio.

## Medição no contexto europeu

O consentimento, o fim dos identificadores de terceiros e as restrições de rastreio tornaram a medição pós-clique menos fiável do que os guias americanos assumem. A ordem das quatro perguntas é que importa.

**Primeiro: o consentimento é pré-requisito, não formalidade.** ⬤ A política de consentimento da UE do Google obriga quem usa os seus produtos a obter consentimento juridicamente válido, no EEE, Reino Unido e Suíça, para o uso de armazenamento local onde a lei o exija e para a recolha e uso de dados pessoais na personalização de anúncios — com registo dos consentimentos e instruções claras de revogação. O incumprimento pode levar à limitação ou suspensão do acesso aos produtos. https://www.google.com/about/company/user-consent-policy/

⬤ Em Portugal a CNPD é explícita: o consentimento tem de ser **prévio, específico, diferenciado por finalidade, inequívoco e resultante de um ato positivo**, e **interfaces enganosas invalidam-no** — botão "Aceitar" em destaque com a recusa escondida **não é consentimento válido**. https://www.cnpd.pt/media/x2zdus50/nota-informativa-cnpd_cookies_20210625.pdf

**Segundo: o modo de consentimento não repõe o que se perdeu — e num negócio pequeno quase nunca chega a ligar-se.** ⬤ **PLAT-023.** A modelação de conversões só se ativa se o modo de consentimento (ou o IAB TCF v2.0) estiver corretamente implementado **e** existir um limiar de **700 cliques em anúncios em 7 dias, por país e por agrupamento de domínio**. Só depois os modelos entram em treino. https://support.google.com/google-ads/answer/10548233

◐ **Tradução:** um negócio pequeno em Portugal quase nunca faz 100 cliques por dia num único domínio. **A modelação não liga**, e o que se vê no gestor é a medição observada, com o buraco todo do lado de quem recusou. Escrever isto evita a conversa em que alguém diz "mas o modo de consentimento resolve".

**Terceiro: a interface do lado do servidor é robustez, não isenção legal.** ⬤ A API de Conversões da Meta é uma ligação servidor-a-servidor cujos eventos são tratados do mesmo modo que os do pixel, com desduplicação. https://developers.facebook.com/docs/marketing-api/conversions-api/

⚠️ **O que tem de ficar a negrito:** enviar o dado pelo servidor **não dispensa a base legal**. O requisito de consentimento aplica-se ao tratamento de dados pessoais para fins publicitários **independentemente do meio técnico** — pixel no navegador ou ligação servidor-a-servidor. A API serve para **não perder eventos de quem consentiu** (bloqueadores, falhas de rede), não para recuperar quem recusou.

**Quarto: o que um negócio pequeno consegue realmente medir hoje na UE.** ◐

| Consegue medir bem | Consegue medir mal | Não consegue medir |
|---|---|---|
| Mensagens e conversas iniciadas na própria plataforma | Conversões no site com consentimento parcial | Visitas à loja (limiares de privacidade não publicados) |
| Contactos recebidos em formulário nativo | Retorno sobre investimento por campanha | Percurso completo entre anúncio e compra ao balcão |
| Chamadas e cliques em direções | Atribuição entre plataformas | Efeito de longo prazo do alcance pago |
| Código promocional e ligação dedicada por campanha | Comparações mês a mês com alterações de consentimento pelo meio | Modelação de conversões abaixo dos 700 cliques/7 dias |
| A pergunta de origem feita ao cliente | | |

> **A regra de medição que resiste na UE é a mais antiga de todas: perguntar.** ◐ Um campo "como nos conheceu?" no momento do pedido produz um dado que nenhuma restrição de privacidade destrói e que nenhuma plataforma pode inflacionar.

**Consequência:** **triangular** (`07-analise-e-relatorio.md`). Analytics para otimização tática, código promocional ou ligação dedicada por campanha, e a pergunta de origem. **Não somar — comparar. A discrepância é o dado.**

## Orgânico e pago não são substitutos

O pago compra distribuição; não compra confiança nem repetição. Uma conta sem base orgânica que só existe quando há verba desaparece no dia em que a verba acaba.

A sequência sã: **orgânico prova o que funciona → pago amplia o que já provou → os resultados do pago voltam a informar o orgânico.**

## Modos de falha

- Promover conteúdo que não provou nada organicamente.
- Mexer na campanha durante a fase de aprendizagem, reiniciando-a.
- Espalhar verba pequena por muitos conjuntos de anúncios, e nenhum sair da aprendizagem.
- Otimizar para um evento demasiado raro — a causa mais comum de aprendizagem limitada num negócio pequeno.
- Correr demasiados anúncios ao mesmo tempo.
- Tratar sugestões de interesses do Advantage+ audience como se fossem fronteiras rígidas, ou assumir que este funcionamento se aplica fora desse âmbito — PLAT-026.
- Citar como facto os ganhos de desempenho da automação, que são material de marketing da plataforma sem metodologia.
- Declarar vencedor um teste ao segundo dia, ou testar três variáveis ao mesmo tempo.
- Medir por impressões em vez de por custo por resultado.
- Não calcular a margem antes: campanhas que "correm bem" e dão prejuízo por unidade.
- Não restringir a geografia num negócio local.
- Usar dados de categorias especiais em anúncios baseados em definição de perfis, ou apresentar anúncios assim perfilados a pessoas que a plataforma saiba com razoável certeza serem menores — proibido pelo DSA.
- Produzir criatividade para uma categoria especial sem verificar as restrições antes.
- Produzir uma campanha de sensibilização sem verificar se cai na proibição de temas sociais da Meta ou na definição mais estreita de publicidade política aplicada por Google/YouTube na UE.
- Aplicar a regra dos 50 eventos fora da Meta, onde ela não existe.
- Prometer medição de visitas à loja a um negócio pequeno com uma morada.
- Instalar a API de conversões a pensar que dispensa consentimento.
- Assumir que promoção paga significa redes sociais, num negócio com morada e procura existente que a pesquisa captaria melhor.
- Declarar vencedor um teste que nunca teve volume para o ser.
- Avançar num setor regulado (saúde, crédito, seguros, jogo, imobiliário) sem ler as obrigações do regulador nacional **antes** da produção. As recusas repetidas acumulam-se ao nível da conta.
- Gerar procura que o negócio não consegue servir.
- Deixar a mesma criatividade a correr até à exaustão.
- Continuar a pagar por falta de um critério escrito de quando desligar.
- Concluir que "as redes não funcionam" a partir de um teste mal montado com verba insuficiente para sair da aprendizagem.

## Do perfil de marca

Existe orçamento e quanto · margem por pedido · custo por evento esperado · capacidade de resposta · área geográfica · o que já provou funcionar organicamente · setor regulado e regulador competente · categorias especiais aplicáveis · **se é associação e faz comunicação de causa** · quem autoriza gastar.
