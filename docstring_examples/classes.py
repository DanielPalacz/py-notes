
import logging
from typing import TypeAlias

LoggerT: TypeAlias = logging.Logger


class LinksExtractor:
    def __init__(self, logger: LoggerT) -> None:
        self.logger = logger


class CareerLinksFetcher(LinksExtractor):
    """Extracts a-tag career related links from provided list of links.

    Usage:
        career_links = CareerLinksExtractor().get_career_links(url)

    Args:
        logger (LoggerT): logger object

    Attributes:
        CAREER_KEYWORDS (list): list with career related keywords
        logger (LoggerT): logger object
    """

    CAREER_KEYWORDS = [
        ...
    ]

    def __init__(self, logger: LoggerT) -> None:
        super().__init__(logger)

    def get_career_links(self, baseurl: str) -> list[str]:
        """Filters for potential career related links from list of the links.

        Args:
            baseurl: base part of url

        Returns:
            List with potential career related links.
        """
        pass


class Monument:
    pass


class MonumentItem:
    """Class for representing monuments and solving sorting issue.

    Args:
        data (Monument): Monument from the 'Monument' model class.
        latitude (str): Latitude of the monument.
        longitude (str): Longitude of the monument.

    Attributes:
        __data (Monument): Monument object (from the 'Monument' model class).
        __latitude (float): Latitude of the monument.
        __longitude (float): Longitude of the monument.
        __reference_measure (float): Calculated reference measure.
    """

    def __init__(self, data: Monument, latitude: str, longitude: str):
        self.__data = data
        self.__latitude = float(latitude)
        self.__longitude = float(longitude)
        self.__reference_measure = self.calc_reference_measure()

    def calc_reference_measure(self) -> float:
        """Provides calculated reference measure.

        Returns:
            Calculated reference measure (float).
        """
        pass
