"""
1) list
2) Create a Scoreboard
3) Nested For loops to generate pattern
a)                  b)              c)                  d)
* * * * *           1 1 1 1 1       0 0 0 0 0           0
* * * * *           1 1 1 1 1       1 1 1 1 1           1 0
* * * * *           1 1 1 1 1       0 0 0 0 0           0 1 0
* * * * *           1 1 1 1 1       1 1 1 1 1           1 0 1 0
* * * * *           1 1 1 1 1       0 0 0 0 0           0 1 0 1 0

e)                  f)              g)                  h)
1                   1 2 3 4 5       01 02 03 04 05      1 0 1 0 1
1 0                 1 2 3 4 5       06 07 08 09 10      0 1 0 1
1 0 1               1 2 3 4 5       11 12 13 14 15      1 0 1
1 0 1 0             1 2 3 4 5       16 17 18 19 20      0 1
1 0 1 0 1           1 2 3 4 5       21 22 23 24 25      1

i)                  j)              k)                  l)
      1             * *   * *       01 02 03 04 05      2
   1    1           *  * *  *       05 04 03 02 01      2 4
  1   1   1         *   *   *       02 04 06 08 10      2 4 8
1   1   1   1       *       *       10 08 06 04 02      2 4 8 16
                    *       *       03 06 09 12 15      2 4 8 16 32
                                    15 12 09 06 03      2 4 8 16 32 64
m)  *       *
    * *   * *
    *   *   *
    *       *
    *       *
"""
'''
runs = 0

wickets = 0
max_wickets = 10

overs = 0
max_overs = 2

current_ball_in_over = 0
no_of_balls_in_over = 6

types_of_runs = ['0', '1', '2', '3', '4', '5', '6']
types_of_extras = ['wb', 'nb']
types_of_wickets = ['lbw', 'b', 'catch', 'ro', 'stump', 'htw']


print(F"Types of runs: {', '.join(types_of_runs)}")
print(F"Types of wickets: {', '.join(types_of_wickets)}")

_run_types = ' '.join(types_of_runs)
string = "Types of runs: {}".format(_run_types)

print('------------')
print(F'{runs} / {wickets}')
print(F'{overs}.{current_ball_in_over} ({max_overs})')

while True:
    if wickets == 10 or overs == max_overs:
        break
    print('------------')

    _input = str(input("Enter run: ")).strip()
    if _input in types_of_extras:
        runs += 1

    elif _input in types_of_runs:
        runs += int(_input)
        current_ball_in_over += 1

    elif _input in types_of_wickets:
        wickets += 1
        current_ball_in_over += 1
    else:
        print('Wrong input')

    if current_ball_in_over == no_of_balls_in_over:
        overs += 1
        current_ball_in_over = 0

    print(F'{runs} / {wickets}')
    print(F'{overs}.{current_ball_in_over} ({max_overs})')
'''

for i in range(0, 5):
    for j in range(0, 5):
        print("*", end=" ")
    print("")
