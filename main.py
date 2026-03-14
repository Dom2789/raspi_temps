from vcgencmd import Vcgencmd
import warnings

def main():
    warnings.filterwarnings("ignore", category=SyntaxWarning, module="vcgencmd")
    print("Hello from raspi-temps!")

    vcgm = Vcgencmd()
    print(f"Temperature: {vcgm.measure_temp()}°C")

if __name__ == "__main__":
    main()
