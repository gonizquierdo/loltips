from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


class MapFunctions:
    """
    Current Summoner's Rift
    min: { x: 0, y: 0}
    max: { x: 14820, y: 14881}
    """
    def __init__(self):
        self._map = {
            "BLUE_BASE" : Polygon([(-120,-120), (561,5000), (1550,4900), (3500,4500), (4300,3700), (5000,1550), (5000,561)]),
            "RED_BASE": Polygon([(14500,14500), (9800,14200), (9800,13200), (10300,11100), (11100,10400), (13200,9800), (14200,9800)]),
            "TOP_LANE":Polygon([(561,5000), (561,14200), (9800,14200), (9800,13200), (4000,13200), (2800,12700), (2000,12000), (1550,4900)]),
            "MIDDLE_LANE":Polygon( [(3500,4500), (10300,11100), (11100,10400), (4300,3700)]),
            "BOTTOM_LANE":Polygon([(5000,1550),(11000,1700), (12000,2200), (12700,3000), (13200,4000), (13200,9800), (14200,9800), (14200,561), (5000,561)]),
            "JUNGLE_TOP":Polygon([(1550,4900), (2000,12000), (2800,12700), (4000,13200), (9800,13200), (9800,14200), (10300,11100), (3500,4500)]),
            "JUNGLE_BOT": Polygon([(4300, 3700), (11100,10400), (13200,9800), (13200,4000), (12700,3000), (12000,2200), (11000,1700),(5000,1550)])
        }

    def get_map_sector_by_xy(self, x, y):
        """

        :param x:
        :param y:
        :return: Sector where x,y coordinates are located.
        """

        point = Point(x,y)
        for sector in self._map:
            if self._map[sector].contains(point):
                res = sector

        return res

