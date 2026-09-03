---
name: otimizar-perfil
description: "Reconstrói perfis de Instagram, Facebook e Google Business Profile — nome, bio, ligação, destaques, fixados, categoria e imagens — e entrega a checklist mensal. Usa sempre que o pedido tocar no perfil, bio, ligação, destaques, Google Maps ou auditoria à conta. TikTok fica LOOK INTO até revisão própria. Não escreve conteúdo: escreve o recipiente."
---

# Otimizar perfil

## Gate de revisão

Antes de executar, correr `../social-media-manager/scripts/verificar_revisao.py`, resolvido relativamente a este ficheiro. Sem terminal, ler os blocos `Calendário` de `05-estado-das-plataformas.md` e `09-estado-da-vigilancia.md`. Se uma data chegou, passou ou é inválida, avisar uma vez por conversa; a primeira linha deve ser exatamente `Skill necessita de revisão`. Continuar com as limitações declaradas. O aviso não autoriza pesquisa, acesso a contas nem atualização.

Skill de execução. A doutrina do perfil — os cinco campos por ordem de valor, a clareza do nome de exibição, os destaques como menu de objeções, os fixados, a auditoria mensal — vive em `../social-media-manager/references/00-a-conta.md`. **Ler esse módulo antes de começar e não o repetir aqui.** Para os sinais de cada plataforma, `../social-media-manager/references/05-plataformas.md`; para uma afirmação volátil, ler o ID em `../social-media-manager/references/05-estado-das-plataformas.md`.

## Arranque imediato

Ao disparar, ir direto ao Passo 0 e ao Passo 1. Não resumir a skill, não listar o que vai produzir, não perguntar se se avança.

## Passo 0. Perfil de marca

Ler o perfil do projeto (`PERFIL-SOCIAL.md`, `MARCA.md`, `MEMORY.md`). Aproveitar as secções 1 (Negócio), 2 (Objetivo), 3 (Público), 4 (Plataformas), 5 (Voz), 6 (Alegações), 8 (quem aparece em câmara e meios de produção) e 9 (perguntas que já chegam) e **dizer numa linha o que foi aproveitado** — não voltar a perguntar o que já lá está.

Se não existir, copiá-lo de `../social-media-manager/assets/PERFIL-MARCA-modelo.md` e preencher com as respostas do Passo 1. Se a secção 5 (Voz) estiver vazia, dizer que a bio vai sair genérica e sugerir correr `construir-voz` primeiro. Se faltarem factos do negócio (preços, prazos, área servida), **perguntar — nunca estimar.**

## Passo 1. Recolher o que falta

**AskUserQuestion**, um lote só, saltando as perguntas já respondidas pelo perfil.

```json
[
  {"question": "Que perfis vamos tratar agora?", "header": "Plataformas", "multiSelect": true,
   "options": [
     {"label": "Instagram", "description": "Bio, destaques, fixados, ligação"},
     {"label": "TikTok", "description": "LOOK INTO — não otimizar nesta versão"},
     {"label": "Facebook", "description": "Página: nome, sobre, capa, botão"},
     {"label": "Google Business Profile", "description": "Negócio com morada ou área servida"}
   ]},
  {"question": "Qual é o único próximo passo que o perfil deve pedir?", "header": "Próximo passo",
   "options": [
     {"label": "Mandar mensagem", "description": "A venda passa por conversa"},
     {"label": "Marcar / encomendar", "description": "Formulário, marcação ou checkout"},
     {"label": "Ir à loja", "description": "Morada e horário são o destino"},
     {"label": "Ligar", "description": "O telefone é o canal que converte"}
   ]},
  {"question": "Que prova verificável se pode escrever numa linha?", "header": "Prova",
   "options": [
     {"label": "Anos de casa", "description": "Ex.: desde 2011"},
     {"label": "Número de clientes ou trabalhos", "description": "Um número que se consegue sustentar"},
     {"label": "Certificação ou prémio", "description": "Com entidade nomeada"},
     {"label": "Escrevo eu", "description": "Tenho outra prova concreta"}
   ]},
  {"question": "Como me dás o estado atual dos perfis?", "header": "Estado atual",
   "options": [
     {"label": "Colo o texto", "description": "Nome, bio e destaques atuais"},
     {"label": "Mando captura de ecrã", "description": "Do telemóvel, como se vê de facto"},
     {"label": "Começar do zero", "description": "Ignora o que está lá"}
   ]}
]
```

⚠️ **A prova tem de passar pela secção 6 do perfil.** Uma alegação que o cliente consegue desmentir sozinho destrói tudo o resto. Se não houver prova para a afirmar, ela não entra.

### Vários destinos ao mesmo tempo

**Um perfil, um recipiente.** Cada plataforma indexa campos diferentes e corta-os de maneira diferente.

- Sai **um conjunto por plataforma** — nome, bio, ligação, categoria e botão — cada um em bloco próprio. Uma bio copiada entre plataformas é uma bio otimizada para nenhuma.
- ⚠️ **Plataformas que não estejam na secção 4 do perfil não se otimizam.** Perguntar porquê primeiro: manter um perfil que ninguém vai alimentar é pior do que não o ter.

## Passo 2. Nome de exibição

◐ O explicador oficial de 2021 listava nome de utilizador e nome de exibição entre os campos comparados pela Pesquisa do Instagram. [Instagram, Pesquisa, 25/08/2021](https://about.instagram.com/blog/announcements/break-down-how-instagram-search-works) · PLAT-004. É um snapshot histórico cuja fonte não foi relida nesta revisão; a skill não tem uma hierarquia atual de campos nem pesos publicados. A fórmula abaixo é uma decisão de clareza e identificação local, não uma promessa de ranking.

Escrever **3 opções**, em bloco de código, na fórmula `Marca | o que faz + onde`. Sem cargos, sem maiúsculas decorativas, sem emojis dentro do nome. Depois usar AskUserQuestion com as três opções escritas por extenso na descrição, para o utilizador escolher.

- **Instagram** — nome de exibição e nome de utilizador são campos diferentes: o nome de utilizador é a morada. O nome de exibição ajuda a identificação; a fonte de pesquisa é um snapshot histórico, não uma promessa atual de ranking. Manter o mesmo nome de utilizador nas plataformas cobertas, ou escrever a razão de não ser.
- **TikTok — `LOOK INTO`.** Não usar nesta versão regras de nome, bio, fixados, pesquisa ou limites de caracteres.
- **Facebook** — nome da Página; alterações passam por revisão, avisar disso.
- **Google Business Profile** — usar o nome real pelo qual o negócio é reconhecido no mundo físico, sem palavras-chave acrescentadas para tentar influenciar o ranking. Escolher o menor conjunto de categorias necessário e manter a informação completa e correta. A Google não publica pesos universais nem permite pagar ou pedir melhor posição; PLAT-012 e PLAT-013.

## Passo 3. Bio, por plataforma

Uma bio por plataforma, cada uma em bloco de código, seguindo a ordem de valor de `00-a-conta.md`: **primeira linha (o que se faz e para quem, em linguagem de cliente) → prova numa linha → um único próximo passo.**

- **Um só pedido.** Uma bio com quatro pedidos é uma bio sem pedido.
- Linguagem de cliente, não de setor. Não "soluções de bem-estar"; "fisioterapia em Alvalade, com marcação no próprio dia".
- Sem limites de caracteres decorados de memória: **verificar na aplicação real, num telemóvel.** O que interessa não é o total — é onde cai o corte e o que fica antes do "mais".
- **Google Business Profile:** a descrição, as categorias, o modelo de atendimento, a morada/área servida e os horários devem representar o negócio com exatidão. A Google não publica pesos fixos por campo; ver PLAT-012 e PLAT-013.

Entregar também a linha do botão de ação de cada plataforma onde ela exista, coerente com o próximo passo escolhido. **No Instagram, os botões disponíveis dependem da categoria da conta** (`00-a-conta.md`): verificar a categoria antes de prometer um botão.

**Acessibilidade da bio** (`04-criacao-de-conteudo.md`): cada emoji é lido em voz alta por um leitor de ecrã. Nada de cadeias decorativas nem de emojis usados como marcadores de lista; se houver hashtag na bio, em CamelCase (#PerguntasFrequentes, não #perguntasfrequentes).

## Passo 4. Ligação

**Uma ligação por objetivo do mês.** Página de ligações só quando houver vários destinos com procura medida — uma página intermédia com sete opções acrescenta um passo a toda a gente para servir a minoria.

Entregar o URL final com UTM, segundo a convenção da secção 12 do perfil. Se não houver convenção, propor uma e escrevê-la no perfil.

## Passo 5. Destaques e fixados

**Destaques = menu de objeções, não álbum.** Derivar os títulos das objeções reais da secção 3 do perfil e das perguntas que já chegam por mensagem (secção 9). Base habitual: Preços · Prazos · Como encomendar · Perguntas frequentes · Provas · Quem somos. Se um destaque não responde a uma pergunta que já chegou, não é destaque — propor apagá-lo.

Entregar: título de cada destaque (curto, cabe sem cortar), o que leva dentro, e o que sai.

⚠️ **Destaque de provas ou testemunhos:** publicar um testemunho com nome, fotografia ou captura de conversa exige **consentimento escrito para esse fim específico**, e as capturas saem com tudo o que identifique o cliente tapado (`10-risco-crise-e-conformidade.md`). Sem consentimento registado, o testemunho não entra — nem em destaque nem em fixado.

**Fixados** — é o único espaço editorial permanente da conta. Três, no máximo: o que se vende e a quanto · a prova mais forte · a peça de entrada para quem nunca ouviu falar. Indicar quais das peças existentes servem; se não existir nenhuma, dizê-lo e remeter para `04-criacao-de-conteudo.md` em vez de inventar.

## Passo 6. Google Business Profile

Só se estiver nas plataformas escolhidas e o negócio for elegível. ⬤ A Google exige contacto presencial com clientes e exclui negócios apenas online; o nome deve ser o usado no mundo real. Fatores de posicionamento local declarados: relevância, distância e proeminência, sem pesos fixos publicados. [Google, elegibilidade e ranking](https://support.google.com/business/answer/13763036?hl=en) · PLAT-012 e PLAT-013.

Executar, por esta ordem de trabalho — não de peso de ranking: confirmar elegibilidade e modelo de atendimento · nome real · categoria principal específica · apenas as categorias secundárias necessárias · morada ou área servida · horários, **incluindo horários especiais de feriado** · atributos · fotografias · avaliações. PLAT-012 e PLAT-013.

⚠️ Instrução morta que ainda circula em guias: ativar o Google Business Messages, encerrado em 31/07/2024. Outras funcionalidades, incluindo Perguntas e Respostas, confirmam-se na interface atual; não inferir uma retirada sem fonte oficial.

## Passo 7. Fotografia de perfil e imagem de capa

**Caminho manual, que funciona sem nada instalado** — entregar um *briefing de fotografia* que a marca executa com o telemóvel: enquadramento, fundo, luz, o que veste, o que não pode aparecer. É o caminho por defeito e, para negócios de artesanato, comida e serviços locais, **é o melhor**: uma fotografia real da pessoa ou do produto ganha a qualquer imagem gerada.

**Caminho melhorado, só se houver gerador de imagem disponível** (Gemini, Claude com geração, ou outro) — entregar prompts autónomos, um por bloco de código, cada um a funcionar isolado. Se não houver ferramenta, não bloquear: seguir com o briefing manual e dizer o que se perde (rapidez a testar variantes de fundo e de cor).

⚠️ **Se a imagem for gerada por IA** (`10-risco-crise-e-conformidade.md`): aplicar o rótulo exigido pela plataforma. O artigo 50.º do AI Act está em vigor desde 2 de agosto de 2026 e cobre *deepfakes* — conteúdo que cria falsamente aparência de autenticidade — e certos textos de interesse público. ◐ Na dúvida, este sistema identifica conteúdo realista ou materialmente alterado por IA. Duas linhas que não se atravessam: **não gerar um rosto que se apresenta como a pessoa do negócio** e **não gerar produto que não corresponde ao que se vende**.

Regras de imagem que se aplicam nos dois caminhos, ◐ prática:

- **Fotografia de perfil:** preparar uma origem quadrada, rosto ou marca ao centro a ocupar 60 a 70% do enquadramento, com margem; confirmar o recorte na conta de Instagram e Facebook. Tem de continuar legível quando reduzida. TikTok está `LOOK INTO`.
- **Capa (Facebook):** compor tudo o que importa numa zona central segura — o recorte é diferente no telemóvel e no computador, e a interface tapa cantos.
- **Capas de destaques (Instagram):** ícones simples, um sistema visual único, legíveis em miniatura. Sem texto pequeno.
- **Pinterest**, se estiver em uso: 2:3 é uma escolha de produção segura; 1000×1500 não é limite orgânico universal. Confirmar os rácios aceites em PLAT-019.
- **Não escrever dimensões em píxeis de memória para as outras plataformas.** Confirmar na página de ajuda da plataforma no dia em que se faz o trabalho, ou entregar o enquadramento em vez do número.
- Vídeo de perfil ou de apresentação, se houver: confirmar primeiro que a superfície o aceita e qual é o rácio. Com fala, **legendas revistas à mão** — as automáticas erram nomes próprios, números e preços. TikTok está `LOOK INTO`.

**Acessibilidade, que não é opcional** (`04-criacao-de-conteudo.md`):

- **Contraste** ⬤ mínimo 4,5:1 para texto normal e 3:1 para texto grande (18pt normal ou 14pt negrito), norma WCAG 2.2 AA. Aplica-se ao texto das capas de destaques e da imagem de capa. **Calcular o rácio dos pares de cor usados e escrevê-lo na saída.** Abaixo do limiar, muda-se a cor.
- **Texto alternativo** para a imagem de capa e para cada capa de destaque, descrevendo função e conteúdo essencial, sem começar por "imagem de".
- **Informação essencial nunca só por cor**, e o que estiver escrito numa imagem tem de estar também em texto (bio, legenda ou destaque).

Cores e tipografia: se o projeto tiver skill própria de tema visual ou paleta, **essa ganha** sobre qualquer sugestão daqui. Senão, usar a paleta já em uso nas peças da marca; se não existir nenhuma, propor duas cores, **fazer confirmar por quem decide** e registá-las no perfil (secção 12, Convenções técnicas — o modelo não tem campo de cor, acrescenta-se um) — não as reinventar a cada trabalho.

## Passo 8. Entregar a auditoria

Fechar com a checklist mensal de `00-a-conta.md`, preenchida com o estado encontrado (✓ / ✗ / não verificável) e a data. É isto que transforma o trabalho de hoje em rotina.

Acrescentar, se se aplicar: acessos e propriedade das contas (secção 4 do perfil), duas pessoas com acesso, dois fatores, e a regra sem exceções — **nenhuma plataforma pede credenciais nem código de dois fatores por mensagem.**

## Regras

- Ir direto ao Passo 0 ao disparar. Sem preâmbulo.
- Todo o texto de perfil (nome, bio, destaques, botões) sai em bloco de código, pronto a copiar.
- Zero LinkedIn. Se o utilizador o pedir explicitamente, tratar como caso à parte e dizer que esta skill não o cobre.
- Nenhum número de caracteres, píxeis ou métrica sem origem. Nível de confiança sempre marcado: ⬤ oficial · ◑ consenso · ◐ prática.
- Nenhum preço, prazo, condição de envio ou alegação escrito a partir desta skill — vêm do perfil ou de uma pergunta.
- Nenhuma peça visual sai sem texto alternativo e sem o contraste calculado. É a primeira camada a desaparecer com pressa; por isso está aqui e não na memória.
- Imagem gerada por IA que represente pessoas, produtos ou lugares reais sai identificada como tal, pelas ferramentas da própria plataforma.
- Nenhuma ferramenta é obrigatória. Se `AskUserQuestion` não existir, as perguntas fazem-se em conversa e a skill chega ao fim na mesma; sem gerador de imagem, vale o briefing de fotografia.
- Verificar sempre na aplicação real, num telemóvel. O que se vê no computador não é o que o cliente vê.
- Escrever as alterações feitas de volta no perfil de marca (secção 4 e secção 12) com a data.
- Português europeu em tudo, incluindo as perguntas.
- Não seguir para calendário, plano de conteúdo ou post de lançamento no fim. Acaba na auditoria.
