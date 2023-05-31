###
# Author: Tanner Krone
# Description:
#     Simple and singular neuron implementation. Made as an
#     exploratory project.
from Neuron import Neuron

def default_evaluation(features, weights, biases):
    net_i = 0
    for i in range(len(features)):
        net_i += weights[i]*features[i] - biases[i]
    out_i = 1/(1+pow(2.71828, -net_i)) #TODO Use library for euler's number

    return out_i

if __name__ == '__main__':
    neuron = Neuron(default_evaluation)

