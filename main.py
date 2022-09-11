greeting = open("Texts/greeting.txt", "r").readlines()
personalQuestions = open("Texts/personalQuestions.txt", "r").readlines()
questions = open("Texts/questions.txt", "r").readlines()

import replit, time
from tools import validateResponse, respondToAge, respondToHome

class person:
  def __init__(self, name, gender, age, home):
    self.name = name
    self.gender = gender
    self.age = age
    self.home = home
    self.favoriteMovie = None
    self.hobby = None
    self.subject = None
    self.pets = None
    self.Siblings = None
    

person1 = person(None, None, None, None)


def promptGreeting():
  print(greeting[0])
  name = input(personalQuestions[0])
  gender = validateResponse(personalQuestions[1], ["Dude","Dudette"])
  age = input(personalQuestions[2])
  print(respondToAge(age))
  home = input(personalQuestions[3])
  print(respondToHome(home))
  person1.__dict__.update({"name": name, "gender": gender, "age": age, "home": home})
  print(f"{greeting[1] % person1.name}")
  time.sleep(3)
  replit.clear()

def promptQuestions():
  movie = input(questions[0])
  person1.movie = movie
  print(f"{questions[1] % person1.movie}")
  hobby = input(questions[2])
  person1.hobby = hobby
  print(f"{questions[3] % person1.hobby}")
  subject = input(questions[5])
  person1.subject = subject
  print(f"{questions[6] % person1.subject}")
  time.sleep(2)
  print(f"Well thats all I have time for today, {person1.name}")
  



  
promptGreeting()
promptQuestions()

