import my_module
from my_module import client
import time



##file upload with purpose = "assistants"
# Upload a file with an "assistants" purpose

##changed assistant code




###1#Create Assistance 
assistant = my_module.CA()
Assistant_ID = assistant.id
print(assistant)




###2#Create Thread
#code 
thread = my_module.CT()
Thread_ID = [thread.id]
print(thread)



####Create initial message
question = my_module.Initial_M("samsung")




###communicate with user
mes_ct = 1
while (question != None) and (question != "#"):
    ###3#Create message
    #code
    message = my_module.CM(Thread_ID, question, "user")
    Messeage_ID = [message.id]
    ##content example 
    #content='I need to solve the equation "3a + 11 = 14". Can you help me?'



    ##4##run
    #code
    run = my_module.CR(Thread_ID, Assistant_ID)
    Run_ID = run.id



    ###5#Check run status --> 여기 Check un status부분 automize.
    run_status = my_module.CRS(Thread_ID, Run_ID)
    print(run)

    ct = 0
    while True:
        run_status = my_module.CRS(Thread_ID, Run_ID)
        print('#', ct, ' current status : ', run_status)
        if (run_status == "completed"):
            break
        if (run_status == "failed"):
            break
        if (run_status == "queued" or "in_progress"):
            time.sleep(2)

    ###6#Display the Assistant's Response 
    result = my_module.Display(Thread_ID)
    print('####', mes_ct, 'result : ', result)
    
    mes_ct = mes_ct+1

    print('\n\n\n')
    print('what is your question? : ')
    question = input()

print("end")