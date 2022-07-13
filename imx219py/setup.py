from setuptools import setup

package_name = 'imx219py'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Wang Guangfu',
    maintainer_email='buaawgf@hotmail.com',
    description='This is python version of imx 219 monocular capturing node.',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	"imx219_pub = imx219py.imx219_pub:main",
        	"imx219_sub = imx219py.imx219_sub:main",
        ],
    },
)
