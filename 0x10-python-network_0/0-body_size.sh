#!/bin/bash
#gettting the content length
curl -I  --silent $1 | grep Content-Length | awk '{print $2}'
