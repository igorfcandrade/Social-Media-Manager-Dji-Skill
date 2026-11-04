# Auditoria incremental de uma sessão

Usar ao receber uma nova sessão de fotografias ou vídeos. É uma execução a pedido, não um
monitor de pasta. O método funciona sem website ou APIs de redes sociais; depende de acesso
real ao lote e ao inventário. Sem acesso, identificar o limite e não simular uma auditoria.

## 1. Comparar com o catálogo antes de analisar

Localizar a fonte canónica do acervo pelo contexto, sem pressupor base de dados ou formato.
Pode ser uma tabela, JSON, base de dados ou índice que aponta para registos de lotes. Manter
um único dono editável de cada registo; relatórios, CSV e pacotes são vistas datadas.

- Inventariar todos os ficheiros do lote: caminho, nome, tipo, bytes, hash de conteúdo e ID
  existente, dimensões/orientação, data EXIF e perfis quando disponíveis. Em vídeo, duração,
  resolução, rotação, taxa de fotogramas e pistas de áudio. Não inferir dados ausentes.
- Comparar hashes e IDs com o catálogo e dentro do lote. Mesmo nome não prova duplicado;
  nomes diferentes podem ter conteúdo idêntico. Registar onde e quanto do acervo foi comparado.
- Classificar como novo, já conhecido e inalterado, nova localização de um conteúdo existente,
  ficheiro alterado/nova versão, ou sem acesso suficiente para comparar. Data/tamanho ajudam
  a triagem, mas não comprovam identidade de conteúdo.
- Reutilizar a análise técnica/visual de conteúdo inalterado com a mesma versão do método.
  Não a repetir integralmente a cada sessão. Reabrir quando a análise anterior for incompleta,
  o destino exigir outro detalhe ou houver dúvida concreta. Rever factos comerciais, aprovações
  e condições de utilização quando necessário; hash igual não os mantém atuais para sempre.
- Preservar IDs estáveis e versões: alteração de bytes atualiza a versão/hash ou cria um registo
  ligado ao anterior, conforme o catálogo. Não apagar o histórico nem substituir decisões humanas.

Sem catálogo, criar um índice mínimo no acervo autorizado, registando a localização no contexto.
Não exigir migração ou aplicação nova. Se não houver acesso de escrita, entregar a atualização
proposta e indicar que a gravação central ficou pendente; não alegar que foi realizada.

## 2. Duplicados exatos e semelhanças

Hash igual identifica duplicação exata de bytes. Referenciar o mesmo conteúdo com as suas
localizações, conservando a proveniência. Preservar os ficheiros recebidos; não apagar, mover
ou substituir nada para “limpar” o acervo.

Fotografias semelhantes, rajadas, recortes, reexportações e pares RAW/JPEG não são duplicados
exatos. Pode usar miniaturas ou assinaturas visuais como triagem, seguida de inspeção. Registar
“semelhante” ou “possível derivado”, com confiança e motivos; não fundir identidades só com
uma pontuação automática. Comparar foco, expressão, luz e espaço de corte para recomendar
qual usar. Declinar uma imagem para a seleção não autoriza eliminá-la.

## 3. Análise útil de fotografias e vídeos

Nas fotografias, avaliar foco/nitidez do assunto, movimento involuntário, exposição, reflexos,
cor relativamente às referências disponíveis, fundo, composição, cortes, resolução e espaço
para texto quando previsto. Não afirmar fidelidade física da cor sem referência do produto.
Distinguir defeito técnico de característica intencional, como profundidade de campo curta.

Nos vídeos, abrir o ficheiro e avaliar movimento/estabilidade, foco ao longo do plano, luz,
orientação, enquadramento, início/fim e duração útil. Ouvir o áudio quando relevante e acessível;
registar ruído, inteligibilidade ou ausência de som. Se não foi ouvido, marcar por verificar.

Para clipes curtos, preferir reprodução integral; para longos, amostrar de forma proporcional,
identificando intervalos analisados. Fotogramas isolados não comprovam estabilidade, movimento
ou qualidade de som. Registar cobertura e limitações, bem como excertos úteis com início/fim
no ficheiro original. Não editar vídeo durante uma auditoria; encaminhar excertos aprovados
para a etapa de produção solicitada.

Confirmar produto/variação na fonte da marca quando possível. Cores visíveis são observações;
nomes comerciais, materiais e composição exigem a fonte ou confirmação do utilizador.

## 4. Relatório da sessão e seleção

Guardar `relatorio-sessao.md` (ou equivalente do projeto), ligado à sessão e aos IDs dos ativos,
e uma galeria/folha de contacto de revisão. O relatório contém:

1. Âmbito, data da análise, localização, ferramentas/método e cobertura efetivamente verificada.
2. Contagens de novos, inalterados, alterados, duplicados exatos, semelhantes e não analisados.
3. Seleção recomendada com miniaturas/IDs, razão de escolha e alternativas; sem apagar rejeitados.
4. Problemas técnicos concretos e limitações por fotografia ou intervalo de vídeo.
5. Classificações propostas: produto principal/secundário, variação, tipo de plano, ocasião e
   etiquetas. Separar o confirmado, observado e por confirmar.
6. Oportunidades de utilização por ativo/excerto: publicação, carrossel, Story, Reel, site ou
   outro uso coerente com o contexto. Não prometer desempenho por aparência apenas.
7. Planos em falta, descrevendo a captação necessária: assunto, ângulo, distância, orientação,
   margem ou movimento. Não pedir uma nova sessão inteira se bastar um plano.
8. Estado das cópias independentes, limitações da verificação e decisões necessárias.
9. Referência à atualização do catálogo: destino, versão/data e o que foi realmente gravado.

Apresentar escolhas concretas para confirmar identidade/cores/materiais ainda incertos, seleção
por IDs e conteúdos/destinos a produzir. Não pedir aprovação genérica sem mostrar a seleção.
Aprovação visual, factual, de produção e de publicação são estados separados; aceitação técnica
não aprova materiais nem direitos por inferência. Aproveitar aprovações já dadas no âmbito exato.

## 5. Catálogo e passagem para produção

Atualizar o catálogo central após auditar, mesmo que a seleção ainda aguarde resposta: guardar
observações como sugestões, método/versão, hash analisado, data e estado de revisão. Preservar
registos e utilizações anteriores. Reler antes de gravar; se houver versão concorrente, integrar
apenas as alterações deste lote. Reabrir a gravação e confirmar IDs/localizações resolúveis.

Após aprovação, registar quem aprovou, quando, que IDs/versões e para que conteúdos/destinos.
Só o âmbito aprovado passa às skills de produção. Se a preparação já foi explicitamente
solicitada com materiais/seleção definidos, registar essa autorização e executar sem repetir
uma pergunta. Pedido só de auditoria termina no relatório; silêncio não é aprovação.

A passagem inclui IDs e caminhos de originais/masters aprovados, excertos com tempos, identidade
confirmada, usos autorizados, regras visuais, proporções, espaço de capa, restrições e lacunas.
Não envia só uma descrição que obrigue a nova análise completa. Registar derivados e respetivos
vínculos ao terminar. Publicação só se regista após confirmação real, com canal/data/URL quando
existirem. Métricas futuras ligam-se à publicação e período; não exigem ligar APIs nesta etapa.

## 6. Camadas de ficheiros e cópias de segurança

- Original: tal como recebido, intacto, mesmo depois de carregar versões no website.
- Master editado: apenas quando uma edição foi pedida e aprovada; manter boa qualidade,
  versão, histórico e ligação ao original. Não criar masters corrigidos por defeito.
- Derivados: exportações independentes por canal, a partir do original ou master aprovado.
  Separar destinos web e redes sociais no catálogo e, quando ambos existirem, nas pastas.

Não usar a versão comprimida para website como fonte habitual de Instagram/Facebook ou de
outros derivados. O otimizador web continua a tratar a sua finalidade; não é preciso substituí-lo.
Se só houver ficheiros do website, identificá-los como fonte recuperada e avaliar dimensão e
qualidade. Pode verificar a existência do upload original no CMS quando houver acesso e pedido;
não prometer recuperar resolução ou metadados perdidos.

Verificar as cópias nos destinos conhecidos/acessíveis e registar evidência/data. Duas pastas
ou um ZIP no mesmo disco não comprovam backup independente. Recomendar uma cópia independente
e uma fora do equipamento principal quando faltarem, distinguindo recomendado de verificado.
Sem acesso aos destinos, estado “não verificado”. Não instalar sincronização, copiar para cloud
ou declarar restauração testada sem execução/autorização próprias. Falta de backup não bloqueia
uma auditoria ou preparação local que preserve os originais.
