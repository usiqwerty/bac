#!/usr/bin/env python3

ALCOHOL_DENSITY: float = 0.8  #: density of alcohol (g/ml)
BLOOD_DENSITY: float = 1.055  #: density of blood (g/ml)
WATER_IN_BLOOD: float = 0.8  #: parts of water in blood (%)
ALCOHOL_DEGRADATION: float = 0.002  #: for kg body weight per minute (g)

#given alcohol gramms
#body water in liter

def promille_to_gramm(*, promille: float, body_water: float) -> float:
	return (promille * (BLOOD_DENSITY * body_water)) / WATER_IN_BLOOD


def get_blood_alcohol_content(age, weight, height, female, volume, percent):
	gramm =  ALCOHOL_DENSITY * volume * (percent / 100)
	if female:
		body_water= 0.203 - (0.07 * age) + (0.1069 * height) + (0.2466 * weight)
	else:
		body_water= 2.447 - (0.09516 * age) + (0.1074 * height) + (0.3362 * weight)

	return (gramm * WATER_IN_BLOOD) / (BLOOD_DENSITY * body_water)



def get_blood_alcohol_degradation(age, weight, height, female, minutes):
	gramm = ALCOHOL_DEGRADATION * weight * minutes
	if female:
		body_water= 0.203 - (0.07 * age) + (0.1069 * height) + (0.2466 * weight)
	else:
		body_water= 2.447 - (0.09516 * age) + (0.1074 * height) + (0.3362 * weight)

	permille= (gramm * WATER_IN_BLOOD) / (BLOOD_DENSITY * body_water)
	return permille
def between(x, a, b):
	if x>=a and x<b:
		return True
	else:
		return False

def calc(age ,weight, height, female, volume, percent, minutes):

	maximum=get_blood_alcohol_content(age ,weight, height, female, volume, percent)

	current = max ( 0, maximum-get_blood_alcohol_degradation(age, weight, height, female, minutes))
	if  current<0.2:
		msg="Трезвое состояние"
	elif between(current, 0.2, 0.3):
		msg="В среднем поведение нормальное, Скрытые проявления, которые могут быть обнаружены специальными тестами"
	elif between(current, 0.3, 0.6):
		msg="Средневыраженная эйфория, расслабление,ощущение радости, говорливость, понижение сдержанности, нарушение концентрации"
	elif between(current, 0.6, 1):
		msg="Притупление ощущения, расторможенность, экстравертность, затруднено рассуждение, снижена глубина восприятия, нарушено периферическое зрение, нарушенное приспособление зрачка к свету"
	elif between(current, 1, 2):
		msg="Сверх-экспрессивность, переменчивость эмоций, гнев или печаль, снижение либидо, заторможены рефлексы, увеличивается время реакции, теряется способность к контролю движения (появляется шатающаяся походка), нечленораздельная речь, временно нарушена эрекция, вероятность временного алкогольного отравления"
	elif between(current, 2, 3):
		msg="Ступор, потеря способности к пониманию, ослабление способностей к ощущению, вероятность потери сознания, потеря сознания, потеря памяти"
	elif between(current, 3, 4):
		msg="Сильное угнетение функций центральной нервной системы, потеря сознания, возможность смерти, теряется контроль над мочеиспусканием, нарушается дыхание, полная утрата чувства равновесия,нарушено сердцебиение"
	elif between(current, 4, 5):
		msg="Полная утрата контроля за поведением, потеря сознания, вероятность смерти, проблемы с дыханием, нарушено сердцебиение, теряется контроль над движением зрачков (Нистагм)"
	elif current>5:
		msg="Высокий риск отравления, возможность смерти"
	return (maximum, current, msg)
if __name__=="__main__":
	age=int(input("age: "))
	weight=int(input("weight (kg): "))
	height=int(input("height (cm): "))
	female=True if input("r u female - y/n? ") == "y" else False
	volume=int(input("volume (ml): "))
	percent=int(input("percent: "))
	minutes=int(input("minutes since intake: "))
	print(age,weight,height, female, volume, percent)

	max, final, msg=calc(age ,weight, height, female, volume, percent, minutes)
	#print ( round(permill, 4) )
	print(msg)
	print("after {} minutes: {} -> {}".format(minutes,round(max, 4), round(final, 4)) )

