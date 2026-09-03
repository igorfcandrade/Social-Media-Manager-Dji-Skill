# Guia para `OPERACOES.md`

## Propósito

Documentar a promessa operacional que pode ser comunicada ao público e o processo de transformar
factos aprovados em conteúdo revisto. Deve responder a duas perguntas: “o que podemos prometer hoje?”
e “como passa uma peça de conteúdo de rascunho a aprovada?”. Procedimentos técnicos detalhados vivem
em SOPs separados.

Um procedimento documentado não concede autorização para o executar: ações externas, publicação e
alterações live continuam dependentes do pedido atual.

## Obrigatório

- Âmbito operacional, mercado/geografia servidos e exclusões.
- Percursos de encomenda por tipo de oferta, CTA e destino atualmente válidos.
- Métodos de pagamento, estado do checkout/formulário e condições relevantes para o cliente.
- Tempos de preparação e transporte, incluindo a forma aprovada de comunicar o prazo total.
- Métodos, custos e restrições de entrega/recolha; fonte e validade de cada valor.
- Capacidade de produção, limites de volume e datas-limite reais para campanhas.
- Opções e limites de personalização, cancelamento, devolução, reclamação e apoio ao cliente.
- Regras de segurança, uso ou cuidado que alterem o que pode ser afirmado.
- Responsável e fonte de cada promessa volátil: prazo, preço operacional, entrega ou capacidade.
- Âmbito do processo de conteúdo, resultado esperado e exclusões.
- Proprietário, executante, revisor, aprovador e pessoa autorizada a publicar ou alterar o sistema.
- Evento de início, pré-condições, entradas, fontes de verdade e outputs.
- Versão dos esquemas de entrada e saída, campos obrigatórios, tipos, unidades e valores permitidos.
- Significado explícito de valores vazios, `null`, zero e estados desconhecidos.
- Ambiente alvo: local, teste, staging ou produção.
- Passo de pré-visualização ou simulação antes de uma alteração material.
- Pontos de aprovação e ações que exigem confirmação imediata.
- Identificadores imutáveis, regras de concorrência e prevenção de duplicados.
- Validações anteriores e posteriores, com critérios observáveis de sucesso.
- Falhas previsíveis, condição de paragem, recuperação e limites do rollback.
- Registo de execução: quem, quando, versão, inputs, resultado e exceções.
- Regras de privacidade, retenção, direitos de ativos e minimização de dados.
- Limites de pesquisa externa, APIs, automação, contacto e publicação.

Para conteúdo, o processo deve separar `factos recebidos`, `geração`, `revisão factual`, `revisão de
marca`, `aprovação` e `publicação`. A publicação nunca deve ser consequência implícita da aprovação do
texto.

## Opcional

- Diagrama do fluxo e matriz RACI.
- Checklist por volume ou nível de risco.
- Automação idempotente para tarefas comprovadamente repetitivas.
- SLAs, notificações e escalamento.
- Exemplos de entradas e saídas fictícias.
- Ligações para SOPs técnicos de importação, publicação, CMS ou deploy.
- Matriz de compatibilidade entre versões de ferramentas.
- Métricas de qualidade e amostragem de controlo.

## Atualidade e governance

- Rever imediatamente depois de alterações a encomenda, pagamento, produção, entrega, devoluções,
  capacidade, ferramentas, esquema, funções ou políticas.
- Confirmar prazos, custos, disponibilidade e percurso de compra antes de campanhas com promessa
  comercial ou data-limite.
- Registar `testado_em`, ambiente, versões relevantes e responsável pelo teste.
- Manter um único processo aprovado e marcar versões antigas como obsoletas.
- Validar periodicamente que os caminhos, nomes de campos e passos ainda correspondem ao sistema.
- Guardar snapshots com data; evitar aplicar um snapshot antigo sobre alterações posteriores.
- Definir retenção e eliminação segura de exports, backups e dados pessoais.
- Tratar produção como ambiente de maior risco, mesmo quando a interface torna a operação simples.
- Rever incidentes e atualizar apenas as regras apoiadas pelo que foi observado.

## O que não deve conter

- Credenciais, tokens, segredos ou dados pessoais reais em exemplos.
- Frases como “é o único erro possível” sem prova e delimitação rigorosas.
- Passos diretos sobre produção sem validação, aprovação e recuperação proporcionais ao risco.
- Uma garantia de rollback quando o backup não cobre todos os dados e ativos afetados.
- Dependência de labels de interface sem data e versão.
- Campos com semântica implícita.
- Valores comerciais live que pertencem às respetivas fontes canónicas.
- Prazos, portes ou capacidade sem fonte, data e validade.
- Procedimentos técnicos extensos que deveriam estar num SOP próprio.
- Instruções que transformem documentação interna em autorização do utilizador.
- Pesquisa externa, mensagens, compras, deploy ou publicação automáticos fora do âmbito autorizado.

## Perguntas de validação

1. Para cada tipo de oferta, qual é o CTA e o percurso de encomenda ativo?
2. O prazo comunicado é o total até ao cliente e tem fonte/data válidas?
3. A geografia, entrega, pagamento, personalização e devolução estão confirmados?
4. A capacidade real suporta a campanha e a respetiva data-limite?
5. Está claro quem pode preparar, rever, aprovar, executar e publicar?
6. Todas as entradas têm fonte, versão e esquema validável?
7. O procedimento distingue preparação, pré-visualização, aprovação e publicação?
8. Que passos alteram estado externo e onde é pedida autorização atual?
9. Existem condições de paragem para dados incompletos, conflito ou falha parcial?
10. Os exemplos estão livres de segredos e dados pessoais?

## Esquema conciso

```yaml
operacao:
  nome: ""
  estado: rascunho | aprovado | obsoleto
  versao: ""
  proprietario: ""
  papeis:
    executante: ""
    revisor: ""
    aprovador: ""
    publicador: ""
  revisto_em: YYYY-MM-DD
  testado_em: YYYY-MM-DD
  ambiente_testado: local | teste | staging | producao
  versoes_dependencias: {}
  autorizacoes_necessarias: []
  promessa_ao_cliente:
    geografias: []
    percursos_encomenda: []
    pagamentos: []
    preparacao: { valor: "", fonte: "", verificado_em: null, valido_ate: null }
    transporte: { valor: "", fonte: "", verificado_em: null, valido_ate: null }
    prazo_total_comunicavel: ""
    entrega_e_recolha: []
    personalizacao: []
    devolucoes_e_reclamacoes: []
    capacidade_e_limites: []
    regras_de_seguranca: []
  inicio: ""
  pre_condicoes: []
  entradas:
    - nome: ""
      fonte: ""
      esquema: ""
      obrigatoria: true
  passos:
    - id: ""
      acao: ""
      altera_estado: false
      aprovacao_antes: false
      validacao_depois: ""
  criterios_de_sucesso: []
  condicoes_de_paragem: []
  recuperacao:
    procedimento: ""
    limites: []
  registo_de_execucao: []
  retencao_e_privacidade: []
  sops_relacionados: []
```
