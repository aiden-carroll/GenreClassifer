import numpy as np

# In future Loss function with weights should be calcuated with
# weight = total tracks / (# of classes * tracks in that class)
def calculate_function(data:np.array):
    loss: np.float32 = 0

    # Sum the negative nat log of the prediction here
    for vec in data:
        break

    try:
        return loss / data.shape[1]
    except ZeroDivisionError as e:
        print(f"Math error: {e}")
        return None