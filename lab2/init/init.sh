#!/bin/sh
set -eu

mkdir -p /data

if [ ! -f /data/counter.txt ]; then
  echo "0" > /data/counter.txt
fi

if [ ! -f /data/app.log ]; then
  : > /data/app.log
fi

echo "[init] data initialized"
