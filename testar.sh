#!/usr/bin/env bash
# Ponto de entrada portátil: humano, Codex, Claude, outro LLM ou GitHub Actions.
set -uo pipefail

RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
estado=0
verificar_instalacoes=1
if [ "${1:-}" = "--sem-instalacoes" ] && [ "$#" -eq 1 ]; then
  verificar_instalacoes=0
elif [ "$#" -ne 0 ]; then
  echo "Uso: ./testar.sh [--sem-instalacoes]" >&2
  exit 1
fi

executar() {
  if ! "$@"; then
    estado=1
  fi
}

cd "$RAIZ"

# Corre primeiro para que, quando devida, a mensagem contratual seja a primeira linha.
# Revisão vencida (2) é aviso; calendário inválido (1) continua a ser erro.
python3 skills/social-media-manager/scripts/verificar_revisao.py
revisao=$?
if [ "$revisao" -ne 0 ] && [ "$revisao" -ne 2 ]; then
  estado=1
fi
executar python3 scripts/validar_repositorio.py
executar python3 scripts/validar_estado_plataformas.py
if [ "$verificar_instalacoes" -eq 1 ]; then
  executar python3 scripts/validar_instalacoes.py
else
  echo "Instalações locais: não comparadas (validação de uma árvore isolada)"
fi
executar python3 -m unittest discover -s tests -p 'test_*.py'
executar bash -n testar.sh instalar.sh
executar git diff --check
executar git diff --cached --check

if [ "$estado" -ne 0 ]; then
  echo "Testes automáticos: FALHARAM" >&2
  exit 1
fi

echo "Testes automáticos: OK"
