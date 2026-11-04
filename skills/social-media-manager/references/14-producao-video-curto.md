# Produção de vídeo curto

Transforma uma ideia ou guião aprovado em material captado, projeto editável e ficheiro pronto
para revisão. Usar para Reels, Shorts e outras superfícies de vídeo curto cuja utilização esteja
confirmada no contexto do caso. Para um lote ou campanha, consolidar IDs, logística e dependências
em `13-plano-de-producao.md`.

Este módulo especifica o trabalho; não publica, agenda, compra ferramentas, altera contas nem
promete capacidades que não tenham sido observadas.

## Três estados, sempre visíveis

Marcar cada decisão que possa parecer regra de plataforma:

- `[PLATAFORMA — confirmado AAAA-MM-DD]`: requisito ou política lida numa fonte oficial, com URL.
- `[PRODUÇÃO]`: escolha prática para reduzir risco ou retrabalho; não é requisito de alcance.
- `[HIPÓTESE]`: opção a comparar num conjunto de peças, com métrica e momento de decisão.

Uma configuração aceite por um editor ou plataforma não prova que melhora distribuição. Um limite
técnico não é uma duração recomendada. Uma prática comum não se promove a requisito sem fonte.

## Entregáveis e estado de prontidão

O percurso pode entregar:

1. brief congelado;
2. guião com intenção por bloco;
3. lista de planos e continuidade;
4. originais identificados;
5. projeto editável;
6. `MASTER-LIMPO`, sem marca de água de outra aplicação e sem música cuja licença fique presa a
   uma superfície;
7. uma ou mais entregas `EXP-###`, apenas quando existe diferença material;
8. ficha de música e direitos;
9. relatório de revisão.

Associar o estado ao **objeto** revisto:

| Objeto | Pronto para revisão quando… |
|---|---|
| Brief/guião | existem texto, intenção, fontes e decisões editoriais; não exige captação |
| Lista de planos | cada plano tem ação, continuidade e critério de aceitação |
| Montagem/exportação | há ficheiro real acessível e cobertura de inspeção declarada |
| Publicação | revisão editorial, técnica, direitos e pré-visualização por destino concluídas |

Usar `proposto`, `pronto-para-captar`, `captado`, `montagem`, `pronto-para-revisão`,
`aprovado` ou `bloqueado` com o objeto indicado. Um guião aprovado não aprova o vídeo final.
`SIMULADO` descreve dados fictícios ou placeholders; uma proposta editorial baseada em factos
reais não é simulação só por faltar filmar. Manter captação/exportação como pendentes.

## 1. Congelar o brief

Ler apenas o contexto necessário: objetivo, público, voz, direção visual, superfície, ação
pretendida, oferta e alegações, capacidade, ativos, direitos e aprovador. Referenciar a fonte de
cada preço, prazo, disponibilidade ou regra da marca; não os copiar para esta documentação.

Registar numa tabela curta:

| Campo | Decisão | Estado/fonte |
|---|---|---|
| Ideia e resultado para quem vê | | confirmado / proposto |
| Superfícies | | confirmadas / exploração |
| Ação seguinte | | uma principal |
| Matéria-prima real | | existente / a captar |
| Restrições de voz e visual | apontar para o dono canónico | |
| Factos comerciais | apontar para a fonte | `POR_CONFIRMAR` se necessário |
| Aprovação | objeto e pessoa/função | |

Não escolher duração por hábito. Definir primeiro o que o vídeo precisa de cumprir e só depois
propor um corte inicial.

## 2. Guião e lista de planos

Usar `guiao-video-curto` para o texto e a estrutura. Converter cada bloco numa linha de captação:

| ID | Função no corte | Enquadramento/ação | Áudio | Texto | Duração útil proposta | Continuidade | Aceitação |
|---|---|---|---|---|---|---|---|
| `PLANO-001` | abertura | | | | | | |

- A duração útil é o trecho pretendido na montagem; gravar margem antes e depois da ação.
- Uma nova tentativa do mesmo enquadramento mantém o ID e recebe `take 1`, `take 2`.
- Um novo gesto, ângulo, preparação, pessoa ou local recebe novo ID.
- Incluir um plano de segurança quando a ausência desse plano obrigaria a repetir a sessão.
- A capa pode ser um fotograma real sem texto. Ler `capa-de-video` quando a capa for parte do pedido.

## 3. Preparar a captação

Antes de gravar:

- limpar lente, libertar espaço suficiente e ativar grelha se ajudar o enquadramento;
- confirmar bateria, armazenamento, orientação, resolução, cadência e HDR/SDR no aparelho real;
- retirar do quadro nomes, moradas, mensagens, etiquetas de cliente e música ambiente protegida;
- preparar peça, fundo, luz, adereços e sequência para evitar mudanças de continuidade;
- fazer um teste curto e vê-lo no próprio telefone com e sem som antes de captar o lote.

### Percurso iPhone

Se for o aparelho disponível, usar [o percurso opcional](producao-video-ferramentas.md) e PLAT-031/PLAT-032 no registo 05. Não carregar as instruções de outros equipamentos.

## 4. Ingerir e conferir originais

Copiar os originais para a localização autorizada sem apagar o telefone. Preservar nome ou mapa de
correspondência com `PLANO-###` e take. Antes de editar, conferir pelo menos:

- o ficheiro abre do início ao fim;
- orientação, resolução, cadência e duração observadas;
- foco, cor, exposição, reflexos, tremor e continuidade;
- voz/som utilizável e ausência de música ambiente não licenciada;
- direitos e consentimentos de tudo o que aparece.

Registar `REAL` com a cobertura da inspeção (metadados, amostras ou duração completa) e `SIMULADO` para placeholders fictícios. Nunca
apresentar uma simulação como captação ou exportação concluída.

## 5. Montar no editor disponível

Montar primeiro a narrativa sem música: selecionar takes, ordenar, aparar, retirar pausas e testar
se a ideia se entende. Só depois tratar texto, legendas, som, cor e capa. Isto reduz o retrabalho
quando o corte muda.

### Caminho manual no Canva

Usar [o percurso opcional](producao-video-ferramentas.md) quando este for o editor escolhido (PLAT-030). O produto ter uma função não significa que um conector a consiga executar.

### Caminho assistido por conector

Antes de prometer qualquer operação, ler as operações declaradas pelo conector naquele ambiente.
Classificar a capacidade como `declarada`, `testada neste design` ou `não disponível`.

- Inserir/substituir um clip, mover/redimensionar um elemento ou alterar texto só é automático se
  a operação correspondente estiver declarada e funcionar num teste reversível.
- Não inferir controlo de timeline, trim/split, mistura de som, legendas sincronizadas, escolha de
  codec ou exportação a partir de uma capacidade genérica de “editar design”.
- Mostrar o resultado intermédio quando a ferramenta o permitir. Guardar/confirmar alterações só
  segundo o contrato da ferramenta e a autorização aplicável.
- Quando faltar uma operação, entregar a instrução manual exata e continuar a partir do ficheiro
  que a pessoa devolver. Não fabricar prova de execução.

## 6. Legendas, texto e acessibilidade

- Rever manualmente transcrição, português, nomes próprios, números, materiais e alegações.
- Marcar fala, texto no ecrã e informação apenas visual. A mensagem essencial deve continuar
  percetível sem som; informação necessária não pode viver apenas na cor.
- Verificar contraste segundo o módulo 04 e legibilidade no telefone real.
- Preparar texto alternativo ou equivalente onde a superfície o suporte; descrever conteúdo e
  função, não repetir a legenda comercial.
- Testar zonas cobertas pela interface e recortes na pré-visualização de cada superfície.

## 7. Som e direitos por faixa, uso e destino

Música é opcional. Voz própria, som do processo ou silêncio intencional podem servir a peça; não
prometer alcance por usar música, áudio em tendência ou uma biblioteca nativa.

Criar uma ficha por faixa, mesmo quando é gratuita:

| Campo | Registo obrigatório |
|---|---|
| `AUD-###` | ID estável |
| Faixa/autor/versão | identificação exata |
| Origem e URL | biblioteca, fornecedor ou prova própria |
| Verificado em | data |
| Uso | orgânico, pago, próprio/terceiro, duração do excerto |
| Destino/território | superfícies e região cobertas |
| Prova | licença, indicação da biblioteca ou contrato guardado |
| Estado | autorizado / `POR_CONFIRMAR` / rejeitado |

Consultar **PLAT-029** para licenciamento Canva e **PLAT-027/PLAT-028** para música e divulgação comercial no TikTok (`LOOK INTO` para os restantes aspetos). Confirmar a faixa, uso, região e destino concretos; uma subscrição não substitui esta verificação.

Para Meta e YouTube, aplicar o módulo 10. Uma licença restrita a uma superfície não entra no
`MASTER-LIMPO`; acrescenta-se na versão desse destino.

## 8. Master limpo e adaptações

`MASTER-LIMPO` é o corte aprovado editorialmente, sem marca de água de outra aplicação e sem áudio
cuja licença impeça reutilização. Voz, som próprio e música com licença multicanal podem permanecer.

Não existe obrigação universal de criar um ficheiro diferente por canal. Criar nova `EXP-###`
apenas quando mudar pelo menos um destes elementos:

- rácio, resolução ou duração necessária;
- montagem, abertura, fecho ou chamada à ação;
- texto integrado, legendas, capa ou zonas seguras;
- música/licença, identificação comercial ou requisito de entrega;
- qualidade observada na pré-visualização.

Se o mesmo ficheiro limpo satisfizer os requisitos confirmados, direitos e pré-visualizações de
duas superfícies, reutilizá-lo e registar duas colocações sobre a mesma `EXP-###`. Adaptar a legenda
da publicação não obriga a reexportar o vídeo.

Consultar **PLAT-033** para o estado das especificações de Instagram. Confirmar requisitos e pré-visualização antes da entrega por destino; um acesso falhado não é confirmação.

As regras gerais orgânicas de TikTok continuam `LOOK INTO`: preparar uma hipótese 9:16 pode ser
uma decisão de produção, mas duração, capa, caixas da interface e aceitação do ficheiro confirmam-se
na conta. Não aplicar especificações de anúncios como se fossem regras orgânicas.

## 9. Exportar e inspecionar

Por cada `EXP-###`, registar o alvo e o observado. Uma exportação só existe depois de o ficheiro
ser descarregado e aberto.

| Campo | Alvo de produção | Observado no ficheiro |
|---|---|---|
| nome/caminho | | |
| formato/codec, se exposto | | |
| dimensões/rácio | | |
| duração/cadência | | |
| tamanho | | |
| áudio | | |
| legenda integrada ou faixa | | |
| hash opcional | | |

`[PRODUÇÃO]` MP4, 1080 × 1920 e 30 fps podem ser um alvo inicial para vídeo vertical simples,
quando o editor e as superfícies o aceitam. Não afirmar que o Canva expõe codec, bitrate ou todos
os controlos técnicos; escrever `não exposto` e validar o ficheiro resultante.

## 10. Revisão final

Fazer três passagens no ficheiro real:

1. **Sem som:** ideia, ordem, foco, cor, texto, legendas, capa e recortes compreensíveis.
2. **Só som/sem olhar:** voz audível, ruído, música, cortes e ausência de conteúdo protegido
   captado por acidente.
3. **Completa, no telefone:** sincronização, ritmo, fidelidade do produto, grafias, zonas de
   interface, chamada à ação e identificação comercial.

Depois verificar:

- factos, alegações, preço, prazo e disponibilidade contra as respetivas fontes, sem duplicá-los;
- consentimentos, privacidade, autoria e ficha de música por destino;
- capa com ou sem texto segundo a direção visual do caso;
- nome do ficheiro, versão, projeto editável e localização autorizada;
- pré-visualização por superfície; publicação continua fora deste módulo.

Entregar o veredicto `APROVAR`, `CORRIGIR` ou `BLOQUEADO`, com uma linha por defeito observável e o
ID afetado. Separar o que foi realmente inspecionado do que ficou simulado ou `POR_CONFIRMAR`.

## Formato económico de entrega

Para uma peça, evitar repetir o plano de produção inteiro. Entregar:

```text
VIDEO-PROD/v1 — [ID]
Estado: [estado] · revisto em [data]
Brief: [ideia | superfície(s) | ação]
Guião/planos: [local ou tabela curta]
Originais: [REAL/SIMULADO + localização]
Projeto: [editor + localização/ID + capacidades testadas]
Master limpo: [localização | POR_CONFIRMAR]
Exportações: [EXP + destinos; uma linha cada]
Música: [AUD + estado + destinos]
Revisão: [APROVAR/CORRIGIR/BLOQUEADO + defeitos]
Limites: [não testado, não exposto ou não autorizado]
```

Só expandir a secção que tenha decisões, riscos ou falhas. Para lotes, usar o modelo completo do
módulo 13.
