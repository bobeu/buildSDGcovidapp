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

severeCasesByRequestedTime = calcValueForSev * 0.15


def hospitalBedByRequestedTime():
    tABed = input_data["totalHospitalBeds"]
    actualAHosBeds = int(tABed - (tABed * (65 / 100)))
    if(actualAHosBeds > severeCasesByRequestedTime):
        val = int(actualAHosBeds - severeCasesByRequestedTime)
        msg_1 = "There is more beds of amount "

        return (msg_1 + str(val))

    elif(actualAHosBeds < severeCasesByRequestedTime):
        val_2 = int(severeCasesByRequestedTime - actualAHosBeds)
        msg_2 = "There is shortage of beds of "

        return (msg_2 + str(val_2))
    else:
        print("There is enough beds to admit patient")


class SevereCasesByRequestedTime():

    def infRBTForImpact(self):
        reqHospToRec = int(calcValueForIm * 0.15)

        return reqHospToRec

    def infRBTForSevere(self):
        reqHospToRec = int(calcValueForSev * 0.15)

        return reqHospToRec


di = SevereCasesByRequestedTime()
valueSevereIm = di.infRBTForImpact()
valueSevereSev = di.infRBTForSevere()


def estimator():

    impact = {
        'CurrentlyInfectedPeople': valueImpact,
        'InfectionsRequestedByTime': calcValueForIm,
        }

    severeImpact = {
        'currentlyInfectedPeople': valueSevere,
        'infectionsRequestedByTime': calcValueForSev,
        }

    severeCBRTime = {
        'valueSevereImpact': valueSevereIm,
        'valueSevereSev': valueSevereSev,
        }

    hospBedReqByTime = hospitalBedByRequestedTime()

    data = {
        'Data': input_data,
        'Impact': impact,
        'SevereImpact': severeImpact,
        'severeCasesByRequestedTime': severeCBRTime,
        'severeCasesRequestedByTime': severeCasesByRequestedTime,
        'hospitalBedByRequestTime': hospBedReqByTime,
        }

    return data


toEstimate = estimator()
print(toEstimate)