# Guia de boas práticas — BRIEF-CAMPANHA.md

## Propósito

Fixar as decisões e os factos verificados de uma campanha concreta antes da produção. O brief liga contexto de marca, oferta, operações, canais, ativos, conformidade e medição, sem duplicar essas fontes de verdade nem conceder autorização implícita para ações externas.

## Informação obrigatória

- ID, nome, responsável, estado, datas e aprovadores.
- Objetivo de negócio, objetivo de comunicação e um KPI principal.
- Público prioritário, necessidade/insight e ação desejada.
- Produto, serviço ou ocasião em foco, com disponibilidade e fonte verificadas.
- Mensagem central, promessa e prova; alegações pendentes ficam bloqueadas.
- Pilar, ideia criativa e motivo da adequação à marca.
- Papel de cada plataforma e entregáveis nativos, evitando simples cópia.
- CTA, destino e percurso de conversão atualmente ativo.
- Ativos aprovados por ID e necessidades de produção ainda não autorizadas.
- Calendário, dependências, prazos operacionais e data-limite real.
- Decisões de direitos, acessibilidade e identificação publicitária.
- Plano de medição: baseline, KPI, métricas secundárias, fontes e janelas.
- Riscos, pendentes, dono de cada resposta e gate de aprovação.
- Permissões separadas para pesquisa externa, APIs, geração de imagens, publicação e investimento pago. O valor por defeito é false até autorização explícita.

## Atualização

- Criar em estado draft; passar a validated apenas depois de confirmar factos e responsáveis.
- Atualizar a cada decisão material e registar a origem da mudança.
- Voltar a validar preço, stock, prazo, CTA e ativos imediatamente antes da aprovação de conteúdo.
- Congelar a versão aprovada; alterações posteriores devem criar uma nova versão ou entrada clara no registo.
- Após a campanha, ligar aos resultados e aprendizagens, sem reescrever retroativamente os objetivos.

## Anti-padrões

- Usar o brief como fonte permanente de marca, catálogo ou operações.
- Definir vários objetivos, públicos ou KPIs como igualmente prioritários.
- Escrever “aumentar engagement” sem baseline, prazo ou resultado de negócio.
- Assumir stock, preço, prazo, funcionalidade ou direitos.
- Produzir o mesmo texto e formato para todas as plataformas.
- Permitir que o brief sobreponha regras de marca ou conformidade.
- Tratar silêncio como aprovação para publicar, pesquisar, usar APIs, gerar imagens ou investir.
- Aprovar com pendentes críticos ou sem responsável.
- Alterar objetivos depois de ver resultados.

## Perguntas de validação

1. Que resultado de negócio se pretende e como será reconhecido?
2. Qual é o único KPI principal?
3. Quem é o público prioritário e que necessidade concreta tem?
4. O produto, preço, stock, prazo e caminho de encomenda foram verificados quando?
5. Que promessa pode ser feita e qual é a prova?
6. Que função diferente tem cada plataforma?
7. Que ativos aprovados existem e o que ainda precisa de ser produzido?
8. Há relação comercial, direitos, consentimentos ou alegações a validar?
9. Como serão assegurados texto alternativo, legendas, legibilidade e áreas seguras?
10. Quais são as janelas e fontes de medição?
11. Que decisões estão pendentes e quem responde por elas?
12. Que ações externas foram explicitamente autorizadas?

## Esquema Markdown/YAML conciso

~~~yaml
---
document_type: brief-campanha
campaign_id: CAMP-YYYY-000
name: ""
owner: ""
version: 1
status: draft # draft | facts_validated | content_approved | closed
created_at: YYYY-MM-DD
last_verified: YYYY-MM-DD
campaign_period:
  from: YYYY-MM-DD
  to: YYYY-MM-DD
approvers: []
source_documents:
  brand: ""
  catalogue: ""
  operations: ""
  social_profile: ""
  assets: ""
  compliance: ""
  metrics: ""
permissions:
  external_research: false
  api_use: false
  image_generation: false
  publishing: false
  paid_media: false
---
~~~

~~~markdown
# Brief de campanha — [nome]

## Decisão central
- Objetivo de negócio:
- Objetivo de comunicação:
- KPI principal:
- Público prioritário:
- Insight/necessidade:
- Ação desejada:

## Oferta e factos verificados
- Produto/serviço/ocasião:
- Disponibilidade:
- Preço/condições:
- Prazo total:
- Fonte e data de verificação:

## Mensagem
- Mensagem central:
- Promessa:
- Prova:
- Pilar:
- Ideia criativa:
- CTA e destino:

## Plataformas e entregáveis
| Plataforma | Papel | Formato/entregável | Adaptação necessária |
|---|---|---|---|

## Ativos e produção
- Ativos aprovados por ID:
- Elementos em falta:
- Dependências:

## Conformidade e acessibilidade
- Direitos/consentimentos:
- Relação comercial e decisão de identificação:
- Alegações:
- Alt text:
- Legendas/transcrição:
- Legibilidade/áreas seguras:
- Revisor e data:

## Medição
- Baseline:
- Métricas secundárias:
- Fontes:
- Janelas de leitura:
- Ligação aos resultados:

## Pendentes, riscos e aprovação
| Item | Impacto | Responsável | Prazo | Estado |
|---|---|---|---|---|

## Registo de alterações
- YYYY-MM-DD — [alteração, motivo, fonte e responsável]
~~~
