import os
from setuptools import setup, find_packages

def package_files(where):
    paths = []
    for directory in where:
        for (path, directories, filenames) in os.walk(directory):
            for filename in filenames:
                paths.append(os.path.join(path, filename).replace('src/metrics/', ''))
    return paths


extra_files = [] #package_files(['src/metrics/assets'])
console_scripts = []

#console_scripts.append('{0}={1}.app:main'.format(find_packages('src')[0].replace('_', '-'),
 #                                                 find_packages('src')[0]))

setup(entry_points={'console_scripts': console_scripts},
      packages=find_packages(where='src'),
      package_dir={'': 'src'},
      package_data={'': extra_files})