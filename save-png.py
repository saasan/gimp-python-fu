#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""PNG形式で画像を保存する"""

import os
from gimpfu import *


FILENAME_ENCODING = 'cp932'


def generate_new_filename(filename):
    """拡張子を.pngにしたファイル名を作成"""
    dirname = os.path.dirname(filename)
    basename_without_ext = os.path.splitext(os.path.basename(filename))[0]
    new_filename = os.path.join(dirname, basename_without_ext + '.png')
    return new_filename


def plugin_func():
    for image in gimp.image_list():
        # 拡張子を.pngにしたファイル名を作成
        filename = generate_new_filename(image.filename)
        # 複製して新しい画像を作成
        new_image = pdb.gimp_image_duplicate(image)
        # レイヤーを統合
        layer = new_image.flatten()
        # 画像を保存
        pdb.gimp_file_save(new_image, layer, filename, '')
        # 複製した画像を削除
        pdb.gimp_image_delete(new_image)


register(
    'save_png',
    'PNG形式で画像を保存',
    'help message',
    'author',
    'copyright',
    'year',
    'PNG形式で画像を保存',
    '*',
    [],
    [],
    plugin_func,
    menu='<Image>/Tools'
)

main()
