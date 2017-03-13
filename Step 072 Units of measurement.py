"""
miles (1 mile = 1609 m),
yards (1 yard = 0.9144 m),
feet (1 foot = 30.48 cm),
inches (1 inch = 2.54 cm),
kilometres (1 km = 1000 m),
meters (m),
centimetres (1 cm = 0.01 m)
millimetres (1 mm = 0.001 m)
"""
units = {'mile': 1609, 'yard': 0.9144, 'foot': 0.3048, 'inch': 0.0254,
         'km': 1000, 'm': 1, 'cm': 0.01, 'mm': 0.001}

n, unit_from, _, unit_to = input().split()
print('{:.2e}'.format(float(n) * units[unit_from] / units[unit_to]))

