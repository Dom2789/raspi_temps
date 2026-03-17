from vcgencmd import Vcgencmd
import warnings
from time import sleep
import paho.mqtt.client as mqtt

NAME = "nextpi"

def main():
    warnings.filterwarnings("ignore", category=SyntaxWarning, module="vcgencmd")
    print("Hello from raspi-temps!")

    vcgm = Vcgencmd()
    client = mqtt.Client()
    client.connect("192.168.178.100", 1883)

    while True:
        temp = vcgm.measure_temp()
        temp_str = f"Temperature: {vcgm.measure_temp()}°C"
        print(temp_str)
        client.publish(f"pi/temps/{NAME}", temp_str)
        sleep(10)

if __name__ == "__main__":
    main()
