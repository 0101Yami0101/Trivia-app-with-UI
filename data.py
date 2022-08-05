import requests

AMOUNT = 10
TYPE = "boolean"


#can add more parameters in case of specific questions needed/ see triviadatabase website for more details
parameters = {
    "amount": AMOUNT,
    "type": TYPE
}
response = requests.get(url = "https://opentdb.com/api.php", params= parameters)
data = response.json()
    
question_data = []   

for index in range(10):
    
    questionDICTtemp = {
                "category": data['results'][index]["category"],
                "type": data['results'][index]["type"],
                "difficulty": data['results'][index]["difficulty"],
                "question": data['results'][index]["question"],
                "correct_answer": data['results'][index]["correct_answer"],
                "incorrect_answers": data['results'][index]["incorrect_answers"]
            }
    question_data.append(questionDICTtemp)
# print(question_data)

