import random 

def rand(): # rand함수 (컴퓨터 1부터 100까지 수 중에서 하나를 랜덤으로 골라주고 리턴해줌)
    num = random.randrange(1, 101)
    return num




print("UP & DOWN 게임에 오신 걸 환영합니다~")
nickname = [] # 이름 기록 리스트 
score = [] # 지금까지 점수 기록
buf = [] # 이름 + 점수 리스트
while 1:
    print("\n1. 게임시작 2. 기록확인 3. 게임종료")
    menu = int(input('>> '))
    ans = rand() # 랜덤으로 1~100까지 정수를 하나 반환
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
                    print('최고기록 갱신~!\n') # 점수리스트에 아무것도 없으면 최고점수
                    name=input('닉네임을 입력하세요 >> ') 
                    score.append(count) # 점수 리스트에 점수 추가
                    nickname.append(name) # 이름 리스트 맨 앞에 이름 추가
                    score.sort() # 리스트 오름차순으로 정렬해놓기(가장 작은수가 앞에 오므로 자동으로 1등이 score[0]이다.)
                    buf=[] # 값을 초기화 ( 이유 : 순위 순으로 넣어주기 위해 )
                    for i in range(0,len(score)): # 지금까지 기록된 기록 갯수
                        buf.append(nickname[i] + ' ' + str(score[i])) # buf 리스트에 닉네임 점수 형식으로 입력하기 위해
                    f=open("/Users/user/Documents/SWING/Python/score.txt", 'w') # buf 리스트에 순위 순으로 정보가 있으므로 w로 해준다.
                    for i in range(0,len(buf)): 
                        f.write(buf[i]+'\n') # 한줄씩 사용자의 닉네임과 점수 파일에 쓰기
                    f.close()
                    break  
                elif count < score[0]: # 1등 기록인 score[0]보다 작으면 최고 점수
                    print('최고기록 갱신~!\n')
                    name=input('닉네임을 입력하세요 >> ') # 닉네임 입력 받은 것 name변수에 저장
                    score.append(count) # 점수 리스트에 점수 추가
                    nickname.insert(0, name) # 이름 리스트 맨 앞에 이름 추가
                    score.sort() # 리스트 오름차순으로 정렬해놓기(가장 작은수가 앞에 오므로 자동으로 1등이 score[0]이다.)
                    buf=[]
                    for i in range(0,len(score)): # 지금까지 기록된 기록 갯수
                        buf.append(nickname[i] + ' ' + str(score[i])) # buf 리스트에 닉네임 점수 형식으로 입력하기 위해
                    f=open("/Users/user/Documents/SWING/Python/score.txt", 'w') # buf 리스트에 순위 순으로 정보가 있으므로 w로 해준다.
                    for i in range(0,len(buf)):
                        f.write(buf[i]+'\n') # 한줄씩 사용자의 닉네임과 점수 파일에 쓰기
                    f.close()
                    break
                else : # 1번 피드백 -> 최고기록 갱신을 하지 않았을때는 아무것도 기록하지 않고 넘어간다.
                    break
            else:
                print('비정상 종료!')
                break
    elif menu == 2 : # 기록확인
        print('\nrank/name/score')

        result=[]
        f=open("/Users/user/Documents/SWING/Python/score.txt", 'r') # 파일에서 읽어오기 r
        lines=f.read() # 문자열로 불러와서 lines에 담기
        if lines: # 읽어온 것이 있다면
            result=lines.split('\n') # 개행 문자을 기준으로 분리
            for i in range(0,len(result)-1):
                print(i+1, result[i]) # 1 mini 3 이라면 1은 (i+1) mini 3은 (result[i])
        else : # 읽어온 데이터가 없다면
            print("아직 기록이 없습니다.")
        f.close()
    
    elif menu == 3 : # 게임종료
        print("게임을 종료하겠습니다.")
        break
    else : 
        print('잘못 입력하셨습니다. 다시 입력해주세요!') # 사용자가 메뉴에 있는 1,2,3이 아닌 다른 수를 입력했을 때

    