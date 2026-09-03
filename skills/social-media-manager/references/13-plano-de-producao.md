# Plano de produção

Transforma um conjunto de peças acordado numa lista única do que é preciso captar, produzir, rever e entregar. O objetivo é evitar duas falhas: descobrir material em falta durante a edição e pedir várias vezes o mesmo ativo porque cada peça foi planeada isoladamente.

Usar este modo quando o utilizador pedir um **plano de produção**, uma lista de fotografias ou planos, um lote, uma campanha, um calendário com várias peças ou uma passagem organizada para gestão de projeto. Numa legenda avulsa ou numa peça simples, só o usar se for pedido ou se a produção tiver dependências materiais.

## Fronteira do modo

O plano especifica a produção; não publica, não agenda, não contrata, não reserva, não compra, não confirma disponibilidade e não atribui pessoas ou datas por suposição.

- **A SMM decide:** decomposição criativa, ativos necessários, enquadramentos, planos, formatos, durações-alvo, reutilização e critérios de aceitação editorial.
- **A PJM coordena:** reconciliação com trabalho já existente, tickets canónicos, ordem, capacidade, compromissos, estados e fecho após aceitação.
- Uma PJM instalada é uma capacidade opcional, não uma dependência. Sem ela, entregar na mesma o bloco normalizado para utilização posterior.
- Um handoff não aumenta a autorização existente. Alterar um quadro, atribuir trabalho, reservar recursos, publicar ou contactar terceiros exige autorização aplicável.

## Entradas mínimas

Ler primeiro as fontes canónicas necessárias e congelar uma linha de base identificada:

1. peças, ideias ou calendário incluídos, cada um com ID estável;
2. objetivo, público, mensagem, formato e plataforma de cada peça;
3. produtos, pessoas, locais e ativos já disponíveis;
4. datas ou janelas **confirmadas**, capacidade e meios de produção;
5. restrições de marca, acessibilidade, direitos, publicidade e aprovação;
6. especificações voláteis da superfície, confirmadas no registo de plataformas ou marcadas `POR_CONFIRMAR`.

Se uma lacuna mudar a quantidade, a legalidade ou a viabilidade da captação, não inventar. Marcar `POR_CONFIRMAR`, indicar o ativo ou a decisão bloqueados e fazer apenas as perguntas essenciais. Um plano pode ser provisório, mas não pode parecer confirmado.

## Unidade de contagem

Contar separadamente a **matéria-prima única** e as **entregas finais**. Nunca somar uma adaptação como se exigisse nova captação quando reutiliza a mesma origem.

| ID | Unidade | Conta como nova quando… | Não aumenta o total quando… |
|---|---|---|---|
| `FOTO-###` | fotografia selecionada | precisa de imagem, enquadramento, momento ou composição materialmente diferente | é apenas corte, redimensionamento ou tratamento da mesma fotografia |
| `PLANO-###` | plano de vídeo a captar | muda a ação, enquadramento, posição de câmara, local, pessoa ou preparação necessária | é uma nova tentativa do mesmo plano |
| `VID-###` | vídeo final montado | tem narrativa ou montagem final autonomamente aprovável | é apenas uma exportação técnica do mesmo corte |
| `GRAF-###` | elemento gráfico de origem | precisa de composição, ilustração ou informação visual própria | é redimensionado sem alterar a informação |
| `AUD-###` | áudio de origem | precisa de locução, música ou captação sonora distinta | é mistura ou normalização do mesmo áudio |
| `EXP-###` | ficheiro final para uma superfície | muda rácio, duração, montagem, texto integrado, capa ou requisitos de destino | o mesmo ficheiro confirmado serve sem alteração |

Uma sequência de carrossel ou Stories deve declarar número de cartões/diapositivos. O total consolidado mostra, no mínimo, fotografias únicas, planos de vídeo, vídeos finais, elementos gráficos, áudios e exportações. Categorias a zero só se apresentam quando a ausência é útil; quantidades incertas ficam `POR_CONFIRMAR`, nunca `0`.

## Procedimento

### 1. Fixar escopo e linha de base

Dar um ID ao plano (`PROD-AAAA-MM-###` ou o padrão canónico do projeto), listar as peças incluídas e excluídas, fontes consultadas, data de validade e conflitos por resolver. Distinguir `aprovado` de `proposto`.

### 2. Inventariar entregas

Criar uma linha por combinação peça × superfície × formato final. A adaptação para outra plataforma é uma entrega própria mesmo quando partilha a origem. A linha inclui ID da peça, objetivo, plataforma/superfície, formato, data confirmada ou `POR_CONFIRMAR`, e IDs de ativos necessários.

### 3. Derivar e deduplicar ativos

Percorrer cada entrega e criar os IDs de origem. Reutilizar um ID apenas quando a mesma captação satisfaz todas as peças sem comprometer enquadramento, direitos, continuidade, qualidade ou sentido. Se houver dúvida, declarar a decisão de reutilização como provisória.

### 4. Especificar fotografias, vídeos e planos

Cada fotografia diz exatamente **o quê, quem, onde e como** deve aparecer, mais orientação, espaço para texto, variações essenciais e critérios de aceitação.

Cada vídeo final aponta para uma lista ordenada de planos. Cada plano inclui enquadramento, ação, duração útil pretendida, áudio/fala, texto visível, pessoa, produto, local, adereços, continuidade e entrega(s) que serve. Não confundir a duração útil do plano com o tempo total de gravação.

### 5. Confirmar formatos

Por exportação, declarar plataforma, superfície, tipo de ficheiro, orientação, rácio, dimensões quando confirmadas, duração-alvo, legendas, texto alternativo ou equivalente, capa e zonas seguras.

Um rácio ou limite volátil traz a origem: ID `PLAT`, fonte canónica da marca, verificação na própria superfície ou `decisão de produção`. Quando a informação não estiver confirmada, escrever `POR_CONFIRMAR antes de captar/exportar`. Não converter uma prática comum em regra da plataforma.

### 6. Fazer a matriz logística e de direitos

Consolidar, sem duplicados:

- pessoas e função em cena;
- produtos e quantidade/estado necessários;
- locais, acesso e janela confirmada;
- adereços, roupa, fundos, equipamento e consumíveis;
- autorizações de imagem, conteúdo de terceiros, música, testemunhos, menores, locais privados e alegações reguladas.

Para cada item, indicar quais ativos bloqueia e se está `confirmado`, `proposto`, `POR_CONFIRMAR` ou `não aplicável`, com fonte ou responsável pela confirmação. Uma menção numa peça não equivale a autorização escrita.

### 7. Mapear reutilização

Criar uma linha por ativo de origem com todas as entregas que serve e a transformação necessária: corte, nova abertura, nova chamada à ação, texto integrado, capa, legendas ou tratamento. Sinalizar conflitos de rácio, resolução, continuidade, direitos e marcas de água.

### 8. Ordenar dependências e aprovações

Separar:

- **dependência dura:** sem ela, a tarefa é impossível, ilegal ou insegura;
- **dependência suave:** reduz retrabalho ou aumenta confiança, mas não impede começar;
- **aprovação:** decisão com objeto, dono, estado, prazo confirmado e consequência.

Não inventar responsáveis nem datas. Uma função sugerida fica `proposta`; um compromisso só fica `confirmado` quando a fonte o sustenta. Aprovar o lote quando o risco e a organização o permitirem.

### 9. Propor unidades de trabalho

Propor tickets apenas para trabalho independentemente atribuível, sequenciável e aceitável. Não criar um ticket por plano de câmara se a sessão inteira tiver o mesmo executor e a mesma aceitação. Uma decomposição típica é: preparação/autorizações → captação por sessão → edição por família de entregas → revisão/acessibilidade → exportação/entrega.

Cada candidato inclui resultado, IDs abrangidos, escopo e não objetivos, dependências, executor/revisor/dono de aceitação propostos ou confirmados, critérios de aceitação e estimativa proporcional à prontidão. Separar esforço ativo, revisão, espera e tempo decorrido quando material; não apresentar datas precisas para trabalho ainda cru.

## Saída obrigatória

Usar `../assets/plano-de-producao-modelo.md` e devolver, por esta ordem:

1. totais consolidados de ativos;
2. lista de fotografias;
3. lista de vídeos e respetivos planos;
4. formatos, rácios e durações-alvo;
5. pessoas, produtos, locais, adereços e autorizações;
6. mapa de reutilização entre peças;
7. dependências e aprovações;
8. handoff normalizado para a PJM.

Antes de entregar, verificar que todos os IDs referidos existem, que cada entrega tem ativos ou uma lacuna explícita, que os totais resultam das listas deduplicadas e que nenhum `POR_CONFIRMAR` foi convertido silenciosamente em decisão.

## Contrato normalizado com a PJM

O handoff usa `schema: smm-production-handoff/v1`. É um contrato portátil em YAML, não uma ordem para alterar um sistema. Deve conter:

- `handoff_id`, `canonical_work_item` e `production_plan_id`;
- resultado aprovado ou pergunta delimitada, dono da decisão e estado;
- executor principal, marcado `proposed` ou `confirmed`;
- escopo, não objetivos, fontes, atualidade, conflitos e linha de base;
- entradas, dependências duras e suaves;
- superfícies permitidas e autorização de alteração;
- entrega e local de registo;
- critérios de aceitação, validação, revisor e dono de aceitação;
- sinais de falha, ações proibidas e condições de paragem;
- candidatos a ticket e relações de dependência;
- contrato de retorno e estado seguinte recomendado.

O executor devolve o mesmo `handoff_id` e `canonical_work_item`, um estado entre `completed`, `partial`, `blocked`, `needs-decision` e `failed`, a localização do resultado, alterações efetuadas, prova, verificações, desvios, limitações, novas dependências, autorização em falta e próximo estado recomendado. `completed` significa que a execução e as verificações do executor terminaram; não significa que o item canónico foi aceite ou fechado.
