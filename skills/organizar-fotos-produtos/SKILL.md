---
name: organizar-fotos-produtos
description: "Audita sessões de fotografias e vídeos de produtos: identifica novos materiais e duplicados, avalia qualidade, atualiza o catálogo central e propõe seleção e utilizações. Prepara cortes, galeria e ZIP quando autorizados. Usa ao receber uma nova sessão ou pedir auditoria/preparação do acervo; não publica nem monitoriza pastas."
---

# Organizar sessões de fotografias de produtos

Executar o modo pedido com os dados disponíveis. Aplicar
`../social-media-manager/references/contexto-do-caso.md`; não fixar marca, domínio, catálogo,
raiz do acervo, assistente ou editor. A skill de contexto fornece o método geral de inventário;
esta audita a sessão, atualiza o catálogo comum e prepara as entregas autorizadas. Usar o
catálogo existente quando disponível.

## Modos e autorização

Em cada nova sessão, começar pela auditoria incremental descrita em
[auditoria da sessão](references/auditoria-sessao.md). Não repetir análise integral de ativos
inalterados já revistos, nem interpretar “automática por sessão” como vigilância de uma pasta.

- **Auditar:** inventariar, preservar, analisar fotos/vídeos, comparar com o catálogo, guardar
  relatório e propor seleção/usos. Um pedido só de auditoria termina aqui, sem produzir conteúdo.
- **Preparar:** usar a seleção e o âmbito aprovados para criar os cortes e entregas abaixo.
  Se o pedido já define materiais e pede expressamente a preparação, aproveitar essa autorização,
  fazer a auditoria necessária e executar sem nova ronda de aprovação. “Organizar uma nova
  sessão” sem seleção/produção definida entrega primeiro a auditoria para revisão.

Registar separadamente identidade, seleção, produção e publicação aprovadas. Havendo decisões
em falta, apresentar a seleção concreta por IDs e as dúvidas; não uma aprovação em branco.

## 1. Contexto e identificação

Ler as fontes do caso sobre identidade visual, catálogo, organização e exportação. Aproveitar
nome recebido no pedido/ficheiros/pastas; não pedir regras já definidas. Se faltarem imagens
ou localização acessível, pedir apenas essa entrada antes de executar a preparação.

Consultar a ficha no website oficial indicado no contexto para conferir nome, categoria,
variações e acabamentos: abrir a página e opções, não confirmar só pelo resultado de pesquisa,
título SEO ou URL. Registar nome recebido, confirmado, variação, fonte, data e evidência.

Se o endereço não estiver identificado, perguntar pelo website, se existir, e continuar as
operações independentes. Marca sem website, produto ainda não publicado ou acesso indisponível
não impedem organizar o lote: manter a identidade fornecida e a confirmação no site pendente
ou não aplicável. Não inventar SKU, material, medidas, nome ou variação por semelhança.
Perguntar apenas por correspondências ambíguas ou informação indispensável.

Distinguir no catálogo produto principal, elementos/produtos secundários, tipo de fotografia
e conjunto comercial. A peça sobre uma base não prova venda em conjunto. Descrições e relações
vivem no catálogo, não precisam de ser ditadas pelo utilizador nem caber no nome do ficheiro.

## 2. Sessão e originais

Usar a raiz e convenções do caso. Sem convenção, propor este padrão para o lote solicitado:

```text
[raiz]/AAAA/MM-MES/AAAA-MM-DD-Sessao-Tema/Nome-do-Artigo-Variacao/
  originais/
  1x1/
  3x4/
  9x16/
  catalogo.json
  catalogo.csv
  galeria-comparacao.html
```

Separar artigo/variação quando necessário; omitir repetição do tema. Usar data indicada,
senão consultar a captação. Guardar separadamente data da sessão, da câmara e da exportação;
não corrigir divergências em silêncio. Acrescentar só o lote pedido.

Guardar em `originais` cópias byte a byte de todos os ficheiros recebidos, com nomes e
formatos intactos, incluindo RAW/JPEG emparelhados. Não mover, substituir ou apagar a origem.
Inventariar as entradas antes de selecionar, comparar com o catálogo e verificar hashes após copiar.
Distinguir duplicados exatos de imagens semelhantes; não eliminar nem fundir por semelhança. Nomes iguais com
conteúdos diferentes usam subpastas de proveniência, sem sobrescrita.

Nos derivados: `nome-do-artigo-variacao_formato_numero.jpg`, minúsculas e hífen entre
palavras, numeração desde 1. Omitir variação quando não se aplicar. Preservar IDs do catálogo
existente; usar hash de conteúdo como identidade técnica quando ainda não houver ID.

## 3. Selecionar e compor — produção autorizada

Por defeito, preparar até seis imagens úteis por formato, quando o material o permitir:
1×1 a 1080×1080, 3×4 a 1080×1440 e 9×16 a 1080×1920. São preferências de produção,
configuráveis pelo caso; não requisitos universais de plataforma.

Começar por plano aberto com a peça inteira, base relevante e ambiente. Alternar vistas e
detalhes úteis sem preencher contagens com repetições. Cada número identifica a mesma vista
nos formatos; se um corte faltar, conservar a lacuna e explicar, não trocar a vista.

Compor cada formato visualmente a partir do original ou da renderização integral fiel.
Não gerar um formato a partir de outro derivado, nem aplicar corte central a todo o lote.
Um original pode alimentar vistas distintas, identificadas por número e descrição.

Na primeira imagem, centrar visualmente o conjunto principal com a base. Se o modelo posterior
tiver barra, rodapé ou título, reservar fundo real na zona adequada sem esconder a peça/base.
A margem depende da composição; não copiar uma margem fixa para todas as imagens.
Entregar fotografia limpa, sem aplicar essa barra ou texto.

Nos Stories, deixar o assunto importante afastado dos limites ocupados pela interface,
confirmando o destino quando necessário. Um detalhe pode excluir outras partes deliberadamente;
não amputar o próprio detalhe. Rever grelha e ampliações à resolução de entrega.

## 4. Fidelidade

Só orientar, cortar realmente e reduzir quando necessário. Sem pedido explícito, não ampliar,
regenerar, estender fundo, criar margens, retocar, filtrar, alterar exposição/cor/nitidez
ou acrescentar elementos. JPEG reencodificado não é original intacto.

Ler [preparação e entrega](references/preparacao-e-entrega.md) para RAW, orientação e cor,
esquema de catálogo e verificação. Usar processamento determinístico para os cortes reais
explicitamente pedidos. Não substituir por geração de imagem.

No RAW, verificar imagem incorporada integral e resolução efetiva; miniatura não basta.
Identificar método e fonte da renderização. Se for preciso desenvolver e alterar a aparência,
explicar antes e obter a decisão necessária. Preservar o RAW entretanto.

Sem resolução suficiente, entregar menor com proporção correta e dimensão identificada.
Sem enquadramento útil, omitir e indicar a fotografia adicional concreta que o resolveria.
Não forçar seis imagens nem disfarçar limites com uma nota genérica.

Conservar as camadas original → master editado aprovado (se existir) → derivados. Não criar
um master corrigido por defeito. Fazer exportações web e redes sociais independentes a partir
do original/master; não reutilizar automaticamente a versão comprimida para website.
Verificar o estado de cópias independentes nos destinos acessíveis, como na referência de
auditoria; uma pasta ou ZIP no mesmo disco não comprovam backup.

## 5. Catálogo e galeria

Usar o catálogo canónico; se não existir, JSON é o registo completo e CSV o índice derivado.
Quando o catálogo central já existir, os ficheiros do pacote são exportações datadas com IDs
e origem declarada, não uma segunda fonte editável. A atualização incremental faz parte da
auditoria: preservar IDs, versões, sugestões, decisões e histórico; reler/verificar a gravação.
Sem catálogo, criar um índice mínimo no acervo autorizado. Sem acesso de escrita, entregar a
alteração proposta e declarar a atualização central pendente. Não simular que foi guardada.

Guardar o relatório da sessão com seleção, qualidade, duplicados, lacunas, oportunidades,
cobertura da análise de vídeo, estado das cópias e próximos passos. A auditoria usa uma galeria
de revisão dos originais/excertos; a galeria comparativa abaixo só existe após preparar cortes.

Registar localização/ID, sessão e datas, original, produto/variação e elementos secundários,
confirmação no site, descrição visual, tipo de plano, sugestões de etiquetas, relação
original–derivados, ordem, formato, caixa do corte, dimensões, limitações e utilização.
Separar factos confirmados, observações e sugestões. Não marcar publicação sem evidência.

Galeria: uma linha por vista na ordem proposta de publicação:
**original integral → 1×1 → 3×4 → 9×16**.
Mostrar nomes/fontes, dimensões, cortes ausentes e limitações; permitir ampliar. Imagens
integrais com `object-fit: contain`, links relativos que funcionem depois de extrair o ZIP.
Mostrar todos os originais, incluindo os não selecionados; identificar previews de RAW.
Para vários artigos, criar um índice da sessão que ligue os pacotes.

## 6. Verificar e entregar

Na entrega de cortes fotográficos, executar `scripts/validar_entrega.py` sobre o esquema da referência ou adaptar a verificação
ao catálogo existente sem o migrar à força. Conferir originais contra entradas, nomes,
proporções, dimensões, ausência de ampliação, correspondência de vistas e conteúdo do ZIP.
Inspecionar visualmente cortes, detalhes, cor e espaço de capa. Testes estruturais não
comprovam composição, identidade comercial nem direitos.

Na auditoria, entregar relatório, seleção visual e atualização do catálogo, identificando
aprovações pendentes. Não exigir cortes ou ZIP de produção para concluir só a auditoria.
Na produção, entregar pasta, galeria e ZIP com a mesma versão, contagens e limitações relevantes.
Passar às skills de conteúdo apenas os IDs/versões aprovados, fontes de qualidade, excertos,
destinos e regras; guardar a relação com os derivados para evitar reanalisar tudo.
Em correções, atualizar só cortes afetados e respetivos registos, CSV, galeria e ZIP;
conferir hashes dos originais e cortes não afetados. Não sobrescrever outro lote.
Registar o ponteiro e o estado no inventário central, preservando os registos existentes.

O resultado é preparação local para revisão. Upload, publicação, agendamento e montagem
gráfica da capa são etapas próprias, executadas apenas quando pedidas.
