#!/usr/bin/env bash
# Esegue uno script SQL nel container Oracle e ne mostra l'output.
# Uso: CONN=hr/<password>@localhost/FREEPDB1 ./esegui.sh percorso/script.sql
set -euo pipefail

CONTAINER="${CONTAINER:-ora}"
CONN="${CONN:?Imposta CONN, per esempio CONN=hr/<password>@localhost/FREEPDB1}"
script="$1"

docker cp "$script" "$CONTAINER:/tmp/$(basename "$script")"
docker exec -i -e NLS_LANG=AMERICAN_AMERICA.AL32UTF8 "$CONTAINER" \
  sqlplus -s "$CONN" "@/tmp/$(basename "$script")" < /dev/null
