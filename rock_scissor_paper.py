import random
def get_player_choice():
    """
    get_player_choice() -> string
    return : "바위" or "가위" or "보"
    """    
    while True:
        player_pick = input("당신의 선택은 ? : ")
        if player_pick =="바위" or player_pick == "가위" or player_pick == "보":
            return player_pick

def get_cpu_choice():    
    """
    get_cpu_choice -> int
    return 0 or 1 or 2
    0:바위
    1:가위
    2:보
    """
    cpu_pick = random.randint(0, 2)    
    return cpu_pick

def who_wins(player, cpu):
    
    cpu_string = ("바위", "가위", "보")
    print(player+" vs "+cpu_string[cpu])    
    if player=="바위" and cpu==0 or player=="가위" and cpu==1 or player=="보" and cpu==2:
            return "none"
    elif player=="바위" and cpu==1 or player=="가위" and cpu==2 or player=="보" and cpu==0:
            return("you")
    else: return("cpu")

def play_one():
    """
    play_one-> string
    return : 플레이어가 이기면 'player'
            컴퓨터가 이기면 'computer'
    """
    while True:
        string=get_player_choice()
        cpu = get_cpu_choice()

        win=who_wins(string, cpu)

        if win!="none":
            return win            
        else: print("draw")

def check_final_winner(result):
    """
    check_final_winner(result) -> string
    result : ex) ['player', 'player']
    return : result 안에 player가 2개 이상이면: player
                        com이 2개 이상이면 : com
            그렇지 않다면, none
    """
    if result.count("you")>2:
        return "player"
    elif result.count("cpu")>2:
        return "computer"
    else: return "none"

def play():    
    result_list=[]
    final_winner = "none"
    while final_winner=="none":
        result_list.insert(0, play_one())
        print(f"player : {result_list.count('you')} , computer : {result_list.count('cpu')}")
        final_winner = check_final_winner(result_list)            
    
    if final_winner=="player":
        print("님 축하")
    else: print("ㅉㅉ")
if __name__=="__main__":
    play()

    