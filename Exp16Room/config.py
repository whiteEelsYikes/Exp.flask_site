
"""
该文件是 urls.py 路由的配置文件
是 urls.py 路由依据

这里是可以使用 Sqlite 来实现的
但我选择更为轻量级的方式 pyconfig

"""
import os
from flask import jsonify


server_config = {
    'SMB': {
        'html': 'server.html',
        'md': 'SMB_server.md',
        'title': 'SMB服务使用教程'
    },
    'CloudDisk': {
        'html': 'server.html',
        'md': 'CloudDisk_server.md',
        'title': '云盘服务使用教程',
    },
    'RMI': {
        'html': 'server.html',
        'md': 'RMI_server.md',
        'title': '资源服务使用教程',
    },
    'ORS': {
        'html': 'server.html',
        'md': 'ORS_server.md',
        'title': '其他服务使用教程',
    },
    'index': {
        'html': 'server.html',
        'md': 'server.md',
        'title': '服务合集',
    },
    'Undefined': {
        'html': 'server.html',
        'md': 'Undefined_server.md',
        'title': '404未找到的服务',
    },
}


documentation_config = {
    'Docsify': {
        'html': 'doc.html',
        'doc': 'Docsify.md',
        'title': 'Docsify模板',
    },
    'SMB': {
        'html': 'doc.html',
        'doc': 'SMB_server_doc.md',
        'title': 'SMB服务文档',
    },
    'CloudDisk': {
        'html': 'doc.html',
        'doc': 'CloudDisk_server_doc.md',
        'title': '云盘服务文档',
    },
    'RMI': {
        'html': 'doc.html',
        'doc': 'RMI_server_doc.md',
        'title': '资源服务文档',
    },
    'ORS': {
        'html': 'doc.html',
        'doc': 'ORS_server_doc.md',
        'title': '其他服务文档',
    },
    'index': {
        'html': 'doc.html',
        'doc': 'doc.md',
        'title': '文档合集',
    },
    'Undefined': {
        'html': 'doc.html',
        'doc': 'Undefined_doc.md',
        'title': '404未找到的文档',
    },
}


egg_hunt_index_config = {
    'html': 'egg_hunt.html',
    'md': 'egg_hunt.md',
    'title': 'Exp.16Room彩蛋合集',
}

egg_hunt_config = {
    'graduate': {
        'html': 'graduate.html',
    },
}

egg_hunt_undefined_config = {
    'html': 'egg_hunt.html',
    'doc': 'Undefined_egg_hunt.md',
    'title': '404未布置的彩蛋',
}

album_index_config = {
    'html': 'album.html',
    'md': 'album_info.md',
    'title': '留影集册合集',
}

album_config = {
    'root': f'{os.path.dirname(os.path.relpath(__file__))}/template/static/album',
    'database_album': '',
}




