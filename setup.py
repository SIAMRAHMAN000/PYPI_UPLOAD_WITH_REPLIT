from setuptools import setup, find_packages
#MAO2116
setup(
    name='PAKAGE NAME',
    packages=find_packages(),
    include_package_data=True,
    version="#######VERSION###",
    description='',
    author='SIAM RAHMAN',
    author_email='s14mbro1@gmail.com',
    long_description=(open("README.md","r")).read(),
    long_description_content_type="text/markdown",
   install_requires=['lolcat','requests','bs4','rich'],
 
    keywords=['ADD TAGS'],
    classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
            'Operating System :: OS Independent',
            'Environment :: Console',
    ],
    
    license='MIT',
    entry_points={
            'console_scripts': [
                'CMD NAME = FROM NAME.IMPORT NAME:MAIN CODE NAME',
                
            ],
    },
    python_requires='>=3.6'
)
