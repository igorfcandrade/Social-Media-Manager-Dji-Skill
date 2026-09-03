---
name: voz-newsletter
description: "Constrói as instruções de escrita da newsletter de uma marca — abertura, estrutura de secções, uso de dados, formatação, fecho e comprimento — a partir de edições antigas ou, na falta delas, de um de seis arquétipos afinado à voz da marca. Escreve o resultado no perfil de marca do projeto. Usa esta skill SEMPRE que aparecer trabalho de newsletter ou email periódico, mesmo sem essas palavras (ex.: \"constrói a voz da newsletter\", \"como devo escrever a newsletter?\", \"vamos lançar um email mensal\", \"analisa as edições que já mandei\", \"que estrutura deve ter a newsletter?\", \"treina no meu email\", \"a newsletter está sempre diferente de edição para edição\"). Dispara também quando alguém colar edições antigas a pedir análise. Requer a voz base já definida no perfil."
---

# Voz da newsletter

## Gate de revisão

Antes de executar, correr `../social-media-manager/scripts/verificar_revisao.py`, resolvido relativamente a este ficheiro. Sem terminal, ler os blocos `Calendário` de `05-estado-das-plataformas.md` e `09-estado-da-vigilancia.md`. Se uma data chegou, passou ou é inválida, avisar uma vez por conversa; a primeira linha deve ser exatamente `Skill necessita de revisão`. Continuar com as limitações declaradas. O aviso não autoriza pesquisa, acesso a contas nem atualização.

Skill de execução, assente na voz base. O critério sobre voz vive em `../social-media-manager/references/02-voz-e-mensagem.md`; sobre planeamento e reaproveitamento, em `../social-media-manager/references/03-planeamento-e-calendario.md` e `04-criacao-de-conteudo.md`; sobre conformidade, em `10-risco-crise-e-conformidade.md`. Não repetir esse conteúdo aqui.

**O âmbito é só a escrita.** Esta skill define **como a newsletter soa e se estrutura**. Captação de subscritores, segmentação, plataforma de envio, automatismos, entregabilidade e taxas de abertura ficam de fora — o conjunto declara email marketing fora de âmbito (`../social-media-manager/SKILL.md`, "O que esta skill não faz"). O que entra é a voz de um canal da marca, não a operação de envio.

**Nenhuma ferramenta é obrigatória.** Esta skill não precisa de chave de API, serviço pago nem ferramenta instalada em passo nenhum, e chega ao fim sem nada disso.

## Pré-requisito: o perfil de marca

Ao disparar, procurar o perfil do projeto (`PERFIL-SOCIAL.md`, `MARCA.md`, `MEMORY.md`, `CLAUDE.md`, pasta `Social Media/` ou equivalente). **Guardar o caminho do ficheiro encontrado — é nele que se escreve no Passo 3, e não num nome fixo.** Verificar se as secções **3 (Público)** e **5 (Voz)** estão preenchidas.

**Se não existirem ou estiverem `POR DEFINIR`:**

> A voz da newsletter assenta na voz base da marca, e essa ainda não está escrita. Corre primeiro a skill `construir-voz` (basta dizeres "aprende a minha voz"), e volta aqui quando as secções 3 e 5 do perfil estiverem preenchidas.

E **parar**. Não continuar, não adivinhar a voz, não escrever um ficheiro provisório.

Se existirem, **ler o perfil** — no mínimo as secções 1, 2, 3, 5, 6 e 7 — e ir direto ao Passo 1. Sem resumir a skill, sem explicar o que vai produzir.

## Passo 1. Há edições antigas?

Perguntar, em conversa:

> Tens 2 ou 3 edições antigas da newsletter que eu possa ler?
>
> **Sim:** cola-as aqui, uma por mensagem ou todas de uma vez.
> **Não:** escreve "arquétipo" e eu construo a partir de um modelo afinado à tua voz.

- 2 ou mais edições → Passo 2a.
- "arquétipo" → Passo 2b.
- 1 edição só → pedir mais uma. ◐ O mínimo de 2 é um limiar operacional desta skill — abaixo dele não há forma de separar padrão de tique de uma edição — não um número medido. Se não houver: "Uma edição não chega para detetar padrão. Uso o modo arquétipo e trato essa edição como referência de tom. Pode ser?"

## Passo 2a. Análise das edições

Ler tudo. Padrões que atravessam as edições, nunca tiques de uma só.

**Abertura** — o que fazem as três primeiras frases (resultado concreto, observação, afirmação, cena, pergunta) · comprimento da abertura até à primeira quebra · como se estabelece autoridade · o que se promete a quem lê.

**Estrutura** — montagem do problema ou do contraste · método nomeado ou prosa livre · passos numerados ou argumento contínuo · padrão de exemplos e prova · secção extra · fórmula de fecho e assinatura.

**Dados e prova** — quantos números concretos por edição (contá-los) · como se atribui a fonte (ligação, nome, sem crédito) · rácio entre exemplo e abstração · admite limites e falhas?

**Formatação** — títulos (frequência e hierarquia) · listas (numeradas, com marcas, com setas) · negrito e itálico · citações e blocos de código · marcadores visuais.

**Comprimento** — intervalo de palavras entre edições, e por secção.

**Marcas próprias do formato** — dicas ou caixas destacadas · fecho virado para a frente · frase de assinatura, se for consistente · meta-transparência (comenta o próprio processo? pede resposta?).

**Sinais de ausência** — o que não aparece em nenhuma edição: construções, tipos de fecho, temas. Escrever com a contagem ("ausente em 3 de 3").

Seguir para o Passo 3.

## Passo 2b. Escolha de arquétipo

Chamar **AskUserQuestion** com uma pergunta. **Se `AskUserQuestion` não existir neste ambiente, fazer exatamente a mesma pergunta em texto corrido, com as seis opções por letra e a descrição de cada uma por extenso, num único turno.** A ferramenta muda a apresentação, não o conteúdo.

```json
[
  {"question": "Que arquétipo de newsletter serve o que queres escrever?", "header": "Arquétipo",
   "options": [
     {"label": "Tutorial com dados", "description": "Números, método passo a passo, exemplos aplicáveis"},
     {"label": "Ensaio de posição", "description": "Assume uma posição, defende-a, nomeia a oposição"},
     {"label": "Análise de um caso", "description": "Um assunto por edição, desmontado a fundo"},
     {"label": "Seleção comentada", "description": "5 a 7 ligações por edição, cada uma com o teu comentário"},
     {"label": "Ensaio pessoal", "description": "Reflexão sobre um tema, a começar pela história"},
     {"label": "Entrevista ou retrato", "description": "Uma pessoa por edição, em perguntas ou em narrativa"}
   ]}
]
```

Carregar os valores por defeito de `references/arquetipos.md` **desta pasta**. Afinar **todos** os campos com a voz e o público do perfil antes de escrever seja o que for — o arquétipo é o esqueleto, o perfil é quem manda; em conflito entre os dois, **manda o perfil**. Marcar no resultado que se usaram valores por defeito e que se revê ao fim de ◐ 5 edições publicadas (limiar de prática desta skill, não medição — a revisão faz-se quando houver material real para analisar).

## Passo 3. Escrever no perfil

**Não criar `newsletter-voice.md` nem nenhum ficheiro de voz paralelo.** A newsletter é um canal da marca; as suas regras vivem no perfil.

Acrescentar **ao ficheiro de perfil localizado no pré-requisito** (`PERFIL-SOCIAL.md` ou o equivalente do projeto) uma subsecção **`## 5b. Voz da newsletter`**, logo a seguir à secção 5, com esta estrutura e no máximo ◐ 1.200 palavras — limite de legibilidade escolhido por esta skill, não um número medido.

**Se já existir uma `5b`:** lê-la primeiro, mostrar em que pontos a nova análise diverge da anterior, e **pedir confirmação antes de substituir**. Não acrescentar uma segunda `5b` nem reescrever por cima em silêncio.

```
### Origem
[Analisadas N edições em AAAA-MM-DD] OU [Arquétipo "X" afinado ao perfil. Rever após 5 edições publicadas.]

### Público e propósito desta newsletter
[Quem a lê e o que leva de lá. Sai da secção 3 do perfil, não de suposição. 2 a 3 frases.]

### Princípios de voz próprios do formato
[3 a 5 frases declarativas. Só o que é específico da newsletter — o que já está na secção 5 não se repete, remete-se.]

### Fórmula de abertura
[Como começam as edições. 2 modelos concretos com marcadores entre parêntesis retos. Comprimento-alvo da abertura.]

### Fluxo de secções
[Estrutura padrão, 5 a 8 secções, o que cada uma faz e quanto ocupa.]

### Dados e prova
[Como entram números e exemplos. Regras concretas. Nível de confiança de qualquer número citado: ⬤ oficial · ◑ consenso · ◐ prática.]

### Formatação
[Títulos, listas, negrito, itálico, citações, marcadores. O que se usa e o que não se usa.]

### Acessibilidade
[Fixo, não opcional. Ver `04-criacao-de-conteudo.md`. Texto alternativo em cada imagem, a descrever função e conteúdo essencial, sem começar por "imagem de" · nenhuma informação essencial existe só dentro de uma imagem, repete-se no texto · texto das ligações que se percebe fora do contexto, nunca "clica aqui" · títulos em hierarquia real, não parágrafos em negrito · ⬤ contraste mínimo 4,5:1 para texto normal e 3:1 para texto grande (18pt normal ou 14pt negrito), norma WCAG 2.2 AA — são limiares, não arredondáveis · se a edição levar vídeo ou áudio, legendas revistas à mão.]

### Rodapé e conformidade
[Fixo. Identificação de quem envia e ligação de cancelamento em todas as edições, sem exceção. Ver a secção "Conformidade" desta skill.]

### Fecho e assinatura
[Como acabam as edições. Frase de assinatura só se for consistente em 2 ou mais edições — nunca inventada.]

### O que esta newsletter nunca faz
[3 a 5 comportamentos, tirados dos sinais de ausência ou do arquétipo. Comportamentos, não lista de palavras proibidas.]

### Comprimento
[Alvo de palavras para uma edição normal, e alvo separado para edições longas se existirem os dois formatos.]

### Reaproveitamento
[Que peças sociais saem de cada edição. Ver `04-criacao-de-conteudo.md`: cada derivado é reexportado e readaptado ao formato de destino, nunca o mesmo ficheiro com marca de água. O rácio confirma-se no destino: Reels usam normalmente vertical; Shorts podem ser quadrados ou verticais (PLAT-017). TikTok está `LOOK INTO`. Cada derivado leva a camada de acessibilidade do módulo 04, que não se herda da edição.]
```

Preencher tudo a partir das edições ou do arquétipo afinado. Onde as edições não cobrirem alguma coisa, escrever **"sem padrão claro nas edições analisadas"** em vez de inventar.

## Passo 4. Confirmar e entregar

Mostrar a subsecção escrita em bloco de código e dizer:

> A `5b. Voz da newsletter` está no perfil, por baixo da voz base. Quando quiseres escrever, diz "escreve a newsletter" e eu uso as duas secções em conjunto.
>
> [Se foi por arquétipo:] Isto saiu de valores por defeito afinados à tua voz, não de edições reais. Ao fim de umas 5 edições publicadas, corre esta skill outra vez com elas — o perfil fica muito mais afiado.

## Conformidade

Uma newsletter é comunicação comercial por email, e isso tem regras que um post não tem. Isto **não é aconselhamento jurídico** — serve para saber quando é preciso perguntar. O critério completo está em `10-risco-crise-e-conformidade.md`.

- ⬤ **Consentimento prévio.** O artigo 22.º do **Decreto-Lei n.º 7/2004, de 7 de janeiro** (na redação do Decreto-Lei n.º 62/2009) sujeita o envio de comunicações de marketing direto por correio eletrónico a pessoas singulares a **consentimento prévio e expresso** — regime de opção positiva. Silêncio, inação e caixas pré-assinaladas não valem. Se ninguém souber dizer como a lista foi angariada, isso é um problema a levantar, não a ignorar.
- ⬤ **Identificação e cancelamento.** O mesmo diploma proíbe o envio que oculte a identidade de quem envia ou que não indique um endereço válido para pedir a cessação. Quem envia identificado e uma ligação de cancelamento que funciona vão em **todas** as edições.
- **Conteúdo gerado por IA.** O artigo 50.º do Regulamento de Inteligência Artificial está em vigor: texto sobre matéria de interesse público exige divulgação quando foi gerado ou manipulado por IA, salvo revisão humana efetiva ou controlo editorial com responsabilidade assumida. Uma correção superficial não basta. Para imagem, áudio ou vídeo, verificar o teste de *deepfake* e a regra da plataforma — módulo 10.
- **Palavras e imagens de terceiros** — citações longas, fotografias, excertos — exigem **autorização por escrito**. Vale sobretudo para o arquétipo "Entrevista ou retrato".
- **Testemunhos de clientes** com nome ou fotografia exigem consentimento **para esse fim específico**. Consentimento dado para uma coisa não serve para outra.
- **Nada de pedidos artificiais de interação** no corpo da edição ("responde a este email para o algoritmo", "reencaminha a três pessoas") quando o objetivo é fabricar métricas. Pedir resposta porque se quer mesmo ouvir alguém é outra coisa e é legítimo; as regras de distribuição do Facebook não se extrapolam para email ou Instagram.
- **Preços, prazos, disponibilidade e alegações reguladas** não são gerados aqui: saem do perfil e passam por um humano.

## Regras

- Exigir o perfil com as secções 3 e 5 preenchidas. Se faltarem, redirecionar para `construir-voz` e parar.
- Mínimo de 2 edições no modo análise. Abaixo disso, oferecer o modo arquétipo.
- Máximo de ◐ 1.200 palavras na subsecção. Apertado bate exaustivo.
- Nenhuma ferramenta é obrigatória. Sem `AskUserQuestion`, a escolha de arquétipo faz-se em conversa e a skill chega ao fim na mesma.
- Escrever no ficheiro de perfil que existe no projeto, seja qual for o nome. Não criar um `PERFIL-SOCIAL.md` novo ao lado de um perfil que já existe com outro nome.
- Os campos `Acessibilidade` e `Rodapé e conformidade` da subsecção 5b são fixos e não se omitem, haja ou não padrão nas edições analisadas.
- Não inventar sinais de voz, frases de assinatura, URL ou nomes que não apareçam em 2 ou mais edições.
- Não duplicar a secção 5 do perfil. Esta subsecção acrescenta só o que é específico da newsletter.
- Português europeu em tudo, incluindo as perguntas ao utilizador.
- Nenhum número sem nível de confiança. Os comprimentos por secção dos arquétipos são ◐ prática, nunca apresentados como estudo.
- Preços, prazos, disponibilidade e alegações reguladas não saem daqui: vêm do perfil e passam por um humano.
- Não oferecer, no fim, escrever já uma edição nem montar um plano de captação de subscritores. Acaba na entrega.
