---
name: comentario-fixado
description: "Escreve o comentário que a marca fixa numa publicação de Instagram ou Facebook, para antecipar uma pergunta sem sobrecarregar a legenda e, quando permitido, indicar a imagem que o acompanha. Usa sempre que pedirem primeiro comentário, comentário fixado ou destino para informação que sobra. TikTok fica LOOK INTO até revisão própria."
---

# Comentário fixado

## Gate de revisão

Antes de executar, correr `../social-media-manager/scripts/verificar_revisao.py`, resolvido relativamente a este ficheiro. Sem terminal, ler os blocos `Calendário` de `05-estado-das-plataformas.md` e `09-estado-da-vigilancia.md`. Se uma data chegou, passou ou é inválida, avisar uma vez por conversa; a primeira linha deve ser exatamente `Skill necessita de revisão`. Continuar com as limitações declaradas. O aviso não autoriza pesquisa, acesso a contas nem atualização.

## Contrato de contexto

Aplicar `../social-media-manager/references/contexto-do-caso.md`. O contexto pode chegar na mensagem, em anexos, em fontes ligadas ou em documentos com qualquer nome e formato. Neste ficheiro, «perfil» significa a fonte de contexto disponível; referências a números de secção servem apenas para o modelo opcional incluído no pacote. Não exigir esse modelo, não o copiar automaticamente e não tratar website, checkout, equipa ou ferramenta como pré-requisito. Pedir apenas a informação que muda materialmente esta tarefa.

Skill de execução. O critério de comunidade, moderação, isco de interação e a mecânica de puxar para privado vive em `../social-media-manager/references/06-comunidade-e-dm.md`. A anatomia da peça e a escada de atrito vivem em `../social-media-manager/references/04-criacao-de-conteudo.md`. **Ler os dois antes de escrever e não os repetir aqui.**

## O que corrigi face à prática corrente

**1. O comentário fixado não é para fabricar interação.** ⚠️ Esta skill nunca escreve um comentário fixado cuja função seja gerar comentários — a tática "comenta X que eu envio-te o link" é *engagement bait* no Facebook e recolha artificial de interação no Instagram. O caso completo está no módulo 06, secção "Automação".

**2. Também não é para "enganar o algoritmo".** ⚠️ Nenhuma plataforma declara que responder a comentários ou fixar um comentário melhore a distribuição da publicação; o que existe é afinidade acumulada **pessoa a pessoa**, que é outra coisa. A cadeia de raciocínio, elo a elo, está no módulo 06, secção "Comentários públicos" — ler lá, não repetir aqui.

**3. Então para que serve.** ◐ Para três coisas, e só estas:

- **Antecipar a pergunta que ia aparecer quarenta vezes** — preço, prazo, disponibilidade, como se encomenda, o que está incluído.
- **Alojar o que não cabe na legenda sem estragar o corte do "ver mais"** — a ficha técnica, as variantes, a morada, o horário.
- **Dar personalidade e contexto humano** à peça, na voz da secção 5 do perfil.

O critério de sucesso é **reduzir o número de vezes que a mesma pergunta chega às mensagens**, não os comentários que o comentário gera. ◐ Que seja "a peça que mais tempo devolve" é impressão, não medição — não há amostra que o sustente e não se afirma.

## A imagem no comentário: o que cada plataforma faz

A prática de origem assume um comentário com imagem. **Nas plataformas deste conjunto isso não é uniforme, e nenhuma destas capacidades se promete sem confirmar:**

- **Facebook** — comentários com imagem são o caso normal.
- **Instagram** — ◑ os comentários aceitam fotografia, além dos GIF da biblioteca GIPHY que já aceitavam. Não há artigo de ajuda oficial que o documente; a confirmação indireta mais recente é a nota de que a edição de comentários altera só o texto e **não** a imagem que o comentário possa ter (TechCrunch, 9 de abril de 2026). A disponibilidade varia por conta e por região. Se não aparecer, a imagem vai para outro sítio: último diapositivo do carrossel, cartão de história ligado à publicação, ou destaque do perfil.
- **TikTok — `LOOK INTO`.** Não afirmar nesta versão se comentários aceitam imagens, links ou respostas em vídeo/fotografia.

**Verificar sempre na aplicação antes de prometer o formato**, porque estas capacidades mudam sem aviso e sem documentação — e o que está escrito acima envelhece. Se não houver imagem no comentário, esta skill **não inventa uma volta** — escreve o comentário em texto e diz onde a imagem deve ficar.

## Arranque imediato

Ao disparar, ir direto ao Passo 0. Não resumir a skill.

## Passo 0. Perfil e peça

1. Ler o perfil (disponível na mensagem, anexos, fontes ligadas ou documentos do projeto) — secções 1 (Negócio), 4 (Plataformas), 5 (Voz), 6 (O que se pode e não se pode afirmar) e 9 (Conversa e atendimento). A secção 9 contém a **janela de resposta declarada**, e é ela que entra no comentário, não uma promessa inventada.
2. Ler a publicação a que o comentário se cola. **Sem a peça, não há comentário fixado** — pedir o texto ou o ficheiro e parar.
3. Sem contexto, pedir apenas os factos indispensáveis e marcar o resto `POR CONFIRMAR`. Não criar
   uma fonte automaticamente. Parar antes de escrever preços, prazos ou condições não confirmados.

## Passo 1. Recolher

**Perguntar num único lote pelo meio interativo disponível**, saltando o que o contexto já responde.

```json
[
  {"question": "Qual é a função deste comentário fixado?", "header": "Função", "multiSelect": false,
   "options": [
     {"label": "Antecipar a pergunta certa", "description": "Preço, prazo, disponibilidade — a que aparece sempre"},
     {"label": "Alojar o que sobra da legenda", "description": "Ficha, variantes, morada, horário"},
     {"label": "Encaminhar para o próximo passo", "description": "Como se encomenda, para onde se escreve"},
     {"label": "Contexto humano", "description": "O bastidor, o episódio, a voz da casa"}
   ]},
  {"question": "Onde é que este comentário vai ser fixado?", "header": "Plataforma", "multiSelect": true,
   "options": [
     {"label": "Instagram", "description": "Aceita foto no comentário, mas confirmar na conta"},
     {"label": "Facebook", "description": "Aceita imagem no comentário"},
     {"label": "TikTok", "description": "LOOK INTO — não produzir segundo regras atuais nesta versão"}
   ]},
  {"question": "Que pergunta é que este post vai gerar?", "header": "Pergunta", "multiSelect": false,
   "options": [
     {"label": "Quanto custa", "description": "Preço ou ordem de grandeza — só se estiver no perfil"},
     {"label": "Com quanta antecedência", "description": "Prazo real, do perfil"},
     {"label": "Fazem para a minha zona", "description": "Área servida e entregas"},
     {"label": "Outra — escrevo a seguir", "description": "Digo eu qual é a pergunta que se repete"}
   ]},
  {"question": "Há imagem para acompanhar?", "header": "Imagem", "multiSelect": false,
   "options": [
     {"label": "Temos fotografia real", "description": "Sempre a melhor opção"},
     {"label": "Quero um pedido de imagem escrito", "description": "Descrevo a imagem para gerar ou fotografar"},
     {"label": "Sem imagem", "description": "Texto chega e muitas vezes é o correto"}
   ]}
]
```

### Vários destinos ao mesmo tempo

**Um destino, uma peça.** Escolher três destinos não é um atalho — é triplicar o trabalho, e o trabalho tem de aparecer aqui em vez de aparecer na entrega.

- Sai **uma peça por destino**, cada uma com **gancho e chamada à ação próprios**. O mesmo texto colado em três sítios é a peça que nenhum dos três premeia.
- O plano declara **uma linha por destino** antes de se escrever, para o custo ficar visível antes do trabalho.
- ⚠️ **Destinos que não estejam na secção 4 do perfil não se produzem.** Perguntar porquê primeiro: uma plataforma que a marca não alimenta não vai dar seguimento à peça, e é assim que a regra de estar bem em duas ou três se contorna — uma peça de cada vez.
- Mais do que dois destinos: dizê-lo antes de começar e confirmar que é mesmo isso que se quer.

## Passo 2. Escrever o comentário

**Curto. Três a cinco linhas.** ◐ Não há estudo publicado sobre comprimento de comentário fixado — este limite é prática editorial desta skill, não um dado. A razão é de leitura: um comentário fixado longo é uma segunda legenda e fica por ler.

Estrutura:

```
Linha 1 — a resposta direta à pergunta antecipada, sem preâmbulo.
Linha 2-3 — o que a torna acionável: âmbito, condição, o que está incluído.
Linha 4 — o passo seguinte, um só, com a janela de resposta real da secção 9.
```

Regras de conteúdo:

- **Escreve-se o preço, não se esconde.** ⚠️ Empurrar tudo para privado ("preços só por DM") gera desconfiança e aproxima-se do território das omissões enganosas no regime das práticas comerciais desleais. Se não houver preço fixo, dá-se a ordem de grandeza e o que a faz variar.
- **Preços, prazos, disponibilidade e condições vêm do perfil ou de um humano.** Sem eles, `[POR CONFIRMAR]` no sítio exato.
- **A janela de resposta vem da secção 9 do perfil e declara-se mais larga do que a que se cumpre** — a regra e a razão estão no módulo 06, "Declarar uma janela que se cumpre". ⚠️ Antes de a escrever, confirmar qual produto e interface atendem o canal. A janela de 24 horas e os modelos do WhatsApp Business Platform **não se aplicam universalmente à app WhatsApp Business gratuita**; PLAT-015. Uma regra de API não define sozinha o prazo público de atendimento.
- **O canal do passo seguinte é o que a marca atende, não o que está à mão.** ⚠️ Em Portugal o canal de mensagem dominante não é o Instagram — ver módulo 06, primeiro aviso. Escrever o canal declarado na secção 9 do perfil, não presumir DM.
- **O link, se houver, vai onde a plataforma o deixa funcionar.** ◑ No Instagram o URL escrito num comentário aparece como texto simples e não é clicável — não está documentado num artigo de ajuda oficial e confirma-se na aplicação. No Facebook o link no comentário funciona. TikTok está `LOOK INTO`, sem exceções operacionais nesta versão. **Confirmar antes de escrever**: onde o link não for clicável, o comentário diz para onde ir e o destino real é a ligação do perfil (ver `otimizar-perfil`), e nunca se escreve "link nos comentários" quando o link não está lá.
- **Uma chamada à ação, do degrau mais barato que serve.** Nunca duas.
- **Na voz da secção 5.** ⚠️ Não é uma voz diferente da da legenda: ◐ é a mesma voz num registo mais próximo — o módulo 02 é explícito em que a voz não muda, só o registo. Sem personagem inventada e sem humor que não seja o da casa.

## Passo 3. A imagem, se houver

Se for fotografia real: dizer o que fotografar em linguagem de execução — enquadramento, luz, o que tem de estar em foco. ◐ Uma fotografia real do trabalho vale mais do que uma imagem gerada, e numa marca pequena é a prova de que existe alguém por trás da conta.

Se for imagem gerada, escrever o **pedido em texto** para o utilizador colar na ferramenta que tiver — não presumir ferramenta nenhuma. Formato:

> "Fotografia realista de [cena]. [Um único elemento visual, descrito em detalhe]. [Enquadramento e luz]. [O que tem de estar legível]."

Três regras: **um só elemento visual** (dois é sempre pior do que um) · **nada de texto essencial só dentro da imagem** · **nunca uma imagem de produto que não corresponde ao produto real** — isso é publicidade enganosa, não estilo.

⬤ Se houver texto sobre a imagem, **contraste mínimo de 4,5:1** para texto normal e 3:1 para texto grande (18pt normal ou 14pt negrito), pela norma WCAG 2.2 AA — limiares, não valores a arredondar. A verificação e o resto da camada de acessibilidade estão em `04-criacao-de-conteudo.md`. Se houver vídeo numa superfície coberta, leva **legendas revistas à mão** — as automáticas erram nomes próprios, preços e datas. TikTok está `LOOK INTO`.

⬤ Se a imagem for gerada ou alterada de forma significativa e for realista, **rotular**: a Meta aplica o rótulo "AI Info" quando deteta indicadores padrão (Content Credentials / C2PA) ou quando a pessoa declara. TikTok está `LOOK INTO`; não prometer uma regra ou formato nessa plataforma.

**Caminho manual e caminho melhorado.** O caminho manual — fotografia da casa, ou o pedido de imagem entregue em texto — funciona sem nada instalado e é o caminho por defeito. Se o projeto tiver uma ferramenta de geração de imagem ligada, usá-la e dizê-lo; se não tiver, **não parar, não pedir chaves de API, não sugerir instalações**. O que se perde no caminho manual é só o tempo de ir colar o pedido noutro lado.

## Passo 4. Entregar

1. **A pergunta antecipada**, numa frase — o que o post ia gerar nos comentários.
2. **O comentário**, em bloco de código, pronto a colar, uma versão por plataforma se forem várias.
3. **A imagem** — a fotografia a tirar ou o pedido em texto, e **onde ela fica** em cada plataforma coberta (comentário no Facebook; comentário no Instagram se a conta o permitir, senão último diapositivo, história ou destaque). TikTok está `LOOK INTO`.
4. **Acessibilidade** — texto alternativo da imagem, escrito à mão; contraste verificado se houver texto sobre a imagem; legendas revistas se a via for vídeo; e se a imagem carrega informação essencial (um preço, uma data), essa informação **também** está no texto do comentário.
5. **Buracos** — o que ficou `[POR CONFIRMAR]` e quem confirma.
6. **Lembrete de operação, uma linha:** fixar não é publicar e esquecer. ◐ O comentário fixado atualiza-se quando o preço ou o prazo mudarem — um comentário fixado desatualizado é pior do que nenhum, porque é lido como compromisso. ⚠️ **Não escrever aqui que é preciso vigiar a publicação na primeira hora:** o módulo 06 é explícito em que uma operação de uma pessoa não responde em uma hora e não deve tentar, e em que o que funciona é um bloco fixo por dia, não vigilância contínua.

## Regras

- **Português europeu** em tudo.
- ⚠️ **Identificar conteúdo comercial.** ⬤ `#PUB` no início quando há dinheiro ou benefício de terceiro — é o que a lei exige. ◐ **"conteúdo promocional"** quando é a própria marca a promover produto, preço, campanha ou desconto — é política interna deste sistema, não redação imposta. **Não trocar as duas:** carimbar `#PUB` numa peça da própria marca afirma uma relação comercial que não existe e dilui a etiqueta onde ela é obrigatória. Se a peça não promove nada, não leva nada. Tabela dos três casos em `../social-media-manager/references/10-risco-crise-e-conformidade.md`.
- ⚠️ **Nunca pedir comentários, gostos ou partilhas como fim** — ⬤ o Facebook despromove *engagement bait*; PLAT-007. O Instagram proíbe recolha artificial de interação.
- **Nunca prometer uma janela de resposta que obrigue a trabalhar ao fim de semana.** ⬤ Se houver trabalhadores por conta de outrem, o artigo 199.º-A do Código do Trabalho impõe o dever de abstenção de contacto no período de descanso, e a violação é contraordenação grave.
- **Nunca escrever preços, prazos ou condições que não venham do perfil ou de um humano.**
- Numa resposta pública, **nunca confirmar que alguém é cliente**, nem referir datas, valores, moradas ou detalhes de encomenda — ⬤ o administrador da página é corresponsável pelo tratamento de dados (TJUE, C-210/16).
- Comentário curto. Se passar de cinco linhas, o conteúdo pertence à legenda, a um destaque ou a uma página, não a um comentário.
- Não inventar personagem, humor recorrente nem "assinatura" que não esteja na secção 5 do perfil.
- Não resumir esta skill. Executá-la.
