#!/bin/bash
echo "Selected algorithm is $1"

if [ -n "$2" ]
then
    echo "Selected time is $2"	
fi
echo "##################################"
###
echo "Examples:"

for f in $(eval echo "{1..3}")
do
    echo "Processing $f"
    python3 main.py $1 data/tsp_example_"$f".txt $2
done
echo "##################################"

###
echo "Test:"

for f in $(eval echo "{1..7}")
do
    echo "Processing $f"
    python3 main.py $1 data/test-input-"$f".txt $2
done
