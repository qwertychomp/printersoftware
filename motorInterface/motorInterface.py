import machine

from stepper import Stepper
# source for revSteps: some random article proably wrrittn by somene who doesnt speak english as there first language
revSteps = 2048
s1 = Stepper(0, 1, steps_per_rev=revSteps,speed_sps=100)
s2 = Stepper(6, 5, steps_per_rev=revSteps,speed_sps=100)