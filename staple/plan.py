""" A possible collection of activities and subplans. """

from datetime import date

from staple import util
from staple.activity import Activity


class Plan:
    def __init__(self):
        self.start_date = None
        self.end_date = None
        self.plans = []
        self.activities = []

    def calculate_activity_totals(self):
        """ This resolves all activities and subplans and returns a set of activities with aggregated time totals. """

        # TODO: activity list class?
        final_activities = {}  # index by node

        for plan in self.plans:
            self.activities.extend(plan.calculate_activity_totals())

        for activity in self.activities:
            if activity.node not in final_activities:
                final_activities[activity.node] = Activity(activity.node)

            # resolve percentages if needed
            # TODO: might want to abstract this elsewhere
            if activity.percent_total is not None:
                activity.time_total = (
                    activity.percent_total
                    * util.day_count(self.start_date, self.end_date)
                ) * (
                    30 / 7
                )  # TODO: fix this constant

            final_activities[activity.node].time_total += activity.time_total
            # TODO: also add the other modality times

        return final_activities
