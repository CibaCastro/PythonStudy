import random

y = random.randint(0, 8)
#print(y)
name = input("What is your name? \n")

print("Hello ", name)
question = input("What is your question? \n")
answer = ""

if y == 0:
  answer = "Yes - definitely"
elif y == 1:
  answer = "It is decidedly so"
elif y == 2:
  answer = "Without a doubt"
elif y == 3:
  answer = "Reply hazy, try again"
elif y == 4:
  answer = "Ask again later"
elif y == 5:
  answer = "Better not tell you now"
elif y == 6:
  answer = "My sources say no"
elif y == 7:
  answer = "Outlook not so good"
else:
  answer = "Very doubtful"

print(name, " asks: ", question)
print("Magic 8-Ball's answer: ", answer)
