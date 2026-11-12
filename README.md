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
Go to the repository <a href="https://github.com/mdeff/fma">https://github.com/mdeff/fma</a>
Download the fma_metadata.zip
Move features.csv to data/fma folder
Move genres.csv to data/fma folder
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

We are starting with:

$$L = \frac{1}{N}\sum_i -\log p_{i,\,y_i}$$

subject to change into:

$$L = \frac{\sum_i w_{y_i},\bigl(-\log p_{i,\,y_i}\bigr)}{\sum_i w_{y_i}}$$

where weights are calculated:

$$w_c = \frac{N}{K \cdot n_c}$$

### Optimization

For now the optimization follows a simple gradient descent

#### One varible example

In the function: $f(x) = (x-3)^2$

the gradient is: $f'(x) = 2(x-3)$

so we find the local minima: $x=3$

#### We apply this to the loss function

In the loss function: $$L = \frac{1}{N}\sum_i -\log p_{i,\,y_i}$$

Using PyTorch's `loss.backwards()` function we break the function down for us and find its gradiant (internally using the chain rule).
