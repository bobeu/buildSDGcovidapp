from data_estimator import Impact, SevereImpact
from data_estimator import InfectionsByRequestedTime


def test_Impact():
    test_1 = Impact.currentlyInfected
    assert test_1(674) == 6740
    # assert test_1(600, 20) == 12000


def test_severe():
    test_2 = SevereImpact.currentlyInfected
    assert test_2(674) == 33700
    # assert test_2(600, 5) == 3000


def test_infectionsBRTImpact():
    test_3 = InfectionsByRequestedTime.forImpact(600)
    assert test_3(512) == 3450880


def test_infectionsBRTSevere():
    test_4 = InfectionsByRequestedTime.forSevere(30000)
    assert test_4(512) == 17254400
