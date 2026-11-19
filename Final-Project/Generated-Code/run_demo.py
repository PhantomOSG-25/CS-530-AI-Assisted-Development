"""Run the final CS-530 classifier verification sequence."""

import CS530_neuron as c


def main():
    data = c.create_synthetic_data_set()
    step_weights = c.calculate_weights("step", data)
    sigmoid_weights = c.calculate_weights("sigmoid", data)

    print("synthetic_data_set=", data)
    print("step_weights=", step_weights)
    print("sigmoid_weights=", sigmoid_weights)
    print("step_predictions=", c.binary_classifier(data, step_weights, "step"))
    print("sigmoid_predictions=", c.binary_classifier(data, sigmoid_weights, "sigmoid"))


if __name__ == "__main__":
    main()
