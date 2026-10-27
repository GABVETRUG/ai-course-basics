#!/usr/bin/env bash
# Esegue due script SQL in due sessioni concorrenti nel container Oracle.
# Il primo parte subito, il secondo dopo un ritardo (predefinito 3 secondi);
# alla fine stampa l'output di entrambi.
# Uso: CONN=hr/<password>@localhost/FREEPDB1 ./esegui_due_sessioni.sh primo.sql secondo.sql [ritardo]
set -euo pipefail

CONTAINER="${CONTAINER:-ora}"
CONN="${CONN:?Imposta CONN, per esempio CONN=hr/<password>@localhost/FREEPDB1}"
primo="$1"
secondo="$2"
ritardo="${3:-3}"

for f in "$primo" "$secondo"; do
  docker cp "$f" "$CONTAINER:/tmp/$(basename "$f")"
done

out_primo="$(mktemp)"
trap 'rm -f "$out_primo"' EXIT

docker exec "$CONTAINER" sqlplus -s "$CONN" "@/tmp/$(basename "$primo")" > "$out_primo" 2>&1 &
pid=$!
sleep "$ritardo"

echo "=== $(basename "$secondo") ==="
docker exec "$CONTAINER" sqlplus -s "$CONN" "@/tmp/$(basename "$secondo")" 2>&1

wait "$pid"
echo "=== $(basename "$primo") ==="
cat "$out_primo"
