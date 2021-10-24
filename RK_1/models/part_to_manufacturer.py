class PartToManufacturer:
    """Многие ко многим"""

    def __init__(self, part_id, manufacturer_id):
        self.part_id = part_id
        self.manufacturer_id = manufacturer_id