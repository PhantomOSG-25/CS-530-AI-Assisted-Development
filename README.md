# CS-530 AI-Assisted Development

## Overview

This repository contains an academic project completed for **CS-530: AI Principles and Applications** at Southern New Hampshire University.

The project demonstrates an iterative AI-assisted software-development workflow using GitHub Copilot. Copilot was used to generate code from functional requirements, while I directed the prompts, reviewed the implementation, tested the results, and verified that the final program satisfied the required behavior.

## Project

The Python program implements a simple single-neuron binary classifier with four main functions:

- `neuron()` calculates a neuron output using a selected activation function.
- `binary_classifier()` applies the neuron to each row of a labeled data set.
- `create_synthetic_data_set()` creates a two-feature binary-classification data set.
- `calculate_weights()` trains weights for the selected activation function.

The neuron supports two activation functions:

- **Step**
- **Sigmoid**

## Testing and Verification

The final implementation was tested by:

1. Generating the synthetic data set.
2. Calculating weights with the step activation function.
3. Calculating weights with the sigmoid activation function.
4. Running the binary classifier with the step weights.
5. Running the binary classifier with the sigmoid weights.
6. Verifying that all required functions completed successfully.

Both activation paths produced matching binary predictions on the generated data set during the final test.

## Skills Demonstrated

- AI-assisted software development
- Prompt refinement
- Requirements interpretation
- Python
- Neural-network fundamentals
- Binary classification
- Step and sigmoid activation functions
- Testing and verification
- Human review of AI-generated code

## Responsible AI Use

This was an **AI-assisted academic project**. The generated code was not treated as automatically correct simply because it ran. The workflow included requirement checks, testing, prompt refinement, and human verification.

One of the strongest lessons from the course was that AI output still requires human understanding, testing, and accountability.

## Repository Contents

- `CS530_neuron.py` - Final generated and verified Python implementation.
- `README.md` - Project overview and documentation.

Course-provided code snippets, assignment documents, rubrics, and exported Copilot chat logs are intentionally not included.

## Author

**Michael B. Wood**  
B.S. Computer Science, Software Engineering concentration  
M.S. Artificial Intelligence student, Southern New Hampshire University
