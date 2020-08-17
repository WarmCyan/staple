""" A collection of nodes. Should always be a DAG. """


class Graph:
    def __init__(self):
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
                    
