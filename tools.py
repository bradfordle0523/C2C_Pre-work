def validateResponse( question, valids):
  answer = input(question)
  if answer in valids:
    return answer
  else:
    print("That's not a valid reponse")
    validateResponse(question, valids)

def respondToAge(age):
  try:
    age = float(age)
  except:
    return "That's not even a number... but ok."
  if age >= 100:
    return "That's pretty old... almost to old."
  elif (age < 100 ) & (age > 10):
    return "Wow! not even triple digits"
  elif (age> 0) & (age <= 10):
    return "You are pretty young."
  else:
    return "Is that even possible??"

def respondToHome(home):
  return f"Oh hey, I use to live in {home} too."
  
    
    