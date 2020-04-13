import datainput as dt
import mymoduleimpact as mymi
import mymodulesevere as myms
import infectionsBRT as covi

# access to datainput
input_d = dt.input_data
# report = dt.input_data["reportedCases"]
# severe = myms.SevereImpact(report)

currentlyInfected = mymi.Impact.currentlyInfected
severe = myms.SevereImpact.currentlyInfected


InfectionBRT = covi.InfectionsByRequestedTime.forImpact
forBRTs = covi.InfectionsByRequestedTime.forSevere

# creating instance of the class Impact
# dni = mymi.Impact.currentlyInfected(report)
# creating instance of the class SvereImpact


def estimator():
      
    impact = [currentlyInfected, InfectionBRT]
    severeImpact = [severe, forBRTs]
    
    data = [input_d, impact, severeImpact]

  
    return data

toEstimate = estimator()
print(toEstimate)