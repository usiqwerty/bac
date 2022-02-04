#!/usr/bin/env python3

ALCOHOL_DENSITY: float = 0.8  #: density of alcohol (g/ml)
BLOOD_DENSITY: float = 1.055  #: density of blood (g/ml)
WATER_IN_BLOOD: float = 0.8  #: parts of water in blood (%)
ALCOHOL_DEGRADATION: float = 0.0025  #: for kg body weight per minute (g)

ALCOHOL_DEGRADATION_WARNING = """
In the next version the value used for alcohol degradation will be lowered. To
keep the current default, you can override `ALCOHOL_DEGRADATION`, or use the new
*degradation* argument to the `calculate_alcohol_degradation` and
`get_blood_alcohol_degradation` functions.
"""


def alcohol_to_ethanol(*, volume: int, percent:float):
	return ALCOHOL_DENSITY * volume * (percent / 100)

def calculate_alcohol_degradation(*, weight: int, minutes: int = 1, degradation: Optional[float] = None) -> float:
	if degradation is None:
		degradation = ALCOHOL_DEGRADATION
	return degradation * weight * minutes


def body_water(*, age: int, weight: int, height: int, female: bool):
	if female:
		return 0.203 - (0.07 * age) + (0.1069 * height) + (0.2466 * weight)
	else:  # male
		return 2.447 - (0.09516 * age) + (0.1074 * height) + (0.3362 * weight)


def promille_to_gramm(*, promille: float, body_water: float) -> float:
	return (promille * (BLOOD_DENSITY * body_water)) / WATER_IN_BLOOD


def gramm_to_promille(*, gramm: float, body_water: float) -> float:
	#given alcohol gramms
	#body water in liter
	return (gramm * WATER_IN_BLOOD) / (BLOOD_DENSITY * body_water)


def get_blood_alcohol_content(age: int,weight: int, height: int, female: bool, volume: int, percent: float) -> float:
	gramm = alcohol_to_ethanol(volume=volume, percent=percent)
	tot_body_water = body_water(age=age, weight=weight, height=height, female=female)
	return gramm_to_promille(gramm=gramm, body_water=tot_body_water)


def get_blood_alcohol_degradation(*,age: int,weight: int,height: int,female: bool,minutes: int = 1) -> float:
	gramm = calculate_alcohol_degradation(weight=weight, minutes=minutes, degradation=ALCOHOL_DEGRADATION)
	tot_body_water = body_water(age=age, weight=weight, height=height, female=female)
	return gramm_to_promille(gramm=gramm, body_water=tot_body_water)


age=30
weight=80
height=180
female=False
volume=100
percent=40
permille=get_blood_alcohol_content(age ,weight, height, female, volume, percent)
print ( round(permille, 1) )
