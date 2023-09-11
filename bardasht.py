def  bardasht(input):
    global hesab
    if input <= hesab:
        hesab = hesab - input
    else:
        print("mojody hesabs shoma kafi namibashad")
