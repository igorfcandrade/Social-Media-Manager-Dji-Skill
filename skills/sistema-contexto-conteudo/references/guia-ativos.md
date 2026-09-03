# Guia de boas práticas — ATIVOS.md

## Propósito

Manter um inventário canónico de fotografias, vídeos, áudio, ilustrações, logótipos, fontes e modelos disponíveis. Permite saber rapidamente o que existe, se representa corretamente a oferta, em que formatos pode ser usado e se os direitos e consentimentos estão documentados.

## Informação obrigatória

- Responsável pelo inventário, estado, última verificação e próxima revisão.
- Um identificador estável e único por ativo.
- Caminho ou localização controlada; nunca depender apenas de uma descrição informal.
- Tipo, conteúdo representado, produto/ocasião associados e data de criação.
- Autor/criador, titular e base de utilização: próprio, licenciado, cedido ou outro.
- Prova de licença ou consentimento, respetivo âmbito, territórios, canais e validade.
- Pessoas identificáveis, menores, conteúdo de clientes e autorizações aplicáveis.
- Música, fontes, marcas ou obras de terceiros presentes no ativo.
- Estado de utilização: aprovado, restrito, bloqueado ou expirado.
- Características técnicas úteis: formato, dimensões, orientação, duração e qualidade.
- Recursos de acessibilidade disponíveis: texto alternativo, legendas e transcrição.
- Restrições, derivados e relação com o ficheiro original.

Não guardar dados pessoais desnecessários. Referenciar a prova de consentimento num local protegido, em vez de a copiar para o inventário.

## Atualização

- Registar o ativo quando entra no sistema, não apenas quando uma campanha precisa dele.
- Atualizar após edição, recorte, mudança de licença, retirada de consentimento ou criação de derivados.
- Rever direitos, validade e adequação antes de cada reutilização.
- Bloquear imediatamente um ativo quando a autorização é incerta, expira ou é retirada.
- Preservar o histórico: um derivado recebe ID próprio e aponta para o original.

## Anti-padrões

- Assumir que um ficheiro pode ser usado porque está numa pasta da marca.
- Usar conteúdo de clientes ou pessoas identificáveis sem prova de autorização.
- Confundir autoria com titularidade ou licença de utilização.
- Registar “sem direitos” ou “royalty-free” sem âmbito e fonte.
- Ignorar música, fontes, embalagens, obras ou marcas visíveis.
- Reutilizar um ativo expirado porque já foi publicado antes.
- Criar várias versões sem relação com o original.
- Aprovar um ativo cuja imagem já não corresponde ao produto real.

## Perguntas de validação

1. Quem criou o ativo e quem detém os direitos relevantes?
2. Onde está a prova de licença ou consentimento?
3. Em que canais, territórios e período pode ser utilizado?
4. Existem pessoas identificáveis, menores ou conteúdo de clientes?
5. Há música, fontes, marcas ou outras obras de terceiros?
6. O ativo ainda representa corretamente o produto, serviço ou equipa?
7. Tem qualidade e enquadramento adequados aos formatos pretendidos?
8. Existem texto alternativo, legendas ou transcrição quando necessários?
9. O estado deve ser aprovado, restrito, bloqueado ou expirado?

## Esquema Markdown/YAML conciso

~~~yaml
---
document_type: inventario-ativos
brand: ""
owner: ""
status: draft # draft | validated | deprecated
last_verified: YYYY-MM-DD
review_due: YYYY-MM-DD
protected_evidence_location: ""
---
~~~

~~~markdown
# Inventário de ativos

## [ASSET-0001] — [nome curto]
- Localização:
- Tipo: fotografia | vídeo | áudio | ilustração | logótipo | fonte | modelo | outro
- Conteúdo/produto/ocasião:
- Criado em:
- Autor:
- Titular:
- Base de utilização:
- Prova de direitos/consentimento:
- Âmbito, canais e territórios:
- Válido até:
- Pessoas identificáveis/menores:
- Elementos de terceiros:
- Estado: approved | restricted | blocked | expired
- Restrições:
- Formato/dimensões/duração/orientação:
- Texto alternativo:
- Legendas/transcrição:
- Original/derivados:
- Última verificação:

## Por confirmar
- [Ativo · questão · responsável · data prevista]

## Registo de alterações
- YYYY-MM-DD — [alteração e responsável]
~~~
