from flask import render_template, redirect, url_for, request, jsonify, abort
from . import *
from .func import *
from .config import *


@Exp16Room_blue.route("/")
def Exp16Room_index():
    return rendering_markdown("Exp16R_index.html", 'Exp16Room.md', 'Exp.16Room')


@Exp16Room_blue.route("/server")
def Exp16Room_server():
    if request.method == "GET":
        server_name = request.args.get("server")
        if server_name is None:
            return rendering_markdown(**server_config.get('index'))
        keyword = server_config.get(server_name)
        if keyword is None:
            return rendering_markdown(**server_config.get('Undefined'))
        return rendering_markdown(**keyword)
    return abort(404)


@Exp16Room_blue.route("/doc")
def Exp16Room_doc():
    if request.method == "GET":
        doc_name = request.args.get("doc")
        if doc_name is None:
            return rendering_doc(**documentation_config.get('index'))
        keyword = documentation_config.get(doc_name)
        if keyword is None:
            return rendering_doc(**documentation_config.get('Undefined'))
        return rendering_doc(**keyword)
    return abort(404)


@Exp16Room_blue.route("/egg_hunt")
def Exp16Room_egg_hunt():
    if request.method == "GET":
        egg_hunt_name = request.args.get("name")
        if egg_hunt_name is None:
            return rendering_markdown(**egg_hunt_index_config)
        keyword = egg_hunt_config.get(egg_hunt_name)
        if keyword is None:
            return rendering_doc(**egg_hunt_undefined_config)
        return rendering_egg_hunt(**keyword)
    return abort(404)


@Exp16Room_blue.route("/album", methods=["GET", "POST"])
def Exp16Room_album():
    if request.method == "GET":
        album_state = {  # 由于不知名的原因 暂时无法抽象到 config.py 可以使用函数返回方式进行尝试 这里就暂时不进行抽象
            'album_path_not_found': jsonify({'state': 'The specified album was not found!'}),
            'column_path_not_found': jsonify({'state': 'The specified column was not found!'}),
            'img_file_not_found': jsonify({'state': 'The specified img was not found!'}),
        }
        album, column, img = request.args.get("album"), request.args.get("column"), request.args.get('img')
        if album is None:
            return rendering_markdown(**album_index_config)
        album_path = album_config.get(album)
        if album_path is None:
            return album_state.get('album_path_not_found')
        if column is None:
            return get_album_column_info(album_path, **album_state)
        if img is None:
            return get_album_column_info(album_path, column, **album_state)
        return get_album_column_info(album_path, column, img, **album_state)
    elif request.method == "POST":
        pass
    return abort(404)


@Exp16Room_blue.route("/album/show")
def Exp16Room_album_show():
    return render_album(album_config.get('root'))


@Exp16Room_blue.route("/members")
def Exp16Room_members():
    if request.method == "GET":
        group = request.args.get('group')
        return abort(404)
    elif request.method == "POST":
        return abort(404)
    return abort(404)


