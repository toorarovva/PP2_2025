import time
from insert_from_console1 import insert_from_console
from connect1 import connect
 
def save_game_state(user_id, level, score):
    conn = connect()
    cur = conn.cursor()
 
    cur.execute("INSERT INTO user_score (user_id, level, score) VALUES (%s, %s, %s)", (user_id, level, score))
    conn.commit()
    cur.close()
    conn.close()
    print(f"Game saved successfully: User {user_id}, Level {level}, Score {score}")
 
def start_game():
    user_id = insert_from_console()
    level = 1
    score = 0
    levels = [
        {"level": 1, "speed": 5},
        {"level": 2, "speed": 7},
        {"level": 3, "speed": 10}
    ]
 
    while True:
        print(f"Level {level}, Speed: {levels[level - 1]['speed']}")
        score += 10 
        action = input("Press Enter to continue or 'P' to pause: ").lower()
        if action == 'p':
            save_game_state(user_id, level, score)
            break
 
        
        if level < len(levels):
            level += 1
 
    print("Game paused.")
 
if __name__ == '__main__':
    start_game()