from sopel import module
from emo.wdemotions import EmotionDetector

global emotion_average
global emotion_total
global count

emotion_total = [0,0,0,0,0,0]
emotion_average = [0,0,0,0,0,0]
count = 0
a = 0.01

emo = EmotionDetector()

@module.rule('')
def hi(bot, trigger):
    print(trigger, trigger.nick)
    #bot.say('Hi, ' + trigger.nick)
    #emo.detect_emotion_in_raw(bot, trigger)
    temp = emo.detect_emotion_in_raw_np(str(trigger))
    i = 0
    count += 1
    for val in temp:
        emotion_total[i] = val + temp[i]
        emotion_average[i] = emotion_average[i] + a * (emotion_total[i])

        i = i + 1

    print(emotion_total)
    print(emotion_average)
    print (count)