#!/bin/bash
if [ $# != 1 ];then
    echo "Invalid arguments. Argument 1 is contest name."
    exit 1
fi
mkdir -p $1
echo \# $(date "+%Y/%m/%d") > $1/${1,,}_a.py
echo \# $(date "+%Y/%m/%d") > $1/${1,,}_b.py
echo \# $(date "+%Y/%m/%d") > $1/${1,,}_c.py
echo \# $(date "+%Y/%m/%d") > $1/${1,,}_d.py
