import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, SafetySetting
import os
import vertexai

# Set the environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ""  # api 키 추가

vertexai.init(project="alert-condition-443702-g2", location="us-central1")
# ... rest of your code ...


def generate():
    vertexai.init(project="alert-condition-443702-g2", location="us-central1")
    model = GenerativeModel(
        "gemini-1.5-flash-002",
    )
    
    file_path = "gemini/d5.txt"

    # 파일 내용 읽기
    with open(file_path, "r", encoding="utf-8") as file:
        file_content = file.read()

    # 읽은 내용을 base64로 인코딩
    encoded_content = base64.b64encode(file_content.encode('utf-8')).decode('utf-8')

    # Part 객체 생성 (data에 인코딩된 파일 내용 사용)
    document1 = Part.from_data(
        mime_type="text/plain",
        data=encoded_content
    )
    responses = model.generate_content(
        [document1, text1],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True,
    )

    for response in responses:
        print(response.text, end="")
        # ... rest of the code ...

text1 = """Question: For the given review, return a TEXT object that has the
fields sentiment and explanation.
The explanation field contains text that explains the sentiment. Must be in Korean except the words, MBTI and LBTI. 
Also, predict user's MBTI and LBTI(important). 
Do not write it is difficult to predict. Just predict as possible. 
Write it like a Psychologist.
Do not say it requires more information. Just do it with a given contents. Write a invigorating quote at the end. 
Compare journal with a newer journal and keep update them. Classify journals with date(year-month-date-day).
Write scores of various emotions. Remove every English words. 
Start the contents with "스마트 AI 감정 분석" 
If there are no previous/comparison journal, 
just use what are given. 
Write every section in detail, and make it more interesting. Just finish with quote and say keep write journals for updates."""

generation_config = {
    "max_output_tokens": 3333,
    "temperature": 1,
    "top_p": 0.95,
}

safety_settings = [
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
]

generate()
