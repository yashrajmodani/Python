from abc import abstractmethod, ABC


class SmartDevice:
    def __init__(self,name="", status=""):
        self._name = name
        self._status = status
        self._bg_level = 0

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    def device_info(self):
        return f"Device name: {self._name} & Status: {self._status}"

    def set_brightness(self, bg_level):
        self._bg_level=bg_level
        return f"The brightness level is set to {self._bg_level}"

class SmartLight(SmartDevice, ABC):
    def __init__(self, name="", status=""):
        super().__init__(name,status)
    def turn_on(self):
        self._status = "ON"
        return f"Light is ON"


    def turn_off(self):
        self._status = "OFF"
        return f"Light is OFF"


light = SmartLight("Greed's light", "OFF")

print(light.set_brightness(80))
print(light.turn_on())
print(light.turn_off())
print(light.device_info())
