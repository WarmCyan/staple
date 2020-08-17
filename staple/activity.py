""" A record or time allotment towards a particular node. """


class Activity:
    def __init__(self, node):
        self.node = node
        self.time_total = 0.0
        self.time_thinking = 0.0
        self.time_learning = 0.0
        self.time_acting = 0.0
        self.percent_total = None
        # TODO: are below percent of this? Yes, right?
        self.percent_thinking = None
        self.percent_learning = None
        self.percent_acting = None
