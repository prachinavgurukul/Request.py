# import requests
# import json
# b=requests.get("https://api.merakilearn.org/courses")
# c=b.json()
# with open("courses.json","w") as file:
#     json.dump(c,file,indent=4)
# d=open("courses.json","r")
# e=d.read()
# data=json.loads(e)
# i=0
# while i<len(data):
#     print(str(i+1)+"-",data[i]["name"],data[i]["id"])
#     i+=1
# print(" ")
# user=int(input("Enter the number of the course: "))
# print(data[user-1]["name"])
# b=requests.get("https://api.merakilearn.org/courses/"+data[user-1]['id']+"/exercises")
# d=b.json()
# a=data[user-1]['name']+"_"+".json"
# with open(a,"w") as f:
#     json.dump(d,f,indent=4)
# s=open(a,"r")
# read=s.read()
# data=json.loads(read)
# i=0
# while i<len(data["course"]["exercises"]):
#     print(str(i+1),data["course"]["exercises"][i]["name"])
#     i+=1
# j=int(input("Enter the point number: "))
# print(data["course"]["exercises"][j-1]["name"])
# i=1
# while i<len(data["course"]["exercises"][j-1]["content"]):
#     print(str(i+1),data["course"]["exercises"][j-1]["content"][i]["value"])
#     i+=1
#     k=input("You want to previous content or next? (n/p)")
#     if k!="n" and k=="p":
#         if k=="previous" and j>1:
#             print(data["course"]["exercises"][j-2]["content"])
#             i=0
#             while i<len(data["course"]["exercises"][j-2]["content"]):
#                 print(data["course"]["exercises"][j-2]["content"][i]["value"])
#                 i+=1
#             j=-1
#         else :
#             i = 0
#             while i < len(data["course"]["exercises"]):
#                 print(str(i+1),data["course"]["exercises"][i]["name"])
#                 i+=1    
#     elif k != "p" and k == "n":
#         if k == "n" and j < len(data["course"]["exercises"]):
#                 print(data["course"]["exercises"][j]["name"])
#                 i = 0 
#                 while i < len(data["course"]["exercises"][j]["content"]):
#                     print(data["course"]["exercises"][j]["content"][i]["value"])
#                     i+=1
#                 j=j=1
#         if j == len(data["course"]["exercises"]):
#             print("topic is completed:")
#     else:
#         print("wrong user_input ")

