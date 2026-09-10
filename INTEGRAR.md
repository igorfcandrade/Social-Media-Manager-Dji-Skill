# Integrar este conjunto num assistente

Este repositório é **agnóstico quanto ao modelo**. Não contém instruções para um assistente
em particular, não gera pacotes para nenhum, e não deve passar a conter.

O que ele contém é uma coisa só: **skills em Markdown, com um ficheiro `SKILL.md` cada uma,
frontmatter com `name` e `description`, e recursos em `references/` e `assets/`.** Qualquer
sistema que saiba ler ficheiros consegue usá-las.

Este documento diz **como as ligar** a cada ambiente. É a única parte do repositório que fala
de assistentes concretos, e é deliberadamente curta: quanto mais ela crescer, menos o
repositório é agnóstico.

---

## A regra

> **Nada específico de um assistente entra no repositório.**
>
> Nem instruções de sistema, nem pacotes gerados, nem configuração de conta ou execução, nem
> cópias reformatadas dos módulos. Metadados opcionais de interface em `agents/`, como nome
> visível e pedido inicial, podem acompanhar a skill; não guardam credenciais nem substituem
> as instruções portáteis do `SKILL.md`. Se um ambiente precisa de outro formato, esse formato produz-se
> **fora** daqui, a partir da fonte, e vive onde esse ambiente vive.
>
> A razão não é purismo. Uma segunda cópia dos módulos é uma segunda fonte de verdade, e uma
> segunda fonte de verdade diverge — em dois dias, medido, sem ninguém dar por isso. É o
> mesmo erro que a arquitetura de duas camadas existe para impedir, um nível acima.

**Consequência prática:** as três coisas abaixo são as únicas formas suportadas de usar isto.
Se um ambiente novo não couber em nenhuma, acrescenta-se uma secção **aqui**, não uma pasta
no repositório.

---

## 1. Ambientes que descobrem skills numa pasta

**Quem:** Claude Code, Codex, e qualquer sistema que leia uma pasta de skills.

É o caminho de primeira classe: as skills são lidas na origem, sem conversão nenhuma.

```bash
./instalar.sh
```

Instala nos ambientes que existirem na máquina — `~/.claude/skills/` e `~/.codex/skills/` —
e ignora os que não existirem. Skills que não venham daqui não são tocadas.

**Correr sempre depois de mexer.** Falhar em corrê-lo não dá erro: as skills antigas continuam
a responder, e a correção fica a apodrecer no repositório. Já aconteceu duas vezes.

```bash
python3 scripts/validar_instalacoes.py
```

Compara o repositório com cada ambiente instalado e diz o ficheiro exato que diverge. Corre
dentro do `./testar.sh`.

⚠️ **Cada skill tem de ficar na raiz da pasta de skills.** Skills aninhadas não são
descobertas — é por isso que o instalador copia em vez de criar ligações para uma subpasta.

---

## 2. Ambientes que leem o repositório diretamente

**Quem:** qualquer assistente com acesso ao sistema de ficheiros ou a um conector de
repositórios.

Não é preciso instalar nada. Aponta-se o assistente ao repositório e diz-se-lhe para começar
em `skills/social-media-manager/SKILL.md`, que é o encaminhador.

**Vantagem:** nunca desatualiza.
**Risco a vigiar:** se o acesso falhar, um assistente responde de memória — que é exatamente
o que este sistema existe para impedir. **O sinal de que aconteceu é começar a citar números
sem amostra.** Se isso surgir, parar e verificar o acesso antes de aceitar seja o que for.

---

## 3. Ambientes que só aceitam texto colado

**Quem:** um GPT personalizado, um Projeto, um assistente sem acesso a ficheiros.

Aqui há mesmo de se produzir outro formato, e **esse formato não vive aqui**. Produz-se fora,
e assume-se o custo:

- **É uma cópia, e vai divergir.** Datar, e regenerar a partir da fonte a cada alteração.
- **Não se edita a cópia.** Uma correção feita só lá perde-se na regeneração seguinte, e até
  lá está a servir uma versão que o repositório já corrigiu.
- **Os caminhos relativos deixam de significar nada.** Num sistema de ficheiros planos,
  `../social-media-manager/references/04-criacao-de-conteudo.md` é uma referência morta.
  Ao aplanar, reduzir ao nome do ficheiro.
- **As mecânicas do repositório não atravessam.** Instruções para correr scripts, validadores
  ou o instalador não fazem sentido num ambiente sem terminal, e uma instrução que não se
  pode cumprir é pior do que nenhuma. Retirar ou substituir pelo equivalente manual.
- **Verificar o que a cópia diz antes de a carregar.** Não basta estar sincronizada:
  sincronizado só prova que os bytes são iguais, não que o conteúdo faz sentido no destino.

Se o sistema tiver limite de caracteres nas instruções, o encaminhador de
`skills/social-media-manager/SKILL.md` é o que se condensa; os módulos vão como material de
consulta.

**Carregar também o contexto da marca do projeto.** Sem ele o resultado é plausível e vazio,
em qualquer ambiente.

---

## O que garantir em qualquer ambiente

Independentemente do caminho escolhido, estas quatro têm de continuar verdadeiras. São o que
distingue este conjunto de um prompt bonito.

1. **A precedência mantém-se:** em conflito, manda o contexto da marca; e as skills próprias
   do projeto ganham sobre os módulos genéricos.
2. **Os níveis de confiança mantêm-se** — ⬤ fonte primária com URL, ◑ consenso com amostra,
   ◐ prática. O que não tiver nível é folclore.
3. **Nenhum facto da marca sai do assistente** — preços, prazos, condições e disponibilidade
   vêm do contexto do projeto ou de uma pessoa.
4. **O aviso de revisão devida chega ao utilizador.** Se o ambiente o engolir, o calendário
   deixa de existir na prática.

**Teste de aceitação, em qualquer ambiente:** pedir um número que o sistema não deva ter —
por exemplo uma taxa de interação de referência para o setor. A resposta certa nomeia a
amostra e a fonte, ou diz que não há dado fiável. Se sair um número redondo sem origem, a
integração não está a funcionar, por muito que os ficheiros estejam lá.
