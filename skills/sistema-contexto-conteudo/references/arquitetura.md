# Arquitetura do contexto de conteúdo

## Objetivo

Dar às skills uma base pequena, completa e atual. Cada facto tem uma fonte canónica; cada ficheiro tem âmbito, responsável e validade claros.

## Pacote recomendado

```text
CONTEXTO-MANIFESTO.md
MARCA.md
CATALOGO.md
OPERACOES.md
CONTEXTO-ATUAL.md
PERFIL-SOCIAL.md
ATIVOS.md
CONFORMIDADE.md
METRICAS-E-APRENDIZAGENS.md
CAMPANHAS/
└── _TEMPLATE-BRIEF.md
```

Os nomes podem mudar, mas o manifesto deve mapear os equivalentes. Evitar ficheiros genéricos como `MEMORY.md` sem âmbito e caminho canónico.

## Extensões condicionais

Não pedir estes ficheiros para uma campanha social simples. Acrescentar apenas quando o trabalho os exigir:

- `SITE-ESTADO.md`: páginas, URLs, checkout, schema e integrações atuais para conteúdo web/SEO.
- `VOZ-DO-CLIENTE-E-FAQ.md`: perguntas reais anonimizadas e respostas aprovadas para artigos, FAQ e atendimento.
- `CALENDARIO-OCASIOES.md`: calendário regional complexo quando não couber de forma clara no catálogo e no contexto atual.

Cada extensão deve seguir os mesmos metadados, atualidade e regras de autorização do núcleo.

## Função de cada camada

| Camada | Ficheiro | Tipo de verdade |
|---|---|---|
| Índice | `CONTEXTO-MANIFESTO.md` | caminhos, donos, estados, precedência e validade |
| Identidade | `MARCA.md` | essência, voz, provas e limites de alegação |
| Oferta | `CATALOGO.md` | produtos/serviços, ocasiões, personalização e jornada |
| Promessa operacional | `OPERACOES.md` | encomenda, produção, entrega, pagamentos e capacidade |
| Estado do momento | `CONTEXTO-ATUAL.md` | prioridades, stock relevante, checkout, prazos e incidentes atuais |
| Canais | `PERFIL-SOCIAL.md` | função, público, formatos e baseline por plataforma |
| Recursos | `ATIVOS.md` | existência, adequação, direitos e estado de cada ativo |
| Limites | `CONFORMIDADE.md` | publicidade, direitos, privacidade e acessibilidade |
| Evidência | `METRICAS-E-APRENDIZAGENS.md` | resultados, hipóteses e decisões validadas |
| Caso concreto | `CAMPANHAS/<id>.md` | objetivo, período, público, mensagem, CTA e entregáveis |

## Metadados comuns

```yaml
---
schema_version: 1
document_status: draft | validated | deprecated
owner: POR_CONFIRMAR
approver: POR_CONFIRMAR
source_of_truth_for: []
not_source_of_truth_for: []
last_verified: YYYY-MM-DD
review_due: YYYY-MM-DD
canonical_path: POR_CONFIRMAR
supersedes: []
---
```

No fim de cada documento incluir `Por confirmar` e `Registo de alterações`. Uma decisão pendente deve continuar explicitamente pendente.

## Metadados para factos voláteis

```yaml
value: POR_CONFIRMAR
source: POR_CONFIRMAR
verified_at: YYYY-MM-DD
verified_by: POR_CONFIRMAR
valid_until: YYYY-MM-DD
publishable: false
```

Usar este nível de detalhe apenas em factos que envelhecem e cuja incorreção altera a promessa: preço, stock, prazo, portes, checkout, promoções, capacidade ou estado de um canal.

A validade pertence ao facto identificado, não automaticamente ao documento inteiro. Um snapshot deve declarar se a validade cobre preço, stock, URL, disponibilidade ou outro campo; na dúvida, não alargar o âmbito.

## Níveis de prontidão

- **Ideação:** marca, oferta geral e objetivo suficientemente claros para propor direções sem alegações ou dados voláteis.
- **Rascunho:** marca, oferta, operações, contexto atual, perfil social e brief válidos para escrever versões por canal.
- **Produção:** além do rascunho, ativos, direitos, acessibilidade e conformidade aprovados para os formatos escolhidos.
- **Publicação:** factos voláteis revalidados, conteúdo final aprovado e autorização explícita no pedido atual para publicar.

Indicar sempre a etapa mais avançada segura. “Pronto para ideação” não significa “pronto para publicar”.

## Precedência por domínio

Não existe uma hierarquia única para todos os factos. A fonte especializada manda no seu domínio:

- `MARCA.md`: voz, posicionamento, diferenciação e alegações.
- `CATALOGO.md`: definição da oferta e personalização.
- `OPERACOES.md`: promessa logística e percurso de encomenda.
- `CONFORMIDADE.md`: direitos, publicidade, privacidade e acessibilidade.
- `PERFIL-SOCIAL.md`: adaptação por canal.
- `ATIVOS.md`: permissão para usar um ativo concreto.
- `CONTEXTO-ATUAL.md`: estado volátil, desde que cite a fonte especializada/live e esteja válido.
- Brief: decide a campanha, mas não pode alterar factos nem contornar marca ou conformidade.

Uma informação explícita e atual dada pelo utilizador no pedido prevalece para essa tarefa. Registar a mudança depois, se o utilizador pedir atualização dos ficheiros.

## Conflitos

1. Identificar os dois valores, caminhos e datas.
2. Verificar qual fonte é canónica para aquele domínio.
3. Se a fonte canónica estiver expirada ou o conflito persistir, não escolher silenciosamente.
4. Explicar o impacto e pedir uma decisão humana.
5. Não corrigir cópias ou migrar dados sem autorização.

## Separação entre skill e projeto

Uma skill pode guardar critérios como “comunicar o prazo total”. O número de dias pertence a `OPERACOES.md` ou `CONTEXTO-ATUAL.md`. Uma skill pode definir como avaliar um Reel; o desempenho real pertence a `METRICAS-E-APRENDIZAGENS.md`.

Esta separação evita que uma atualização do negócio exija editar a skill e impede que regras antigas pareçam factos atuais.

## Integração com skills de conteúdo

Antes de uma skill escrever ou planear:

1. validar o manifesto e a validade das fontes do domínio;
2. carregar o brief da campanha e apenas os documentos necessários ao formato;
3. usar `PERFIL-SOCIAL.md` para diferenças entre plataformas;
4. usar `ATIVOS.md` e `CONFORMIDADE.md` antes de recomendar ou reutilizar elementos visuais/áudio;
5. impedir que números ou estados mencionados na própria skill substituam dados do projeto;
6. no fecho, ligar os resultados a `METRICAS-E-APRENDIZAGENS.md`.

Uma skill de canal continua responsável pelo formato e pela qualidade criativa. Esta skill é responsável pela suficiência, proveniência e atualidade das entradas.
