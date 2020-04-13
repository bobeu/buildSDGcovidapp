import mymoduleimpact as mymi
import mymodulesevere as myms
import datainput as dt

factor = 2 ** 9
inputdata = dt.input_data["reportedCases"]
currentlyInfected = mymi.Impact.currentlyInfected(inputdata)
currentlyInfected_sev = myms.SevereImpact.currentlyInfected(inputdata)

class InfectionsByRequestedTime:
    """Modelling infectiousByRequestedTime"""
    def __init__ (self, z):
        """Initialize name and age attribute"""
        self.z = z

    def forImpact(self):
        """Calculate infection Impact"""
        self.z = currentlyInfected
        calcForImpact = currentlyInfected * factor

        return calcForImpact

    def forSevere(self):
        """Calculate infection's severeImpact"""
        self.z = currentlyInfected_sev
        calForSevere = currentlyInfected_sev * factor
        
        return calForSevere



