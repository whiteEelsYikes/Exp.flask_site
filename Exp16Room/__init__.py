from flask import Blueprint

Exp16Room_blue = Blueprint(
    'Exp16Room',
    __name__,
    url_prefix='/Exp16R',
    static_folder='./template/static',
    template_folder='./template',
    root_path='./Exp16Room/'
)
from . import urls
