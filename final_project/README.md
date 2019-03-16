# Travel Saleman Problem

## To the run the program

```
python3 main.py [algorithm] [input_file] [time]
```

* algorithm = **knn** for K-Nearest Neighbor or **ga** for Genetic Algorithm.
* input_file = the position where the input file is at (e.g. **data/tsp_example_1.txt** if the tsp_example_1.txt in data folder, or **tsp_example_1.txt** if the tsp_example_1.txt at the same level as main.py).
* time(optional) = set the time to stop the program, if no argument passed, then the program will stop at 5 minutes.

## Expected Results
The optimal tour Lengths are the values stated in the project description.

### KNN

* tsp_example 1:108159
    * Time: 0.04567408561706543
    * Length: 130921
* tsp_example 2: 2579 
    * Time: 1.8191642761230469
    * Length: 2975
* tsp_example 3: 1573084
    * Time: 309.187805891037
    * Length: 1936941

**For full credit:**

* Test case 1 <= 6600
    * Time: 0.014127969741821289
    * Length: 5911
* Test case 2 <= 9200
    * Time: 0.11811113357543945
    * Length: 8011
* Test case 3 <= 15000
    * Time: 1.3867180347442627
    * Length: 14826
* Test case 4 <= 21400
    * Time: 12.897594213485718
    * Length: 19711 
* Test case 5 <= 30100
    * Time: 123.83275985717773
    * Length: 27128
* Test case 6 <= 42800
    * Time: 299.0716700553894
    * Length: 39834
* Test case 7 <= 67000
    * Time: 299.6045079231262
    * Length: 62110

### GA
* tsp_example 1:108159
    * Time: 18.386559009552002
    * Length: 337541
* tsp_example 2: 2579 
    * Time: 41.28453016281128
    * Length: 27639
* tsp_example 3: 1573084
    * Time: 299.0136749744415
    * Length: 1934200

**For full credit:**

* Test case 1 <= 6600
    * Time: 14.512681007385254
    * Length: 10488.71
* Test case 2 <= 9200
    * Time: 18.30189299583435
    * Length: 32837
* Test case 3 <= 15000
    * Time: 34.44625997543335
    * Length: 103387
* Test case 4 <= 21400
    * Time: 73.32604813575745
    * Length: 220727
* Test case 5 <= 30100
    * Time: 200.42861986160278
    * Length: 465770
* Test case 6 <= 42800
    * Time: 299.00313663482666
    * Length: 39834
*  Test case 7 <= 67000
    * Time: 299.00823521614075
    * Length: 62110

For tsp_example 3 you may use up to 15 minutes