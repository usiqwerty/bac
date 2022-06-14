#!/usr/bin/env python3

ALCOHOL_DENSITY: float = 0.8  #: density of alcohol (g/ml)
BLOOD_DENSITY: float = 1.055  #: density of blood (g/ml)
WATER_IN_BLOOD: float = 0.8  #: parts of water in blood (%)
ALCOHOL_DEGRADATION: float = 0.002  #: for kg body weight per minute (g)

#given alcohol gramms
#body water in liter

def get_blood_alcohol_content(age, weight, height, female, volume, percent, minutes):

	if female:
		body_water= 0.203 - (0.07 * age) + (0.1069 * height) + (0.2466 * weight)
	else:
		body_water= 2.447 - (0.09516 * age) + (0.1074 * height) + (0.3362 * weight)

	gramm =  ALCOHOL_DENSITY * volume * (percent / 100)
	maximum = (gramm * WATER_IN_BLOOD) / (BLOOD_DENSITY * body_water)

	#turns into 0 if minutes are equal to 0
	#so no condition needed
	degrad_factor = ALCOHOL_DEGRADATION * weight * minutes
	decrease = (degrad_factor * WATER_IN_BLOOD) / (BLOOD_DENSITY * body_water)

	return maximum-decrease, maximum

def bac(age ,weight, height, female, volume, percent, minutes):
	current, maximum =  get_blood_alcohol_content(age, weight, height, female, volume, percent, minutes)

	current = max (0, current)	#it could be negative if minutes are too big

	if  current < 0.2:
		msg="Трезвое состояние"
	elif 0.2 <= current < 0.3:
		msg="В среднем поведение нормальное, Скрытые проявления, которые могут быть обнаружены специальными тестами"
	elif 0.3 <= current < 0.6:
		msg="Средневыраженная эйфория, расслабление,ощущение радости, говорливость, понижение сдержанности, нарушение концентрации"
	elif 0.6 <= current < 1:
		msg="Притупление ощущения, расторможенность, экстравертность, затруднено рассуждение, снижена глубина восприятия, нарушено периферическое зрение, нарушенное приспособление зрачка к свету"
	elif   1 <= current < 2:
		msg="Сверх-экспрессивность, переменчивость эмоций, гнев или печаль, снижение либидо, заторможены рефлексы, увеличивается время реакции, теряется способность к контролю движения (появляется шатающаяся походка), нечленораздельная речь, временно нарушена эрекция, вероятность временного алкогольного отравления"
	elif   2 <= current < 3:
		msg="Ступор, потеря способности к пониманию, ослабление способностей к ощущению, вероятность потери сознания, потеря сознания, потеря памяти"
	elif   3 <= current < 4:
		msg="Сильное угнетение функций центральной нервной системы, потеря сознания, возможность смерти, теряется контроль над мочеиспусканием, нарушается дыхание, полная утрата чувства равновесия,нарушено сердцебиение"
	elif   4 <= current < 5:
		msg="Полная утрата контроля за поведением, потеря сознания, вероятность смерти, проблемы с дыханием, нарушено сердцебиение, теряется контроль над движением зрачков (Нистагм)"
	elif current > 5:
		msg="Высокий риск отравления, возможность смерти"
	return maximum, current, msg
if __name__=="__main__":
	age=int(input("age: "))
	weight=int(input("weight (kg): "))
	height=int(input("height (cm): "))
	is_female=True if input("r u female - y/n? ") == "y" else False
	volume=int(input("volume (ml): "))
	percent=int(input("percent: "))
	minutes=int(input("minutes since intake: "))
	print(age,weight,height, is_female, volume, percent)

	max, final, msg = bac(age, weight, height, is_female, volume, percent, minutes)
	#print ( round(permill, 4) )
	print(msg)
	print("after {} minutes: {} -> {}".format(minutes,round(max, 4), round(final, 4)) )

