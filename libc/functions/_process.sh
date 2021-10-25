#!/bin/sh

echo "# Functions"
echo ""

for i in `find . -name "*.md" | sort`; do

	name=`echo $i | awk -F/ '{ print $3 }'`
	ext=`echo $name | awk -F. '{ print $2 }'`
	fun=`echo $name | awk -F. '{ print $1 }'`

	if [ "X$ext" ==  "Xmd" ]; then
		echo '[`'$fun'`]('$i'),'
	fi
	
	if [ "X$ext" ==  "Ximpl" ]; then
		echo '[`'$fun'`]('$i'),'
	fi
	
	if [ "X$ext" ==  "Xpart-impl" ]; then
		echo '[`'$fun'`]('$i'),'
	fi

done