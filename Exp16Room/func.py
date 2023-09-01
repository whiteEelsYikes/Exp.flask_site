import os
from json import loads, dump
from markdown import markdown
from flask import render_template, Markup, jsonify, send_file
from . import Exp16Room_blue as blueprint


def rendering_markdown(html, md, title):
    extensions = [
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.tables',
        'markdown.extensions.toc',
    ]
    md_content = ""
    if ('\\' not in md) and ('/' not in md):
        markdown_path = os.path.dirname(blueprint.root_path + blueprint.template_folder)
        md = rf'{markdown_path}\template\markdown\{md}' if '\\' in markdown_path else rf'{markdown_path}/template/markdown/{md}'
    with open(md, 'r', encoding='utf-8') as f:
        md_content = f.read()
    md_html = markdown(md_content, extensions=extensions)
    content = Markup(md_html)
    # Markup就是把内容转换成字符串，str不可以
    # 也可以不用这个，但是前端的内容要加safe，像这样 {{content | safe}}
    return render_template(html, content=content,
                           title=title)  # content = content 可以换成 ** local(), 这个是把所有的参数都传过去    return render_template('Exp16R_index.html', content=content)


def rendering_docx(html, docx, title):
    pass


def rendering_pdf(html, pdf, title):
    pass


def rendering_txt(html, txt, title):
    pass


def rendering_doc(html, doc, title):
    doc_path, doc_type = doc.rsplit('.', 1)
    if doc_type == 'md':
        return rendering_markdown(html=html, md=doc, title=title)
    elif doc_type == 'docx':
        pass
    elif doc_type == 'pdf':
        pass
    elif doc_type == 'txt':
        pass
    else:
        raise TypeError('不支持的doc类型(文件类型)')


def rendering_egg_hunt(html):
    return render_template(html)


def get_album_column_info(album_path, column=None, img=None, info_json_name='album_info.json', encoding='utf-8',
                          album_path_not_found=None, column_path_not_found=None, img_file_not_found=None,
                          ):
    album_path_not_found = album_path_not_found if not (album_path_not_found is None) else jsonify(
        {'state': 'The specified album was not found!'})
    column_path_not_found = column_path_not_found if not (column_path_not_found is None) else jsonify(
        {'state': 'The specified column was not found!'})
    img_file_not_found = img_file_not_found if not (img_file_not_found is None) else jsonify(
        {'state': 'The specified img was not found!'})
    if not (column is None):
        info_json = os.path.join(album_path, column, info_json_name)
        if not os.path.exists(info_json):
            return column_path_not_found  # 如果 没有找到符合要求的 column
        if img is None:
            with open(info_json, 'r', encoding=encoding) as file:  # 这里使用 .json 配置数据 可以修改 扫描目录 动态生成目录对应的 json
                dict_json = loads(file.read())
            return jsonify(dict_json)
        img = os.path.join(album_path, column, img)
        if not os.path.exists(os.path.join(img)):
            return img_file_not_found
        return send_file(img)  # 返回 图片/视频
    if not os.path.exists(album_path):
        return album_path_not_found  # 如果 没有找到符合要求的 album
    listdir = os.listdir(album_path)
    album_dict = {}
    for item in listdir:
        item_path = os.path.join(album_path, item)
        info_json = os.path.join(item_path, info_json_name)
        if (not os.path.isdir(item_path)) or (not os.path.exists(info_json)):
            continue
        with open(info_json, 'r', encoding=encoding) as file:  # 这里使用 .json 配置数据 可以修改 扫描目录 动态生成目录对应的 json
            dict_json = loads(file.read())
        album_dict.update(
            {
                item: dict_json,
            }
        )
    return jsonify(album_dict)


def post_album_column_info(album_path, column=None, img=None, info_json_name='album_info.json', encoding='utf-8',
                           new_column=None,
                           album_path_not_found=None, column_path_not_found=None, img_file_not_found=None, ):
    album_path_not_found = album_path_not_found if not (album_path_not_found is None) else jsonify(
        {'state': 'The specified album was not found!'})
    column_path_not_found = column_path_not_found if not (column_path_not_found is None) else jsonify(
        {'state': 'The specified column was not found!'})
    img_file_not_found = img_file_not_found if not (img_file_not_found is None) else jsonify(
        {'state': 'The specified img was not found!'})


def render_album(album_path, column=None, info_json_name='album_info.json', encoding='utf-8'):
    listdir = os.listdir(album_path)
    album_dict = {}
    for item in listdir:
        item_path = os.path.join(album_path, item)
        info_json = os.path.join(item_path, info_json_name)
        if (not os.path.isdir(item_path)) or (not os.path.exists(info_json)):
            continue
        with open(info_json, 'r', encoding=encoding) as file:  # 这里使用 .json 配置数据 可以修改 扫描目录 动态生成目录对应的 json
            dict_json = loads(file.read())
        album_dict.update(
            {
                item: dict_json,
            }
        )
    return render_template('album_show.html', album_dict=album_dict)
