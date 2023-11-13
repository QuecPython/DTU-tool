# Copyright (c) Quectel Wireless Solution, Co., Ltd.All Rights Reserved.
#  
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#  
#     http://www.apache.org/licenses/LICENSE-2.0
#  
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
from pathlib import Path


DEFAULT_LANGUAGE = 'en_US'
LANGUAGE_DESC = {
    'en_US': "English(US)",
    "zh_CN": "简体中文"
}
LANGUAGE_NAME = None
TRANSLATION_MAP = {}


def get_language_code(name):
    for k, v in LANGUAGE_DESC.items():
        if name == v:
            return k
    else:
        raise ValueError('can not found language code for: {}'.format(name))

def get_language():
    global LANGUAGE_NAME
    if LANGUAGE_NAME is not None:
        return LANGUAGE_NAME
    path = Path(__file__).with_name('language')
    if path.exists():
        with path.open('r') as f:
            LANGUAGE_NAME = f.read()
            return LANGUAGE_NAME
    else:
        LANGUAGE_NAME = DEFAULT_LANGUAGE
    return LANGUAGE_NAME


def set_language(code):
    path = Path(__file__).parent / 'language'
    if code not in LANGUAGE_DESC:
        raise ValueError('un supported language: {}'.format(code))
    with path.open('w') as f:
        f.write(code)


def init_translation_map():
    global TRANSLATION_MAP
    language_name = get_language()
    language_file_path = Path(__file__).with_name(language_name + '.json')
    if language_file_path.exists():
        with open(str(language_file_path), 'r', encoding='utf8') as f:
            TRANSLATION_MAP = json.load(f)


# load translation file to a dict
init_translation_map()


def tr(stringvar):
    temp = None
    if LANGUAGE_NAME == 'zh_CN':
        temp = TRANSLATION_MAP.get(stringvar, None)
    temp = temp or stringvar
    return temp
