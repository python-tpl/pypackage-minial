# -*- coding:utf-8 -*-

import delegator
from candy_prompt.prompt import *


def construct():
    history = os.path.join(os.path.expanduser('~'), '.templates', 'tpl.history')
    author = delegator.run("git config --get user.name").out.strip()
    licenses = ['Apache License 2.0',
                'MIT License',
                'BSD 2-clause "Simplified" License',
                'BSD 3-clause "New" or "Revised" License',
                'Eclipse Public License 1.0',
                'GNU General Public License v2.0',
                'GNU Lesser General Public License v2.1',
                'GUN General Public License V3.0',
                'GNU Affero General Public License v3.0',
                'GNU Lesser General Public License v3.0',
                'Mozilla Public License 2.0']
    classifiers_file = open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'classifiers'))
    classifier_options = [c.strip() for c in classifiers_file if c.strip()]
    res = {
        'package_name': prompt('Package Name: ', history=history),
        'description': prompt('Description: ', history=history),
        'author': prompt_list('Author: ', default=author, history=history),
        'license': prompt_list('License: ', default='MIT License', completions=licenses, history=history)
    }
    classifiers = []
    while True:
        input = prompt_list('Classifier: ', completions=classifier_options)
        if input == 'q':
            break
        classifiers.append(input)
    res.update({'classifiers': classifiers})
    return res
