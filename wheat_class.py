from crop_class import *
class Wheat(Crop):
    """A potato crop"""
    def __init__(self):
        #growth rate = 1; light need = 3; water need = 6
        super().__init__(1,3,6)
        self._type = "Wheat"

    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
            if self._status == "Seedling" and water > self._water_need:
                self._growth += self._growth_rate *2
            elif self._status == "Young" and water > self._water_need:
                self._growth += self._growth_rate *1.5
            else:
                self._growth =+ self._growth_rate
        self._days_growing =+ 1
        self._update_status()

def main():
    wheat_crop = Wheat()
    print(wheat_crop.report())
    manual_grow(wheat_crop)
    print(wheat_crop.report())
    manual_grow(wheat_crop)
    print(wheat_crop.report())

if __name__ == "__main__":
    main()
