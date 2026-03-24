from gemini_engine import GeminiClient as clank
api_key = input("Enter api key\n")
gemini = clank(api_key)
command = "Hey there!"
while(command!="quit"):
    prompt = f"{command}"
    ans = gemini.send_msg(prompt)
    print(f"{ans}")
    command = input()
