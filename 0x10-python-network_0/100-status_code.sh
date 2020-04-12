#!/bin/bash
# Script
curl -so /dev/null -w "%{http_code}" "$1"
