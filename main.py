from vcgencmd import Vcgencmd

def main():
    print("Hello from raspi-temps!")

    vcgm = Vcgencmd()
    print("Temperature: " + vcgm.measure_temp() + "°C")

if __name__ == "__main__":
    main()
