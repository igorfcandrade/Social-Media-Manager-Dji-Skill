# Guia — `CONTEXTO-MANIFESTO.md`

## Propósito

Ser a primeira leitura da skill. Declara onde vive cada fonte canónica, quem a mantém e até quando é considerada atual. Resolve duplicados, nomes alternativos e referências ambíguas.

## Informação obrigatória

- raiz canónica do projeto;
- tabela de documentos com caminho relativo, âmbito, responsável, estado, última verificação e próxima revisão;
- aliases e cópias obsoletas que não devem ser usadas;
- precedência por domínio;
- ordem de leitura por tipo de tarefa;
- ações que exigem autorização atual do utilizador;
- convenção para `POR_CONFIRMAR`, exemplos e decisões pendentes.

## Atualização

Atualizar quando um ficheiro é criado, renomeado, movido, substituído ou muda de responsável. Rever trimestralmente mesmo sem alterações.

## Não deve conter

- preços, stock, prazos ou métricas;
- copy de marca;
- credenciais;
- uma autorização permanente para publicar, usar APIs ou pesquisar.

## Esquema recomendado

```markdown
---
schema_version: 1
document_status: validated
owner: NOME
last_verified: YYYY-MM-DD
review_due: YYYY-MM-DD
canonical_root: CAMINHO
---

# Manifesto de contexto

## Fontes canónicas
| domínio | ficheiro | responsável | estado | verificado | rever até |
|---|---|---|---|---|---|

## Aliases e fontes obsoletas
| caminho | substituído por | motivo |
|---|---|---|

## Ordem de leitura por tarefa

## Regras de conflito e atualidade

## Ações que exigem autorização no pedido atual

## Por confirmar

## Registo de alterações
```

## Perguntas de validação

- Há dois ficheiros com o mesmo nome ou âmbito?
- Cada domínio tem uma única fonte canónica?
- Os caminhos existem e são relativos à raiz declarada?
- Alguma fonte passou da data de revisão?
- O manifesto repete factos que deveriam viver noutro documento?
