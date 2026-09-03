---
name: guiao-video-curto
description: "Escreve o guião completo de um vídeo curto — Reel ou Short — em duas colunas (o que se diz | o que se vê e lê), por blocos de tempo, com gancho nas três camadas, chamada à ação única e a camada de acessibilidade. Confirma o rácio na superfície; Shorts podem ser quadrados ou verticais. TikTok fica LOOK INTO até revisão própria. Pode partir de um vídeo de referência e fazer-lhe engenharia inversa, por análise manual guiada ou automática se existirem ferramentas autorizadas. Usa esta skill SEMPRE que o pedido envolver um vídeo curto."
---

# Guião de vídeo curto

## Gate de revisão

Antes de executar, correr `../social-media-manager/scripts/verificar_revisao.py`, resolvido relativamente a este ficheiro. Sem terminal, ler os blocos `Calendário` de `05-estado-das-plataformas.md` e `09-estado-da-vigilancia.md`. Se uma data chegou, passou ou é inválida, avisar uma vez por conversa; a primeira linha deve ser exatamente `Skill necessita de revisão`. Continuar com as limitações declaradas. O aviso não autoriza pesquisa, acesso a contas nem atualização.

Skill de execução para vídeo curto. Reels usam normalmente vertical; Shorts podem ser quadrados ou verticais nas condições de PLAT-017. Confirmar o rácio na superfície. TikTok está `LOOK INTO` e não recebe regras atuais.

O julgamento vive nos módulos: a anatomia da peça, as três camadas do gancho, a escada de chamadas à ação e a lista de acessibilidade estão em `../social-media-manager/references/04-criacao-de-conteudo.md` — **ler esse módulo antes de escrever**. O método de plataformas está em `../social-media-manager/references/05-plataformas.md`; para qualquer regra volátil citada abaixo, ler também o ID em `../social-media-manager/references/05-estado-das-plataformas.md`. O critério para entrar ou não numa tendência está em `../social-media-manager/references/09-tendencias-e-concorrencia.md`.

## Arranque imediato

Se o tema ou o link já vierem na mensagem, usá-los e saltar diretamente para o passo que faltar. Não resumir a skill, não explicar o que é um gancho antes de o escrever, não pedir autorização para começar.

## Passo 0. Perfil de marca

Ler `PERFIL-SOCIAL.md` na raiz do projeto (ou o nome que o projeto usar: `MARCA.md`, `MEMORY.md`, `CLAUDE.md`, uma pasta `Social Media/`, ou a memória do projeto). Interessam a secção 5 (voz), a 7 (pilares), a 6 (o que se pode afirmar), a 8 (quem aparece em câmara e meios de produção) e a 11 (aprendizagens — é onde o tempo médio de visualização real da conta fica registado, **se alguém o tiver lá escrito**; o modelo não tem campo próprio para ele. Não estando lá, o número tira-se das estatísticas da própria conta, não se estima).

Se não existir, criá-lo a partir de `../social-media-manager/assets/PERFIL-MARCA-modelo.md` e **parar até existir**, pelo menos nas secções 5, 6 e 8. Um guião escrito sem voz definida sai correto na forma e genérico em tudo o resto, e é o tipo de peça que não se publica.

Em conflito entre esta skill e o perfil, **manda o perfil**.

## Passo 1. Vídeo de referência — opcional, dois caminhos

Um vídeo de referência é matéria-prima útil, não requisito. Se não houver, dizer numa linha que se avança sem referência e ir para o Passo 2.

Existindo referência, verificar primeiro o ambiente:

```
! echo "APIFY:${APIFY_API_TOKEN:+definido}${APIFY_API_TOKEN:-em falta} · GEMINI:${GOOGLE_AI_API_KEY:+definido}${GOOGLE_AI_API_KEY:-em falta}"
```

**Nunca parar por falta de chave.** A ausência muda o caminho, não o resultado.

### 1A. Caminho manual — o predefinido, funciona sem nada instalado

Pedir ao utilizador que veja o vídeo de referência **duas vezes** (uma com som, outra em silêncio) e responder. Usar **AskUserQuestion** para o que é escolha, e pedir texto livre para o resto.

**Sem `AskUserQuestion` disponível**, fazer exatamente as mesmas perguntas em texto corrido, numeradas, num turno só, com as opções listadas por letra. A ferramenta muda a apresentação, não o conteúdo — e esta skill não precisa de ferramenta nenhuma em passo nenhum.

```json
[
  {"question": "O que acontece nos primeiros 3 segundos?", "header": "Gancho", "multiSelect": false,
   "options": [
     {"label": "Resultado primeiro", "description": "Mostra o fim antes do processo (cold open)"},
     {"label": "Pergunta ou identificação", "description": "\"Se fazes X, isto é para ti\""},
     {"label": "Afirmação contrária", "description": "Contraria o senso comum ou avisa de um erro"},
     {"label": "Quebra de padrão visual", "description": "Movimento, som ou imagem inesperada"}
   ]},
  {"question": "Como está construído o ritmo?", "header": "Ritmo",
   "options": [
     {"label": "Plano único a falar", "description": "Uma pessoa, câmara fixa, texto no ecrã"},
     {"label": "Cortes frequentes", "description": "Muda de plano várias vezes por passo"},
     {"label": "Processo mostrado", "description": "Mãos a fazer, sem rosto"},
     {"label": "Texto conduz, imagem ilustra", "description": "O ecrã escrito carrega a mensagem"}
   ]},
  {"question": "Como fecha?", "header": "Fecho",
   "options": [
     {"label": "Pergunta para comentário", "description": "Abre conversa"},
     {"label": "Convite a guardar ou enviar", "description": "Gesto com custo"},
     {"label": "Volta ao início", "description": "Fecha o ciclo e provoca revisualização"},
     {"label": "Corta a seco", "description": "Sem CTA explícita"}
   ]}
]
```

E a seguir, em texto livre, três coisas que valem mais do que qualquer análise automática:
1. **As primeiras palavras ditas, transcritas à letra**, e o texto que está no ecrã no mesmo instante.
2. **A duração total** e mais ou menos onde cada secção começa e acaba.
3. **Em que segundo é que perdeste o interesse na segunda visualização** — é o dado mais honesto que existe e nenhuma API o fornece.

### 1B. Caminho automático — só se as chaves existirem

Com `APIFY_API_TOKEN` e `GOOGLE_AI_API_KEY` definidas, é possível descarregar o vídeo e obter transcrição com marcas de tempo, contagem de planos e estrutura, poupando ao utilizador o trabalho manual. Perguntar antes de o fazer — descarregar um ficheiro exige autorização explícita.

Se qualquer passo automático falhar (actor sem resultados, vídeo privado, quota), **não fabricar análise**: dizer o que falhou numa linha e cair para 1A.

### O que se perde no caminho manual, dito com honestidade

Perde-se a transcrição literal completa com marcas de tempo, a contagem exata de cortes e as métricas públicas do vídeo (visualizações, gostos, comentários). Não se perde nada do que decide o guião: a estrutura, o mecanismo do gancho e o ponto de queda de interesse são melhor observados por uma pessoa do que extraídos por uma API. E as métricas públicas de um vídeo alheio são o dado menos útil de todos — alcance, guardados e envios, que são o que as plataformas premeiam, **não são visíveis de fora** (`../social-media-manager/references/09-tendencias-e-concorrencia.md`).

Nunca inventar números do vídeo de referência. O que não foi observado não se escreve.

⚠️ **A referência analisa-se, não se recicla.** Nada do ficheiro alheio — imagem, áudio, legendas, texto no ecrã — entra no vídeo novo. O que se reaproveita é a *estrutura*, que não é de ninguém. A orientação de originalidade do Instagram considera insuficientes alterações cosméticas a conteúdo alheio; consultar PLAT-002 antes de apresentar a regra como atual e confirmar o Estado da conta quando a decisão depender dela.

## Passo 2. Tema, comportamento e duração

Se não vier na mensagem, **AskUserQuestion**:

```json
[
  {"question": "Qual é o tema do vídeo?", "header": "Tema", "multiSelect": false,
   "options": [
     {"label": "Escrevo o tema", "description": "Uma frase a seguir"},
     {"label": "Aconteceu isto", "description": "Um episódio real — a matéria-prima mais forte"},
     {"label": "Adaptar peça existente", "description": "Colo o post, artigo ou email a reaproveitar"}
   ]},
  {"question": "Que comportamento queres provocar?", "header": "Objetivo",
   "options": [
     {"label": "Ver até ao fim", "description": "Retenção — descoberta junto de quem não segue"},
     {"label": "Enviar a alguém", "description": "O gesto mais caro e o que mais alarga alcance"},
     {"label": "Guardar", "description": "Referência utilizável, para voltar"},
     {"label": "Comentar", "description": "Conversa — abre caminho à mensagem privada"}
   ]},
  {"question": "Onde vai sair?", "header": "Destino", "multiSelect": true,
   "options": [
     {"label": "Instagram Reels", "description": "9:16"},
     {"label": "TikTok", "description": "LOOK INTO — não produzir como regra atual sem revisão autorizada"},
     {"label": "YouTube Shorts", "description": "Quadrado ou vertical até 3 min, com datas por tipo de canal; PLAT-017"},
     {"label": "Facebook Reels", "description": "9:16"}
   ]}
]
```

**Um comportamento só.** Escolher dois é escolher nenhum.

**Duração:** calibrar pelo tempo médio de visualização real da conta — registado na secção 11 do perfil ou, não estando, lido nas estatísticas da conta — e não pelo limite da plataforma. ◑ Na ausência desse dado, a referência do módulo 04 é um tempo médio por Reel na ordem dos 8,5 segundos (amostra de 24,3M de publicações de 375K contas geridas profissionalmente) — o que significa que **cada segundo depois do oitavo tem de justificar-se**. ◐ Alvo de partida defensável: 20 a 40 segundos, dois pontos no máximo, nunca três.

### Vários destinos ao mesmo tempo

**Um destino, uma exportação.** O que se diz pode servir mais do que uma superfície; o ficheiro nunca serve.

- Confirmar o **rácio e a duração** de cada destino **antes de filmar** — muda o enquadramento na captação e não se corrige na montagem.
- O **texto no ecrã e as legendas mudam de sítio** entre superfícies, porque as zonas da interface não coincidem. Uma linha por destino na coluna do que se vê.
- Reexportar por destino, sem marca de água de outra aplicação.
- ⚠️ **Destinos que não estejam na secção 4 do perfil não se produzem.** Perguntar porquê primeiro.

## Passo 3. Escrever o guião

Espinha por blocos de tempo, do módulo 04:

| Bloco | Função |
|---|---|
| `0-3s` | Gancho nas **três camadas** |
| `3-8s` | Promessa explícita do que vem a seguir |
| corpo | Passos, **cada um com mudança visual** |
| `3-5s` finais | Fecho e chamada à ação, uma só |

**Duas colunas, sempre.** A coluna do que se vê assegura que a informação essencial não depende apenas do som. Acrescentar legendas revistas é prática de acessibilidade. Shorts podem ser quadrados ou verticais e ter até três minutos nas condições de PLAT-017; TikTok está `LOOK INTO` e não fornece regras atuais.

O gancho escreve-se nas três camadas em simultâneo — **o que se vê · o que se ouve · o que está escrito no ecrã** — e as três apontam para a mesma promessa. Se for preciso gerar variações antes de escolher, chamar `gerar-ganchos`.

Rever **de trás para a frente**: a chamada à ação é coerente com a promessa? O corpo cumpre-a? O gancho promete o que o corpo entrega? Se não, corrige-se o gancho, não o corpo.

A chamada à ação não pode custar mais do que aquilo que o vídeo acabou de dar — escada de atrito no módulo 04. ⚠️ Nada de "marca três amigos" nem "comenta EU QUERO": ⬤ o Facebook declara a despromoção de *engagement bait* e de Páginas reincidentes; PLAT-007. ⬤ O Instagram proíbe a recolha artificial de gostos, seguidores ou partilhas. Pedidos genuínos de ajuda, conselho ou recomendação são diferentes de interação como fim.

## Passo 4. Verificações antes de entregar

- [ ] Rácio confirmado para a superfície, legível, sem bordas nem marca de água de outra aplicação e com informação essencial também visível — boa prática de produção; Shorts podem ser quadrados ou verticais (PLAT-017) e a lista de distribuição publicada pelo Instagram em 2023 é histórica (PLAT-011).
- [ ] Reexportado por plataforma, não o mesmo ficheiro com logótipo de outra app.
- [ ] Legendas revistas **à mão** — nomes próprios, números e preços saem errados nas automáticas.
- [ ] Texto e legendas fora das zonas da interface (nome de utilizador, botões laterais, barra de progresso), verificadas na aplicação real.
- [ ] Contraste do texto sobre imagem: ⬤ mínimo 4,5:1 (3:1 para texto grande), WCAG 2.2 AA.
- [ ] Informação essencial nunca só na cor nem só no áudio.
- [ ] Hashtags dentro do limite confirmado na conta — produzir até cinco é compatível com o rollout oficial conhecido; PLAT-003. Não inventar uma data global de entrada em vigor.
- [ ] Texto alternativo escrito para a capa (não fica só no formato de saída — verifica-se aqui).
- [ ] Rótulo de IA segundo a plataforma e o módulo 10. ⬤ A Meta aplica informação por deteção ou declaração. TikTok está `LOOK INTO`. ⬤ O artigo 50.º do AI Act exige a quem publica profissionalmente divulgar *deepfakes* e certos textos de interesse público. ◐ Na dúvida, este sistema identifica conteúdo realista ou materialmente alterado por IA.
- [ ] **Áudio:** se for som em tendência, confirmar que a licença cobre uso comercial. Uma conta de empresa não tem acesso à mesma biblioteca de uma conta pessoal, e usar o que não pode custa o som — ou o vídeo inteiro.
- [ ] **Identificação publicitária**, havendo parceria paga ou promoção de produto próprio: ⬤ a menção vai **no início** — sobreposta enquanto se fala do produto ou dita em voz alta antes — nunca só no fim nem enterrada nas hashtags. Usar também a ferramenta nativa da plataforma. Módulo 10.
- [ ] **Quem aparece em câmara** está na secção 8 do perfil e deu autorização. Cliente, testemunho ou imagem de terceiros: autorização **por escrito**, para este uso. Uma marcação não transfere licença nem direito de imagem.
- [ ] Nenhum preço, prazo ou condição escrito a partir desta skill: vêm do perfil ou de um humano.

## Passo 5. Formato de saída

```
GUIÃO — [título de trabalho]
Destino: [Reels / Shorts] · rácio [confirmado] · alvo [N]s
Comportamento pretendido: [um]
Referência: [link ou "sem referência"] · análise: [manual / automática]

| Tempo | O que se diz | O que se vê e lê |
|---|---|---|
| 0-3s  | ...          | Vê: ... / Lê: ... |
| 3-8s  | ...          | ... |
| ...   | ...          | ... |
| fecho | ...          | ... |

LEGENDA DA PUBLICAÇÃO
[texto, com a primeira linha a funcionar antes do corte do "ver mais"]

ACESSIBILIDADE
Legendas: [a rever à mão em ...] · Texto alternativo da capa: ... · Contraste: ...

NOTAS DE RODAGEM
Planos, luz, fundo, quantas coisas é preciso ter à mão antes de gravar.
```

Terminar com **duas linhas**: o que foi tirado da referência e o que é original, e **o que ficou por verificar**. Numa área onde metade dos números publicados não tem origem, dizer o que não se sabe vale mais do que uma estimativa confiante.

## Passo 6. Passo seguinte

> Queres que eu trate da capa e do primeiro fotograma? Chamo `capa-de-video`.

## Regras

- **Português europeu** em tudo — incluindo o texto no ecrã e a legenda.
- ⚠️ **Identificar conteúdo comercial.** ⬤ `#PUB` no início quando há dinheiro ou benefício de terceiro — é o que a lei exige. ◐ **"conteúdo promocional"** quando é a própria marca a promover produto, preço, campanha ou desconto — é política interna deste sistema, não redação imposta. **Não trocar as duas:** carimbar `#PUB` numa peça da própria marca afirma uma relação comercial que não existe e dilui a etiqueta onde ela é obrigatória. Se a peça não promove nada, não leva nada. Tabela dos três casos em `../social-media-manager/references/10-risco-crise-e-conformidade.md`.
- **Vídeo curto, com rácio confirmado.** Não impor 9:16 a Shorts quadrados; TikTok fica `LOOK INTO`.
- **Nunca parar por falta de APIFY_API_TOKEN ou GOOGLE_AI_API_KEY.** São aceleradores, não requisitos.
- **Nunca inventar métricas, transcrições ou estrutura do vídeo de referência.** Se a análise falhou, dizer que falhou.
- **Nunca inventar números, resultados, prazos, preços ou casos de cliente** para o guião. Vêm do perfil.
- Um gancho que o corpo não cumpre não se entrega — destrói o tempo de visualização, que é o sinal que mais pesa.
- Uma ideia e uma chamada à ação por vídeo.
- Descarregar ficheiros e publicar exigem autorização explícita do utilizador, sempre.
- **Nunca reutilizar imagem, áudio ou texto do vídeo de referência.** Analisa-se a estrutura; copia-se nada.
- **Nunca usar imagem de uma pessoa sem autorização escrita** — cliente, colaborador ou terceiro.
- A camada de acessibilidade nunca é opcional e é a primeira a desaparecer com pressa. Por isso está na lista.
- Não repetir números sem fonte. Os intervalos de corte que circulam ("um corte a cada 1,5-4 segundos") não têm estudo por trás: vale o princípio da mudança visual frequente, não o número.
- Não resumir esta skill. Executá-la.
