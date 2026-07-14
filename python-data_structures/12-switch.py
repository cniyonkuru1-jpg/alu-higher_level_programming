#!/usr/bin/env bash
a=10
b=89
a=$((a+b)); b=$((a-b)); a=$((a-b))
echo "a=$a - b=$b"
