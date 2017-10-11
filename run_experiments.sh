#!/bin/bash
echo "<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
echo "         START HERE"
echo ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>"

python mirapie.py toydata/ toydata/initL.csv -m 3 -p 1 >> results.txt 

echo "<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
echo "         FINISH!!!!"
echo ">>>>>>>>>>>>>>>>>>>>>>>>>>>>"
