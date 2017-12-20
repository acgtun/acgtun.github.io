import os
import sys
import time
from os import walk

reload(sys)
sys.setdefaultencoding('utf8')


def write_post(problem, lang, content, create_time):
    create_time = time.gmtime(create_time)
    file_name = time.strftime("%Y-%m-%d-%H-%M-%S", create_time)
    file = open(file_name + '-' + problem.replace(' ', '-') + '.md', 'w')
    file.write('---\n')
    file.write('layout: post\n')
    file.write('title: ' + problem + '\n')
    file.write('date: ' + time.strftime("%Y-%m-%d %H:%M:%S", create_time) + '\n')
    file.write('categories: leetcode\n')
    file.write('---\n\n')
    #file.write('{{ % raw %}}\n\n')
    #file.write('{{% highlight ' + lang + ' %}}\n\n')
    file.write('```' + lang + '\n')
    file.write('{{ % raw %}}\n')
    file.write('{{')
    file.write(content + '\n')
    file.write('}}\n')
    file.write('{{ % endraw %}}\n')
    file.write('```')
    #file.write('{{% endhighlight %}}\n')
    #file.write('{{ % endraw %}}\n\n')
    file.close()


def get_solutions():
    langs = ['cpp', 'java', 'python']
    path = os.path.join(os.path.expanduser('~/gitcode/leetcode/algorithms/'))
    print('path: {}'.format(path))
    problems = {}
    for lang in langs:
        dir = os.path.join(path, lang)
        for dirpath, dirnames, filenames in walk(dir):
            for file in filenames:
                problem = file.replace('.' + lang, '')
                if problem not in problems.keys():
                    problems[problem] = {}
                file_path = os.path.join(dir, file)
                with open(file_path, 'r') as content_file:
                    content = content_file.read()

                write_post(problem, lang, content, os.path.getmtime(file_path))


if __name__ == '__main__':
    get_solutions()
