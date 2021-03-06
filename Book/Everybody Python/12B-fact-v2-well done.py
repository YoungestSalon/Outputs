
while True:                                                                                         # 무한반복 프로그램으로 설정
    
    user_choice = input("덧셈/곱셈 프로그램입니다. 덧셈과 곱셈 중 선택해주세요. 프로그램을 중지하고 싶으시다면 중지를 입력해주세요.")       # 사용자 설정 입력 요청

    if user_choice == str("중지"):                                                                  # 중지 입력 시 명령어 설정
        print("그럼, 안뇨옹~")
        break                                                                                       # 중지 입력 시 프로그램이 멈춤

    else:                                                                                           # 중지 외의 내용을 입력할 시 명령어 설정
        if user_choice == str("덧셈"):                                                              # 덧셈 입력 시 명령어 설정
    
            def sum_func(n,m):                                                                      # 덧셈 함수 설정
                s = n
                for x in range (n+1, m+1):
                    s = s+x
                return s

            user1 = input("두 개의 숫자를 골라주시면 두 숫자 사이의 모든 숫자를 더한 합을 구합니다. 시작 숫자를 알려주세요. 단, 시작 숫자는 끝 숫자보다 작아야 하며 정수여야 합니다.")
            user2 = int(user1)                                                                      # 덧셈 시작 값을 입력 받아 정수로 변환하여 저장
            user3 = input("끝 숫자를 알려주세요. 끝 숫자 역시 정수여야 합니다.")
            user4 = int(user3)                                                                      # 덧셈 끝 값을 입력 받아 정수로 변환하여 저장

            print(user1,"부터",user3,"까지의 합은",sum_func(user2, user4),"입니다.")                # 결과값을 사용자에게 출력 (출력 후 프로그램은 자동으로 재시작)


        else:                                                                                       # 중지도, 덧셈도 아닌 다른 명령어 입력 시 명령 설정
            if user_choice == str("곱셈"):                                                          # 곱셈 입력 시 명령어 설정
                def factorial(m,n):                                                                 # 곱셈 함수 설정
                    fact = m
                    for x in range(m+1, n+1):
                        fact = fact * x
                    return fact

                user1 = input("두 개의 숫자를 골라주시면 두 숫자 사이의 모든 숫자를 곱한 결과값을 구합니다. 시작 숫자를 알려주세요. 단, 시작 숫자는 끝 숫자보다 작아야 하며 정수여야 합니다.")
                user2 = int(user1)                                                                  # 곱셈 시작 값을 입력 받아 정수로 변환하여 저장
                user3 = input("끝 숫자를 알려주세요. 시작 숫자와 마찬가지로 정수여야 합니다.")
                user4 = int(user3)                                                                  # 곱셈 끝 값을 입력 받아 정수로 변환하여 저장

                print(user1,"부터",user3,"까지 곱한 결과는",factorial(user2, user4),"입니다.")      # 결과값을 사용자에게 출력 (출력 후 프로그램은 자동으로 재시작)

            else:
                print("입력값이 틀렸습니다. 덧셈/곱셈/중지 중 한 가지를 입력해주세요. 프로그램의 시작점으로 돌아갑니다.")            #덧셈/곱셈/중지가 아닌 경우 프로그램 재시작        

