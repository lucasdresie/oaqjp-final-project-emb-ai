import requests
import json

#Emotion detection function
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)
    format_response = json.loads(response.text)


    #Extract emotions and their scores:
    anger_score = format_response["emotionPredictions"][0]["emotion"]["anger"]
    disgust_score = format_response["emotionPredictions"][0]["emotion"]["disgust"]
    fear_score = format_response["emotionPredictions"][0]["emotion"]["fear"]
    joy_score = format_response["emotionPredictions"][0]["emotion"]["joy"]
    sadness_score = format_response["emotionPredictions"][0]["emotion"]["sadness"]

    #Determine the dominant emotion with the highest score:
    emotion_list = [anger_score, disgust_score, fear_score, joy_score, sadness_score]
    dominant_emotion_index = emotion_list.index(max(emotion_list))
    emotion_keys = ["anger", "disgust", "fear", "joy", "sadness"]
    dominant_emotion_key = emotion_keys[dominant_emotion_index]

    #Format the response into the required output format: 
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion_key
    }

    return result