import time
import dice_set as ds


def tim(start_time):
    current_time = time.time()
    elap = current_time - start_time
    if 30-int(elap) <= 0:
        print('時間到!')
    return elap <= 30


# 判斷位置是否重疊
def check_position(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) <= 100:
                return True
    return False


# 骰骰子
def dice_play(dice, width_ran, height_ran):
    for index, value in enumerate(dice):
        if value == 1:
            ds.dice1(width_ran[index], height_ran[index])
        elif value == 2:
            ds.dice2(width_ran[index], height_ran[index], width_ran[index] % 2)
        elif value == 3:
            ds.dice3(width_ran[index], height_ran[index], height_ran[index] % 2)
        elif value == 4:
            ds.dice4(width_ran[index], height_ran[index])
        elif value == 5:
            ds.dice5(width_ran[index], height_ran[index])
        else:
            ds.dice6(width_ran[index], height_ran[index])
