class Impact:
    """Determining Impact of infection"""
    def __init__ (self, x, y=10):
    #     """Initializing attribute for reportCases"""
        self.x = x
        self.y = y

    def currentlyInfected(self):
        """Calculate currentlyInfected value for impact effect"""
        currentlyinfectedPeople = self.x * self.y

        return currentlyinfectedPeople

