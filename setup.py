# setup.py

"""Setup script."""

from setuptools import setup

with open('requirements.txt', 'r', encoding='UTF-8') as f:
    required: list[str] = f.read().splitlines()

with open("README.md", 'r', encoding='UTF-8') as f:
    long_description: str = f.read()

setup(
    name='wolfsoftware.shamir-secret-sharing',
    version='0.1.1',
    packages=['wolfsoftware.shamir_secret_sharing'],
    entry_points={
        'console_scripts': [
            'shamir-secret-sharing=wolfsoftware.shamir_secret_sharing.main:main',
        ],
    },
    author='Wolf Software',
    author_email='pypi@wolfsoftware.com',
    description="A CLI implementation of Shamir's secret sharing",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/GreyTeamToolbox/shamir-secret-sharing-package',
    project_urls={
        ' Source': 'https://github.com/GreyTeamToolbox/shamir-secret-sharing-package',
        ' Tracker': 'https://github.com/GreyTeamToolbox/shamir-secret-sharing-package/issues/',
        ' Documentation': 'https://github.com/GreyTeamToolbox/shamir-secret-sharing-package',
        ' Sponsor': 'https://github.com/sponsors/WolfSoftware',
    },
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
    ],
    python_requires='>=3.9',
    install_requires=required,
)
