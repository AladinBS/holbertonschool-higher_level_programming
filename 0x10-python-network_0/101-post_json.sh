#!/bin/bash
# Script
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
