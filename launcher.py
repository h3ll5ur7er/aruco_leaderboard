from rc_leaderboard import main

if __name__ == "__main__":
    while True:
        try:
            main("0.0.0.0", 80)
        except Exception as e:
            print(e)

