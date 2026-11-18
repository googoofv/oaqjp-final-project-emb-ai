import json
import requests

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    myobj = {"raw_document": {"text": text_to_analyze}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json=myobj, headers=header)

    # Convert the response text into a dictionary
    response_data = json.loads(response.text)
    scores = response_data["emotionPredictions"][0]["emotion"]

    # Extract the required scores
    result = {
        "anger": scores["anger"],
        "disgust": scores["disgust"],
        "fear": scores["fear"],
        "joy": scores["joy"],
        "sadness": scores["sadness"],
    }

    # Add the emotion with the highest score
    result["dominant_emotion"] = max(result, key=result.get)

    return result
