""" Represents a node in the graph (objective, project, goal, etc.) """


class Node:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.activations = []
        # TODO: add the different modality times
        self.time = 0.0
        self.time_hist = []
        self.completed = None
        self.deadline = None
