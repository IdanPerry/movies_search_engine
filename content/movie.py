from dataclasses import dataclass


@dataclass
class MovieContent:
    """
    This class represents a movie.
    """
    
    _title: str
    _year: int
    _rating: float
    _type: str
    _actors: str
    _trailer: str
    _description: str
    _source: str
    _url: str
    _image: str

    @classmethod
    def by_data(cls, data):
        return cls(
            _title=data.title,
            _year=data.year,
            _type=data.type,
            _rating=data.rating,
            _description=data.description,
            _actors=data.actors,
            _trailer=data.trailer,
            _source='',
            _url='',
            _image=''
            )

    @classmethod
    def by_content(cls, content):
        return cls(        
            _title=content.name,
            _type=content.type,
            _url=content.url,
            _image=content.image,
            _source=content.source,
            _year=0,
            _rating=0.0,
            _trailer='',
            _actors='',
            _description=''
            )

    def __repr__(self) -> str:
        return f'{self._title} {self._year} {self._rating}'

    def __eq__(self, other) -> bool:
        return self._title == other.title

    def __hash__(self) -> int:
        return hash(self._title)

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, value):
        self._year = value
    
    @property
    def rating(self) -> float:
        return self._rating

    @rating.setter
    def rating(self, value):
        self._rating = value

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def actors(self) -> str:
        return self._actors

    @actors.setter
    def actors(self, value):
        self._actors = value

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def trailer(self) -> str:
        return self._trailer

    @trailer.setter
    def trailer(self, value):
        self._trailer = value

    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    @property
    def image(self) -> str:
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def source(self) -> str:
        return self._source

    @source.setter
    def source(self, value):
        self._source = value

    def merge(self, data):
        """
        Merges two MovieContent objects with partial data.
        """
        
        self._year = data.year
        self._trailer = data.trailer
        self._rating = data.rating
        self._description = data.description
        self._actors = data.actors
