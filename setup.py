from setuptools import setup

setup(
    name='math_quiz',
    version='1.0.0',    
    description='A math quiz',
    author='Alap Mundayoor',
    license='Apache',
    packages=['math_quiz'],
    install_requires=['random', 'unittest'                    
                      ],

    classifiers=[
        'Development Status :: Game',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache-2.0 license', 
    ],
)