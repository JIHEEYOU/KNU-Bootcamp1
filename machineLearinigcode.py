from tkinter import E
import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "c0ff9cf0-1eb3-11ed-84e3-ffc2659697d0625043bb-3ace-47dc-b69e-d17d043fa9f6"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()




#메인 시작
chatbot_dic={
    'digestive_medicine': '소화제가 필요하시네요',
    'menstrual_pain_medication':'생리통약이 필요하시네요',
    'antiallergic_drug': '알레르기 약이 필요하시네요',
    'ointment': '연고가 필요하시네요',
    'pain_relief_patch': '파스가 필요하시네요'
    }


while True:
    q=input("[포켓약국] : 증상을 입력하세요! (종료를 원하시면 bye를 입력하시오)\n")
    if q=='bye' or q== 'BYE':
        print('안녕히 가세요!')
        break



    demo=classify(q)
    label = demo["class_name"]
    confidence = demo["confidence"]

    print(f'[포켓 약국]:{chatbot_dic[label]}')
    print ("result: '%s' with %d%% confidence\n" % (label, confidence))

    if confidence<40:
        print('[포켓 약국]: 잘 모르겠습니다'
        )
        continue

    #소화제
    while True:
        if label=='digestive_medicine':
            a=input('1. 알약 형태의 약을 원하시나요?(Y/N)')
            if a=='Y' or a== 'y':
                gas=input('2. 가스가 차시나요?(Y/N)')
                if gas=='Y' or gas== 'y':
                    oil=input('3. 기름진 음식을 드셨나요?(Y/N)')
                    if oil=='Y' or oil== 'y':
                        print('닥터 배아제를 복용하세요!')
                        break
                    elif oil=='N' or oil== 'n':
                        print('배아제를 복용하세요!')
                        break
                elif gas=='N' or gas== 'n':
                    eat=input('3. 과식을 하셨나요?(Y/N)')
                    if eat=='Y' or eat== 'y':
                        print('훼스탈 플러스정을 복용하세요!')
                        break
                    elif eat=='N' or eat== 'n':
                        print('큐자임정을 복용하세요!')
                        break
                    

            elif a=='N' or a== 'n':
                    baby=input('2. 임산부이신가요?(Y/N)')
                    if baby=='Y' or baby== 'y':
                        print('까스명수를 복용하세요!')
                        break
                    elif baby=='N' or baby== 'n':
                        pain=input('3. 배가 아픈가요?(Y/N)')
                        if pain=='Y' or pain== 'y':
                            print('까스명수를 복용하세요!')
                            break
                        elif pain=='N' or pain== 'n':
                            print('까스활명수를 복용하세요!')
                            break
            else:
                print('질문에 맞게 다시 입력해주세요')
                pass

        #계절성 알레르기약
        elif label=='antiallergic_drug':
            b=input('1. 결막염이 있습니까?(Y/N)')
            if b=='Y' or b== 'y':
                print('지르텍을 복용하세요!')
                break

            elif b=='N' or b== 'n':
                sleep=input('2. 졸림현상에 예민하신가요?(Y/N)')
                if sleep=='Y' or sleep== 'y':
                    print('지르텍을 복용하세요!')
                    break
                elif sleep=='N' or sleep== 'n':
                    print('클라리틴을 복용하세요!')
                    break
            else:
                print('질문에 맞게 다시 입력해주세요')
                pass


        #생리통약
        elif label=='menstrual_pain_medication':
            c=input('1. 아랫배 통증이 있습니까?(Y/N)')
            if c=='Y' or c== 'y':
                print('샤이닝정이나 부스코판 플러스정을 복용하세요!')
                break
            elif c=='N' or c=='n':
                camouflage=input('2. 위장장애가 있습니까?(Y/N)') #camouflage=위장
                if camouflage=='Y' or camouflage== 'y':
                    print('탁센이브나 이지엔6이브를 복용하세요!')
                    break
                if camouflage=='N' or camouflage== 'n':
                    print('탁센400을 복용하세요!')
                    break
            else:
                print('질문에 맞게 다시 입력해주세요')
                pass


        #파스
        elif label=='pain_relief_patch':
            d=input('1. 염증이 동반된 통증 입니까?(Y/N)')
            if d=='Y' or d=='y':
                feel=input('2. Cool한 느낌을 원하십니까?(Y/N)')
                if feel=='Y' or  feel=='y':
                    lotion=input('3. 로션형태를 원하십니까?(Y/N)')
                    if lotion=='Y' or lotion== 'y':
                        print('맨소래담 로션을 사용하세요!')
                        break
                    
                    elif lotion=='N' or  lotion=='n':
                        print('신신파스 COOL를 사용하세요!')
                        break

                elif feel=='N' or feel== 'n':
                    print('신신파스 HOT을 사용하세요!')
                    break

            elif d=='N' or d=='n':
                print('아렉스를 사용하세요!')
                break
            else:
                print('질문에 맞게 다시 입력해주세요')
                pass

        #연고
        elif label=='ointment':
            e=input('1. 다친 지 2~3주 정도 지났습니까?(Y/N)')
            if e=='Y' or e=='y':
                burn=input('2. 화상을 입었습니까?(Y/N)')
                if burn=='Y' or burn=='y':
                    print('힐텀스카겔을 사용하세요!')
                    break

                elif burn=='N' or burn== 'n':
                    antibiotic=input('3. 항생제가 들어있는 제품을 찾으시나요?(Y/N)') #antibiotic=항생제
                    if antibiotic=='Y' or antibiotic== 'y':
                        print('후시딘, 마데카솔 케어를 사용하세요!')
                        break

                    elif antibiotic=='N' or antibiotic== 'n':
                        print('메디폼을 사용하세요!')
                        break

            elif e=='N' or e== 'n':
                steroid=input('2.스테로이드 성분이 들어간 제품을 찾으시나요?(Y/N)')
                if steroid=='Y' or steroid== 'y':
                    print('복합 마데카솔을 사용하세요!')
                    break
                elif steroid=='N' or steroid== 'n':
                    print('마데카솔젤을 사용하세요!')
                    break
            else:
                print('질문에 맞게 다시 입력해주세요')
                pass
