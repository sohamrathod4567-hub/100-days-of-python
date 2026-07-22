sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {name : len(name) for name in sentence.lower().split()}

print(result)