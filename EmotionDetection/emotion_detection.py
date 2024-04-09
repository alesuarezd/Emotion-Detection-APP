from flask import Flask, request
import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=myobj, headers=headers)
    formatted_response = json.loads(response.text)
    if(response.status_code == 400):
        
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None
        return {'anger': anger_score, 'disgust': disgust_score,'fear': fear_score,'joy': joy_score,'sadness': sadness_score,'dominant_emotion': dominant_emotion}
    else:
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        emotions_score = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        }
        max_score = 0
        for score in emotions_score:
             if(float(emotions_score[score])>max_score):
                max_score=float(emotions_score[score])
                dominant_emotion = score
        return {'anger': anger_score, 'disgust': disgust_score,'fear': fear_score,'joy': joy_score,'sadness': sadness_score,'dominant_emotion': dominant_emotion}