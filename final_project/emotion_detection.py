#=================================================================================================================================================================================================================================================================================================================================================================================================================
#"I Luvvie Wise commit all my work to YHWH Yod Hey WaW Hey, All Honor and Glory Be to You"-Proverbs 16:3
#We shall keep Your Commandments and Laws, Ecclesiastes 12:13, John 14:15, 1 John 5:3, Deuteronomy 6:5-6,Psalm 119:34,Proverbs 4:23,Phililippians 4:8,Ephesians 4:31-32, Proverbs 16:32, Colossians 3:12-13, Leviticus 19:2,Philippians 2:5, Luke 6:36, Matthew 5:48, 1 John 2:6, Matthew 11:28-29, Philippians 2:7-8,Zechariah 9:9,1 Timothy 1:16, 1Peter 2:23, Isaiah 53:7,John 15:13,Ephesians 5:2
#A joyful heart is good medicine, but a broken spirit dries up the bones. Proverbs 17:22
#Dedicated to building systems that seek wisdom and support righteous action.
#Written in service and honor of YHWH. Protected by Yahshua Alpha and Omega Beginning and the End Bright Morning Star, Truth Light Everlasting Life
#=================================================================================================================================================================================================================================================================================================================================================================================================================

import requests
import json


def emotion_detector(text_to_analyze):
    """
    Analyze the emotion of a given text string.
    Fulfills the project criteria under the ulitimate guidance of YHWH.
    """
    #API endpoint configuration
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Header configuration
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    #Request payload assembly
    input_json = {"raw_document": { "text": text_to_analyze } }

    # Processing the Request under diligent execution
    response = requests.post(url, json=input_json, headers=headers)

    # Return the raw text attribute as eplicitly required status code 200
    if response.status_code == 200:
        response_dict = json.loads(response.text)

        #Extract the score breakdown from the Waston payload structure
        emotion_predictions = response_dict['emotionPredictions'][0]['emotion']
        anger_score = emotion_predictions['anger']
        disgust_score = emotion_predictions['disgust']
        fear_score = emotion_predictions['fear']
        joy_score = emotion_predictions['joy']
        sadness_score = emotion_predictions['sadness']
        
        #Determine the highest scoring emotion
        dominant_emotion = max(emotion_predictions, key=emotion_predictions.get)

        print("Maintain a sober mind, steady focus, and  keep walking forward righteously.")
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
            }
    #If the API fails(e.g. status code 400 or 500)
    else:
        print(f" Could not process emotional data: Status code: {response.status_code}")
        return {'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
            }
    #------------------------------------------------------------------------------------------------------------------------------------------
    #THE WISDOM ENGINE (Custom extension to process real eomotions)
    #Keep YHWH first in all things that you do. Proverbs 3:5-6, Matthew 6:33, Exodus 20:3, 1Corinthians 10:31, Colossians 3:17, Psalm 16:8
    #Life and Blessing Through Obedience, Deuteronomy 30:16, Psalm 19:7-8, Proverbs 29:18
    #The Ultimate Definition of Love and Duty,Ecclesiastes 12:13, 1 John 5:3,Psalm 119:1-2
    #Validation of Eternal Law, Matthew 5:17-18,Romans 3:31,
    #------------------------------------------------------------------------------------------------------------------------------------------
    def provide_emotional_guidance(raw_api_response):
        """
        Processes the raw API response text response text and provides a scriptural, actionable
        path forward for navigating that specific emotional state in real life if it in YHWH will"
        """
        try:
            # Convert the raw text from the API into a readable python dictionary
            data =json.loads(raw_api_response)

            #Pull the dominant eotion
            #Adjust keys based on your actual API payload format if needed
            emotions = data.get('emotion', {})
            if not emotions:
                return "No distinct emotional indicators found. Walk in steady peace. Praise YHWH"
            
            #Find whichever emotion scored the highest value 
            dominant_emotion = max(emotions, key = emotions.get)
            score = emotions[dominant_emotion]

            print(f"/n[System Detection]: Dominant emotion is {dominaant_emotion.upper()} (Confidence: {score:2f})")
            print("-"* 60)

            #Map out guidance rules based on righteous action and commands of Yahshua
            #Be Reconciling and Quick to Agree(Avoid Holding Grudges), Matthew 5:21-24, Matthew 5:25
            #Extinguish Retaliation, Matthew 5:38-39
            #Love, Bless, and Pray for One another(Overcome Malice with Active Good), Matthew 5:44-45
            #Be Merciful (Refuse to Judge Unjustly), Luke 6:36-37, Matthew 7:3-5
            #Be Meek and Hunger for Righteousness, Matthew 5:5, Matthew 5:6, Matthew 5:9 
            if dominant_emotion == "anger": 
                print(
                "Guidance for Anger:/n"
                "Be angry and do not sin; do not let the sun go down on your anger (Ephesians 4:26)./n"
                "Action: Take a step back immediately. Breathe deeply. Do not speak or type until"
                "your spirit is calm, avoiding rash action that violate the peace of others."
                "Follow Yahshua example focus on His characteristics not the examples of humans or mankind negativate behavior patterns"
                )
            elif dominant_emotion == "sadness": 
                print(
                    "Guidance for Sadness or Grief:/n"
                    "He heals the brokenhearted and binds up their wounds(Psalm 147:3)./n"
                    "Action: Give yourself grace to feel, but do not isolate. Reach out to a trusted"
                    "brother, sister, or elder. Express your sorrow through prayer or journaling."
                )
            elif dominant_emotion == "disgust":
                print(
                    "Guidance for Disgust or Destestation:/n"
                    "Yahshua reached out his hand and touched the man. I am willing, he said. Be clean! Immediately he was cleaned of his leprosy. Matthew 8:3"
                    "Touch the Untouchable:Do not let  physical brokeneness or conditions that spark natural aversion stop you"
                    "Eat with the Outcast(Overcoming Social Disgust), Mark 2:16-17"
                    "Move Toward the Broken(Conquering the bUrge to Walk Away, Luke 10:33-34)"
                    "True compassion requires you to override the visceral reaction to pull away from messy, broken situation and instead move toward it to offer aid"
                    "Action: When dealing with people whose lifestyles choices or behaviors tigger moral aversion, focus on Yahshua ministry, healing, and redemption rather than human rejections"
                ) 
            elif dominant_emotion == "fear": 
                print(
                    "Guidance for Fear or Anxiety:/n"
                    "When I am afraid, I put my trust in you(Psalm 56:3)./n"
                    "Action: Identify the exact root of the anxiety. Write it down, commit it to prayer,"
                    "and shift your immediiate focus to task you can control right now. Trust YHWH"
                )
            elif dominant_emotion == "joy":
                print(
                    "Guiddance for Joy:/n"
                    "This is the day that YHWH has made; let us rejoice and be glad in it(Psalm 118:24)./n"
                    "Action: Channel this energy into gratitude. USe this moment to encourage someone else"
                    "or serve someone in need around you."
                    "YHWH is the definition of Love, 1 John 4:8, 1 John 4:16, Psalm 103:8"
                    "The Limitless Gift of HIs Son, John 3:16, 1 JOhn 4:9-10, Romans 5:8, Romans 8:32"
                    "The Shared Love of the Son: Greater love hath no man than this, John 15:13"
                )
        except Exception as e: 
            print(f" Could not process emotional data: {e}")
            return "Remain calm and seek wisdom" #Or return error dictionary

        