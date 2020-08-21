""" A collection of nodes. Should always be a DAG. """

import json
from staple.node import Node

class Graph:
    def __init__(self):
        self.name = ""
        self.nodes = []

    def apply_plan(self, plan):
        """ Adds all of the planned activity times to each relevant node's new_time """
        activities = plan.calculate_activity_totals()
        for activity in activities:
            for node in self.nodes:
                if node == activity.node:
                    node.new_time += activity.time_total

    # def find_leaves(self):
    #     leaves = []
    #     for node in self.nodes:
    #         if len(nodes.children) == 0:
    #             leaves.append(children)

    def resolve_activations(self):
        """ Run activations to propagate leaf new times up all the way throughout graph. """
        for node in self.nodes:
            node.activation_applied = False

        for node in self.nodes:
            node.activate()

        # TODO: technically can probably go in loop above?
        for node in self.nodes:
            node.time += node.new_time
            node.new_time = 0
                    
    def node_names(self):
        """ Just return an array of node names """
        return [node.name for node in self.nodes]


    def save(self, path):
        node_cereal = []
        for node in self.nodes:
            node_cereal.append(node.serialize())

        cereal = {"name": self.name, "nodes": node_cereal}
            
        with open(path, 'w') as outfile:
            json.dump(node_cereal, outfile)
    
    def load(self, path):
        self.nodes = []
        with open(path, 'r') as infile:
            info = json.load(infile)

        self.name = info["name"]
        
        for node_info in info["nodes"]:
            node = Node()
            node.load(node_info)
            self.nodes.append(node)
        
