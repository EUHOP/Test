import os
import anthropic
from dotenv import load_dotenv
load_dotenv()
client=anthropic.Anthropic(api_key=os.environ.get("Anthropic_API_Key"))
messages=[]
print("welcome to euhop assistant type quit exit end to end the chat")
#whole chat bot lies on While loop
while True:
    temp_in=input("choose the AI Mode of the model, 1 is for precise and 2 for creative and 3 for balance")
    user_input=input("you: ").strip()
    if "spanish" not in user_input.lower():
        print("I am a spanish tutor, pl give questions related to spanish")
        break
    temp_map={"1":0.0,"2":1.0,"3":0.50}
    temp=temp_map.get(temp_in,0.50) #0.5 we have because it becomes defulth response 
    end_methods=["end","close","quit","q","exit","bye","terminate","completed"]
    if user_input.lower() in end_methods:
        print("\n Thank You Buddy...see u next time")
        break
    messages.append({"role":"user","content":user_input})
    system_prompt="""your are a very experienced language tutor with 10 years of experience,answer every question as if you are teching to a 5 years old with tricks & clear meaningful answers & suggest some out of the box exercises
    .give lesson planning forecast the learning topics and give the examples based on common mistakes"""
    response=client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1500,
        temperature=temp,
        system=system_prompt,
        messages=messages
    )
    assistant_message=response.content[0].text
    messages.append({"role":"assistant","content":assistant_message})
    print(f"\nClaude: {assistant_message}\n")
    #Temperature : It is a parameter that controls how predective or creative the claude response can be. It is like a creativity dial
    #Claude normally breaks the input in chunks, then predicts the next possible word & then it assigns the tockes as por the probability of the word
#Range of termprature is 0 to 1. O means it becomes very relastic or authentic or precise & picks the highest probabale token
#The range 1 becomes more dramatic or out of the box & probability is more distributed among all the options & more creative in giving answers 
#0=precise AI mode #0.5=Balanced AI Mode #1=Creative Mode
#Github : it's a hosting service,
#GIT is a versoning control system 
#GIT CLI is a command line intigration 
#To active the venv we must use "source venv/bin/activate "
#branch - we create different versions of the main version to update the product 
#main - it is a initial stable version 
#commit - It is taking a responsibility for new changes 
#git add - It is adding the chnages to the respective files 
#git status - this is used to know the number of changes files 