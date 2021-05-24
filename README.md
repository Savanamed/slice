## SLiCE (Savana's SampLe size Calculator for Evaluations)

### What is SLiCE for?
SLiCE enables users to estimate the minimum sample size required to obtain robust metrics of performance where robustness is determined by pre-defining confidence intervals (CI) widths and levels. The method has been designed assuming that the metrics to perform the evaluation are the standard metrics for IE in evaluations in NLP, namely: Precision (P), Recall (R) and F1-score.

### Installation of SLiCE (working for LINUX and WINDOWS)

1. Open your favorite python IDE (e.g. PyCharm)
2. Clone the SLiCE library by executing the below command in the terminal
```bash
# https
git clone https://github.com/Savanamed/slice.git     
```
3. Create virtual environment as described here: https://python-poetry.org/docs/managing-environments/
4. Activate venv
4. Install the library
```bash
# change directory to /slice
cd /your/path/to/slice
poetry install
```

### SLiCE parameters
```python
    parser = ArgumentParser(description="Input parameters for SLiCE")
    parser.add_argument("--precision", type=float, default=0.80, required=False, dest="precision")
    parser.add_argument("--recall", type=float, default=0.85, required=False, dest="recall")
    parser.add_argument(
        "--frequency", type=float, default=0.3, required=False, dest="frequency"
        )
    parser.add_argument("--alpha", type=float, default=0.05, required=False, dest="alpha")
    parser.add_argument("--interval-width", type=float, default=0.05, required=False, dest="interval_width")
    parser.add_argument("--int_freq", type=bool, default=True, required=False, dest="int_freq")
```
### How to use SLiCE? ###
### LINUX

```python
# default parameters
cd /slice/scr/slice
python slice.py 
# with custom parameters
cd /slice/scr/slice
python slice.py  --precision 0.95 --recall 0.7 --frequency-rate 0.6 --alpha 0.05  --interval-width 0.05 --int_freq True
```

### SLiCE output
```python
Selected parameter values:
|-----------|--------|-----------|-------|----------------|----------|
|--precision|--recall|--frequency|--alpha|--interval-width|--int_freq|
|====================================================================|
|0.8        |0.85    |0.3        |0.05   |0.05            |True      |
|-----------|--------|-----------|-------|----------------|----------|

The results of SLiCE based on the selected parameter values:
|-----|--------------|--------------|-----|-----|-----|-----|
|Total|Total positive|Total negative|TP   |FP   |TN   |FN   |
|===========================================================|
|883  |265           |618           |212  |53   |581  |37   |
|-----|--------------|--------------|-----|-----|-----|-----|

```

### SLiCE result explanation
    total: Sum of total_positive and total_negative
    total_positive: Classified as belonging to a class
    total_negative: Classified as not belonging to a class
    true_positive: Correctly classified as belonging to your class
    true_negative: Correctly classified as not belonging to your class
    false_positive: Incorrectly classified as belonging to your class
    false_negative: Incorrectly classified as not belonging to your class


This project is licensed under the terms of the MIT license.