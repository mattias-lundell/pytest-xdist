from setuptools import setup

setup(
    name="pytest-xdist",
    version='1.8.dev2',
    description='py.test xdist plugin for distributed testing and loop-on-failing modes',
    long_description=open('README.txt').read(),
    license='GPLv2 or later',
    author='holger krekel and contributors',
    author_email='py-dev@codespeak.net,holger@merlinux.eu',
    url='http://bitbucket.org/hpk42/pytest-xdist',
    platforms=['linux', 'osx', 'win32'],
    packages = ['xdist'],
    entry_points = {'pytest11': ['xdist = xdist.plugin'],},
    zip_safe=False,
    install_requires = ['execnet>=1.0.8', 'pytest>=2.2.1.dev2'],
    classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Operating System :: POSIX',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: MacOS :: MacOS X',
    'Topic :: Software Development :: Testing',
    'Topic :: Software Development :: Quality Assurance',
    'Topic :: Utilities',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    ],
)
