from vcgencmd import Vcgencmd

def main():
    print("Hello from raspi-temps!")

    vcgm = Vcgencmd()
    print(vcgm.version())
    print(vcgm.measure_temp())


if __name__ == "__main__":
    main()
