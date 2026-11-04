---
name: social-media-manager
description: "Diagnostica, planeia e coordena redes sociais em pedidos amplos, estratégicos ou de ciclo completo. Para um artefacto concreto, encaminha para a executora correspondente. Recebe o contexto do caso sem pressupor negócio, website, assistente ou ferramenta."
---

# Social Media Manager

## Contexto e âmbito

Aplicar [contexto-do-caso](references/contexto-do-caso.md): o método vive nas skills, os factos
e decisões nas fontes do caso, e as ferramentas no ambiente disponível. Ler apenas o contexto
necessário; uma pergunta geral de ofício não exige perfil de marca. Pedir só lacunas que mudem
a tarefa. Não inventar produto, preço, prazo, disponibilidade, direito ou compromisso.

Prevalecem o pedido e a autorização do utilizador, depois o contexto canónico no seu domínio.
As regras de método de uma etapa vivem no módulo responsável. Uma executora não as redefine.
SEO de site, blogue, email marketing, design de produto e vídeo longo ficam fora do âmbito.
LinkedIn não tem cobertura; TikTok, Threads e X mantêm cobertura geral `LOOK INTO`, com eventuais
afirmações delimitadas no registo de plataformas.

## Gate de revisão

Antes de executar, correr `python3 skills/social-media-manager/scripts/verificar_revisao.py`
a partir da raiz do repositório; noutra localização, resolver `scripts/verificar_revisao.py`
relativamente a este ficheiro. Sem terminal, ler só os blocos `Calendário` dos estados 05 e 09.
Se uma data chegou, passou ou é inválida, a primeira linha do aviso é exatamente
`Skill necessita de revisão`. Avisar uma vez por conversa e continuar o trabalho independente.
O aviso não autoriza novas ações externas nem apaga autorização já dada pelo utilizador.

Revisão vencida é pendência de conhecimento, não bloqueio global. Verificar no ponto de uso a
afirmação da qual a decisão depende; se não for possível, deixá-la `POR_CONFIRMAR`. Guião,
triagem, captação e montagem podem avançar onde não dependam dela. Nunca mudar datas para
silenciar o aviso. Regras de Graph API/Instagram Platform: PLAT-009.

## Escolher a etapa e ler só o necessário

| Pedido | Referência |
|---|---|
| Perfil, acessos, incidentes | `references/00-a-conta.md` |
| Estratégia, público, arranque | `references/01-estrategia-e-publico.md` |
| Voz e mensagem | `references/02-voz-e-mensagem.md` |
| Calendário e cadência | `references/03-planeamento-e-calendario.md` |
| Criação editorial e visual | `references/04-criacao-de-conteudo.md` |
| Regra de plataforma | `references/05-plataformas.md` e ID aplicável em `references/05-estado-das-plataformas.md` |
| Comunidade e conversas | `references/06-comunidade-e-dm.md` |
| Métricas e relatório | `references/07-analise-e-relatorio.md` |
| Promoção paga | `references/08-promocao-paga.md` |
| Pesquisa de tendências | `references/09-tendencias-e-concorrencia.md`; estado em `references/09-estado-da-vigilancia.md` |
| Direitos, publicidade, crise | `references/10-risco-crise-e-conformidade.md` |
| Benchmark | `references/11-numeros-de-referencia.md`, amostra e metodologia antes de citar |
| Modelo de operação altera o método | `references/12-contextos-de-negocio.md` |
| Lote, campanha ou dependências materiais | `references/13-plano-de-producao.md` |
| Produzir vídeo até ao ficheiro | `references/14-producao-video-curto.md` |

As fontes primárias estão em `references/FONTES.md`. Afirmações voláteis, incluindo ferramentas
de produção, pertencem ao registo 05; os consumidores apontam para o ID, sem repetir políticas.

## Skills executoras

Usar diretamente a executora para um pedido concreto. `sistema-contexto-conteudo` prepara fontes
e inventário quando esse trabalho for necessário; não exige criar um pacote para um pedido simples.

| Skill | Faz | Módulo que a governa |
|---|---|---|
| `construir-voz` | Extrai a voz de textos reais e preenche as secções de público e voz do perfil | 02 |
| `voz-newsletter` | Acrescenta regras de escrita de newsletter ao perfil | 02 |
| `otimizar-perfil` | Reconstrói perfis de Instagram, Facebook e Google Business Profile | 00 |
| `escrever-post` | Redige um post a partir do perfil | 04 |
| `formatar-post` | Tema para post pronto, com estrutura declarada | 04 |
| `gerar-ganchos` | Variações de gancho, testadas contra imediato/específico/verdadeiro | 04 |
| `comentario-fixado` | Comentário fixado que antecipa a pergunta repetida | 06 |
| `guiao-video-curto` | Guião para Reels e Shorts, por blocos de tempo | 04 |
| `organizar-fotos-produtos` | Audita fotos/vídeos, compara com o catálogo e prepara cortes/entregas autorizados | 13 |
| `capa-de-video` | Capa e primeiro fotograma no rácio confirmado do vídeo | 04 |
| `photo-first-art-direction` | Investiga e define um sistema visual social liderado por fotografia; não cria peças durante a fase de direção | 04 |
| `design-grafico` | Decide entre gráfico em código e imagem gerada | 04 |
| `infografico` | Infográfico | 04 |
| `carrossel` | Carrossel, diapositivo a diapositivo | 04 |
| `post-de-citacao` | Peça de citação com imagem | 04 |
| `avaliar-post` | Pontua um rascunho contra o histórico real da conta | 07 |
| `painel-metricas` | Exportação de métricas para painel e decisões | 07 |
| `matriz-de-conteudo` | Pilares × formatos, para encher o banco de ideias | 03 |
| `pesquisa-de-nicho` | O que se está a passar no nicho, com critério de adesão | 09 |


A direção visual vem do caso. `photo-first-art-direction` define ou revê o sistema visual quando
pedido; não reabre essa pesquisa a cada peça. `organizar-fotos-produtos` audita a sessão,
atualiza os registos no catálogo comum e prepara fotografias quando autorizado;
`sistema-contexto-conteudo` fornece o método geral de inventário. Não criar catálogos concorrentes.

## Modos de operação

No arranque, reconhecer contexto e estado da conta, propor objetivo e medição, escolher canais
segundo público/capacidade, depois pilares e cadência sustentável. Quantidades são decisões do
caso. No ciclo corrente, partir do calendário e resultados existentes, sem reiniciar a estratégia.

A cadência de revisão é proporcional ao trabalho: acompanhar execução, consolidar resultados e
propor ajustes com evidência. Recaps e atualizações só se executam no âmbito autorizado. Um
pedido avulso termina no artefacto pedido; sugerir planeamento quando útil sem o impor.

### Plano de produção

Para lote/campanha, seguir `references/13-plano-de-producao.md` e
`assets/plano-de-producao-modelo.md`: deduplicar matéria-prima e entregas e usar
`smm-production-handoff/v1` quando houver passagem para coordenação. Para um único vídeo,
usar a ficha curta do módulo 14; não exigir as oito secções do plano de lote.

`adaptive-project-manager` é uma capacidade independente e opcional. Se não estiver disponível,
entregar o mesmo handoff portátil. Não copiar a PJM; não alterar quadros, atribuições ou datas
sem autorização aplicável. Propostas continuam propostas até aceitação.

## Critérios de decisão

- **Reutilização:** validar por destino e reexportar apenas perante diferença material, segundo
  o módulo 14. O mesmo ficheiro limpo pode servir vários destinos. PLAT-011 é histórico e não
  prova perda atual de alcance.
- **Criatividade:** definir uma intenção principal e cumprir a promessa. Som, texto, capa,
  duração e frequência de cortes são escolhas fundamentadas, não garantias de alcance.
  Vídeos silenciosos, capas sem texto e peças sem CTA explícita podem cumprir a intenção.
- **Medição:** manter definições e denominadores comparáveis, identificar amostra e período.
  Uma repetição é evidência a avaliar, não prova causal nem um limiar estatístico universal.
- **Proporcionalidade:** avançar com partes independentes; bloquear apenas a decisão afetada
  por falta de material, identidade, direito, autorização ou informação indispensável.
- **Prontidão:** identificar objeto e etapa. Um guião escrito é um entregável real, mesmo sem
  captação. Um vídeo pronto para revisão exige ficheiro real e cobertura de inspeção declarada.
  Aprovação editorial, inspeção técnica e publicação são estados diferentes.
- **Execução:** usar capacidades realmente disponíveis. Sem integração, entregar o percurso
  manual e o estado alcançado; nunca descrever uma instrução como operação concluída.
- **Factos e direitos:** aplicar o módulo 10 no âmbito pertinente. A aprovação de uma tarefa não
  autoriza publicação, contacto, gastos ou alterações de contas não abrangidos pelo pedido.

## Evidência e entrega

⬤ Fonte primária: URL ou ID que resolve para fonte e data. ◑ Evidência de terceiros: metodologia
e amostra junto da conclusão. ◐ Prática: recomendação identificada. Distinguir observação,
hipótese e requisito; uma fonte oficial antiga não prova atualidade.

Entregar o resultado pedido, localização quando existe, estado por etapa e limitações relevantes.
Calendário não inclui legendas completas por defeito; relatório termina em decisões propostas,
com responsável/prazo apenas quando confirmados. Referenciar factos e regras de marca pelos
seus donos. Não repetir formulários, briefings ou avisos já resolvidos na mesma execução.
