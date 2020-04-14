input_data = {"region": {
    "name": "Africa",
    "avgAge": 19.7,
    "avgDailyIncomeInUSD": 5,
    "avgDailyIncomePopulation": 0.71
    },
    "periodType": "days",
    "timeToElapse": 58,
    "reportedCases": 674,
    "population": 66622705,
    "totalHospitalBeds": 1380614,
    }


class Impact:
    # Determining Impact of infection
    def __init__(self, reportedCase):
        self.reportedCase = reportedCase

    def currentlyInfected(self):
        # Calculate currentlyInfected value for impact effect
        value_infected = self.reportedCase * 10

        return (value_infected)


class SevereImpact:
    """Determining Impact of infection"""    
    def __init__(self, reportedCase):
        self.reportedCase = reportedCase

    def currentlyInfected(self):
        """Calculate currentlyInfected value for severeImpact effect"""
        severe_value = self.reportedCase * 50

        return (severe_value)


data_in = input_data["reportedCases"]
calcForImpact = Impact(data_in)
print("Input data is " + str(calcForImpact.reportedCase) + ".")
valueImpact = calcForImpact.currentlyInfected()
# print(calcForImpact)

calcForSevere = SevereImpact(data_in)
print("Input data is " + str(calcForSevere.reportedCase) + ".")
valueSevere = calcForSevere.currentlyInfected()
# print(calcForSevere)

factors = 2 ** 9


class InfectionsByRequestedTime:
    """Modelling infectiousByRequestedTime"""
    def __init__(self, factor):
        "Initialize name and age attribute"""
        self.factor = factor

    def forImpact(self):
        """Calculate infection Impact"""
        self.output_val = valueImpact * self.factor

        return (self.output_val)

    def forSevere(self):
        """Calculate infection's severeImpact"""
        self.output_val_sev = valueSevere * self.factor
        return (self.output_val_sev)


infeBRTs = InfectionsByRequestedTime(factors)
print("Factor value is " + str(infeBRTs.factor) + ".")
calcValueForIm = infeBRTs.forImpact()
# print(calcValueForIm)

calcValueForSev = infeBRTs.forSevere()
# print(calcValueForSev)

# currentlyInfected = mymi.Impact.currentlyInfected
# severe = myms.SevereImpact.currentlyInfected


# InfectionBRT = covi.InfectionsByRequestedTime.forImpact
# forBRTs = covi.InfectionsByRequestedTime.forSevere

# creating instance of the class Impact
# dni = mymi.Impact.currentlyInfected(report)
# creating instance of the class SvereImpact


def estimator():

    impact = {
        'CurrentlyInfectedPeople': valueImpact,
        'InfectionsRequestedByTime': calcValueForIm
        }

    severeImpact = {
        'currentlyInfectedPeople': valueSevere,
        'infectionsRequestedByTime': calcValueForSev
        }
    data = {'Data': input_data, 'Impact': impact, 'SevereImpact': severeImpact}

    return data


toEstimate = estimator()
print(toEstimate)