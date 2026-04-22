from setuptools import find_packages, setup

package_name = 'rfid_pubsub'

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
    maintainer='javier',
    maintainer_email='javier.borquez@usach.cl',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = rfid_pubsub.publisher_member_function:main',
            'listener = rfid_pubsub.subscriber_member_function:main',
            'rfid_talker = rfid_pubsub.rfid_publish:main',
        ],
    },
)
