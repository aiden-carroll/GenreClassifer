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
