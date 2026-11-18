# GenreClassifer

## Setup (Linux)
```
git clone "https://github.com/aiden-carroll/GenreClassifer"
cd GenreClassifier
pip install virtualenv
virtualenv .venv
source .venv/bin/activate
.venv/bin/pip install -r requirements.txt
```
## Setup (Windows)
```
git clone "https://github.com/aiden-carroll/GenreClassifer"
cd GenreClassifier
pip install virtualenv
virtualenv .venv
./.venv/Scripts/activate
pip install -r requirements.txt
```

## Setup Training Data

<pre>
Download the <a href=https://os.unil.cloud.switch.ch/fma/fma_metadata.zip>fma_metadata.zip</a>
Unzip the folder to get the .csv files
Create a <b>data</b> subfolder inside the repo root
Create a <b>fma</b> subfolder inside the <b>data</b> folder
Move <b>features.csv</b> from the download to <b>data/fma</b> folder
Move <b>genres.csv</b> from the download to <b>data/fma</b> folder
Move <b>tracks.csv</b> from the download to <b>data/fma</b> folder
</pre>

## Resources
### Testing Library:
https://www.geeksforgeeks.org/python/unit-testing-python-unittest/

## Specifics

### Loss Function

#### Symbol meanings

| Symbol | Meaning |
|--------|---------|
|    N   | Number of tracks |
|   i    | Which track from 1 to N |
| $y_i$  | True genre of track given as id |
| $p_{i,\,y_i}$ | Probability of model to give matching true id |

#### Functions

We are using standard cross-entropy given from the following function:

$$L = \frac{1}{N}\sum_i -\log p_{i,\,y_i}$$

### Optimization

The optimization follows the Adam's algorithm

This uses a running count of squared gradients, dividing it by the square root. This lessens the gradient count to fit within a
32 bit float, while keeping or improving the accuracy

#### One varible example

In the function: $f(x) = (x-3)^2$

the gradient is: $f'(x) = 2(x-3)$

so we find the local minima: $x=3$

#### We apply this to the loss function

Using PyTorch's `loss.backwards()` function we break the function down for us and find its gradiant (internally using the chain rule).
