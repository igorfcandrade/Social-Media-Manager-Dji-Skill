# Preparação técnica e entrega

Esta referência e `scripts/validar_entrega.py` aplicam-se à entrega de **cortes fotográficos**.
Para auditoria incremental, vídeos, relatório, aprovações e catálogo central, ler
[auditoria da sessão](auditoria-sessao.md). Não executar o verificador de cortes como se
validasse uma auditoria sem derivados ou a qualidade de vídeo/áudio.

Quando houver master editado aprovado, guardar o seu ID/versão e o vínculo ao original. A fonte
imediata de cada corte deve ser identificada; adaptar o registo/verificação ao catálogo real,
sem atribuir ao RAW coordenadas de uma edição diferente. Web e redes sociais recebem derivados
independentes do original/master, com canal/finalidade registados; não encadear compressões.

## Originais e cor

Trabalhar numa pasta temporária separada. Não escrever previews, perfis ou EXIF sobre os originais.

- JPEG/PNG/TIFF: abrir com um descodificador adequado, respeitar orientação EXIF e manter o perfil ICC. Escolher coordenadas **depois** de orientar. Exportar JPEG de alta qualidade, sem sharpening. A compressão JPEG inerente à entrega não é uma cópia intacta; só `originais` é byte a byte.
- RAW: inspecionar dimensões, orientação, data, espaço de cor e imagens incorporadas com ExifTool. Preferir o JPEG de **resolução completa** produzido pela câmara quando existir e representar a aparência recebida; declarar o método. `JpgFromRaw` pode ser extraído com `exiftool -b -JpgFromRaw ficheiro.CR3 > trabalho/camara.jpg`. Verificar as dimensões reais do JPEG; uma miniatura/PreviewImage pequena não equivale ao original completo.
- A orientação do RAW pode não acompanhar o JPEG extraído. Ler o código EXIF e aplicar a transformação correspondente, incluindo espelhamento quando necessário. Não assumir que toda a fotografia é vertical nem repetir a rotação se já vier aplicada.
- Se o JPEG da câmara declarar sRGB e não trouxer ICC, pode incorporar o perfil sRGB correspondente sem transformar os pixels. Não atribuir sRGB a Adobe RGB/P3 ou a um espaço desconhecido. Não comparar imagens ignorando os respetivos perfis.
- Sem uma renderização integral fiel utilizável, não iniciar um desenvolvimento RAW que mude a aparência silenciosamente. Procurar a exportação correspondente fornecida; se faltar, explicar a limitação e pedir uma exportação de resolução completa com o aspeto pretendido ou autorização para desenvolver o RAW. Preservar entretanto todos os RAW.
- HEIC ou formatos não suportados: converter apenas uma cópia de trabalho com ferramenta que respeite orientação e perfil, sem melhoria automática. Distinguir conversão técnica de tratamento criativo; se houver HDR e uma conversão SDR necessária, explicar o efeito e não alegar identidade de aparência sem verificação.

Criar uma folha de contacto dos originais orientados. Para enquadrar, podem usar-se grelhas de coordenadas nas previews de trabalho, nunca nos JPG finais. As coordenadas de cada formato partem da imagem integral. Limitar a redução à dimensão preferencial; jamais aumentar.

## Esquema de catálogo compatível com o verificador

O catálogo de cada artigo/variação tem este núcleo. Os dados abaixo são **um exemplo de estrutura**, não um produto real. Acrescentar os campos editoriais necessários sem alterar os nomes do núcleo:

```json
{
  "schema": 1,
  "marca": "Nome recebido no contexto",
  "sessao": "AAAA-MM-DD-Sessao-Tema",
  "data_sessao": "AAAA-MM-DD",
  "produto_principal": "Nome confirmado",
  "variacao": "Valor confirmado ou null",
  "identificacao_site": {
    "nome_recebido": "Nome do ficheiro sem numeração",
    "nome_ficha": "Título visível",
    "url": "URL real da ficha consultada",
    "verificado_em": "AAAA-MM-DD",
    "estado": "confirmado | parcialmente confirmado | por confirmar | não aplicável",
    "atributo": "Nome real do seletor",
    "valor_variacao": "Valor real ou null",
    "evidencia": "Observação curta que sustenta a associação"
  },
  "originais": [
    {
      "id": "sha256:HASH_REAL",
      "ficheiro": "originais/Nome Original.CR3",
      "origem_recebida": "/caminho/real/Nome Original.CR3",
      "sha256": "HASH_REAL",
      "data_camera": "DATA_EXIF",
      "largura_ficheiro": 6240,
      "altura_ficheiro": 4160,
      "orientacao_exif": 8,
      "produto_secundario": "Base visível; modelo por confirmar",
      "conjunto_comercial": "não confirmado",
      "descricao_visual": "Descrição feita pelo assistente",
      "etiquetas_sugeridas": ["ambiente", "Natal"],
      "estado": "preservado; não publicado"
    }
  ],
  "derivados": [
    {
      "ordem": 1,
      "titulo": "Plano aberto",
      "formato": "1x1",
      "ficheiro": "1x1/nome-variacao_1x1_1.jpg",
      "fonte": "originais/Nome Original.CR3",
      "fonte_id": "sha256:HASH_REAL",
      "renderizacao": "Método real de leitura/renderização",
      "dimensoes_fonte_orientada": [4160, 6240],
      "corte_xyxy": [170, 1650, 3770, 5250],
      "dimensoes_corte": [3600, 3600],
      "dimensoes_entrega": [1080, 1080],
      "ampliacao": false,
      "sha256": "HASH_REAL_DO_JPG",
      "estado": "exportado; não publicado"
    }
  ],
  "limitacoes": [],
  "revisao_visual": {
    "realizada": true,
    "observacoes": "Registar apenas verificações realmente feitas."
  }
}
```

A data de análise, o responsável e a próxima revisão podem ficar ao nível da sessão. Guardar a proveniência dos dados; classificações visuais são sugestões até confirmação. Não copiar preços/stock/prazos para a biblioteca. Para uma base identificada no site, guardar também a sua URL; não atribuir um modelo só por semelhança.

Originais com nomes iguais e conteúdo diferente podem usar `originais/proveniencia-1/Nome.CR3`; o catálogo aponta para a localização real. Se houver JPEG inicialmente enviados que não alimentam os novos cortes, preservá-los e mostrá-los numa secção de arquivo da galeria; não inventar uma ligação a RAW por ordem de ficheiro.

## Galeria e verificação

Criar HTML local com uma linha por número, original integral e três cortes, dimensões e nome da fonte. As imagens devem aparecer completas nos seus quadros (`object-fit: contain`), sem outro corte feito pelo CSS. Permitir ampliar. Incluir uma indicação explícita para cortes omitidos ou menores. A galeria tem ligações relativas para funcionar após extrair o ZIP; previews de RAW podem ser incorporadas no HTML. Uma folha de comparação JPG é um complemento útil.

O helper requer Python 3 e Pillow, disponível no ambiente ou instalado num ambiente virtual de trabalho. Não fixar na skill caminhos de ambientes temporários de uma sessão antiga.

O núcleo usa `formatos` opcional, por exemplo `{"1x1": [1080, 1080], "3x4": [1080, 1440], "9x16": [1080, 1920]}`, e `maximo_por_formato` (6 por defeito). Não obriga a preencher seis vistas. O CSV usa UTF-8, separador `;` e colunas `ordem;formato;ficheiro;original;dimensoes`; pode acrescentar campos editoriais, derivados do JSON. As dimensões podem escrever-se `1080 × 1080`.

```bash
python3 scripts/validar_entrega.py /caminho/para/pacote-da-peca --received /caminho/para/lote-recebido
python3 scripts/validar_entrega.py /caminho/para/pacote-da-peca \
  --zip /caminho/para/AAAA-MM-DD-Peca.zip \
  --prefix AAAA/MM-MES/AAAA-MM-DD-Sessao-Tema/Nome-Variacao
```

O verificador confere hashes, nomes, fontes, proporções, dimensões, limites das caixas, ausência de ampliação, coerência CSV/JSON e presença dos links da galeria. `--received` confere a completude contra as entradas exatas; sem essa lista, o script avisa que só conhece o inventário preservado. Com `--zip`, cria e compara cada ficheiro do arquivo por hash; `--check-zip ficheiro.zip --prefix caminho/interno` confere um ZIP existente sem o alterar. Recusa substituir um ZIP existente; usar `--replace-zip` **apenas para atualizar a entrega correspondente a uma revisão pedida**, depois de conferir o destino. Não usar para sobrescrever outro lote.

O verificador lê as dimensões reais das fontes descodificáveis. Em RAW não descodificado, não comprova a resolução da imagem incorporada nem a fidelidade da renderização: emite aviso para conferir com ExifTool/descodificador e inspeção visual. A existência de links também não comprova a ordem visual ou o funcionamento do zoom; abrir a galeria extraída e rever separadamente.

Uma dimensão abaixo da preferencial ou corte omitido tem de declarar a limitação concreta e, quando a resolveria, a fotografia adicional necessária. Menos de seis vistas pode ser uma seleção suficiente; explicar a seleção sem inventar uma falta. Nem a contagem nem o verificador decidem se uma composição é boa.

Na revisão final, verificar visualmente: plano aberto com peça/base completas; espaço para composição posterior quando previsto; mesma vista em cada linha; detalhes úteis sem repetição; Stories sem o assunto encostado ao topo/rodapé; nenhuma mudança de cor/luz. Atualizar o catálogo só com verificações feitas.
