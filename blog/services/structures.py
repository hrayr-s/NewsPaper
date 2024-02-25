import dataclasses
import datetime
from typing import List


@dataclasses.dataclass
class Article(object):
    id: int
    title: str
    description: str
    content: str
    published_at: datetime.datetime
    slug: str
    author: str
    tags: List[str]
    cover_image_url: str
    category_name: str
    related_categories_ids: List[int]
