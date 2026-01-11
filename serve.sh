#!/bin/bash
# Simple HTTP server for the vaccine dashboard
# Usage: ./serve.sh [port]

PORT=${1:-8080}
DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Starting server at http://localhost:$PORT"
echo "Press Ctrl+C to stop"
echo ""

cd "$DIR"
python3 -m http.server $PORT
