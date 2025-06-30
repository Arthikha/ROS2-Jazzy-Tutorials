from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'core_concepts'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/task3', ['core_concepts/task3/values.csv']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='arthi',
    maintainer_email='arthi@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pose_re_pub = core_concepts.task1.pose_re_pub:main',
            'params_setter = core_concepts.task2.params_setter:main',
            'twist_from_database = core_concepts.task3.twist_from_database:main',
            'zero_twist = core_concepts.task4.zero_twist:main',
            'param_reader = core_concepts.task6.param_reader:main',
            'chatter = test.chatter:main',
            'listener = test.listener:main'
        ],
    },
)
