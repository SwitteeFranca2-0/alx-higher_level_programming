#!/usr/bin/bash
curl -o /dev/null -s -w "%{http_code}\n" $1
