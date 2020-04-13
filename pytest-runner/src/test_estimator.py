import mymoduleimpact
import mymodulesevere
import infectionsBRT

def test_Impact():
    test_1 = mymoduleimpact.Impact.currentlyInfected(600)
    assert  test_1(600) == 6000
    assert  test_1(600, 20) == 12000

def test_severe():
    test_2 = mymodulesevere.SevereImpact.currentlyInfected(600)
    assert test_2(600) == 30000
    assert test_2(600, 5) == 3000


def test_infectionsBRTImpact():
    test_3 = infectionsBRT.InfectionsByRequestedTime.forImpact(6000)
    assert test_3(6000) == 3072000
    
def test_infectionsBRTSevere():
    test_4 = infectionsBRT.InfectionsByRequestedTime.forSevere(30000)
    assert test_4(30000) == 15360000

    