# Guia de boas práticas — PERFIL-SOCIAL.md

## Propósito

Registar o contexto atual de cada rede social para que uma campanha seja adaptada ao papel, público e capacidade reais de cada canal. Este ficheiro descreve o estado presente das contas; não substitui a estratégia de marca nem o histórico detalhado de métricas.

## Informação obrigatória

- Marca, responsável, estado de validação, data da última verificação e próxima revisão.
- Fonte e período de observação de qualquer dado quantitativo.
- Por plataforma: nome da conta, URL ou identificador, estado da conta e mercado/idioma.
- Papel no funil, objetivo principal e ação que se espera da pessoa.
- Público observado, distinguindo dados medidos de hipóteses ainda por validar.
- Caminho atual de conversão: link, formulário, loja, mensagem ou outro.
- Pilares, formatos e cadência que a equipa consegue sustentar.
- Baseline resumida e aprendizagens atuais, com ligação ao ficheiro de métricas.
- Restrições conhecidas, funcionalidades disponíveis e questões por confirmar.
- Responsável por aprovar e publicar. Nunca guardar palavras-passe, tokens ou códigos de recuperação.

## Atualização

- Rever pelo menos mensalmente e antes de uma campanha relevante.
- Atualizar após mudanças de conta, público, funil, links, capacidade de produção ou funcionalidades da plataforma.
- Datar alterações e preservar a fonte. Se uma funcionalidade ou especificação não tiver sido verificada, marcá-la como “por confirmar”.
- Não copiar resultados mensais extensos para este ficheiro; atualizar apenas a síntese que ainda orienta decisões.

## Anti-padrões

- Tratar redes diferentes como se fossem o mesmo canal.
- Descrever o público apenas por intuição sem assinalar que é uma hipótese.
- Registar métricas sem período, fonte ou denominador.
- Fixar dimensões, limites ou funcionalidades da plataforma sem data de verificação.
- Confundir número de seguidores com objetivo de negócio.
- Definir uma cadência que a equipa não consegue produzir.
- Guardar credenciais ou dados pessoais de seguidores.

## Perguntas de validação

1. A conta e o respetivo link estão ativos?
2. Qual é o papel concreto desta plataforma no percurso até ao pedido ou compra?
3. O público descrito é observado nos dados ou apenas assumido?
4. Que formatos tiveram evidência suficiente de bom desempenho?
5. Qual é a cadência sustentável com os recursos atuais?
6. O CTA e o destino do link continuam corretos?
7. Há limitações de conta ou funcionalidades ainda não confirmadas?
8. Quem aprova e quem publica?

## Esquema Markdown/YAML conciso

~~~yaml
---
document_type: perfil-social
brand: ""
owner: ""
status: draft # draft | validated | deprecated
last_verified: YYYY-MM-DD
review_due: YYYY-MM-DD
data_window:
  from: YYYY-MM-DD
  to: YYYY-MM-DD
sources: []
metrics_reference: ""
---
~~~

~~~markdown
# Perfil social

## Contexto comum
- Mercado e idioma:
- Fase do funil:
- Capacidade semanal:
- Aprovação:
- Publicação:

## Plataformas

### [Plataforma]
- Conta/URL:
- Estado:
- Papel no funil:
- Objetivo principal:
- Público observado:
- Hipóteses por validar:
- CTA e destino:
- Pilares:
- Formatos:
- Cadência sustentável:
- Baseline datada:
- Aprendizagens atuais:
- Restrições/funcionalidades:
- Última verificação:

## Por confirmar
- [Questão · responsável · data prevista]

## Registo de alterações
- YYYY-MM-DD — [alteração, fonte e responsável]
~~~
