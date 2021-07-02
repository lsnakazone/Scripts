#!/bin/bash

cat result.json | jq -r '.subdomains' | tr -d \",[]" " | grep "\S"  > filtered.txt
echo $domain > securitytrails.txt

while read line; do
        echo $line.$domain >> securitytrails.txt
done < filtered.txt


