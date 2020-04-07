#!/usr/bin/env bash
# This script prints out Content-Length of a curl HTTP request
curl -so /dev/null $1 -w %{size_download}
