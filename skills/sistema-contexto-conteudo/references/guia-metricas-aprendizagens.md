# Guia de boas práticas — METRICAS-E-APRENDIZAGENS.md

## Propósito

Transformar resultados de conteúdo em decisões futuras, mantendo separados os dados observados, a interpretação e a decisão. O ficheiro guarda baselines e aprendizagens acionáveis; dados brutos devem permanecer na respetiva fonte ou exportação e ser referenciados.

## Informação obrigatória

- Responsável, estado, período analisado, última verificação e fontes.
- Fase atual do funil e definição de cada métrica utilizada.
- Baseline anterior a campanhas ou mudanças estruturais.
- Identificadores de campanha, conteúdo e plataforma.
- Objetivo e KPI principal definidos antes da leitura dos resultados.
- Resultados por janela temporal, com denominadores quando aplicável.
- Resultados de negócio e passos intermédios, não apenas sinais de atenção.
- Comparação apropriada com baseline, objetivo ou conteúdos equivalentes.
- Observação, hipótese explicativa e fatores de confusão separados.
- Nível de confiança, tamanho da amostra e limitações.
- Decisão concreta, responsável, prazo e forma de voltar a testar.
- Data de validade ou revalidação de cada aprendizagem.

Evitar dados pessoais. Sempre que possível, usar informação agregada e apontar para a fonte original.

## Atualização

- Guardar a baseline antes de campanhas e alterações de funil.
- Recolher resultados nas janelas definidas no brief; não impor a mesma janela a todos os formatos.
- Fazer uma síntese mensal e uma revisão após campanhas relevantes.
- Revalidar aprendizagens quando muda o público, plataforma, formato, oferta ou percurso de conversão.
- Corrigir dados históricos apenas com nota de alteração; nunca apagar silenciosamente resultados desfavoráveis.

## Anti-padrões

- Tratar likes ou seguidores como prova de impacto no negócio.
- Misturar métricas com definições diferentes entre plataformas.
- Comparar números sem período, alcance, impressões ou outro denominador relevante.
- Inferir causalidade a partir de correlação ou de um único conteúdo.
- Escolher apenas os resultados que confirmam a hipótese.
- Transformar uma hipótese em regra permanente.
- Somar conversas, cliques e compras como se fossem o mesmo evento.
- Alterar a fase do funil sem guardar uma baseline.
- Copiar dados brutos extensos para o documento sem produzir uma decisão.

## Perguntas de validação

1. Que decisão esta análise precisa de apoiar?
2. Qual era o objetivo e KPI principal antes da publicação?
3. A definição da métrica é consistente no período comparado?
4. Qual é a fonte, janela, denominador e baseline?
5. Que resultado de negócio ou passo do funil foi observado?
6. A diferença pode dever-se a formato, distribuição paga, ocasião ou outra variável?
7. A amostra é suficiente para uma conclusão ou apenas para uma hipótese?
8. Que ação concreta resulta da análise?
9. Como e quando a aprendizagem será novamente testada?
10. Há dados pessoais ou informação sensível que não deve ser guardada?

## Esquema Markdown/YAML conciso

~~~yaml
---
document_type: metricas-aprendizagens
brand: ""
owner: ""
status: draft # draft | validated | deprecated
funnel_phase: ""
period:
  from: YYYY-MM-DD
  to: YYYY-MM-DD
last_verified: YYYY-MM-DD
review_due: YYYY-MM-DD
sources: []
metric_definitions_reference: ""
---
~~~

~~~markdown
# Métricas e aprendizagens

## Baseline
| Métrica | Definição | Valor | Período | Fonte |
|---|---|---:|---|---|

## Resultados
| Campaign ID | Content ID | Plataforma | Objetivo | KPI | Janela | Resultado | Comparação |
|---|---|---|---|---|---|---:|---|

## Aprendizagens
### [LEARN-0001] — [título]
- Observação:
- Hipótese:
- Evidência:
- Amostra/limitações:
- Confiança: low | medium | high
- Decisão:
- Responsável e prazo:
- Próximo teste:
- Válida até/rever em:
- Estado: hypothesis | supported | disproved | retired

## Por confirmar
- [Questão · dados necessários · responsável]

## Registo de alterações
- YYYY-MM-DD — [alteração, fonte e responsável]
~~~
