def cToFConverter():
    while True:
        cTemp = input("Please enter C degree: ")
        if cTemp:
            cTemp = float(cTemp)
            # fTemp = 9 * cTemp / 5 + 32
            fTemp = round(9 * cTemp / 5 + 32, 1)
            print(f"{cTemp}C is converted to {fTemp}F")
            break

        else:
            print("cTemp input is empty")
            continue # tiep tuc vong lap


def main():
    # print("hello world")
    cToFConverter()


if __name__ == '__main__':
    main()
