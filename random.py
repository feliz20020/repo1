
import random

rand = random.random()
randint = random.randint(1, 100)
randrange = random.randrange(0, 100, 2)
randuni = random.uniform(3, 5)

sample_list = [1, 2, 3, 4, 5, 6]

randchoice = random.choice(sample_list)
random.shuffle(sample_list)

print(sample_list)