""" A collection of nodes. Should always be a DAG. """


class Graph:
    def __init__(self):
        self.nodes = []

    def apply_plan(self, plan):
        activities = plan.calculate_activity_totals()
        for activity in activities:
            for node in self.nodes:
                if node == activity.node:
                    node.time += activity.time_total
