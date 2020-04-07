#!/bin/bash
# Advanced task 7
curl $1 -si | grep 'HTTP/1.0' | cut -d ' ' -f2
