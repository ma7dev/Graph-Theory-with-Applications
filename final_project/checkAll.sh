#!/bin/bash
echo "Selected algorithm is $1"

echo "##################################"
###
echo "Examples:"

for f in $(eval echo "{1..3}")
do
    echo "      Processing $f"
    python3 tsp-verifier.py data/tsp_example_"$f".txt data/tsp_example_"$f".txt.tour
done
echo "##################################"

###
echo "Test:"

for f in $(eval echo "{1..7}")
do
    echo "      Processing $f"
    python3 tsp-verifier.py data/test-input-"$f".txt data/test-input-"$f".txt.tour
done
