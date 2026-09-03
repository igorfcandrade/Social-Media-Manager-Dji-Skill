# Guia para `CATALOGO.md`

## Propósito

Documentar a arquitetura da oferta e indicar onde obter os factos comerciais atuais. A estrutura do
catálogo e o inventário live são camadas diferentes: a primeira explica como os produtos se organizam;
a segunda confirma o que pode ser comunicado numa data concreta.

## Obrigatório

- Metadados: proprietário, aprovador, estado, versão e datas de revisão.
- Fonte de verdade por campo: estrutura, produto, preço, stock, prazo, URL e ativos.
- Definições sem sobreposição para categorias, atributos, etiquetas, ocasiões, variantes e extras.
- Estado da estrutura: `proposta`, `aprovada`, `implementada` ou `divergente_do_live`.
- Identificador estável de cada produto ou serviço.
- Registo atual por item: nome aprovado, estado, categoria, ocasiões, materiais ou componentes,
  variantes, personalização, preço e moeda, stock ou disponibilidade, prazos, CTA, URL e data do dado.
- Prazo total percebido pelo cliente, quando aplicável, e fonte operacional desse prazo.
- Alegações e restrições específicas do item, com evidência.
- Inventário de fotografias e vídeos utilizáveis, incluindo direitos, consentimentos e validade.
- Regras para datas móveis e sazonalidade, com região e ano de validação.
- Decisões pendentes e efeito concreto de cada lacuna na comunicação.

Preço, stock, disponibilidade e prazos devem vir de um snapshot autorizado ou de uma fonte live
autorizada. O documento estrutural não os torna atuais por os mencionar.

## Opcional

- Conjuntos, compatibilidades, venda cruzada e substitutos.
- Ordem editorial ou comercial das famílias.
- Mapeamento para SEO, filtros, navegação e feeds.
- Cuidados, manutenção, embalagem e perguntas frequentes.
- Custos e margens numa camada interna com acesso restrito.
- Histórico de descontinuação e migração de taxonomia.
- Padrões de conteúdo por tipo de produto.

## Atualidade e governance

- Manter a arquitetura estável separada de exports ou snapshots voláteis.
- Datar todo o snapshot e indicar a origem, o responsável e a validade prevista.
- Verificar preço, stock, prazo, promoção, URL e ativos antes de cada campanha.
- Não consultar APIs ou sistemas externos sem a autorização necessária; pedir um export atual quando
  esse for o meio permitido.
- Rever a taxonomia quando a oferta mudar e comparar regularmente estrutura aprovada com estrutura
  implementada.
- Revalidar anualmente calendários e datas dependentes de país, região ou calendário móvel.
- Uma alteração de nome ou identificador deve preservar a ligação ao histórico.
- Nunca promover um item `rascunho`, `indisponível`, `obsoleto` ou sem direitos confirmados.

## O que não deve conter

- Métricas antigas apresentadas como estratégia permanente.
- Valores live sem fonte e data.
- Produtos desejados confundidos com produtos disponíveis.
- Stock baixo transformado automaticamente em urgência comercial.
- Custos internos na camada usada para comunicação pública.
- Campos vazios com significado implícito ou ambíguo.
- Informação regulada, de segurança ou sustentabilidade não validada.
- Procedimentos de importação, deploy ou publicação; devem viver em operações.
- Datas anuais copiadas indefinidamente sem mecanismo de revisão.

## Perguntas de validação

1. A estrutura aprovada coincide com o catálogo implementado?
2. Cada produto tem um identificador estável e uma fonte canónica?
3. Preço, stock, disponibilidade, prazo e URL foram confirmados para esta campanha?
4. Um campo vazio significa “não aplicável”, “não disponível” ou “a confirmar”?
5. As variantes e extras alteram produto, preço, prazo ou CTA de forma clara?
6. As ocasiões estão definidas pelo motivo do cliente e com datas regionais válidas?
7. As fotografias e vídeos correspondem ao item e têm direitos de uso?
8. As alegações do produto estão cobertas pelo registo de evidência?
9. Que lacunas impedem a publicação e quais apenas reduzem a qualidade?

## Esquema conciso

```yaml
catalogo:
  estado: rascunho | aprovado | obsoleto
  versao: ""
  proprietario: ""
  aprovador: ""
  revisto_em: YYYY-MM-DD
  fontes_de_verdade:
    estrutura: ""
    produtos: ""
    preco_e_stock: ""
    prazos: ""
    ativos: ""
  estrutura:
    estado_live: proposta | aprovada | implementada | divergente_do_live
    categorias: []
    atributos: []
    etiquetas: []
    ocasioes: []
  snapshot:
    origem: ""
    gerado_em: YYYY-MM-DDTHH:MM:SSZ
    valido_ate: YYYY-MM-DDTHH:MM:SSZ
  produtos:
    - id: ""
      nome: ""
      estado: rascunho | ativo | indisponivel | descontinuado
      categoria: ""
      ocasioes: []
      materiais: []
      variantes: []
      personalizacao: []
      preco: { valor: null, moeda: "", verificado_em: null }
      disponibilidade: { estado: "", quantidade: null, verificado_em: null }
      prazo_total: { valor: "", fonte: "", verificado_em: null }
      cta: ""
      url: ""
      alegacoes: []
      ativos: []
  pendentes: []
```
