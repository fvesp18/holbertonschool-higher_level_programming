#!/bin/bash
# Advanced task 7
curl -so /dev/null -w "%{http_code}\n" $1
