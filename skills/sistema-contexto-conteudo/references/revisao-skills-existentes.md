# Revisão de skills de conteúdo existentes

## Âmbito

Auditoria por leitura das skills já usadas num projeto para voz, tema, calendário, posts, vídeo curto, métricas, atendimento e outras frentes de conteúdo. Este ficheiro regista padrões a corrigir; não é fonte factual da marca.

## Achados

- Verificar se as skills consultam apenas `MARCA.md` ou um ficheiro genérico de memória e ignoram catálogo, operações, perfil por canal, ativos, métricas ou conformidade.
- Detetar ficheiros agregadores que misturam envios, funil, campanhas, publicações e métricas sem um âmbito único nem caminho inequívoco.
- Procurar factos mutáveis dentro das próprias skills: portes, prazos, checkout, cadências, prioridade editorial, volume de oferta e conclusões sobre canais ou formatos.
- Confirmar se auditorias datadas estão a ser tratadas como contexto corrente sem revalidação.
- Verificar se direitos, publicidade identificada e acessibilidade têm uma fonte transversal clara.

## Risco

Uma skill pode aplicar corretamente o seu método e, ainda assim, produzir uma resposta errada porque o facto embutido envelheceu. Repetir o mesmo valor em várias skills também cria contradições difíceis de detetar.

## Migração recomendada

1. Substituir referências genéricas a `MEMORY.md` por caminhos declarados em `CONTEXTO-MANIFESTO.md`.
2. Mover prazos, portes, pagamento, checkout e capacidade para `OPERACOES.md` e `CONTEXTO-ATUAL.md`.
3. Mover estado, papel, público observado, formatos e cadência por canal para `PERFIL-SOCIAL.md`.
4. Mover resultados e conclusões de desempenho para `METRICAS-E-APRENDIZAGENS.md`, com período e confiança.
5. Mover inventário, música, UGC, consentimentos e validade para `ATIVOS.md`.
6. Centralizar publicidade, direitos, privacidade e acessibilidade em `CONFORMIDADE.md`.
7. Deixar em cada skill apenas critérios duráveis: estrutura do output, decisões de formato, gates e perguntas a fazer.
8. Antes de usar um valor, exigir fonte canónica, data de verificação e validade. Sem isso, perguntar ou omitir.

## Regra para futuras skills

Se um facto pode mudar sem que a lógica da tarefa mude, esse facto não pertence à skill. A skill deve dizer **onde o confirmar** e **o que fazer se estiver ausente ou expirado**.
