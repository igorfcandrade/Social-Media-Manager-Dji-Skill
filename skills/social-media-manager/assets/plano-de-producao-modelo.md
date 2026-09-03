# Plano de produção — [campanha ou lote]

> Usar `POR_CONFIRMAR` onde falte uma decisão ou fonte. Não converter propostas em compromissos nem contar duas vezes um ativo reutilizado.

## 0. Controlo

| Campo | Valor |
|---|---|
| ID do plano | `PROD-AAAA-MM-###` |
| Item canónico/campanha | `POR_CONFIRMAR` |
| Estado | proposto / aprovado / em revisão |
| Resultado pretendido | `POR_CONFIRMAR` |
| Dono da decisão | `POR_CONFIRMAR` |
| Peças incluídas | |
| Fora de âmbito | |
| Linha de base/data | |
| Fontes consultadas e atualidade | |
| Conflitos ou pressupostos | |

## 1. Totais consolidados de ativos

Contar matéria-prima única separadamente dos ficheiros finais.

| Tipo | IDs únicos | Quantidade confirmada | Quantidade `POR_CONFIRMAR` | Nota de contagem |
|---|---|---:|---:|---|
| Fotografias selecionadas (`FOTO`) | | | | |
| Planos de vídeo a captar (`PLANO`) | | | | |
| Vídeos finais montados (`VID`) | | | | |
| Elementos gráficos de origem (`GRAF`) | | | | |
| Áudios de origem (`AUD`) | | | | |
| Exportações por superfície (`EXP`) | | | | |

## Inventário de entregas

| ID da entrega | ID da peça | Objetivo | Plataforma/superfície | Formato final | Data confirmada | Ativos de origem | Estado |
|---|---|---|---|---|---|---|---|
| `EXP-001` | `PECA-001` | | | | `POR_CONFIRMAR` | | proposto |

## 2. Lista de fotografias

| ID | Entregas servidas | Fotografia exata | Enquadramento/orientação | Pessoa/produto/local | Adereços/preparação | Espaço para texto/variações | Direitos/autorização | Critério de aceitação | Estado |
|---|---|---|---|---|---|---|---|---|---|
| `FOTO-001` | | | | | | | `POR_CONFIRMAR` | | proposto |

## 3. Lista de vídeos e planos

### Vídeos finais

| ID | Entregas servidas | Conceito/resultado | Duração-alvo | Planos usados | Áudio/locução | Texto integrado/legendas | Capa | Critério de aceitação | Estado |
|---|---|---|---|---|---|---|---|---|---|
| `VID-001` | | | | | | | | | proposto |

### Planos a captar

| Ordem | ID | Vídeo(s) | Enquadramento e movimento | Ação/o que aparece | Duração útil alvo | Fala/áudio/texto visível | Pessoa/produto/local/adereços | Continuidade e direitos | Critério de aceitação |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `PLANO-001` | `VID-001` | | | | | | | |

## 4. Formatos, rácios e durações-alvo

| ID da exportação | Plataforma/superfície | Ficheiro/orientação | Rácio | Dimensões confirmadas | Duração-alvo | Capa/zona segura | Acessibilidade | Origem da especificação e estado |
|---|---|---|---|---|---|---|---|---|
| `EXP-001` | | | `POR_CONFIRMAR` | `POR_CONFIRMAR` | `POR_CONFIRMAR` | | | PLAT-ID / fonte canónica / verificação na superfície / decisão de produção |

## 5. Pessoas, produtos, locais, adereços e autorizações

| ID | Tipo | Item/requisito | Ativos bloqueados | Disponibilidade/estado | Fonte ou responsável pela confirmação | Autorização/prova necessária |
|---|---|---|---|---|---|---|
| `LOG-001` | pessoa / produto / local / adereço / equipamento / autorização | | | `POR_CONFIRMAR` | | |

Confirmar, quando aplicável: direito de imagem · menores · testemunhos · conteúdo de terceiros · música · local privado · alegações reguladas · identificação de publicidade.

## 6. Mapa de reutilização entre peças

| Ativo de origem | Entregas/peças servidas | Transformação por destino | Poupança sem nova captação | Conflito de rácio, qualidade, continuidade ou direitos | Decisão |
|---|---|---|---|---|---|
| `FOTO-001` / `PLANO-001` / `GRAF-001` / `AUD-001` | | | | | confirmado / proposto / `POR_CONFIRMAR` |

## 7. Dependências e aprovações

| ID | Tipo | Requisito ou decisão | Bloqueia | Responsável | Prazo confirmado | Estado/prova | Consequência ou próximo passo |
|---|---|---|---|---|---|---|---|
| `DEP-001` | dura / suave / aprovação | | | proposto / confirmado / `POR_CONFIRMAR` | `POR_CONFIRMAR` | | |

## Candidatos a tickets

Não criar tickets por cada plano quando uma sessão tem o mesmo executor e a mesma aceitação.

| ID proposto | Resultado aceitável | Ativos/entregas | Escopo e não objetivos | Dependências | Executor | Revisor/dono de aceitação | Estimativa e confiança | Critérios de aceitação |
|---|---|---|---|---|---|---|---|---|
| `TKT-PROP-001` | | | | | proposto / confirmado | | XS–XL ou O/M/P; confiança | |

## 8. Handoff normalizado para a PJM

```yaml
schema: smm-production-handoff/v1
handoff_id: HANDOFF-PROD-AAAA-MM-###
canonical_work_item: POR_CONFIRMAR
production_plan_id: PROD-AAAA-MM-###
decision:
  approved_outcome_or_question: POR_CONFIRMAR
  owner: POR_CONFIRMAR
  state: proposed
executor:
  capability_id: adaptive-project-manager
  assignment_state: proposed
scope:
  in_scope: []
  non_goals: []
evidence:
  sources: []
  freshness: POR_CONFIRMAR
  unresolved_conflicts: []
baseline:
  id_or_location: POR_CONFIRMAR
  captured_at: POR_CONFIRMAR
inputs: []
dependencies:
  hard: []
  soft: []
permissions:
  permitted_surfaces: []
  mutation_authorization: propose-only
deliverable:
  description: Plano de produção e tickets reconciliados
  production_plan_location: POR_CONFIRMAR
  recording_location: POR_CONFIRMAR
acceptance:
  criteria: []
  validation_method: POR_CONFIRMAR
  reviewer: POR_CONFIRMAR
  owner: POR_CONFIRMAR
controls:
  failure_signals: []
  prohibited_actions:
    - publicar ou agendar sem autorização explícita
    - atribuir pessoas ou assumir compromissos sem confirmação
    - alterar um quadro ou sistema fora da autorização declarada
  stop_conditions: []
ticket_candidates:
  - id: TKT-PROP-001
    outcome: POR_CONFIRMAR
    asset_and_deliverable_ids: []
    dependencies: []
    executor: proposed
    acceptance_criteria: []
    estimate:
      active_effort: POR_CONFIRMAR
      review_or_decision_time: POR_CONFIRMAR
      waiting_time: POR_CONFIRMAR
      elapsed_forecast: POR_CONFIRMAR
      confidence: low
return_contract:
  allowed_statuses: [completed, partial, blocked, needs-decision, failed]
  required_fields:
    - handoff_id_and_canonical_work_item
    - output_and_location
    - mutations_and_affected_surfaces
    - evidence_and_checks
    - deviations_assumptions_limitations
    - new_dependencies
    - authorization_or_decision_required
    - recommended_next_state
next_state_after_return: review
```

## Verificação antes do handoff

- [ ] Todos os IDs referidos existem e os totais batem certo com as listas deduplicadas
- [ ] Cada entrega tem ativos suficientes ou uma lacuna explícita
- [ ] Rácios, dimensões e durações têm origem e estado
- [ ] Direitos, acessibilidade e publicidade foram verificados ou marcados `POR_CONFIRMAR`
- [ ] Dependências duras e suaves estão separadas
- [ ] Pessoas, datas e atribuições propostas não aparecem como compromissos confirmados
- [ ] A autorização de alteração está explícita
- [ ] O handoff conserva escopo, critérios de aceitação e contrato de retorno
