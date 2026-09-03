# 7 — Análise de dados e relatório

Transformar números de plataforma em decisões — e, tão importante, saber o que cada número **não** diz.

**Cadência:** diário é vigilância, não análise · semanal é o primeiro nível legítimo de leitura · mensal é o cavalo de batalha · trimestral é revisão estratégica · anual é auditoria da própria medição.

**Delegabilidade:** ✓ Quase total, exceto extrair os dados (as APIs são autenticadas e o acesso é do dono) e conhecer o contexto que não está nos dados. Esta é também a área onde uma IA pode fazer mais estragos com ar de competência — produzir uma percentagem convincente a partir de uma amostra sem valor. **Salvaguarda: declarar sempre a base de cálculo e o tamanho da amostra ao lado de cada número.**

## O erro central da área

**Reagir a um único post.**

Um resultado excecional é quase sempre qualidade real **mais ruído aleatório**. A regressão à média garante que o seguinte será mais normal — o que leva a concluir erradamente que "a fórmula deixou de funcionar". ◑

A decisão toma-se sobre **grupos** de peças, nunca sobre uma peça.

**Regra dos três**, substituto pragmático da significância estatística para contas sem volume: ◐

| Observações | Estado |
|---|---|
| 1 vez | Nota |
| 2 vezes | Hipótese |
| 3 ou mais | Hipótese de trabalho — muda o plano |

É prática defensável, não método estatístico. Reduz o risco de confundir ruído com padrão; não o elimina.

## Definir antes de medir

Ordem obrigatória — *Digital Marketing and Measurement Model*, Avinash Kaushik ◑ (https://www.kaushik.net/avinash/digital-marketing-and-measurement-model/):

```
objetivo de negócio → meta → indicador → ALVO NUMÉRICO → segmentos de análise
```

O alvo numérico é o passo mais saltado e o mais crítico. **Sem alvo definido antes, qualquer resultado pode ser narrado como sucesso.**

O passo dos segmentos força a pensar em análise por grupo (formato, tema, hora) em vez de post a post — é a defesa estrutural contra o erro central.

## Separar atividade de resultado

O framework mais útil para distinguir vaidade de negócio, porque torna a distinção **estrutural em vez de moral** — o *Integrated Evaluation Framework* da AMEC, a associação internacional de medição de comunicação: ◑ https://amecorg.com/amecframework/

```
objetivos → inputs → atividades → outputs → outtakes → outcomes → impacto
```

- **Outputs** — o que foi produzido e distribuído (publicámos 20 posts, tivemos X impressões).
- **Outtakes** — o que a audiência retirou (notoriedade, atenção, pedidos de informação).
- **Outcomes** — mudanças de conhecimento, atitude ou comportamento.
- **Impacto** — resultado organizacional: vendas, reputação, relações.

**Se todas as métricas do relatório estão em "outputs", o relatório mede atividade, não resultado.**

Num negócio pequeno sem capacidade de medir outcomes com rigor, a aplicação honesta é: medir bem outputs e outtakes, e usar **proxies declarados e assumidos como tal** para outcomes — mensagens recebidas, pedidos de orçamento, respostas ao inquérito de origem.

## Vaidade não é propriedade da métrica

Teste de uma pergunta: **"se este número subir 30% no próximo mês, o que faço de diferente?"** Se a resposta for "nada" ou "não sei", é vaidade **nesse contexto**. ◑

Nota crítica: número de seguidores é vaidade para uma clínica que precisa de marcações, e pode ser acionável para uma marca que vende presença a parceiros. O critério é sempre a relação com a decisão, nunca a métrica em si.

## As fórmulas não são comparáveis

O problema técnico mais consequente da área, e o mais ignorado.

A mesma "taxa de interação" calculada sobre **alcance**, sobre **seguidores** ou sobre **impressões** dá resultados diferentes e incomparáveis:

- ⬤ A fórmula oficial do LinkedIn para páginas é **interações ÷ impressões**, e as interações **incluem cliques**. [LinkedIn Help](https://www.linkedin.com/help/linkedin/answer/a564051)
- ◐ Como o numerador e o denominador diferem dos usados noutras plataformas, comparar diretamente "a taxa do LinkedIn" com "a do Instagram" é comparar métricas diferentes com o mesmo nome.
- Uma fonte reporta ~3% para Instagram e outra 0,48% para o mesmo período. **As duas estão certas nas suas metodologias e são incomparáveis entre si.**

**Escolher uma fórmula, escrevê-la no perfil, e não a mudar durante o ano.** Trocar o denominador a meio pode duplicar a taxa sem que nada tenha mudado no desempenho real.

## O que as plataformas não contam exatamente

- ⬤ **As métricas da Meta que contam pessoas — incluindo alcance — são amostradas, não contadas exaustivamente.** https://www.facebook.com/business/help/181058782494426 Implicação subvalorizada: pequenas variações de alcance entre semanas podem ser ruído de amostragem, não mudança real.
- ◐ **Não somar alcance de vários posts ou períodos.** Cada valor pode conter as mesmas pessoas; sem desduplicação entre unidades, a soma não representa pessoas únicas alcançadas.
- ⬤ O LinkedIn declara que as impressões são "uma estimativa e podem não ser precisas" — usado aqui como **exemplo metodológico**, não como recomendação de canal. https://www.linkedin.com/help/lms/answer/a564051
- ⬤ A 21 de abril de 2025, a API de Insights do Instagram descontinuou `impressions` em *media insights* e *user insights* e `plays` em *media insights*, orientando as integrações para `views`; permaneceu uma exceção legada para certas impressões de media antigo consultadas em v21 ou anterior. [Instagram Platform Changelog](https://developers.facebook.com/documentation/instagram-platform/changelog)
- ◐ Uma comparação que atravesse essa mudança precisa de nota metodológica; não tratar como contínua uma série que misture métricas antigas e novas.
- ⬤ A Meta identifica quais métricas são estimadas, estão em desenvolvimento ou são modeladas. [Meta Business Help](https://www.facebook.com/business/help/metrics-labeling)
- ◐ Levar essa qualificação para o relatório, sobretudo quando o número sustenta uma decisão de investimento.

## Atribuição: o problema honesto

◑ Uma experiência controlada mediu que **100% do tráfego proveniente de WhatsApp e vários outros canais testados chegou às analytics classificado como "direto"**, sem informação de origem. É uma medição datada do conjunto testado, não regra universal nem especificação atual de plataforma. TikTok está `LOOK INTO`.
*SparkToro e Really Good Data, abril de 2023.* https://sparktoro.com/blog/new-research-dark-social-falsely-attributes-significant-percentages-of-web-traffic-as-direct/
*Amostra: 1.113 visitas em 10 dias, 16 páginas de teste em subdomínio sem tráfego prévio, cerca de 100 painelistas maioritariamente dos EUA/Canadá, abril de 2023. Os autores declaram que o painel não é representativo e que provavelmente **sobre-representa** o tracking disponível — na vida real a perda é provavelmente pior.*

**Consequência:** concluir a partir de tráfego "direto" que o social não traz visitas é uma leitura errada dos dados.

### Triangulação

Três vias independentes, cada uma errada de maneira diferente:

| Via | Capta | Falha em |
|---|---|---|
| Analytics + UTM | O que é rastreável | Partilha privada |
| Código promocional ou link dedicado | Ação real | Quem se esquece de o usar |
| "Como nos conheceu?" no momento do pedido | Memória | Enviesamento de ordem e de recência |

**Não somar as três — compará-las. A discrepância é o dado.**

Analytics para otimização tática dentro dos canais rastreáveis; inquérito declarado para decisões estratégicas sobre canais não rastreáveis. Para negócios locais e de serviços, o inquérito declarado é frequentemente a fonte **mais** fiável, não a menos.

Mitigações do inquérito: rodar a ordem das opções entre respondentes, incluir sempre campo aberto, perguntar no momento do pedido e não depois.

⬤ Nota técnica (https://support.google.com/analytics/answer/10596865): os modelos de atribuição de primeiro clique, linear, decaimento temporal e posicional foram descontinuados no Google Analytics 4 em 2023. Restam atribuição *data-driven* e último clique — o que penaliza estruturalmente o social, que vive nos toques intermédios.

**UTM:** minúsculas sempre (os parâmetros são sensíveis a maiúsculas, e `LinkedIn` e `linkedin` aparecem como duas fontes), separadores consistentes, valores documentados numa tabela, e **nunca marcar links internos** — quebra a sessão e reatribui o utilizador.

## Testes

Uma variável de cada vez · critério de paragem definido **antes** · registar o resultado mesmo quando é inconclusivo.

◐ Testes A/B em conteúdo orgânico de contas pequenas raramente atingem significância estatística. **Um post que alcança 340 pessoas não é uma experiência válida** — dizer isso é uma das funções mais valiosas de quem analisa. A alternativa defensável é acumular padrões replicados ao longo do tempo.

> Os limiares que circulam ("esperar 500 a 1.000 impressões por variante") são regras práticas sem origem estatística verificável.

## Sentimento automático

◑ O sarcasmo e a ironia são a maior limitação conhecida: investigação académica documenta quebras de precisão da ordem dos 50% na deteção automática, e os modelos são treinados maioritariamente em inglês — **em português europeu a fiabilidade é ainda menor**.
*Sykora, Elayan e Jackson (2020), Big Data & Society.* https://journals.sagepub.com/doi/10.1177/2053951720972735

Num negócio pequeno, com dezenas de menções por mês, **ler as menções manualmente é mais fiável do que qualquer classificador**. Percentagens de sentimento automáticas servem como indicador grosseiro de direção, nunca como medida.

## Share of voice

```
menções da marca ÷ total de menções do conjunto competitivo × 100
```

Variante mais informativa: a quota das menções **positivas**, em vez do volume bruto.

O número só tem significado se o conjunto competitivo for **definido explicitamente e mantido estável** entre períodos. Mudar os concorrentes incluídos torna a série inútil.

## Relatório que gera decisões

Cada secção em quatro tempos: **Situação** (o que era esperado) → **Complicação** (o que mudou) → **Questão** (o que isso levanta) → **Resposta** (a decisão proposta).

E cada secção termina numa frase no formato **ação + quantidade + prazo + responsável**:

> "Passar a dois carrosséis por semana no pilar X durante setembro — responsável: Y."

Se uma secção não consegue produzir essa frase, ou faltam dados ou a secção não devia estar no relatório.

Para quem decide, abrir com **impacto de negócio**, não com taxa de interação.

Estrutura completa e modelo em `../assets/relatorio-mensal-modelo.md`.

**Comparar sempre com o mês anterior E com o mesmo mês do ano anterior** — sem isso, a sazonalidade lê-se como desempenho.

**Usar mediana, não média.** A distribuição em social é fortemente enviesada por virais; qualquer benchmark que reporte médias sem medianas merece desconfiança.

## Métricas que não vêm das redes sociais

Num negócio elegível com atendimento presencial, o Google Business Profile merece secção própria. Usar apenas os campos presentes na exportação atual; uma divisão dos termos em marca vs. categoria pode ser uma classificação manual útil, desde que a regra seja documentada e estável, não apresentada como métrica nativa. Ver `12-contextos-de-negocio.md`, PLAT-012 e PLAT-013.

Um relatório que ignora um Google Business Profile elegível e relevante pode deixar de fora uma parte importante da procura local.

## As plataformas limitam o histórico disponível

A consequência operacional mais ignorada desta área: **uma análise que não foi exportada pode deixar de ser reproduzível na mesma interface ou com a mesma granularidade.**

| Fonte | Janela | Estatuto |
|---|---|---|
| Instagram, métricas de utilizador/conta | dados armazenados até 90 dias | ⬤ [Instagram Platform Insights](https://developers.facebook.com/documentation/instagram-platform/insights) |
| LinkedIn, destaques da página no desktop | até 365 dias | ⬤ [LinkedIn Page analytics](https://www.linkedin.com/help/linkedin/answer/a564051) |
| Google Search Console, relatório de desempenho | 16 meses | ⬤ [documentação atual do Google Search Central](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops) |
| Google Analytics 4, propriedades standard, dados ao nível do utilizador e do evento usados em explorações | 2 ou 14 meses, conforme a configuração | ⬤ [Google Analytics Help](https://support.google.com/analytics/answer/7667196?hl=pt) |
| TikTok | `LOOK INTO` | sem regra atual de retenção nesta cobertura |
| Google Business Profile | cerca de 6 meses | ◑ não declarado oficialmente |

**Exportar todos os meses, para uma folha própria.** Sem exportação, o negócio pode perder granularidade, comparabilidade e acesso a períodos que já saíram da janela; alguns relatórios agregados podem continuar disponíveis, mas já não reproduzem necessariamente a análise original.

⚠️ **Uma das decisões irreversíveis se for adiada:** se a análise depender dos dados ao nível do utilizador e do evento usados em explorações e a retenção do Google Analytics estiver no valor mais curto, mudá-la para o mais longo **agora**. Os dados que expirarem entretanto não voltam; esta definição não afeta os relatórios agregados standard. Exportar métricas com janelas próprias antes de expirarem é a outra proteção.

E o dado de resultado que **não expira** e não depende de plataforma nenhuma: a resposta à pergunta "como nos conheceu?", registada no momento do pedido.

## Registo de aprendizagens

Hipótese · variante · resultado · decisão · data · vezes observado.

Sem isto, a mesma pergunta é reinvestigada de trimestre a trimestre e o conhecimento evapora-se com a rotação de quem gere a conta. As conclusões que se mantêm verdadeiras voltam para o perfil de marca.

## Modos de falha

- Reagir a um único post.
- Mudar o denominador da taxa a meio do ano e comparar os resultados.
- Comparar com um benchmark cuja metodologia não se verificou.
- Comparar taxas entre plataformas como se medissem a mesma coisa.
- Tratar o alcance da Meta como contagem exata, ou somar alcances.
- Concluir que o social não traz visitas a partir do tráfego "direto".
- Escolher uma única fonte de atribuição e tratá-la como verdade.
- Usar último clique num negócio com ciclo de decisão longo.
- Parar um teste quando o resultado dá jeito.
- Otimizar uma métrica até ela deixar de significar o que significava — iscos de comentários para subir a taxa de interação.
- Apresentar crescimento do alcance **total** como melhoria quando o alcance **médio por post** desceu.
- Confiar em percentagens de sentimento automáticas.
- Calcular share of voice mudando o conjunto competitivo entre períodos.
- Relatar médias em vez de medianas.
- Páginas de gráficos bonitos que terminam sem uma única decisão.
- Comparar mês com mês sem controlar sazonalidade.
- Definir indicadores sem alvo numérico prévio.
- Medir tudo o que a plataforma oferece: 40 números não geram decisões, geram paralisia.
- Aplicar benchmarks de perfis de influenciador a contas de marca.
- Não registar as aprendizagens.
- **Prometer medição de retorno que a estrutura do negócio não permite.** Num negócio onde a conversão acontece ao balcão, sem inquérito de origem não há atribuição — dizer isso é mais profissional do que apresentar um número inventado.

## Do perfil de marca

Resultado de negócio e métrica-norte · indicadores e alvos · linha de base com data · fórmula e denominador escolhidos · convenção de UTM · existe percurso digital mensurável? · sazonalidade e ciclo de compra · quem lê o relatório.
