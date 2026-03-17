from vcgencmd import Vcgencmd
import warnings, psutil
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
        cpu = psutil.cpu_percent(interval=1)  # → 7.2
        temp_str = f"Temperature: {vcgm.measure_temp()}°C CPU: {cpu}%"
        print(temp_str)
        client.publish(f"pi/temps/{NAME}", temp_str)
        sleep(10)

if __name__ == "__main__":
    main()


