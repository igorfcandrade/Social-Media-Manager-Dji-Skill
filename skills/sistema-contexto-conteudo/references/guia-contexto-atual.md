# Guia — `CONTEXTO-ATUAL.md`

## Propósito

Concentrar o estado volátil necessário para decidir o que pode ser comunicado hoje. Substitui memórias genéricas e snapshots espalhados, sem duplicar as regras estáveis dos outros documentos.

## Informação obrigatória

- data e hora de referência, fuso horário e responsável;
- prioridade comercial/editorial atual;
- campanhas ativas e próximas datas relevantes;
- produtos/serviços prioritários com estado, fonte e validade;
- stock ou capacidade relevante para comunicação;
- estado do checkout, formulário, links e canais de encomenda;
- prazo total atual, cobertura geográfica e alterações logísticas;
- promoções ou condições ativas, com início/fim e aprovação;
- incidentes, bloqueios e decisões temporárias;
- lista curta de factos expirados ou por confirmar.

Não copiar o catálogo inteiro. Registar apenas o que pode alterar uma decisão no período atual e apontar para a fonte canónica.

## Atualização

Rever antes de cada campanha e, enquanto houver atividade regular, pelo menos semanalmente. Atualizar imediatamente após alteração de stock, capacidade, checkout, prazo, promoção ou canal.

## Não deve conter

- identidade ou tom de voz;
- aprendizagem histórica extensa;
- instruções técnicas de administração;
- permissões permanentes para ações externas;
- factos sem fonte e data.

## Esquema recomendado

```markdown
---
schema_version: 1
document_status: validated
owner: NOME
as_of: YYYY-MM-DDTHH:MM:SS+00:00
review_due: YYYY-MM-DD
source_of_truth_for: [estado operacional atual]
---

# Contexto atual

## Prioridade deste período

## Campanhas e ocasiões próximas
| id | tema | janela | estado | fonte |
|---|---|---|---|---|

## Oferta e capacidade relevantes
| item | estado | fonte | verificado em | válido até | publicável |
|---|---|---|---|---|---|

## Percurso de encomenda ativo

## Prazos e entrega atuais

## Condições comerciais ativas

## Incidentes e limitações temporárias

## Expirado ou por confirmar

## Registo de alterações
```

## Perguntas de validação

- A data de referência ainda cobre o período da campanha?
- O estado do produto e o CTA vêm da mesma jornada de compra?
- Prazo e entrega estão expressos como total para o cliente?
- Há uma promoção ou alteração de canal que já terminou?
- Algum facto contradiz `CATALOGO.md`, `OPERACOES.md` ou a fonte live?
