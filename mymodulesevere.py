class SevereImpact:
    """Determining Impact of infection"""
    def __init__ (self, x, y=50):
        self.x = x
        self.y = y

    def currentlyInfected(self):
        """Calculate currentlyInfected value for severeImpact effect"""
        currentlyinfectedPeople = self.x * self.y 

        return currentlyinfectedPeople

