


from dog import

if __name__ == '__main__':
    
    Summer = Dog('Summer', True)

    Winter = Dog('Winter', False)

    print('Winter has this many legs: ' + str(Winter.legs))
    print('Summer has this many legs: ' + str(Summer.legs))

    print(Summer.horrible_accident())

    print('Winter has this many legs: ' + str(Winter.legs))