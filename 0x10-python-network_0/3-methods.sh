#!/bin/bash
# Requests allowed methods
curl -X GET -X OPTIONS $1 -si | grep 'Allow:' | cut -d ' ' -f2,3,4
