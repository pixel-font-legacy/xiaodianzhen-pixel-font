import json
import shutil
import zipfile

from loguru import logger

from tools import configs
from tools.configs import path_define
from tools.configs.options import FontFormat


def make_release_zips(font_sizes: list[int], font_formats: list[FontFormat]):
    path_define.releases_dir.mkdir(parents=True, exist_ok=True)

    for font_format in font_formats:
        file_path = path_define.releases_dir.joinpath(f'xiaodianzhen-pixel-font-{font_format}-v{configs.version}.zip')
        with zipfile.ZipFile(file_path, 'w') as file:
            file.write(path_define.project_root_dir.joinpath('LICENSE-FONT.md'), 'README.md')
            for font_size in font_sizes:
                file_path = path_define.outputs_dir.joinpath(f'xiaodianzhen-{font_size}px.{font_format}')
                file.write(file_path, file_path.name)
        logger.info("Make release zip: '{}'", file_path)


def update_www(font_sizes: list[int]):
    if path_define.www_fonts_dir.exists():
        shutil.rmtree(path_define.www_fonts_dir)
    path_define.www_fonts_dir.mkdir(parents=True)

    for path_from in path_define.outputs_dir.iterdir():
        if not path_from.name.endswith('.otf.woff2'):
            continue
        path_to = path_from.copy_into(path_define.www_fonts_dir)
        logger.info("Copy file: '{}' -> '{}'", path_from, path_to)

    db_file_path = path_define.www_fonts_dir.joinpath('db.js')
    db_file_path.write_text(f'export default {json.dumps(font_sizes, indent=4, ensure_ascii=False)}\n', 'utf-8')
    logger.info("Build: '{}'", db_file_path)

    css_file_path = path_define.www_fonts_dir.joinpath('index.css')
    with css_file_path.open('w', encoding='utf-8') as file:
        for font_size in font_sizes:
            file.write('\n')
            file.write('@font-face {\n')
            file.write(f'    font-family: xiaodianzhen-{font_size}px;\n')
            file.write(f'    src: url("xiaodianzhen-{font_size}px.otf.woff2");\n')
            file.write('}\n')
    logger.info("Build: '{}'", css_file_path)
