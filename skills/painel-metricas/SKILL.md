---
name: painel-metricas
description: "Transforma dados ou exportações de redes sociais fornecidos num painel e relatório acionável. Usa para analisar um conjunto de dados concreto. Não define a estratégia de medição do zero nem inventa métricas ausentes; pedidos amplos de diagnóstico pertencem à social-media-manager."
---

# Painel de métricas

## Gate de revisão

Antes de executar, correr `../social-media-manager/scripts/verificar_revisao.py`, resolvido relativamente a este ficheiro. Sem terminal, ler os blocos `Calendário` de `05-estado-das-plataformas.md` e `09-estado-da-vigilancia.md`. Se uma data chegou, passou ou é inválida, avisar uma vez por conversa; a primeira linha deve ser exatamente `Skill necessita de revisão`. Continuar com as limitações declaradas. O aviso não autoriza pesquisa, acesso a contas nem atualização.

## Contrato de contexto

Aplicar `../social-media-manager/references/contexto-do-caso.md`. O contexto pode chegar na mensagem, em anexos, em fontes ligadas ou em documentos com qualquer nome e formato. Neste ficheiro, «perfil» significa a fonte de contexto disponível; referências a números de secção servem apenas para o modelo opcional incluído no pacote. Não exigir esse modelo, não o copiar automaticamente e não tratar website, checkout, equipa ou ferramenta como pré-requisito. Pedir apenas a informação que muda materialmente esta tarefa.

Skill de execução. Todo o critério — regressão à média, incomparabilidade das fórmulas, atribuição, mediana vs média, estrutura do relatório — vive em `../social-media-manager/references/07-analise-e-relatorio.md`. **Ler esse módulo antes de tocar nos dados e não o repetir aqui.** Para o negócio com morada física, `../social-media-manager/references/12-contextos-de-negocio.md`. Para benchmarks, `../social-media-manager/references/11-numeros-de-referencia.md`. Modelo de relatório em `../social-media-manager/assets/relatorio-mensal-modelo.md`.

## Arranque imediato

Ao disparar, ir direto ao Passo 0. Não resumir a skill, não explicar a metodologia antes de a aplicar.

## Passo 0. Contexto do caso

Localizar e ler objetivo, métrica-norte, indicadores, alvos definidos antes da medição, linha de base,
cadência, aprendizagens e fórmula de taxa. Não exigir que estejam num ficheiro ou esquema específico.
Sem objetivo e alvo prévios, é possível descrever os dados, mas não classificar o resultado como
sucesso ou fracasso. Se faltar uma fórmula, propô-la e obter confirmação antes de a fixar; não a
mudar entre períodos comparáveis.

## Passo 1. Recolher as exportações

**Nada aqui exige API, ferramenta paga ou ligação autenticada.** O caminho manual é a exportação que qualquer pessoa descarrega. **Perguntar num único lote pelo meio interativo disponível**:

```json
[
  {"question": "Que exportações tens?", "header": "Fontes", "multiSelect": true,
   "options": [
     {"label": "Instagram / Facebook", "description": "Meta Business Suite → Insights → intervalo de datas → Exportar. CSV ou XLSX."},
     {"label": "TikTok", "description": "LOOK INTO — instruções de exportação não validadas nesta cobertura."},
     {"label": "Google Business Profile", "description": "Negócio elegível com atendimento presencial. Perfil da empresa → Desempenho → exportar."},
     {"label": "Site: Analytics e Search Console", "description": "Só se houver site. Sem isto não há UTM nem triangulação de atribuição no Passo 3 — e a via do inquérito passa a ser a única."},
     {"label": "Não tenho nada exportado", "description": "Digo-te exatamente o que ir buscar e onde, e paramos aqui até haver ficheiro."}
   ]},
  {"question": "Que período estamos a analisar?", "header": "Período", "multiSelect": false,
   "options": [
     {"label": "Mês fechado", "description": "O cavalo de batalha. Compara com o mês anterior E com o mesmo mês do ano passado."},
     {"label": "Trimestre", "description": "Revisão estratégica: pilares, mix de plataformas, cadência."},
     {"label": "Semana", "description": "Primeiro nível legítimo de leitura. Sem conclusões de conteúdo."},
     {"label": "Desde o início", "description": "Linha de base ou auditoria de conta herdada."}
   ]}
]
```

Se não houver ficheiro nenhum, **parar e dizer onde ir buscar** — não estimar números.

## Passo 2. A conversa das janelas de retenção — antes de tudo

⚠️ **Uma análise que não foi exportada não se refaz.** Verificar e dizer, sempre, na primeira entrega:

| Fonte | Janela | Estatuto |
|---|---|---|
| Instagram, métricas de conta | até 90 dias | ⬤ documentação da API |
| Google Search Console | 16 meses | ⬤ |
| Google Analytics 4 | retenção ao nível de evento configurável em 2 ou 14 meses, em propriedades padrão | ⬤ |
| TikTok | `LOOK INTO` | não dar retenção ou exportação como atuais |
| Google Business Profile | cerca de 6 meses — o painel não deixa recuar mais | ◑ |

As duas últimas linhas só se aplicam se houver site. Manter a marcação de confiança tal como está no módulo 07: não subir nem descer o nível para um número parecer mais firme.

**Ação imediata, irreversível se adiada:** se a retenção do Google Analytics estiver no valor mais curto, **recomendar mudar hoje** para o mais longo. É uma definição de conta de quem é dono dela — a decisão e o clique são humanos. Os dados que expiram não voltam.

**Recomendar uma rotina de exportação mensal** para o arquivo escolhido pelo caso. Sem isso, os dados
podem expirar e deixar de ser comparáveis. Não impor uma pasta ou alterar o sistema de arquivo sem
autorização.

## Passo 3. Ler os dados sem os estragar

Antes de qualquer gráfico:

1. **Declarar a base de cálculo e o tamanho da amostra ao lado de cada número.** Sem isto, uma percentagem convincente sai de uma amostra sem valor.
2. **Mediana, não média** — a distribuição é enviesada por virais. Se reportares média, reporta a mediana ao lado.
3. **Nunca somar alcance** ⬤ — não desduplica pessoas; a soma não significa nada. E ⬤ o alcance da Meta é **amostrado**: variações pequenas entre semanas podem ser ruído.
4. **Não comparar taxas entre plataformas.** As fórmulas medem coisas diferentes com o mesmo nome. Comparar cada plataforma **consigo mesma ao longo do tempo**.
5. ⬤ **Séries que atravessam 21 de abril de 2025** misturam impressões/reproduções com visualizações no Instagram. Declarar a quebra ou cortar a série.
6. **Separar alcance de seguidores de alcance de não-seguidores.** É a distinção que diz se a conta está a crescer ou a falar para os mesmos. Se a exportação não a der, dizê-lo.
7. **Alcance total a subir com alcance mediano por peça a descer não é melhoria** — é mais volume.
8. **Agrupar por tema, formato e faixa horária.** Nunca analisar peça a peça: é o erro central da área.
9. **Padrão só conta a partir de três observações.** 1 = nota, 2 = hipótese, 3+ = hipótese de trabalho. ◐ É prática defensável e não método estatístico — reduz o risco de confundir ruído com padrão, não o elimina (módulo 07).
10. **Sinalizar problemas de qualidade** — colunas em falta, intervalos estranhos, dias sem dados — em vez de contornar em silêncio.

**Atribuição:** ◑ uma experiência controlada encontrou tráfego de WhatsApp e vários outros canais sociais classificado como “direto”; é uma medição datada, não regra universal. **Concluir que o social não traz visitas a partir do tráfego direto é ler os dados ao contrário.** Triangular três vias — UTM, código ou link dedicado, e “como nos conheceu?” no momento do pedido — e **comparar, não somar: a discrepância é o dado**. UTM sempre em minúsculas, e nunca em links internos. TikTok está `LOOK INTO`.

## Passo 4. O painel

Um painel só é útil se cada bloco existir para sustentar uma decisão. **Não incluir blocos que não terminam em decisão.** ◐ Prática, sem estudo por trás: manter a primeira vista abaixo de uma dezena de números. O que está ancorado no módulo 07 é o modo de falha, não o teto — **medir tudo o que a plataforma oferece produz paralisia, não decisões**. Se um número da primeira vista não corresponde a um indicador da secção 2 do perfil, sai.

Vista de topo: métrica-norte do perfil (secção 2) face ao **alvo fixado antes** · alcance mediano por peça · alcance de não-seguidores · taxa pela fórmula da secção 12 · peças publicadas e **número de semanas com publicação** · conversas iniciadas ou pedidos.

Depois, por grupo e não por peça: desempenho por **pilar**, por **formato**, e por faixa horária se houver volume que o justifique. Quadrantes úteis, alcance × interação: muito alcance e pouca interação (chegou a quem não interessa) · pouco alcance e muita interação (assunto certo, distribuição fraca) · e os dois extremos.

**Negócio elegível com atendimento presencial:** secção própria com o Google Business Profile. Usar os termos de pesquisa e interações que a exportação atual realmente trouxer; se se classificar procura por marca vs. categoria, declarar a regra manual e não a apresentar como métrica nativa. Resto em `references/12`. PLAT-012 e PLAT-013.

**Entrega:** tabela markdown por defeito. Se a superfície suportar artefacto interativo e o volume o justificar, painel HTML com os mesmos blocos — nunca em vez do texto das decisões. **Gráficos bonitos que terminam sem uma decisão são desperdício de tempo.**

**Acessibilidade — obrigatória, e é a primeira coisa que desaparece com pressa:**

- **Nenhum gráfico sem a tabela de números por baixo.** Quem usa leitor de ecrã não lê um gráfico; e a tabela é também o que permite verificar a conta.
- **Texto alternativo em cada gráfico**, com a leitura e não a descrição: o que o gráfico mostra, não que é um gráfico de barras.
- **Contraste mínimo de 4,5:1** para texto e para números; 3:1 para elementos gráficos e limites de área. Verificar, não presumir.
- **Nunca codificar informação só por cor** — subida e descida levam sinal ou seta, não só verde e vermelho. Um painel que só se lê a cores não se lê em daltonismo nem impresso a preto e branco.

## Passo 5. O relatório que gera decisões

Estrutura, quatro tempos por secção e exemplo: módulo 07, secção *Relatório que gera decisões*, e o esqueleto preenchível em `assets/relatorio-mensal-modelo.md`. Aqui fica só o que é execução:

- A **Situação** de cada secção sai do alvo fixado na secção 2 do perfil, não do que aconteceu. Sem alvo escrito antes, não há secção — há narrativa.
- Cada secção **termina numa frase no formato ação + quantidade + prazo + responsável**. O responsável é uma pessoa nomeada do perfil (secção 8, quem aprova o quê), nunca "a equipa" nem um nome inventado.
- Se uma secção não consegue produzir essa frase, ou faltam dados ou a secção não devia estar no relatório.
- **Abrir com impacto de negócio, não com taxa de interação.**
- Comparar sempre com o mês anterior **e** com o mesmo mês do ano anterior — sem isso, a sazonalidade lê-se como desempenho.
- **No máximo três decisões.** Um relatório que propõe oito não muda nada.

Fechar com: **o que não foi possível verificar**, e **as aprendizagens a devolver à secção 11 do perfil** (hipótese, resultado, decisão, data, vezes observado).

## Regras

- **Português europeu.** Sem gerúndio de ação em curso, sem "você", sem vocabulário do Brasil.
- **Nunca inventar uma métrica que não está na exportação.** Se falta, diz-se que falta.
- **Nunca citar um benchmark sem amostra verificada** (módulo 11). Nem aplicar números de perfis de influenciador a uma conta de marca.
- **Nunca decidir com um post.** Nunca mudar o denominador da taxa a meio do ano.
- **Nunca prometer medição de retorno que a estrutura do negócio não permite.** Se a venda acontece ao balcão e não há inquérito de origem, não há atribuição — dizê-lo é mais profissional do que apresentar um número inventado.
- **Decisões de sair de uma plataforma são trimestrais e humanas.** Recomendar, sim; decidir, não.
- **Correlação não é causa.** Um pico coincidente com uma mudança não a prova.
- **Nunca propor iscos de interação como resposta a uma taxa em queda.** ⬤ No Facebook, "marca três amigos", "comenta X para receber" e "partilha para ganhar" correspondem ao *engagement bait* documentado, e a reincidência pode afetar a Página inteira; PLAT-007. Não extrapolar essa penalização específica para Instagram. Otimizar a métrica até ela deixar de significar o que significava é o modo de falha clássico de quem lê um painel (módulos 07 e 10).
- **As exportações e os relatórios contêm dados pessoais.** Respostas ao "como nos conheceu?", nomes em conversas, capturas de Insights com identificadores de quem interagiu. Não colar nomes, moradas, telefones nem capturas por tapar dentro do relatório; agregar, e tapar tudo o que identifique. Módulo 10, secção RGPD.
- **Não exportar nem tratar dados de plataforma através de serviços de terceiros** sem o dono da conta saber o que foi ligado a quê. Uma ligação de conveniência é uma decisão de tratamento de dados.
- Se a análise pedir replanear, passar a `matriz-de-conteudo` ou ao calendário — não replanear aqui de improviso.
- Não resumir esta skill ao utilizador. Executá-la.
