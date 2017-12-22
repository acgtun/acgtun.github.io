# generate a markdown file with link to each problem
import os
from os import walk

if __name__ == '__main__':
    langs = {'cpp': 'cpp', 'java': 'java', 'python': 'py'}
    path = '/Users/haifeng.chen/gitcode/leetcode/algorithms'

    solutions = {}
    problems = set()
    for lang in langs.keys():
        solutions[lang] = {}
        dir = os.path.join(path, lang)
        for dirpath, dirnames, filenames in walk(dir):
            for file in filenames:
                if file == '.DS_Store':
                    continue
                problem = file.replace('.' + langs[lang], ' ')
                solutions[lang][problem] = os.path.join(dir, file).replace(' ', '\%20')
                print(lang)
                print(problem)
                # print(os.path.join(link, lang, file).replace(' ', '\%20'))
                problems.add(file.replace('.' + langs[lang], ' '))

    md_file = 'leetcode.html'
    f = open(md_file, 'w')
    f.write('---\n')
    f.write('layout: default\n')
    f.write('title : Leetcode Solutions\n')
    f.write('---\n\n')

    f.write('<center><h1><a href="https://leetcode.com/problemset/algorithms/">https://leetcode.com/problemset/algorithms</a></h1></center>\n\n')
    f.write('<table border="1" align="center">')
    f.write('<tr> <td><b>Problem</b></td> <td><b>C/C++</b></td> <td><b>Java</b></td></tr>\n')
    for problem in problems:
        cpp_link = ''
        cpp_show = ''
        java_link = ''
        java_show = ''
        python_link = ''
        python_show = ''
        # problem_link = 'https://leetcode.com/problems/{}'.format(problem.replace(' ', '-'))
        if (problem in solutions['cpp'].keys()):
            cpp_show = 'cpp'
            cpp_link = solutions['cpp'][problem]
        if (problem in solutions['java'].keys()):
            java_show = 'java'
            java_link = solutions['java'][problem]
        if (problem in solutions['python'].keys()):
            python_show = 'python'
            python_link = solutions['python'][problem]
        problem = problem.strip()
        f.write('<tr>\n')
        f.write('\t<td>{}</td>\n'.format(problem))
        if len(cpp_show) == 0:
            f.write('\t<td></td>\n')
        else:
            f.write(
                '\t<td><a href="{}">{}</a></td>\n'.format('/posts/' + problem.replace(' ', '-') + '.' + cpp_show,
                                                          cpp_show))
        if len(java_show) == 0:
            f.write('\t<td></td>\n')
        else:
            f.write(
                '\t<td><a href="{}">{}</a></td>\n'.format('/posts/' + problem.replace(' ', '-') + '.' + java_show,java_show))

        """                                                  
        if len(python_show) == 0:
            f.write('\t<td></td>\n')
        else:
            f.write('\t<td><a href="{}">{}</a></td>\n'.format('/posts/' + problem.replace(' ', '-') + '.' + python_show,
                                                              python_show))
        """
        f.write('</tr>\n\n')
    f.write('</table>')
    f.close()
