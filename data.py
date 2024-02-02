import requests

API_endpoint_URL = "https://opentdb.com/api.php"   # extras/parameters: ?amount=10&type=boolean

#extract everything after the ? from the API URL, and place that data below into the proper parameters (it goes there inSTEAD of above. One or the other, but not both)

# YOU CAN CHANGE THESE PARAMETERS, FROM https://opentdb.com/api_config.php, and then update the parameters from this EndPoint, after the ?: https://opentdb.com/api.php?     amount=30&category=18&difficulty=hard
parameters_in_python_dictionary_form = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get(url=API_endpoint_URL, params=parameters_in_python_dictionary_form)  # optional:
response.raise_for_status()   #handles all the Exception Handling
# print(response_with_separate_params.raise_for_status())

# data = str(response_with_separate_params.json()['response_code']['results'])
data = response.json()["results"]   # We ONLY want the Value of the Key, 'results' because response_with_separate_params code's Value is 0 only, and 'results' contains the List of data we are interested in. ["response_code"] was parallel with 'results' and is not needed. Bypass that and get the data directly from response_with_separate_params.
# print(type(data))
# print(data)

question_data = data
#
#
# question_data = [
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The HTML5 standard was published in 2014.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The first computer bug was formed by faulty wires.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "FLAC stands for 'Free Lossless Audio Condenser'.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "All program codes have to be compiled into an executable file in order to be run. This file can then be executed on any machine.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "Linus Torvalds created Linux and Git.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "The programming language 'Python' is based off a modified version of 'JavaScript'",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "AMD created the first consumer 64-bit processor.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "'HTML' stands for Hypertext Markup Language.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "In most programming languages, the operator ++ is equivalent to the statement '+= 1'.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "hard",
#         "question": "The IBM PC used an Intel 8008 microprocessor clocked at 4.77 MHz and 8 kilobytes of memory.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     }
# ]
