#!/usr/bin/bash
curl -I  --silent $1 | grep Content-Length | awk '{print $2}'
