# from Body.Speak import Speak
# from Body.Listen import MicExecution

# def MainExe():
#     Speak("Main execution start")
#     while True:
#         query = MicExecution()
#         if "hello" in query:
#             Speak("Hi sir ! I am jarvis")
#         elif "bye" in query:
#             Speak("Hello Bye.")










# from Brain.AIBrain import ReplyBrain
from Body.Listen import MicExecution
print(">> Starting The Jarvis : Wait For Some Second")
from Body.Speak import Speak
from Features.clap_detection import Tester
Speak(">> Starting The Jarvis : Wait For Some Second")
def MainExecution():
    Speak("Hello Sir")
    Speak("I'm Jarvis , I'm Ready to assist you Sir.")
    while True:
        Data = MicExecution()
        Data = str(Data)
        from Brain.AIBrain import ReplyBrain
        Reply = ReplyBrain(Data)
        Speak(Reply)
        # kk= input("Enter : ")
        # ReplyBrain(kk)

def ClapDetect():
    query = Tester()
    if "True-Mic" == query:
        print("")
        print(">> Clap detected!! >>")
        print("")
        MainExecution()
    else:
        pass

ClapDetect()