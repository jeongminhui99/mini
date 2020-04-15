import random 


print("UP & DOWN 게임에 오신 걸 환영합니다~")
score = [] # 지금까지 점수 기록
while(1):
    print("1. 게임시작 2. 기록확인 3. 게임종료")
    menu = int(input('>> '))
    ans = random.randint(1,100) # 랜덤으로 1~100까지 정수를 하나 반환
    first = 1 # 숫자 고르기 범위 시작
    last = 100 # 숫자 고르기 범위 마지막
    count = 1 # 사용자가 도전한 게임 횟수(기회는 10회까지만 있음)
    if menu == 1 : # 게임시작
        while(count <= 11):
            if count==11: # count 11이면 게임종료
                print("입력횟수를 초과하였습니다! 게임오버!!")
                break
            user=int(input('%d번째 숫자 입력(%d~%d)>>'%(count, first, last))) # 사용자가 숫자 입력한 값 user
            if user > ans and user <= last: # 사용자가 입력한 값이 정답보다 크고 범위중 가장 큰 수 보다 작을 때
                count += 1 # 도전 수 1추가
                print("DOWN") 
                last = user # 범위의 마지막수가 사용자가 입력한 값으로 바뀜
            elif user < ans and user >= first: # 사용자가 입력한 값이 정답보다 작고 범위중 가장 작은 수보다 클 때
                count += 1 # 도전 수 1 추가
                print("UP")
                first = user # 범위 중 가장 작은 수(처음 수)가 사용자가 입력한 값으로 바뀜
            elif user > last or user < first: # 범위중 가장 큰수보다 크거나 범위 중 가장 작은 수보다 작을 때 
                print("범위 밖 숫자입니다. 다시 입력해주세요.") # 도전 수가 올라가지는 않음
            elif user == ans: # 사용자가 입력한 값이 정답일 때
                print('정답입니다!!')
                print('%d번째만에 맞추셨습니다' %count) # 몇 번째로 맞췄는지 count로 알려줌
                if not score:
                    print('최고기록 갱신~!') # 점수리스트에 아무것도 없으면 최고점수
                    score.append(count) # 점수 리스트에 점수 추가
                    score.sort() # 리스트 오름차순으로 정렬해놓기(가장 작은수가 앞에 오므로 자동으로 1등이 score[0]이다.)
                    break  
                elif count < score[0]: # 1등 기록인 score[0]보다 작으면 최고 점수
                    print('최고기록 갱신~!')
                    score.append(count) # 점수 리스트에 점수 추가
                    score.sort() # 리스트 오름차순으로 정렬해놓기(가장 작은수가 앞에 오므로 자동으로 1등이 score[0]이다.)
                    break
                else :
                    score.append(count) # 최고 점수가 아니면 그냥 점수만 추가한다.
                    score.sort() # 리스트 오름차순으로 정렬해놓기(가장 작은수가 앞에 오므로 자동으로 1등이 score[0]이다.)
                    break
            else:
                print('비정상 종료!')
                break
    elif menu == 2 : # 기록확인
        for i in range(0,len(score)): # score리스트 인덱스가 i이면 등수는 i+1이므로 리스트에 저장되어 있는 순서대로 i+1과 같이 출력
            print(i+1, score[i])
    
    elif menu == 3 : # 게임종료
        print("게임을 종료하겠습니다.")
        break
    else : 
        print('잘못 입력하셨습니다. 다시 입력해주세요!') # 사용자가 메뉴에 있는 1,2,3이 아닌 다른 수를 입력했을 때

        