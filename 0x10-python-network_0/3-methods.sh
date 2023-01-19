#!/bin/bash
#sending a curl request
curl -I -s OPTIONS $1 | grep Allow | awk '{for (i=2; i<NF; i++) printf $i " "; print $NF}'
