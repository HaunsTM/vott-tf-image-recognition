class image_measurement_data:

    def __init__(self, height: int, width: int):
        self._height = height
        self._width = width

    def get_height(self) -> int:
        return self._height

    def get_width(self) -> int:
        return self._width
