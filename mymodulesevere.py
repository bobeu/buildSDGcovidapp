multiplied = 50

class SevereImpact:
    """Determining Impact of infection"""
    def __init__ (self, y):
        self.y = y

    def currentlyInfected(self):
        """Calculate currentlyInfected value for severeImpact effect"""
        currentlyinfectedPeople = self.y * multiplied

        return currentlyinfectedPeople

