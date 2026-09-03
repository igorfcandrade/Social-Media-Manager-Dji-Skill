# Guia de boas práticas — CONFORMIDADE.md

## Propósito

Organizar verificações de direitos, privacidade, alegações, identificação de publicidade, regras de plataforma e acessibilidade. Este documento é uma checklist operacional, não aconselhamento jurídico definitivo. Requisitos legais e redações de divulgação devem ser confirmados por uma pessoa responsável com fontes autoritativas, datadas e adequadas aos mercados da campanha.

Quando houver dúvida material, o estado é “bloqueado para validação”; a skill não deve interpretar silêncio, publicação anterior ou prática comum como autorização.

## Informação obrigatória

- Mercados e jurisdições em que o conteúdo será usado.
- Responsável interno e, quando aplicável, revisor jurídico ou de conformidade.
- Data da revisão, próxima revisão e fontes autoritativas datadas.
- Matriz de relações comerciais: conteúdo da própria marca, pago, oferecido, afiliado, parceria ou outro.
- Processo para decidir se é necessária identificação publicitária e qual a formulação validada.
- Regras de direitos para imagem, vídeo, música, fontes, UGC, marcas e outras obras.
- Regras de consentimento, privacidade, testemunhos, pessoas identificáveis e menores.
- Alegações que exigem prova; localização e validade da evidência.
- Requisitos por plataforma que alterem publicação, áudio, divulgação ou formato.
- Critérios de acessibilidade verificáveis.
- Estado e aprovador por peça de conteúdo, incluindo pendentes e bloqueios.

### Mínimo de acessibilidade

- Texto alternativo útil para imagens informativas.
- Legendas sincronizadas e revisão humana em vídeo com fala; transcrição quando necessária.
- Informação essencial não comunicada apenas por áudio, cor, posição ou movimento.
- Texto legível, contraste adequado e elementos importantes dentro das áreas seguras do formato.
- Evitar flashes ou movimento potencialmente problemático; sinalizar quando não seja possível.
- Linguagem clara, ordem compreensível e uso moderado de emojis, maiúsculas e símbolos.

## Atualização

- Rever em periodicidade definida pelo nível de risco e sempre que mudar legislação, mercado, plataforma, parceria, tipo de conteúdo ou política interna.
- Registar a fonte, a data de consulta, o responsável pela interpretação e a data prevista para nova revisão.
- Rever cada campanha antes da aprovação final; conteúdo com relação comercial ou pessoas identificáveis exige decisão explícita.
- Não substituir fontes antigas silenciosamente: manter registo da alteração e dos conteúdos afetados.

## Anti-padrões

- Declarar que uma prática é “legal” ou “obrigatória” sem validação competente e fonte datada.
- Aplicar automaticamente uma etiqueta publicitária a todos os casos ou omiti-la por hábito.
- Usar apenas termos vagos como “cumprir acessibilidade”.
- Assumir que crédito ao autor substitui uma licença.
- Assumir consentimento por presença num evento, mensagem privada ou publicação anterior.
- Fazer alegações de saúde, ambiente, origem, exclusividade ou desempenho sem prova.
- Tratar regras de uma plataforma ou país como universais.
- Aprovar quando a decisão ainda é incerta.

## Perguntas de validação

1. Em que mercados e jurisdições será usado o conteúdo?
2. Existe pagamento, oferta, afiliado, parceria ou outra relação comercial?
3. A necessidade e a forma de identificação publicitária foram validadas para este caso?
4. Todos os elementos de terceiros têm direitos documentados e atuais?
5. Pessoas identificáveis e menores têm a autorização adequada?
6. Cada alegação factual tem prova suficiente, atual e rastreável?
7. O conteúdo cumpre os critérios de acessibilidade aplicáveis ao formato?
8. Há dados pessoais, testemunhos ou UGC que exijam tratamento adicional?
9. As fontes e regras de plataforma foram revistas recentemente?
10. Quem fez a validação humana e quando?

## Esquema Markdown/YAML conciso

~~~yaml
---
document_type: conformidade-conteudo
brand: ""
owner: ""
status: draft # draft | validated | deprecated
markets: []
jurisdictions: []
last_verified: YYYY-MM-DD
review_due: YYYY-MM-DD
human_reviewer:
  name: ""
  role: ""
  reviewed_at: YYYY-MM-DD
authoritative_sources:
  - title: ""
    url_or_reference: ""
    published_or_updated_at: YYYY-MM-DD
    consulted_at: YYYY-MM-DD
---
~~~

~~~markdown
# Conformidade de conteúdo

## Política validada
### Publicidade e relações comerciais
- Casos cobertos:
- Processo de decisão:
- Formulações validadas:
- Casos que exigem escalamento:

### Direitos, consentimento e privacidade
- Requisitos:
- Evidência aceite:
- Pessoas identificáveis/menores:
- UGC e testemunhos:

### Alegações
- Alegações permitidas e prova:
- Alegações proibidas ou por validar:

### Acessibilidade
- Imagem:
- Vídeo/áudio:
- Texto e contraste:
- Movimento/flashes:

### Plataformas
- [Plataforma · regra · fonte · data]

## Revisão por conteúdo
- Content ID:
- Relação comercial:
- Identificação necessária: yes | no | uncertain
- Formulação aprovada:
- Direitos: pass | fail | uncertain
- Consentimentos: pass | fail | uncertain
- Alegações: pass | fail | uncertain
- Acessibilidade: pass | fail | uncertain
- Decisão: approved | blocked
- Revisor e data:

## Por confirmar
- [Questão · risco · responsável · data prevista]

## Registo de alterações
- YYYY-MM-DD — [alteração, fonte e conteúdos afetados]
~~~
