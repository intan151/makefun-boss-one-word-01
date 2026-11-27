#!/bin/bash
# Retry `gh repo create` every 5 minutes until it succeeds (GitHub rate limit
# "created too many repositories, too quickly"). Ops file only - NOT committed.
set -euo pipefail
REPO="intan151/makefun-boss-one-word-01"
while true; do
  if gh repo create "$REPO" --public --description "One Word for the Boss — make.fun entry: one word for the boss. Built by an AI agent for make.fun's bounty." --homepage "https://make.fun/c/u-swift-badger-44-one-word-for-the-boss-6b48c735" 2>&1; then
    echo "REPO CREATED: $REPO"
    exit 0
  fi
  echo "create failed, retrying in 5 minutes..."
  sleep 300
done
