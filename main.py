from vcgencmd import Vcgencmd
import warnings, psutil, argparse
from time import sleep
import paho.mqtt.client as mqtt

def main():
    print("Hello from raspi-temps!")

    name = "default"
    # parsing command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-n")
    args = parser.parse_args()
    if args.n is not None:
        name = args.n

    warnings.filterwarnings("ignore", category=SyntaxWarning, module="vcgencmd")

    vcgm = Vcgencmd()
    client = mqtt.Client()
    client.connect("192.168.178.100", 1883)

    while True:
        cpu = psutil.cpu_percent(interval=1)  # → 7.2
        temp_str = f"Temperature: {vcgm.measure_temp()}°C CPU: {cpu}%"
        print(temp_str)
        client.publish(f"pi/temps/{name}", temp_str)
        sleep(10)

if __name__ == "__main__":
    main()


