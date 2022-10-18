class image_label_data:

    def __init__(self, xmin: float, ymin: float, xmax: float, ymax: float, label: str, label_index: int):
        self._xmin = xmin
        self._ymin = ymin
        self._xmax = xmax
        self._ymax = ymax
        self._label = label
        self._label_index = label_index

    def get_xmin(self) -> float:
        return self._xmin

    def get_ymin(self) -> float:
        return self._ymin

    def get_xmax(self) -> float:
        return self._xmax

    def get_ymax(self) -> float:
        return self._ymax

    def get_label(self) -> str:
        return self._label

    def get_label_index(self) -> str:
        return self._label_index