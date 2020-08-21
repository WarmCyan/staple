""" Represents a node in the graph (objective, project, goal, etc.) """


class Node:
    def __init__(self, name=""):
        self.id = None # auto assign??
        self.name = name
        self.description = ""
        self.activations = []
        self.type = ""
        self.children = []
        # TODO: add the different modality times
        self.time = 0.0
        self.time_hist = []
        self.new_time = 0.0  # this is for activations that have not yet been resolved?
        self.completed = None
        self.deadline = None

        self.activation_applied = False  # this is used by Graph to determine if it has grabbed time from all of its children yet or not

    def add_activation(self, node, weight):
        """ Adds a connection FROM this node TO the passed node with given weight in [0, 1] """

        self.activations.append((node, weight))
        node.children.append(self)

    def get_connection_weight(self, node):
        """ Return the weight of the connection between this node TO the node passed """
        for activation in self.activations:
            if activation[0] == node:
                return activation[1]

    def activate(self):
        """ Update new_time from children's new_time. (Propagate's up from leaves) Pseudo-recursive """
        if not self.activation_applied:
            for child in self.children:
                child.activate()
                self.new_time += child.new_time * child.get_connection_weight(self)
            self.activation_applied = True

    def serialize(self):

        cereal_activations = []
        for activation in self.activations:
            cereal_activations.append((activation[0].id, activation[1]))
            
        cereal_children = []
        for child in self.children:
            cereal_children.append(child.id)
        
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "activations": cereal_activations,
            "type": self.type,
            "children": cereal_children,
            "time": self.time,
            "time_hist": self.time_hist,
            "new_time": self.new_time,
            "completed": self.completed,
            "deadline": self.deadline,
        }

    def load(self, dictionary):
        self.id = dictionary["id"]
        self.name = dictionary["name"]
        self.description = dictionary["description"]
        self.type = dictionary["type"]
        self.time = dictionary["time"]
        self.time_hist = dictionary["time_hist"]
        self.new_time = dictionary["new_time"]
        self.completed = dictionary["completed"]
        self.deadline = dictionary["deadline"]

