##Basic Setting for use OPENAI API
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
API_KEY = os.environ['OPENAI_API_KEY']
print(API_KEY)

client = OpenAI(api_key = API_KEY)



####File list 
#1. financial_statement_sheet.csv
#2. thesis_eng - paper1000000.json ~ paper 1000012.json 
#3. report_eng - report10000001.json ~ report 10000018.json


#####upload files
file_id = []


##add csv file - 기업 재무 상태표 업로드 -> 단일 파일
with open("datasets/DART_samsung_financial_statement_cp.csv", "rb") as file1:
    uploaded_file = client.files.create(
        file=file1,
        purpose='assistants'
    )
file_id = file_id + [uploaded_file.id]


##add thesis files - 금융 도메인 학습용 학술논물 파일 (.json) 업로드
#사용할 thesis file = 9장
number_of_thesis = 9
file_number = 1
while file_number<=number_of_thesis:
    with open(f"datasets/finance_thesis/paper{file_number}.json", "rb") as file1:
        uploaded_file = client.files.create(
            file=file1,
            purpose='assistants'
        )
    file_id = file_id + [uploaded_file.id]
    file_number = file_number + 1

##add report files - 금융 도메인 학습용 리포트 파일 (.json) 업로드
#사용할 report file = 9장
number_of_report = 9
file_number = 1
while file_number<=number_of_report:
    with open(f"datasets/finance_thesis/paper{file_number}.json", "rb") as file1:
        uploaded_file = client.files.create(
            file=file1,
            purpose='assistants'
        )
    file_id = file_id + [uploaded_file.id]
    file_number = file_number + 1






####constants
##1#assistnat instruction
assis_instruction = "You are a finance reporter."
"You are financial expert."
"Your task is to deliver objective information about the stock items entered by the user."
"You must answer whether the company\'s financial position is healthy"
"You can answer what industry the company is in."
"You can tell user which other industries your company belongs to."
"You can tell user which social factors influence the industry your company belongs to."
"You can answer about the current market size and expected market growth rate of the industry in which your company belongs."
"If you need to explain a concept, provide clear and concise explanations."
"Always verify the correctness of the code before delivering the answer."

##2#run instruction
run_instructions="Users do not have much information about the company,"
"nor do they have much information about the industry to which the company belongs."
"You should generate your answer using only as objective and verified information as possible."
"You must answer whether the company\'s financial position is healthy"
"You can answer what industry the company is in."
"You can tell user which other industries your company belongs to."
"You can tell user which social factors influence the industry your company belongs to."
"You can answer about the current market size and expected market growth rate of the industry in which your company belongs."
"If you need to explain a concept, provide clear and concise explanations."
"Always verify the correctness of the code before delivering the answer."






####functions (with type hint)
#Generate Initial Message
def Initial_M(corp_name: str) -> str:
    ret_initial_message = f"I want know about{corp_name}"
    f"I want to know whether {corp_name}’s financial condition is sound.\n"
    f"I want to know about the industry to which {corp_name} belongs.\n"
    "I would like to know about the current market size of the relevant industry.\n"
    f"I want to know which industries the industry group {corp_name} belongs to is related to.\n"
    f"I want to know what social factors the industry to which {corp_name} belongs is related.\n"
    f"I want to know about the future prospects of {corp_name} and the industry to which {corp_name} belongs."
    f"Lastly, I would like to hear your overall evaluation opinion on {corp_name}’s stock items."

    return ret_initial_message






#Create Assistant
def CA(inst: str = assis_instruction):
    ret_assistant = client.beta.assistants.create(
    name='Finance_Reporter',
    instructions = inst,
    tools=[{'type': 'code_interpreter'}],
    tool_resources={
        "code_interpreter": {
            "file_ids": file_id
        }
    },
    temperature=0.2,
    top_p=0.2,
    model='gpt-4o-mini'
    )

    return ret_assistant


#Create thread
def CT() -> str:
    ret_thread = client.beta.threads.create()
    return ret_thread


#Create message
def CM(t_id: list, question: str, role: str = "user"):
    ret_message = client.beta.threads.messages.create(
    thread_id=t_id[0],
    role='user',
    content=question
    )
    
    return ret_message


#Create Run
def CR(t_id: list, a_id: str, r_inst: str = run_instructions):
    ret_run = client.beta.threads.runs.create(
    thread_id=t_id[0],
    assistant_id=a_id,
    instructions=r_inst,
    temperature=0.2,
    top_p=0.2
    )

    return ret_run


#Check Run Status
def CRS(t_id: list, r_id: str) -> str:
    run = client.beta.threads.runs.retrieve(
    thread_id=t_id[0],
    run_id=r_id
    )

    return run.status


#Display Assistant's Response
def Display(t_id: list) -> str:
    messages = client.beta.threads.messages.list(
    thread_id=t_id[0]
    )
    return messages.data[0].content[0].text.value

