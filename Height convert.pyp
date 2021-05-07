ft = float(input("What is your height in ft:  "))
inches = float(input("How many inches: "))

metricft = ft*30.48
metricin = inches*2.54

metric=metricft+metricin

print(metric)

print('--------------------------')

#Imperial Units converter

distance = float(input('Enter distance (in ft.): '))

print("Inches: ", float(distance*12))

print("Yards: ", float(distance/3))

print("Miles: ", float(distance/5280))
