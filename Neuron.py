class Neuron:
    def __init__(self, weight=3, feature=0, target=10):
        self.weight = weight
        self.feature = feature  # Single feature in this example
        self.target = target
        self.evalFunc = evaluation

    def set_weight(self, weight):
        self.weight = weight

    def set_feature(self, feature):
        self.feature = feature

    def set_target(self, target):
        self.target = target

    def get_output(self):
        return self.evalFunc(self.feature, self.weight)


def evaluation(feature, weight):
    return feature*weight



