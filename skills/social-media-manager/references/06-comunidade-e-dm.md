# 6 — Comunidade, atendimento e conversa de venda

Tudo o que envolve responder a pessoas. É a área com maior retorno imediato, a menos documentada, e a que tem mais obrigações legais escondidas.

> ⚠️ **Estado da sustentação, atualizado a 2026-09-03.** A legislação portuguesa e os quatro acórdãos do TEDH têm agora **ligação oficial colada ao facto**, com números de queixa e datas confirmados. ⚠️ O `diariodarepublica.pt` não permite leitura automática: **o diploma está identificado, o articulado não foi relido por este sistema.** E **quatro estudos continuam sem autores nem publicação identificados** — o ensaio dos agentes automáticos, as perguntas de seguimento, a antropomorfização e as respostas acomodatícias. Estão assinalados no `FONTES.md`; enquanto assim for, usar a direção e a amostra que o texto declara e **não os citar como estudo publicado**.

**Cadência:** diária. É a única área que não tolera acumulação.

**Delegabilidade:** ◐ Um assistente rascunha respostas e propõe o passo seguinte; quem envia decide. **Preços, prazos e compromissos nunca saem sem validação humana.** ⬤ Desde 2 de agosto de 2026, quando um sistema de IA interage diretamente com uma pessoa, o artigo 50.º exige que esta seja informada de que fala com IA, o mais tardar na primeira interação, salvo quando isso for óbvio. https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32024R1689

> ⚠️ **Em Portugal, o canal principal de mensagem é o WhatsApp, não o Instagram.** ◑ *Marktest, «Os Portugueses e as Redes Sociais 2025» — 801 entrevistas online entre 3 e 15 de julho de 2025* (https://www.marktest.com/wap/a/grp/p~96.aspx). O **WhatsApp** aparece pela primeira vez como a rede com **maior penetração** em Portugal, 89,9% das referências entre utilizadores de redes sociais. O **Instagram é o mais utilizado** — mais de 32% das referências — e é onde se seguem marcas; o Facebook desce a terceiro em utilização mantendo a maior notoriedade. **A rede onde se seguem marcas e a rede onde a conversa acontece não são a mesma.** Planear a partir daí.

## Duas funções diferentes com o mesmo nome

| | Gestão de comunidade | Apoio ao cliente |
|---|---|---|
| Objetivo | Relação e presença | Resolver um problema |
| Voz | Participa na conversa | Responde como a marca |
| Métricas | Sentimento, temas, participação | Tempo de resposta, resolução |

Num negócio pequeno acumulam — e o conflito é real: as mensagens com intenção de compra chegam ao mesmo sítio que as reclamações.

## As janelas técnicas dependem do produto usado

Não transformar uma regra de API numa regra da aplicação. Antes de prometer automação, seguimento ou resposta fora de horas, registar no perfil **qual produto e interface a equipa usa**. A janela técnica condiciona o método de envio; a janela pública de atendimento deve ser realista e compatível com esse método, não copiada de uma API.

⬤ **Messenger Platform e Instagram Messaging API** — a janela standard permite uma resposta comum durante **24 horas** após a mensagem da pessoa. Na API do Instagram, a permissão e etiqueta `HUMAN_AGENT` permitem a um agente humano responder até **7 dias** em casos que não se resolvem na janela standard; não é autorização para automação promocional. Estas são regras das APIs, não das aplicações usadas manualmente. [Meta Messenger Platform API](https://www.postman.com/meta/messenger-platform-api/folder/vilwbh4/send-api) · [Meta Instagram API](https://www.postman.com/meta/instagram/documentation/6yqw8pt/instagram-api?entity=request-23987686-af579d08-121e-4897-8f45-5fd41ace49df)

⬤ **WhatsApp Business Platform** — as mensagens livres e os modelos seguem regras próprias da Platform. **Não aplicar essas regras à app WhatsApp Business gratuita**, nem tratar listas tradicionais, Business Broadcasts e Platform como o mesmo produto; PLAT-015. Confirmar na documentação da implementação os limites e custos atuais antes de automatizar.

> **A consequência operacional:** numa implementação da Business Platform, uma mensagem recebida antes do fim de semana pode exigir um fluxo diferente quando a equipa regressa. Na app gratuita, não afirmar que reabrir uma conversa exige um modelo pago. Registar o produto usado e confirmar a regra atual antes de desenhar o fluxo.
>
> Responder **uma linha** antes de fechar ao fim de semana pode preservar contexto e confiança, mas não se apresenta como obrigação universal da plataforma.

◐ **Não usar o distintivo "Muito recetivo a mensagens" como meta operacional.** A página oficial que descreve os limiares está atualmente fechada atrás de autenticação e não foi relida nesta revisão. https://www.facebook.com/business/help/201893553741970 Se o distintivo existir na página, confirmar no próprio interface o período e os critérios atuais; para um negócio de uma pessoa, persegui-lo pode levar a respostas apressadas. Declarar antes a janela real de atendimento.

## Velocidade: o que se sabe e o que se vende

◑ **Cerca de três em cada quatro consumidores dizem esperar resposta em 24 horas ou menos.** *Amostra: 4.044 consumidores que seguem pelo menos cinco marcas, mais 900 profissionais, nos EUA, Reino Unido, Canadá e Austrália, setembro de 2024.*
⚠️ **Conflito a declarar:** a fonte vende software de caixa de entrada unificada e redução de tempo de resposta. Um estudo dela a concluir "responda depressa" é interessado. A amostra está declarada e a pergunta é banal — mas dizê-lo é exatamente o que esta skill ensina a fazer.

⚠️ **O número dos "7 vezes mais" em uma hora não é para aqui.** Existe, tem amostra, e é de 2011, sobre venda por telefone nos EUA — e **um dos autores era diretor da empresa que vendia o software de resposta rápida que o artigo conclui ser necessário**. Serve como direção do efeito, não como alvo. **Uma operação de uma pessoa não consegue responder em uma hora e não deve tentar.**

**A leitura honesta:** a curva de decaimento é acentuada nas primeiras horas. A diferença entre 20 minutos e 2 horas importa menos do que a diferença entre 2 horas e dois dias.

## Declarar uma janela que se cumpre ◐

- **Escrever a janela no perfil e na mensagem de ausência**, com dias e horas concretos.
- **Declarar mais largo do que se cumpre.** Prometer 24h e cumprir 6h produz melhor reputação do que prometer 2h e cumprir 6h. É a única alavanca gratuita desta área.
- **Duas classes de mensagem, não uma.** "Está a decidir agora" (preço, disponibilidade, prazo urgente) e "pode esperar". Fora de horas só a primeira justifica interromper o descanso — e mesmo aí, uma linha a acusar a receção preserva contexto e, quando existe na implementação usada, **a janela técnica**.
- **Um bloco fixo por dia, não vigilância contínua.** A vigilância contínua é o que mais depressa leva ao abandono da função.
- **Não prometer uma janela que exija estar disponível ao domingo**, se ao domingo não se quer trabalhar.

⚠️ ⬤ **Se houver sequer um trabalhador por conta de outrem, isto deixa de ser preferência.** O **artigo 199.º-A do Código do Trabalho**, aditado pela [Lei n.º 83/2021, de 6 de dezembro](https://diariodarepublica.pt/dr/detalhe/lei/83-2021-175397114), impõe ao empregador o **dever de abstenção de contacto** durante o período de descanso, salvo força maior. A violação é contraordenação grave. **Não se pode montar uma escala informal de "vai vendo as mensagens ao domingo".**

## Duas obrigações legais que vivem nesta função

⬤ **Livro de reclamações eletrónico.** O [DL n.º 156/2005](https://diariodarepublica.pt/dr/detalhe/decreto-lei/156-2005-143320), alterado pelo DL n.º 74/2017, obriga a **divulgar no sítio na Internet, em local visível e destacado, o acesso à Plataforma Digital** (art. 5.º-B). Abrange também associações com atividade equiparada. A violação é contraordenação grave.

⬤ **Resolução alternativa de litígios.** O artigo 18.º da [Lei n.º 144/2015](https://diariodarepublica.pt/dr/detalhe/lei/144-2015-70215248) obriga a informar sobre a entidade de RAL competente, no sítio na Internet e nos contratos. Não obriga a aderir; obriga a informar. Coimas de 500 a 25.000 euros.

> Quando alguém escreve uma reclamação, a resposta correta em Portugal inclui, no momento certo, indicar o livro de reclamações e a entidade de RAL. **Não é hostilidade — é cumprimento, e é melhor ser a marca a dizê-lo do que o cliente a descobri-lo irritado.**

## Conversa de venda por mensagem

⚠️ **Aviso de honestidade:** **não existe investigação publicada sobre venda por mensagem direta.** O que existe é investigação sobre venda complexa por telefone dos anos 70-80, analítica publicada por quem vende software de analítica, e psicologia de conversação em laboratório. Esta secção é **prática informada por analogia** ◐ — marcá-la como tal é mais forte do que fingir prova.

**O que se transpõe com fundamento:** ◑ investigação que codificou mais de 35.000 chamadas de venda concluiu que técnicas de fecho agressivo funcionam em vendas pequenas e **correlacionam-se negativamente com o sucesso** em vendas grandes. A assimetria transfere-se: **quanto maior e mais irreversível a decisão, mais a conversa deve descobrir e menos deve empurrar.**

◑ E perguntar é subestimado: em três estudos de conversas reais entre pares, quem faz mais perguntas — sobretudo **perguntas de seguimento que retomam o que o outro acabou de dizer** — é mais apreciado. O mecanismo medido é a **responsividade**: escutar, compreender, validar, cuidar. As pessoas não esperam este efeito.
*Huang, Yeomans, Brooks, Minson e Gino, «It Doesn't Hurt to Ask», Journal of Personality and Social Psychology 113(3), 2017, pp. 430-452.* https://doi.org/10.1037/pspi0000097

### Estrutura de qualificação ◐

1. **Uma pergunta de enquadramento** que sirva para orçamentar *e* mostrar interesse — a data, a ocasião, a quantidade, o problema. Nunca mais do que uma de cada vez.
2. **Uma pergunta de seguimento sobre o que a pessoa disse**, não sobre o que falta ao formulário mental. É esta que constrói relação, e é a que quase toda a gente salta.
3. **Uma pergunta de restrição** — prazo, orçamento aproximado, o que não se pode falhar. Evita orçamentar para quem nunca ia comprar.
4. **Devolver o resumo antes do preço:** "então é para 40 pessoas, dia 12, sem glúten — é isto?" Um resumo confirmado transforma o preço seguinte em resposta a um pedido concreto, em vez de tabela abstrata.

### O preço ◐

- **Dar sempre.** A pergunta não é *se*, é *depois de quê*.
- **Uma pergunta de qualificação antes, não cinco.** Adiar por mais de uma troca lê-se como manobra.
- **Com âncora de âmbito, não número solto.** "Para 40 pessoas com estas três alterações fica em X, e inclui A e B" define o que está a ser comparado.
- **Dizê-lo uma vez, num parágrafo, e passar ao passo seguinte na mesma mensagem.** Um preço sozinho cria silêncio, e o silêncio depois de um número lê-se como negociação a abrir.
- **Não justificar sem ser perguntado.**
- ⚠️ **Nunca esconder o preço para "só em privado".** Além da desconfiança, aproxima-se do território das omissões enganosas no regime das práticas comerciais desleais.

### Objeções ◐

| Objeção | O que fazer | O que não fazer |
|---|---|---|
| **"É caro"** | Perguntar **com o que está a comparar**. Comparar com um concorrente é uma conversa; comparar com "não comprar" é outra | Baixar o preço, oferecer desconto não pedido, listar custos internos |
| **"Vou pensar"** | Perguntar o que falta decidir e propor data concreta de retoma. Um "sim" transforma o seguimento em compromisso, não em insistência | Aceitar em silêncio e ficar à espera |
| **"Tenho de falar com X"** | Perguntar o que o X vai querer saber, e dar isso **por escrito, pronto a reencaminhar** | Insistir em falar com o X |
| **Prazo impossível** | Honestidade imediata e alternativa concreta | Aceitar e esperar conseguir |
| **Comparação com mais barato** | Responder sobre o que é factualmente diferente. Às vezes o mais barato é a escolha certa para aquela pessoa | Desvalorizar o concorrente |
| **Pedido de reasseguramento disfarçado** ("e se não gostar?") | Um facto verificável **e uma política** — prazos, garantias, o que acontece se correr mal | Responder com entusiasmo |
| **Silêncio depois do preço** | Ver abaixo | Baixar o preço para quebrar o silêncio |

◑ Observação com conflito declarado (de quem vende software de análise de chamadas): os vendedores bem-sucedidos **fazem pausas mais longas depois de uma objeção** do que em qualquer outro momento. **O equivalente por escrito** é não responder no primeiro impulso e não responder a três coisas ao mesmo tempo. **Uma objeção, uma resposta.**

### Seguimento e fecho ◐

- **O seguimento tem de ter sido combinado.** Nasce da pergunta feita no fim da mensagem anterior. Sem esse acordo, qualquer seguimento é interrupção.
- **Dois seguimentos, no máximo.** O primeiro com **informação nova**, não "só a lembrar".
- **A mensagem de fecho de porta é a mais eficaz e a menos usada:** dizer que se vai deixar de incomodar, deixar a porta aberta, e não voltar. Liberta a pessoa da obrigação de responder — e é frequentemente ela própria que gera a resposta.
- **Fechar com pergunta de confirmação, não pedido de decisão.** "Reservo o dia 12?" tem resposta de uma palavra; "então, o que me diz?" obriga a redigir.
- ⚠️ **A janela técnica muda a mecânica apenas quando o produto usado a impõe.** Na WhatsApp Business Platform, confirmar as regras atuais antes de planear um seguimento fora da janela. Na app gratuita, não declarar a conversa tecnicamente morta nem exigir um modelo pago; PLAT-015.

⚠️ ⬤ **Reabrir conversas mortas por difusão em massa não é seguimento — é comunicação comercial não solicitada.** O [artigo 22.º do DL n.º 7/2004](https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-lei/2004-73199154-73197486) exige **consentimento prévio** para marketing direto por meios eletrónicos a pessoas singulares. E o [DL n.º 62/2009](https://diariodarepublica.pt/dr/detalhe/decreto-lei/62-2009-604821) cria a **lista nacional** de quem recusa comunicações publicitárias, mantida pela DGC e de **consulta obrigatória** por quem promove marketing direto.

## Automação: a conclusão que muda a prática

### O que se automatiza sem risco

⬤ **WhatsApp Business (aplicação gratuita):** perfil, catálogo, mensagem de saudação, mensagem de ausência, respostas rápidas, etiquetas, código QR, horário. [WhatsApp Business](https://whatsappbusiness.com/products/business-app-features/)
⬤ **Instagram:** as "Palavras ocultas" filtram comentários e pedidos de mensagem indesejados e aceitam uma lista personalizada. [Instagram Help Centre](https://help.instagram.com/700284123459336)
⬤ **Facebook:** o filtro de linguagem ofensiva e a lista personalizada ocultam também variações comuns das palavras, incluindo erros ortográficos, plurais, abreviaturas e substituições por números. [Facebook Help Centre](https://www.facebook.com/help/131671940241729)

**A regra:** automatiza-se o que **não é uma resposta** — enquadramento, triagem, organização e defesa. Respostas rápidas são atalhos de escrita usados por um humano que escolhe usá-los, não gatilhos.

### A tensão que decide tudo

◑ **Divulgar que se está a falar com um sistema destrói a conversão.** Ensaio de campo com mais de **6.200 clientes** distribuídos aleatoriamente: os agentes **não divulgados** foram tão eficazes como trabalhadores experientes; divulgar a identidade de máquina **antes** da conversa reduziu a taxa de compra em **mais de 79,7%**. *Mecanismo medido: percecionam-se como menos conhecedores e menos empáticos. O efeito é mitigado por divulgação tardia e por experiência prévia com IA.*
*Luo, Tong, Fang e Qu, «Frontiers: Machines vs. Humans», Marketing Science 38(6), 2019, pp. 937-947.* https://doi.org/10.1287/mksc.2019.1192

⬤ **E a lei obriga a divulgar.** O [artigo 50.º do Regulamento da IA](https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32024R1689), aplicável **desde 2 de agosto de 2026**, exige que as pessoas sejam informadas de que estão a interagir com um sistema de IA, de forma clara e **o mais tardar na primeira interação**. A exceção — quando é óbvio para uma pessoa razoavelmente informada — é interpretada de forma **restritiva** nas [orientações da Comissão Europeia](https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-transparency-obligations).

> **A síntese que muda a prática:** a investigação mostra que o único modo em que a automação de conversa é comercialmente competitiva é aquele em que ela **não se identifica**. A lei europeia obriga-a a identificar-se.
>
> Portanto, para um negócio pequeno em Portugal, **a automação de conversa de venda não compensa** — não porque seja má tecnologia, mas porque a versão legal custa quase 80% da conversão e a versão que não custa é ilegal.
>
> **Automatize o enquadramento, a triagem, a organização e a moderação. Escreva as respostas.**

◑ E se houver automação, **ela deve ser mais seca quando o assunto é uma falha, não mais simpática**: cinco estudos mostram que dar traços humanos a um agente conversacional tem **efeito negativo** na satisfação, na avaliação da empresa e na intenção de compra **quando o cliente entra já zangado** — e não tem efeito quando não está. O mecanismo declarado pelos autores é a **violação de expectativa**: a antropomorfização infla a expectativa de eficácia antes do contacto. O bot alegre com nome próprio a responder a uma reclamação é a pior combinação possível.
*Crolic, Thomaz, Hadi e Stephen, «Blame the Bot», Journal of Marketing 86(1), 2022, pp. 132-148.* https://doi.org/10.1177/00222429211045687

### O que nunca

- Automatizar objeções, reclamações, preços fora de tabela, prazos e compromissos.
- Automatizar qualquer coisa que produza **um número ou uma data que a marca tenha de cumprir**.
- Mensagem automática a novos seguidores — é o que mais depressa treina as pessoas a arquivar a conversa.
- ⬤ Na **WhatsApp Business Platform**, usar automação durante a janela de atendimento de 24 horas sem oferecer uma via de escalada rápida, clara e direta. A [política do WhatsApp Business](https://business.whatsapp.com/policy) exige esse caminho neste âmbito e admite, entre os exemplos, agente humano, telefone, email, suporte web, loja ou formulário.
- Usar ferramentas que não passem pelas interfaces oficiais.

⚠️ **A tática "comenta X que eu envio-te o link"** cai no ⬤ *engagement bait* documentado para o Facebook — publicações e Páginas reincidentes são despromovidas; PLAT-007. No Instagram, a fonte oficial proíbe recolher artificialmente gostos, seguidores ou partilhas, mas não sustenta a mesma penalização para todos os casos. **Que exista uma ferramenta para automatizar não torna a mecânica neutra.**

## Comentários públicos

**Responder sempre** — serve duas audiências: quem perguntou e quem está a ler. Curto em público; **puxar para privado quando a conversa vira pedido**.

### Mas não pelo motivo que se costuma dizer

⚠️ **Nenhuma plataforma declara que responder a comentários melhore a distribuição da publicação.** Mosseri afirmou publicamente que responder a comentários **não está entre os sinais principais** — os declarados são tempo de visualização, gostos por alcance e envios por alcance.

◐ **O que existe é uma hipótese indireta:** no explicador oficial de 2023, o Instagram incluía o histórico de interação entre duas contas entre os sinais de algumas superfícies. https://about.instagram.com/blog/announcements/instagram-ranking-explained Responder é uma interação; é, por isso, plausível que reforce a probabilidade de **aquela pessoa** voltar a ver **aquela conta**. Não prova aumento do alcance da publicação nem descreve necessariamente o sistema atual.

◑ A melhor medição disponível é correlacional: a análise do Buffer a **mais de 700.000 publicações** encontrou interação mais alta, face à linha de base da própria conta, quando o autor responde aos comentários. https://buffer.com/resources/replying-to-comments-boosts-engagement/
⚠️ **É correlação, não causalidade**, e a explicação alternativa é óbvia: publicações que já correm bem geram mais comentários a que responder.
⚠️ Quem publicou **vende software de publicação e gestão de interação**.
⚠️ **As 68.000 contas e os ~63% dos perfis não foram reconfirmados na fonte** — usar a direção, não esses números.

> **A conclusão prática não muda; o motivo sim.** Responde-se porque é prova social para quem lê, porque acumula afinidade pessoa a pessoa, porque é onde as vendas começam, e porque não responder é visível. **Não se responde para enganar o algoritmo.**

## Moderação — e a jurisprudência que quase ninguém conhece

⬤ **O titular de uma página responde pelos comentários de terceiros.** No acórdão *Sanchez c. França* (queixa n.º 45581/15, Grande Secção do Tribunal Europeu dos Direitos Humanos, **15 de maio de 2023**), um autarca foi condenado **não pelo seu próprio texto**, mas pela **falta de vigilância e de reação** a comentários de terceiros no seu mural público, que não removeu. O Tribunal concluiu, por maioria, **não haver violação do artigo 10.º**. [Comunicado do Tribunal](https://hudoc.echr.coe.int/app/conversion/pdf/?library=ECHR&id=003-7648098-10537594&filename=Grand+Chamber+judgment+Sanchez+v.+France+-+Applicant%E2%80%99s+conviction+for+not+promptly+deleting+unlawful+comments+on+Facebook.pdf)

Critérios que o Tribunal usou, e que interessam a qualquer negócio:

- A escolha de tornar a página pública e permitir comentários **não é censurável, mas não é isenta de consequências**.
- O Tribunal declarou que **"um grau mínimo de moderação posterior ou de filtragem automática seria desejável"**.
- A responsabilidade é **graduada consoante a situação objetiva de cada um**.
- **Apagar um comentário não isenta da responsabilidade pelos restantes** do mesmo fio.
- Um aviso público a pedir cuidado **não substitui a moderação** — foi o que ele fez, e foi condenado à mesma.

⬤ **A escala observada nos outros acórdãos depende dos factos de cada caso:** o Tribunal aceitou deveres mais pesados para um portal de notícias comercial gerido profissionalmente em [*Delfi AS c. Estónia*](https://hudoc.echr.coe.int/eng?i=001-155105) (n.º 64569/09, Grande Secção, 16/06/2015); em [*Pihl c. Suécia*](https://hudoc.echr.coe.int/eng?i=001-172145) (n.º 74742/14, **decisão de inadmissibilidade de 07/02/2017**), ponderou, entre outros fatores, a pequena dimensão e natureza não lucrativa do blogue e a remoção no dia seguinte à notificação; em [*MTE e Index.hu c. Hungria*](https://hudoc.echr.coe.int/eng?i=001-160314) (n.º 22947/13, 02/02/2016), distinguiu comentários ofensivos dos elementos de discurso de ódio e incitamento presentes em *Delfi* e concluiu que houve **violação** do artigo 10.º.

**Um negócio pequeno em Portugal está perto do polo *Pihl*, mas nunca é imune** — porque o critério operativo é sempre o mesmo: **o que fez o titular da página depois de saber.**

### A grelha que substitui "nunca apagar"

A regra "nunca apagar críticas legítimas" está **certa como regra de reputação e errada como regra de moderação**. A decisão faz-se em **dois eixos independentes**:

| | Conteúdo lícito | Conteúdo ilícito (ódio, ameaça, difamação, dados de terceiros) |
|---|---|---|
| **Crítica de boa-fé** | **Nunca apagar.** Responder em público, resolver em privado | Remover, registar, e responder ao que for legítimo em separado |
| **Provocação ou má-fé** | Não alimentar. Não responder é decisão válida. Ocultar é aceitável | **Remover prontamente e registar.** Aqui não há juízo de reputação a fazer |

> **Remover prontamente conteúdo claramente ilícito não é censura — é o que a jurisprudência espera de quem abriu a página aos comentários.**

**Consequências operacionais:**
1. **Não se responde por comentários que não se conhece.** Responde-se por não os remover **depois** de os conhecer.
2. **A moderação regular é uma defesa, não um risco.** Ativar as palavras ocultas e os filtros **é prova de diligência**.
3. **Não existe "não vi"** numa página pública com comentários abertos.
4. **Registar:** data em que se soube, data em que se atuou, captura de ecrã.

**Bloquear** ◐ — não encontrei jurisprudência que limite um negócio privado no bloqueio na sua própria página. Regra defensável: **bloquear é para quem impede a conversa** (spam, burla, assédio, repetição), não para quem discorda. E bloquear **não apaga** os comentários já publicados nem a responsabilidade por eles.

⬤ **Proteção de dados numa resposta pública.** No processo [C-210/16](https://curia.europa.eu/juris/liste.jsf?num=C-210/16), o TJUE concluiu que o administrador de uma página de Facebook pode ser corresponsável, com o Facebook, pelo tratamento de dados dos visitantes nas operações para cujas finalidades e meios contribui; não declarou uma corresponsabilidade universal por todo o tratamento feito pela plataforma.

◐ **Regra defensiva de ofício:** numa resposta pública a uma avaliação, não confirmar que a pessoa é cliente nem referir datas, valores, moradas, diagnósticos ou detalhes de encomenda, mesmo que tenha sido ela a expô-los primeiro. Numa clínica, qualquer resposta que possa revelar dados de saúde exige validação humana e, quando necessário, jurídica.

## Avaliações

### A evidência é boa — e está dividida

Esta é a correção mais importante deste módulo. A literatura **não** diz o que a indústria repete.

◑ **Estudo A (2017), em *Marketing Science*:** hotéis que **começam a responder** passam a receber **12% mais avaliações** e a classificação sobe **0,12 estrelas**. *Desenho: diferenças-em-diferenças explorando a diferença de prática entre duas plataformas — os hotéis respondem no TripAdvisor e quase nunca no Expedia.*

◑ **Estudo B (2018), na mesma revista, e contradi-lo.** Hipótese: como os gestores respondem mais a avaliações negativas, responder estimula **sobretudo** a atividade de avaliação negativa. Confirmou-se. *Amostra: 1.843 hotéis norte-americanos, todas as avaliações de 2009 a 2014.* Resultados: **+1,27 avaliações** e **−0,065 estrelas**. Os autores escrevem que os resultados "contrastam com" o estudo A, e argumentam que a sua amostragem é mais robusta.

◑ **Estudo C — uma estrela a mais corresponde a 5 a 9% mais receita.** *Descontinuidade de regressão nos limiares de arredondamento do Yelp, cruzada com dados fiscais estatais.*
⚠️ **A ressalva decisiva que muda tudo:** o efeito é **inteiramente conduzido por restaurantes independentes**. Nas cadeias, a classificação **não** afeta a procura — as avaliações substituem formas tradicionais de reputação, e quem já tem marca conhecida não ganha nada com elas. *Dados anteriores a 2010.*

**O que se retira:**

> **Estabelecido:** a classificação move receita, e move-a **sobretudo em negócios pequenos e independentes**, precisamente porque não têm outra reputação a que o cliente recorra. **Estabelecido:** começar a responder aumenta o volume de avaliações — os dois estudos concordam nisto.
>
> **Não estabelecido:** que responder faça **subir** a classificação. Um estudo mediu +0,12 estrelas; outro, posterior e com amostra maior, mediu **−0,065**. A explicação da divergência é plausível e importante: responder sinaliza que alguém está a ouvir, e **quem tem uma queixa fica mais motivado a escrevê-la**.
>
> **Consequência:** responder vale a pena — pelo motivo certo. Vale porque a resposta é lida por quem vai comprar a seguir, porque traz mais avaliações e portanto uma média mais estável e recente, e porque uma queixa sem resposta é pior. **Não vale como truque para subir a média.** Quem responder à espera de ver as estrelas subir vai provavelmente ver aparecer mais queixas primeiro — e desistir a meio é o pior resultado de todos.

### Como responder

◑ A resposta **acomodatícia** (reconhecer, assumir, dizer o que se corrigiu) e a **defensiva** (explicar, contextualizar) não são melhor e pior — **são para casos diferentes**: acomodatícia para **falhas concretas e imputáveis**, defensiva para **críticas vagas ou abstratas**. A razão medida: uma crítica concreta aumenta a atribuição de responsabilidade e a perceção de que o problema era controlável; uma abstrata não. A negação pura prejudica a confiança mesmo quando o problema estava fora do controlo.
*«Tailoring management response to negative reviews», Computers in Human Behavior, 2018 — ⚠️ autores por confirmar.* https://www.sciencedirect.com/science/article/abs/pii/S0747563218301146

⚠️ Responder de forma acomodatícia a uma crítica vaga ("péssimo serviço", sem mais) **admite uma falha que não se sabe qual é**.

### Pedir avaliações — e a armadilha que quase ninguém vê

⬤ A Google **proíbe** oferecer incentivos em troca de avaliações, desencorajar avaliações negativas e **solicitar seletivamente as positivas**. [Google Maps User Contributed Content Policy](https://support.google.com/contributionpolicy/answer/7400114?hl=pt)

⚠️ **"Review gating"** — filtrar quem recebe o convite — é a violação mais comum e a mais cara: **a sanção pode ser a remoção de todas as avaliações**, não apenas das obtidas por seleção. E o inquérito interno de satisfação que só encaminha para o Google quem respondeu 4 ou 5, **vendido como boa prática por muitas ferramentas, é exatamente a prática proibida**.

**O convite tem de ir a todos, ou a nenhum.**

◑ **E é por isso que pedir a todos melhora a média.** Em Portugal, cerca de **51,6%** dos utilizadores de redes sociais leem comentários de outros consumidores antes de comprar, mas só **18,1%** costumam dar opinião ou classificar. *(801 entrevistas online, Marktest, julho de 2025.)* Quem está satisfeito não escreve espontaneamente; quem está zangado escreve. **Sem convite sistemático, a amostra pública é estruturalmente pior do que a realidade.**

### O regime europeu

⬤ A Diretiva Omnibus, transposta pelo [DL n.º 109-G/2021](https://diariodarepublica.pt/dr/detalhe/decreto-lei/109-g-2021-175744207), que alterou o regime das práticas comerciais desleais, tornou práticas **enganosas em qualquer circunstância** — proibidas por si, sem ser preciso demonstrar efeito:

- Declarar que as avaliações são de consumidores reais **sem adotar medidas razoáveis para o verificar**;
- **Apresentar avaliações falsas**, ou mandar terceiros apresentá-las, ou **apresentar avaliações distorcidas nas redes sociais** para promover produtos.

E tornou **informação substancial** — cuja omissão é enganosa — a informação sobre **se e como** se garante que as avaliações vêm de quem usou ou comprou.

Traduzido:

1. **Publicar testemunhos no próprio site sem dizer nada sobre a origem é permitido.** Não é permitido **dar a entender** que são verificados sem ter processo para o verificar.
2. **Escrever avaliações próprias, pedi-las a amigos e família, ou encomendá-las, é proibido em qualquer circunstância.**
3. **Publicar só os testemunhos bons e omitir os maus**, apresentando o conjunto como representativo, cai na proibição.
4. A **remoção seletiva de avaliações negativas** é tratada como prática enganosa por omissão.

⚠️ **A alegação de "coimas de milhões" foi retirada:** não havia decisão oficial identificada que sustentasse destinatário, infração e montante. Não a citar.

### Avaliações falsas contra o próprio negócio

⬤ O [**Regulamento dos Serviços Digitais**](https://eur-lex.europa.eu/eli/reg/2022/2065/oj) estabelece: **artigo 16.º** — mecanismos acessíveis de notificação e ação para denunciar conteúdo ilegal; **artigo 20.º** — acesso à reclamação interna durante pelo menos seis meses após a decisão, tratada sob supervisão de pessoal qualificado e não decidida apenas por meios automatizados; **artigo 21.º** — possibilidade de recorrer a organismos certificados de resolução extrajudicial de litígios.

**Ordem certa** ◐: (1) não responder à quente e **nunca acusar em público**; (2) resposta neutra e curta, escrita para quem lê a seguir; (3) denunciar pela plataforma, com prova; (4) se rejeitada, reclamação interna e depois o artigo 21.º; (5) só então via legal.

> **Uma avaliação falsa afundada entre trinta genuínas faz menos dano do que uma guerra pública sobre ela.**

## Interação proactiva

Aparecer intencionalmente em conversas para além do próprio conteúdo. ◐ Um comentário com substância num post com muito alcance é a forma mais barata de visibilidade que existe para uma conta pequena. Exige constância.

Regra: comentar como quem tem alguma coisa a dizer, nunca como quem vai buscar tráfego.

## Comunidade própria

### Porque a maior parte morre ◐

⚠️ Os números que circulam ("95% das comunidades falham") não têm universo, definição de falha nem amostra, e vêm de quem vende software de comunidade.

**Os três modos de morte, por ordem de frequência:**

1. **Morte por vazio inicial.** Ninguém escreve porque não há ninguém a ler. Fatal em semanas. A única solução conhecida é o dono alimentá-la sozinho durante mais tempo do que quase toda a gente aguenta.
2. **Morte por dependência do dono.** Funciona enquanto o dono publica todos os dias — não é comunidade, é difusão com comentários, e morre na primeira semana de férias.
3. **Morte por ausência de razão para voltar.** Se o valor for "conteúdo da marca", já existe no feed. **Comunidades sobrevivem quando os membros ganham alguma coisa uns dos outros.**

◐ Sobre a "regra 90-9-1": a proporção exata é folclore, **a assimetria é real**. Uma comunidade de 200 pessoas não tem 200 participantes — tem talvez cinco. **Planear em função dos cinco.**

### O que é mesmo "próprio"

| Canal | Portátil? | Quem controla a entrega |
|---|---|---|
| Lista de correio, com endereços exportáveis | **Sim** | O negócio |
| Lista de números com consentimento | **Sim** | O negócio, mais as regras do WhatsApp |
| Grupo ou canal de difusão numa plataforma | **Não** | A plataforma |
| Comunidade em plataforma de terceiros | **Não** | A plataforma |

**Só o que se pode exportar e levar é próprio.** Um canal de difusão é alcance emprestado com outro nome.

⚠️ **E converter tem regra legal.** ⬤ Recolher o contacto não basta: o [artigo 22.º do DL n.º 7/2004](https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-lei/2004-73199154-73197486) exige **consentimento prévio expresso** para marketing direto a pessoas singulares, e a lista nacional da DGC é de consulta obrigatória ([DL n.º 62/2009](https://diariodarepublica.pt/dr/detalhe/decreto-lei/62-2009-604821)). **O cliente que deu o número para combinar uma entrega não deu consentimento para receber promoções.** No WhatsApp acumulam-se as duas exigências — a legal e a da plataforma.

### Quando vale a pena ◐

As três condições ao mesmo tempo: os clientes têm **razão para falar uns com os outros** · há **compra repetida ou relação continuada** · há **alguém que consegue estar lá todos os dias, e daqui a um ano**.

**Não vale a pena** quando o objetivo real é "ter um canal onde o alcance não dependa do algoritmo". Para isso o instrumento é uma **lista de contactos** — muito mais barata e sem risco de morrer em público.

⚠️ **Fechar uma comunidade que teve gente dentro custa reputação. É melhor não abrir do que abrir e fechar.**

## Modos de falha

- Respostas que soam a copy-paste de loja.
- Prometer prazos, preços ou condições de memória própria.
- Despejar toda a informação na primeira mensagem, ou terminar sem próximo passo.
- Fugir ao preço, ou justificá-lo sem ser questionado.
- Discutir encomendas ou reclamações em público extenso.
- **Confirmar em público que a pessoa é cliente** ao responder a uma avaliação.
- **Apagar críticas legítimas** — e o inverso: **deixar conteúdo claramente ilícito por remover depois de o conhecer.**
- Publicar um aviso de "regras da comunidade" e não moderar nada. Prova que se sabia e não se agiu.
- **Ignorar ao fim de semana uma conversa urgente**, ou, quando a equipa usa a WhatsApp Business Platform, deixar fechar a janela aplicável sem um fluxo previamente confirmado.
- **Perseguir o distintivo "Muito recetivo a mensagens"** numa operação de uma pessoa.
- **Usar "comenta X que eu envio-te"** — é despromovível.
- **Responder de forma acomodatícia a uma crítica vaga**, admitindo uma falha que não se sabe qual é.
- **Filtrar quem recebe o convite para avaliar** — arrisca a remoção de todas as avaliações.
- Publicar só os testemunhos bons apresentando-os como representativos.
- Automatizar a objeção e o caso complexo — e, agora, ter um sistema a atender sem se identificar.
- Prometer resposta imediata e falhar metade das vezes.
- Tratar grupos e canais de difusão como canais próprios.
- **Converter contactos para promoções sem consentimento prévio.**
- Abrir uma comunidade sem quem a alimente daqui a um ano.
- Publicar e desaparecer na primeira hora.

## Do perfil de marca

Canal principal de mensagem · onde chegam as mensagens · janela de resposta declarada · perguntas frequentes e respostas certas · preços, prazos e condições · o que se responde em público e o que passa a privado · o que se escala e a quem · **política escrita de moderação** (o que se remove, quem decide, onde se regista) · **entidade de RAL competente** · ligação ao livro de reclamações eletrónico · **quem deu consentimento para comunicações comerciais, e quando**.
