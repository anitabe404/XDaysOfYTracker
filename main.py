import datetime as dt
import challenge_tracker as ct

if __name__ == '__main__':
    start_date = input('Enter start date in ISO format: ')
    duration = int(input('Enter challenge duration in days: '))

    new_challenge = ct.ChallengeTracker(start_date, duration)

    print()
    print("================== Your Challenge Information ====================")
    print(f'Your start date is {new_challenge.start_date.strftime("%b %d, %Y")}')
    print(f'Your end date is {new_challenge.end_date.strftime("%b %d, %Y")}')
    print(f'You are currently on Day {new_challenge.currentDay()}')
    print(f'You have {new_challenge.remainingDays()} days left')
    print("===================================================================")