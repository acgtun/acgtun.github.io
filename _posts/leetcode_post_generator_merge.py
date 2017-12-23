import os
import sys
import time
from os import walk

reload(sys)
sys.setdefaultencoding('utf8')

langs = {'cpp': 'cpp', 'java': 'java', 'python': 'py'}
path = '/Users/haifeng.chen/gitcode/leetcode/algorithms'


def write_posts(problems, solutions):
    for problem in problems:
        create_time = time.localtime()
        file_name = time.strftime("%Y-%m-%d-", create_time) + problem.replace(' ', '-') + '.md'
        file = open(file_name, 'w')
        file.write('---\n')
        file.write('layout: post\n')
        file.write('title: ' + problem + '\n')
        file.write('date: ' + time.strftime("%Y-%m-%d %H:%M:%S", create_time) + '\n')
        file.write('categories: leetcode\n')
        file.write('---\n\n')

        file.write('<div class="tab">\n')
        for lang in langs.keys():
            if problem in solutions[lang]:
                file.write('<button class="tablinks" onclick="openCity(event, ' + "'" + lang + "'" + ')">' + lang + '</button>\n')
        file.write('</div>\n')

        for lang in langs.keys():
            if problem in solutions[lang]:
                content = solutions[lang][problem]
                file.write('<div id="' + lang + '" class="tabcontent">\n')
                file.write('<h3>' + lang + '</h3>\n')
                file.write('```' + lang + '\n')
                content = content.replace('{{', '{ {').replace('}}', '} }')
                file.write(content + '\n')
                file.write('```\n')
                file.write('</div>\n')
        file.close()


if __name__ == '__main__':

    solutions = {}
    problems = set()
    for lang in langs.keys():
        solutions[lang] = {}
        dir = os.path.join(path, lang)
        for dirpath, dirnames, filenames in walk(dir):
            for file in filenames:
                if file == '.DS_Store':
                    continue
                problem = file.replace('.' + langs[lang], '')
                print(problem)
                file_path = os.path.join(dir, file)
                with open(file_path, 'r') as content_file:
                    content = content_file.read()
                    solutions[lang][problem] = content
                    print(content)
                problems.add(problem)

    # write posts
    write_posts(problems, solutions)
