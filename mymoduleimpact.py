class Impact:
    """Determining Impact of infection"""
    def __init__ (self, x):
    #     """Initializing attribute for reportCases"""
        self.x = x

    def currentlyInfected(self):
        """Calculate currentlyInfected value for impact effect"""
        currentlyinfectedPeople = self.x * 10

        return currentlyinfectedPeople

