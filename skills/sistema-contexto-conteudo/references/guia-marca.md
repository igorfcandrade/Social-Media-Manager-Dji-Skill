# Guia para `MARCA.md`

## Propósito

Definir a informação de marca necessária para que pessoas e sistemas produzam comunicação coerente,
reconhecível e verificável. O ficheiro preenchido deve ser uma fonte aprovada para identidade, voz e
alegações; não deve funcionar como campanha, catálogo live ou manual técnico do site.

## Obrigatório

- Metadados: projeto, proprietário, aprovador, estado, versão, última revisão e próxima revisão.
- Âmbito: matérias para as quais o ficheiro é ou não é fonte de verdade.
- Essência: propósito, proposta de valor, promessa e descrição factual da oferta.
- Posicionamento: categoria, diferenciação, alternativas e limites do posicionamento.
- Mercado e idioma: geografias servidas, variante linguística e convenções de tratamento.
- Público: segmentos prioritários, necessidades, contexto de compra e base factual das conclusões.
- Voz: atributos, ritmo, vocabulário preferido, palavras a evitar, CTAs e exemplos aprovados.
- Alegações: frase autorizada, evidência, limites, formulações proibidas, responsável e data de revisão.
- Identidade visual essencial: versões do logótipo, paleta, tipografia, fotografia e licenças dos ativos.
- Adaptação por canal: o que se mantém e o que pode variar, incluindo exceções de formato.
- Regras de direitos, publicidade identificada, privacidade e acessibilidade aplicáveis à comunicação.
- Hierarquia de decisão para resolver conflitos e lista explícita de temas ainda por aprovar.

Os dados de audiência devem distinguir `público estratégico` de `público observado`. Dados observados
precisam de fonte, período e dimensão da amostra.

## Opcional

- História de origem e marcos relevantes.
- Arquétipos, referências estéticas e território sensorial.
- Exemplos por canal e por tipo de mensagem.
- Temas sensíveis, resposta a crise e limites de humor.
- Pronúncia, grafia de nomes e glossário próprio.
- Matriz entre pilares de mensagem e públicos.

## Atualidade e governance

- Rever o núcleo após qualquer mudança estratégica e segundo uma cadência explícita.
- Rever dados de audiência, referências culturais e regras de plataforma com maior frequência.
- Uma alegação só é publicável enquanto a evidência e o âmbito continuarem válidos.
- Datar decisões que anulam regras anteriores e manter uma única versão aprovada.
- Separar o núcleo estável das especificações voláteis de canais e plataformas.
- Registar licenças, validade e restrições de logótipos, fontes, fotografia, música e outros ativos.
- Marcar claramente conteúdo `aprovado`, `provisório`, `pendente` ou `obsoleto`.

## O que não deve conter

- Preço, stock, disponibilidade, promoção ou prazo live.
- Objetivos, datas ou peças de uma campanha específica.
- Código CSS, detalhes de implementação ou dívida técnica do site, salvo ligação para outra fonte.
- Aspirações apresentadas como factos atuais.
- Perfis de público sem evidência ou data.
- Alegações legais, ambientais, de origem ou desempenho sem suporte verificável.
- Regras universais de formato que entrem em conflito com os canais abrangidos.
- Instruções para publicar, comprar mídia ou contactar terceiros.

## Perguntas de validação

1. Duas pessoas escreveriam textos reconhecidamente da mesma marca a partir deste ficheiro?
2. A promessa é concreta e distingue a marca sem depender de superlativos?
3. Cada alegação publicável tem evidência, limites e data de revisão?
4. O público descrito é uma decisão estratégica ou uma observação medida?
5. A voz tem exemplos suficientes de “sim” e “não” para reduzir ambiguidades?
6. Existem conflitos entre regras visuais gerais e formatos de plataformas específicas?
7. Estão definidos tratamento, variante linguística, CTA, emojis e acessibilidade?
8. Os direitos e licenças dos ativos estão confirmados?
9. Os temas pendentes estão impedidos de aparecer como factos?

## Esquema conciso

```yaml
marca:
  projeto: ""
  estado: rascunho | aprovado | obsoleto
  versao: ""
  proprietario: ""
  aprovador: ""
  revisto_em: YYYY-MM-DD
  proxima_revisao: YYYY-MM-DD
  fonte_de_verdade_para: []
  nao_e_fonte_de_verdade_para: []
  essencia:
    proposito: ""
    proposta_de_valor: ""
    promessa: ""
    oferta_factual: ""
  posicionamento:
    categoria: ""
    diferenciadores: []
    nao_somos: []
  mercado:
    geografias: []
    idioma: ""
    tratamento: ""
  publicos:
    - nome: ""
      tipo: estrategico | observado
      necessidade: ""
      fonte: ""
      periodo: ""
  voz:
    atributos: []
    preferir: []
    evitar: []
    cta: []
    exemplos_aprovados: []
  alegacoes:
    - frase: ""
      evidencia: ""
      limites: ""
      revisto_em: YYYY-MM-DD
      publicavel: true
  visual:
    ativos_canonicos: []
    paleta: []
    tipografia: []
    fotografia: []
    licencas: []
  acessibilidade_e_direitos: []
  pendentes: []
```
