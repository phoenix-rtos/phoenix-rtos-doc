#!/bin/sh

for i in `cat ./files`; do
	
	if [ -f $i.md ]; then
		echo '[`'$i-'`]('$i.md'), '
	fi
	if [ -f $i.impl.md ]; then
		echo '[`'$i'`]('$i.impl.md'), '
	fi
	if [ -f $i.part-impl.md ]; then
		echo '[`'$i+'`]('$i.part-impl.md'), '
	fi
		if [ -f $i.tb-impl.md ]; then
		echo '[`'$i-+'`]('$i.tb-impl.md'), '
	fi
	
done