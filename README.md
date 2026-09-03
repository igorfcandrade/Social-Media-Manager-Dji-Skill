# Social Media Skills (PT-PT)

Conjunto de **19 skills** de gestão de redes sociais em português de Portugal, para
Claude Code, Codex e qualquer assistente que descubra skills em disco.

Uma skill **governa** e dezoito **executam**. O ofício vive nas skills; os factos da
tua marca vivem nos ficheiros do teu projeto. As duas camadas nunca se misturam.

## O que faz

| Área | Skills |
|---|---|
| **Estratégia e ideias** | `social-media-manager` (governa) · `matriz-de-conteudo` · `pesquisa-de-nicho` |
| **Voz e contexto** | `construir-voz` · `voz-newsletter` · `sistema-contexto-conteudo` |
| **Escrita** | `escrever-post` · `formatar-post` · `gerar-ganchos` · `comentario-fixado` |
| **Vídeo curto** | `guiao-video-curto` · `capa-de-video` |
| **Visual** | `design-grafico` · `carrossel` · `infografico` · `post-de-citacao` |
| **Perfis e dados** | `otimizar-perfil` · `painel-metricas` · `avaliar-post` |

Serve qualquer setor — restauração, artesanato, SaaS, clínica, loja local, serviços.

## O que NÃO faz — lê isto antes de instalar

- **LinkedIn está fora de âmbito.** Não é coberto como canal. Onde o nome aparece
  nos módulos é como exemplo metodológico ou declaração de financiador de um estudo.
- **TikTok, Threads e X estão `LOOK INTO`.** Sem afirmações atuais sobre algoritmo,
  limites ou funcionalidades. Fora de cobertura validada.
- **Vídeo longo está fora.** O conjunto produz vídeo curto vertical (Reels, Shorts).
- **Não publica nada.** Não acede a contas, não envia, não agenda, não gasta em
  anúncios. Produz rascunhos para um humano aprovar.
- **Não inventa factos da tua marca.** Preços, prazos, produtos e promessas vêm dos
  teus ficheiros. Se não existirem, a skill pergunta — não estima.

## Antes de usar: o ficheiro obrigatório

**A skill não funciona sem contexto de marca.** É a única peça que tens mesmo de criar.

Escolhe conforme o tamanho do projeto:

### Projeto simples — um ficheiro

Copia `skills/social-media-manager/assets/PERFIL-MARCA-modelo.md` para a raiz do teu
projeto com o nome **`PERFIL-SOCIAL.md`** e preenche-o. O que não souberes fica
`POR DEFINIR` — nunca preenchas por adivinhação.

As secções que mais falta fazem:

| Secção | Porquê |
|---|---|
| **1. Identidade** | Quem é a marca, e **quem é o responsável humano** que aprova |
| **3. Público** | Sem isto, o conteúdo sai genérico |
| **4. Canais** | Onde se publica. Um destino fora desta lista **não se produz** |
| **5. Voz** | Como a marca soa. A skill `construir-voz` preenche-a a partir de textos teus |
| **6. Oferta e limites** | O que se pode e não se pode afirmar |

### Projeto com várias fontes ou campanhas

Usa o pacote em `skills/sistema-contexto-conteudo/assets/pacote-contexto/`, que
começa por um `CONTEXTO-MANIFESTO.md` a declarar caminhos canónicos e precedência.

Corre a skill `sistema-contexto-conteudo` para te guiar na criação.

## Instalação

```bash
git clone https://github.com/igorfcandrade/Social-Media-Manager-Dji-Skill.git
cd Social-Media-Manager-Dji-Skill
./instalar.sh
```

Instala em todos os ambientes detetados (`~/.claude/skills/` e `~/.codex/skills/`) e
ignora os que não existem. **Reinicia a sessão** para as skills serem reconhecidas.

⚠️ **Skills aninhadas não são descobertas** — por isso o instalador copia cada uma
para a raiz da pasta de skills, em vez de as deixar em subpastas.

Para confirmar:

```bash
./testar.sh
```

## Como usar

Descreve o que precisas em linguagem normal. A governante escolhe o caminho:

- *"o que publicamos esta semana?"* → calendário
- *"escreve um post sobre isto"* → `escrever-post`
- *"porque é que o alcance caiu?"* → análise
- *"faz-me um carrossel disto"* → `carrossel`
- *"vale a pena pagar anúncios?"* → promoção paga

Não precisas de saber os nomes das skills.

## Duas coisas que vais ver e convém perceber

### `Skill necessita de revisão`

As regras das plataformas mudam. As afirmações voláteis — algoritmo, limites, APIs —
vivem num registo datado (`05-estado-das-plataformas.md`) com data da última
releitura. Quando essa data passa, a skill **avisa uma vez** e continua a trabalhar
com as limitações declaradas.

O aviso não pesquisa, não acede a contas e não atualiza nada sozinho. **É um convite
a verificares tu**, não um erro. Se o vires, trata os factos de plataforma como
possivelmente desatualizados até confirmares na fonte oficial.

### Marcas de confiança: ⬤ ◑ ◐

Todo o facto nos módulos está marcado:

- **⬤ Fonte primária** — plataforma, regulador, lei, tribunal ou estatística
  oficial, **sempre com URL colado ao facto**
- **◑ Consenso** — várias fontes de indústria convergem, com metodologia e amostra
  declaradas
- **◐ Prática** — juízo profissional defensável, sem estudo por trás

O que não tiver marca é folclore. Um número sem amostra conhecida não é um dado.

Mantém estas marcas no que escreveres a partir dos módulos.

## Dependências externas

**Todas opcionais.** Cada skill tem um caminho manual que funciona sem chaves de API
nem serviços pagos, e um caminho melhorado se a ferramenta existir. Nenhuma para por
falta de ferramenta.

## Conformidade

O conjunto foi escrito para Portugal e para a UE: identificação de conteúdo
comercial segundo o Guia de Boas Práticas da Auto Regulação Publicitária, RGPD,
DSA, rotulagem de IA, licenciamento de música em contas de empresa, consentimento
escrito para testemunhos, e acessibilidade.

⚠️ **Não é aconselhamento jurídico.** Setores regulados — saúde, finanças, jogo,
álcool — exigem verificação própria.

## Licença

MIT. Ver [LICENSE](LICENSE).

As dezassete skills de execução são obras derivadas de
[charlie947/social-media-skills](https://github.com/charlie947/social-media-skills)
de Charlie Hills (MIT) — ver [LICENSE-upstream](LICENSE-upstream) e
[CREDITOS.md](CREDITOS.md). A skill governante e a de contexto são originais.

## Contribuir

Este repositório é gerado a partir de uma fonte privada. **Pedidos de integração
não são aceites diretamente aqui** — abre uma *issue* a descrever o problema ou a
proposta.
