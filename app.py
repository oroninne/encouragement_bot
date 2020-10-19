print("Title of program: Encouragement bot")
print()
while True:
  description = input("Could you describe how you feel in a sentence?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("to hang in there, you will be okay. Cheer yourself up by indulging in some of your hobbies, because even if not tomorrow, the day after and next will be a better day")
      counter += 1
    if each_word == "depressed":
      feelings_list.append("depressed")
      encouragement_list.append("to talk to someone. Take a deep breath and listen to some music, relax and empty your head of the negative thoughts, and do something therapeutic like drawing or reading. No matter how alone you feel, there will be someone willing to listen, be it online or in person. Keep going like you always have, you are strong for enduring and living")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("that it's okay to rest when you're burnt out and exhausted. Take a break and indulge in your hobbies, it's alright to let your guard down :)")
      counter += 1
    if each_word == "empty":
      feelings_list.append("empty")
      encouragement_list.append("even if there is no meaning to life today, there might be one tomorrow. To find the sunlight, we have to wait for the storm to end, and to find a rainbow, there must be both sun and rain. Each day has their up and downs like Yin and Yang, so hang in there and keep going. No matter how slow, it's still progress :D")
      counter += 1
    if each_word == "hungry":
      feelings_list.append("hungry")
      encouragement_list.append("to take care of yourself! Eat your fill, but make sure not to overeat. Taking small bites is okay, as long as you keep going. Eating comfortably should be a privillege everyone deserves ^_^")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("to keep smiling! You're doing very well, it's good that you feel lighter. Keep it up, you're awesome (^-^)b")
      counter += 1

  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember "+ encouragement_list[0] + "! You are amazing and strong <3 Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
