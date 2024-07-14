import random

def main():
	temperatures = []
	days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
	avg_temp = 0
	for i in range(7):
		temperatures.append(random.randint(26,40))
		avg_temp += temperatures[i]
	avg_temp /= 7

	good_days_count = 0
	for temperature in temperatures:
		if temperature % 2 == 0:
			print(temperature)
			good_days_count += 1
	

	highest_temp = temperatures[0]
	highest_temp_day = ""
	lowest_temp = temperatures[0]
	lowest_temp_day = ""

	above_avg = []
	for temperature in temperatures:
		if temperature > highest_temp:
			highest_temp = temperature
		elif temperature < lowest_temp:
			lowest_temp = temperature

		if temperature > avg_temp:
			above_avg.append(days_of_the_week[temperatures.index(temperature)])

	highest_temp_day = days_of_the_week[temperatures.index(highest_temp)]
	lowest_temp_day = days_of_the_week[temperatures.index(lowest_temp)]

	print("The weather report:")
	for i in range(7):
		print("    " + days_of_the_week[i] + ": " + str(temperatures[i]))


	print("    *\n    *\n    Shelly had " + str(good_days_count) + " good days\n    *\n    *")
	print("    The hottest temperature was: " + str(highest_temp) + " on " + highest_temp_day)
	print("    The lowest was: " + str(lowest_temp) + " on " + lowest_temp_day + "\n    *\n    *")
	print("    The average temperature was: " + str(avg_temp))
	print("    The days with above average temperatures were:", end='')
	for day in above_avg:
		print(" " + day + ",", end='') 

if __name__ == "__main__":
	main()