#!/usr/bin/env bash
# Instala as skills deste repositório nos ambientes locais detetados.
# Correr sempre que houver alterações: ./instalar.sh
#
# Instala em ~/.claude/skills e em ~/.codex/skills, mas SÓ nos que já existem:
# criar a pasta de um ambiente que não está instalado nesta máquina seria
# inventar um destino. Se nenhum existir, avisa e não falha.
#
# Só toca nas skills que vêm deste repositório. As outras — a PJM, por
# exemplo — ficam onde estão.
set -euo pipefail

ORIGEM="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/skills"

# ambiente:raiz. A pasta de skills é sempre <raiz>/skills.
AMBIENTES=(
  "Claude:$HOME/.claude"
  "Codex:$HOME/.codex"
)

instalados=0

for entrada in "${AMBIENTES[@]}"; do
  nome_ambiente="${entrada%%:*}"
  raiz="${entrada#*:}"
  destino="$raiz/skills"

  if [ ! -d "$raiz" ]; then
    printf "· %s não está instalado nesta máquina (%s) — ignorado\n\n" "$nome_ambiente" "$raiz"
    continue
  fi

  mkdir -p "$destino"
  echo "A instalar de $ORIGEM para $destino  ($nome_ambiente)"
  echo

  for pasta in "$ORIGEM"/*/; do
    nome="$(basename "$pasta")"
    rm -rf "${destino:?}/$nome"
    cp -R "$pasta" "$destino/$nome"
    linhas=$(find "$destino/$nome" -name '*.md' -exec cat {} + | wc -l | tr -d ' ')
    printf "  ✓ %-26s %s linhas\n" "$nome" "$linhas"
  done

  echo
  instalados=$((instalados + 1))
done

if [ "$instalados" -eq 0 ]; then
  echo "Nenhum ambiente local detetado. Nada instalado." >&2
  exit 0
fi

echo "Feito em $instalados ambiente(s). Reinicia a sessão para as skills novas serem reconhecidas."
echo "As skills que não vêm deste repositório — a PJM, por exemplo — não são tocadas."
echo "Para confirmar: python3 scripts/validar_instalacoes.py"
