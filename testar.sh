#!/usr/bin/env bash
# Ponto de entrada portátil: humano, Codex, Claude, outro LLM ou GitHub Actions.
set -uo pipefail

RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
estado=0

executar() {
  if ! "$@"; then
    estado=1
  fi
}

cd "$RAIZ"

# Corre primeiro para que, quando devida, a mensagem contratual seja a primeira linha.
# A função executar regista a falha e continua, por isso os testes estruturais não ficam ocultos.
executar python3 skills/social-media-manager/scripts/verificar_revisao.py
executar python3 scripts/validar_repositorio.py
executar python3 scripts/validar_estado_plataformas.py
executar python3 scripts/validar_instalacoes.py
executar python3 -m unittest discover -s tests -p 'test_*.py'
executar bash -n testar.sh instalar.sh
executar git diff --check
executar git diff --cached --check

if [ "$estado" -ne 0 ]; then
  echo "Testes automáticos: FALHARAM" >&2
  exit 1
fi

echo "Testes automáticos: OK"
