"""
Simple artificial neuron implementation. Utilizes a default sigmoid
transfer function. Allows for a variable number of features customizable
evaluation function.

Based on diagram found here: https://www.baeldung.com/cs/neural-networks-neurons
"""
class Neuron:
    def __init__(self, weights=[], features=[], target=10, biases = [], evalFunc=evaluation):
        self.weights = weights
        self.features = features  # Single feature in this example
        self.target = target
        self.biases = biases
        self.evalFunc = evaluation

    def set_weights(self, weight):
        self.weight = weight

    def set_features(self, feature):
        self.feature = feature

    def set_biases(self, biases):
        self.biases = biases

    def add_feature(self, feature, weight, bias):
        self.weights += weight
        self.features += feature
        self.biases += bias

    def set_target(self, target):
        self.target = target

    def get_output(self):
        return self.evalFunc(self.features, self.weights, self.biases)


def evaluation(features, weights, biases):
    net_i = 0
    for i in range(len(features)):
        net_i += weights[i]*features[i] - biases[i]
    out_i = 1/(1+pow(2.71828, -net_i)) #TODO Use library for euler's number

    return out_i



