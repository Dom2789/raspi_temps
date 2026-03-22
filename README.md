# raspi-temps

A Python script that monitors Raspberry Pi CPU temperature and usage, publishing the data to an MQTT broker at regular intervals.

## Features

- Reads CPU temperature via `vcgencmd`
- Reads CPU usage percentage via `psutil`
- Publishes metrics to an MQTT topic every 10 seconds
- Supports a configurable device name via command-line argument

## Requirements

- Raspberry Pi (with `vcgencmd` available)
- Python 3.12+
- Running MQTT broker

## Dependencies

- `paho-mqtt >= 2.1.0`
- `psutil >= 7.2.2`
- `vcgencmd >= 0.1.1`

## Installation

```bash
uv sync
```

## Usage

```bash
python main.py [-n NAME]
```

| Argument | Description | Default |
|----------|-------------|---------|
| `-n NAME` | Name of the Raspberry Pi (used in MQTT topic) | `default` |

## MQTT

- **Broker:** `192.168.178.100:1883`
- **Topic:** `pi/temps/{name}`
- **Payload example:** `Temperature: 42.8°C CPU: 7.2%`

Messages are published every 10 seconds.
