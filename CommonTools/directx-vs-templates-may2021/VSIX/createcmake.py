import argparse
from pathlib import Path
import shutil
import os

def replace_single_projectname(template_dir, str_file_name, target_dir, project_name):
        template_path = template_dir + '/' + str_file_name
        reader = open(template_path, 'r')
        input_data = reader.read()
        output_data = input_data.replace('$projectname$', project_name)
        output_data = output_data.replace('$safeprojectname$', project_name)
        target_path = target_dir + '/' + str_file_name
        writer = open(target_path, 'w')
        writer.write(output_data)

def replace_projectname(template_dir, file_names, target_dir, project_name):
    for file_name in file_names:
        str_file_name = file_name.name
        replace_single_projectname(template_dir, str_file_name, target_dir, project_name)

def copy_files(src_paths, target_path):
    for src_path in src_paths:
        shutil.copy(src_path, target_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some arguments')
    parser.add_argument('templatedir')
    parser.add_argument('projectname')
    parser.add_argument('targetdir')

    args = parser.parse_args()
    
    template_dir = args.templatedir
    project_name = args.projectname
    target_dir = args.targetdir

    template_dir = os.path.abspath(template_dir)

    if not Path(template_dir + '/' + 'CMakeLists.txt').exists():
        print(template_dir, ' does not contain a CMakeLists.txt')
        exit()

    cpplist = Path(template_dir).glob('*.cpp')
    headerlist = Path(template_dir).glob('*.h')

    target_dir = os.path.abspath(target_dir)
    target_dir_path = Path(target_dir)
    if not target_dir_path.exists():
        try:
            target_dir_path.mkdir(parents=True)
        except BaseException:
            print('Can not make directory: ', target_dir_path)

    replace_projectname(template_dir, cpplist, target_dir, project_name)
    replace_projectname(template_dir, headerlist, target_dir, project_name)

    replace_single_projectname(template_dir, 'CMakeLists.txt', target_dir, project_name)

    #shutil.copy(Path(template_dir + '/' + 'CMakeLists.txt'), target_dir_path)
    copy_files(Path(template_dir).glob('*.json'), target_dir_path)
    copy_files(Path(template_dir).glob('*.rc'), target_dir_path)
    shutil.copy(Path(template_dir + '/' + 'directx.ico'), target_dir_path)
    shutil.copy(Path(template_dir + '/' + 'settings.manifest'), target_dir_path)

