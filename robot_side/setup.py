from setuptools import find_packages, setup

package_name = 'robot_side'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='developer8g@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            f'math_server = {package_name}.math_server:main',
            f'publisher = {package_name}.publisher:main',
            f'subscriber = {package_name}.subscriber:main',
        ],
    },
)
