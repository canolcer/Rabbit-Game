a = input("Please Enter Feeding Map as a List:")
b = input("Please Enter Directions of Movement as a List:")
print("Your Board is:")
list1 = eval(a)
for i in a.split("],"):
    for j in i:
        if j == "W" or j == "X" or j == "C" or j == "M" or j == "A" or j == "P" or j == "*":
            print(j, end=" ")
    print()
print("Your Output Should be like this:")
score = 0
for i in list1:
    for j in i:
        if j == "*":
              rabbit_in_general = list1.index(i)
              star1 = i.index(j)
              for direction in b:
                  if direction == "]":
                      for z in list1:
                          for f in z:
                              print(f, end=" ")
                          print()
                      print("Your Score is:", score)
                      exit()
                  if direction == "U":
                      if rabbit_in_general == 0:
                          continue
                      elif list1[rabbit_in_general - 1][star1] == "W":
                          continue
                      elif list1[rabbit_in_general - 1][star1] == "C":
                          list1[rabbit_in_general - 1][star1] = "*"
                          list1[rabbit_in_general][star1] = "X"
                          rabbit_in_general -= 1
                          score += 10
                          continue
                      elif list1[rabbit_in_general - 1][star1] == "A":
                          list1[rabbit_in_general - 1][star1] = "*"
                          list1[rabbit_in_general][star1] = "X"
                          rabbit_in_general -= 1
                          score += 5
                          continue
                      elif list1[rabbit_in_general - 1][star1] == "M":
                          list1[rabbit_in_general - 1][star1] = "*"
                          list1[rabbit_in_general][star1] = "X"
                          rabbit_in_general -= 1
                          score -= 5
                          continue
                      elif list1[rabbit_in_general - 1][star1] == "P":
                          list1[rabbit_in_general - 1][star1] = "*"
                          list1[rabbit_in_general][star1] = "X"
                          for z in list1:
                              for f in z:
                                  print(f, end=" ")
                              print()
                          print("Your Score is:",score)
                          exit()
                      else:
                          list1[rabbit_in_general - 1][star1] = "*"
                          list1[rabbit_in_general][star1] = "X"
                          rabbit_in_general -= 1
                          continue
                  if direction == "D":
                      if rabbit_in_general == len(list1)-1:
                          continue
                      elif list1[rabbit_in_general + 1][star1] == "W":
                          continue
                      elif list1[rabbit_in_general + 1][star1] == "C":
                          list1[rabbit_in_general + 1][star1] = "*"
                          list1[rabbit_in_general][star1] = "X"
                          rabbit_in_general += 1
                          score += 10
                          continue
                      elif list1[rabbit_in_general + 1][star1] == "A":
                          list1[rabbit_in_general + 1][star1] = "*"
                          list1[rabbit_in_general][star1] = "X"
                          rabbit_in_general += 1
                          score += 5
                          continue
                      elif list1[rabbit_in_general + 1][star1] == "M":
                          list1[rabbit_in_general + 1][star1] = "*"
                          list1[rabbit_in_general][star1] = "X"
                          rabbit_in_general += 1
                          score -= 5
                          continue
                      elif list1[rabbit_in_general + 1][star1] == "P":
                          list1[rabbit_in_general + 1][star1] = "*"
                          list1[rabbit_in_general][star1] = "X"
                          for z in list1:
                              for f in z:
                                  print(f, end=" ")
                              print()
                          print("Your Score is:", score)
                          exit()
                      else:
                          list1[rabbit_in_general + 1][star1] = "*"
                          list1[rabbit_in_general][star1] = "X"
                          rabbit_in_general += 1
                          continue
                  if direction == "L":
                      if star1 == 0:
                          continue
                      elif list1[rabbit_in_general][star1-1] == "W":
                          continue
                      elif list1[rabbit_in_general][star1 - 1] == "C":
                          list1[rabbit_in_general][star1 - 1] = "*"
                          list1[rabbit_in_general][star1] = "X"
                          star1 -= 1
                          score += 10
                      elif list1[rabbit_in_general][star1 - 1] == "A":
                          list1[rabbit_in_general][star1 - 1] = "*"
                          list1[rabbit_in_general][star1] = "X"
                          star1 -= 1
                          score += 5
                      elif list1[rabbit_in_general][star1 - 1] == "M":
                          list1[rabbit_in_general][star1 - 1] = "*"
                          list1[rabbit_in_general][star1] = "X"
                          star1 -= 1
                          score -= 5
                      elif list1[rabbit_in_general][star1 - 1] == "P":
                          list1[rabbit_in_general][star1 - 1] = "*"
                          list1[rabbit_in_general][star1] = "X"
                          for z in list1:
                              for f in z:
                                  print(f, end=" ")
                              print()
                          print("Your Score is:", score)
                          exit()
                      else:
                          list1[rabbit_in_general][star1 - 1] = "*"
                          list1[rabbit_in_general][star1] = "X"
                          star1 -= 1
                          continue
                  if direction == "R":
                      if star1 == len(i)-1:
                          continue
                      elif list1[rabbit_in_general][star1+1] == "W":
                          continue
                      elif list1[rabbit_in_general][star1 + 1] == "C":
                          list1[rabbit_in_general][star1 + 1] = "*"
                          list1[rabbit_in_general][star1] = "X"
                          star1 += 1
                          score += 10
                      elif list1[rabbit_in_general][star1 + 1] == "A":
                          list1[rabbit_in_general][star1 + 1] = "*"
                          list1[rabbit_in_general][star1] = "X"
                          star1 += 1
                          score += 5
                      elif list1[rabbit_in_general][star1 + 1] == "M":
                          list1[rabbit_in_general][star1 + 1] = "*"
                          list1[rabbit_in_general][star1] = "X"
                          star1 += 1
                          score -= 5
                      elif list1[rabbit_in_general][star1 + 1] == "P":
                          list1[rabbit_in_general][star1 + 1] = "*"
                          list1[rabbit_in_general][star1] = "X"
                          for z in list1:
                              for f in z:
                                  print(f, end=" ")
                              print()
                          print("Your Score is:", score)
                          exit()
                      else:
                          list1[rabbit_in_general][star1 + 1] = "*"
                          list1[rabbit_in_general][star1] = "X"
                          star1 +=1
                          continue

for z in list1:
    for f in z:
        print(f,end=" ")
    print()
print("Your Score is:",score)