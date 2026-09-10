# Social Media Skills (PT-PT)

Conjunto de **20 skills** de gestão de redes sociais em português de Portugal, portáteis entre
ambientes que consigam carregar skills em Markdown.

Uma skill **governa**, uma **prepara o contexto factual** e dezoito **executam**. O ofício vive nas skills; os factos do caso chegam
pela mensagem, anexos, fontes ligadas ou documentos do projeto. O ambiente fornece os meios de
interação e execução. As três camadas nunca se misturam.

## O que faz

| Área | Skills |
|---|---|
| **Estratégia e ideias** | `social-media-manager` (governa) · `matriz-de-conteudo` · `pesquisa-de-nicho` |
| **Voz e contexto** | `construir-voz` · `voz-newsletter` · `sistema-contexto-conteudo` |
| **Escrita** | `escrever-post` · `formatar-post` · `gerar-ganchos` · `comentario-fixado` |
| **Vídeo curto** | `guiao-video-curto` · `capa-de-video` |
| **Visual** | `photo-first-art-direction` · `design-grafico` · `carrossel` · `infografico` · `post-de-citacao` |
| **Perfis e dados** | `otimizar-perfil` · `painel-metricas` · `avaliar-post` |

Serve qualquer organização sem pressupor setor, dimensão, equipa, website ou percurso de conversão.

## O que NÃO faz — lê isto antes de instalar

- **LinkedIn está fora de âmbito.** Não é coberto como canal. Onde o nome aparece
  nos módulos é como exemplo metodológico ou declaração de financiador de um estudo.
- **TikTok, Threads e X estão `LOOK INTO`.** Sem afirmações atuais sobre algoritmo,
  limites ou funcionalidades. Fora de cobertura validada.
- **Vídeo curto de ponta a ponta.** O módulo operacional cobre brief, planos, captação, edição,
  legendas, som, master limpo, exportações e revisão, sem depender de editor ou conector específico.
  Uma capacidade só é apresentada como automática depois de estar declarada e testada.
- **Vídeo longo está fora.** O conjunto produz vídeo curto vertical (Reels, Shorts).
- **Não publica nada.** Não acede a contas, não envia, não agenda, não gasta em
  anúncios. Produz rascunhos para um humano aprovar.
- **Não inventa factos da tua marca.** Preços, prazos, produtos e promessas vêm dos
  teus ficheiros. Se não existirem, a skill pergunta — não estima.

## Contexto do caso

A skill usa apenas o contexto necessário para o pedido atual. Esse contexto pode estar na própria
mensagem, em anexos, em fontes ligadas ou nos documentos que o projeto já utiliza. Não exige um
ficheiro, nome ou estrutura específicos.

Quando um projeto quer criar uma estrutura documental, pode usar opcionalmente
`skills/social-media-manager/assets/PERFIL-MARCA-modelo.md` ou o pacote modular de
`sistema-contexto-conteudo`. São modelos, não pré-requisitos.

Se faltar um facto indispensável, a skill pergunta. Se a ausência não bloquear o trabalho, marca
`POR CONFIRMAR`. Nunca presume website, checkout, equipa, preços, prazos ou ferramentas.

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
