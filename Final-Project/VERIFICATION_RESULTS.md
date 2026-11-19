# Final Project Verification Results

The generated classifier was tested through the same sequence required by the Module 9 functional requirements.

## Test Sequence

1. Create the synthetic data set.
2. Calculate weights with the step activation function.
3. Calculate weights with the sigmoid activation function.
4. Run the binary classifier using the step weights.
5. Run the binary classifier using the sigmoid weights.

## Recorded Final Results

### Step weights

```text
[0.08999999999999986, 0.06, -0.6300000000000003]
```

### Sigmoid weights

```text
[0.6634598031162788, 0.6147952771284224, -5.589951868342394]
```

### Step classifier predictions

```text
[0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
```

### Sigmoid classifier predictions

```text
[0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
```

The final Copilot run reported that all required functions completed successfully.
