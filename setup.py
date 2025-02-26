from setuptools import setup, find_packages

setup(name='pytorch2timeloop',
        version='0.2',
        url='https://github.com/PN-54/pytorch2timeloop-converter',
        license='MIT',
        install_requires=[
            "torch==1.13.1",
            "torchvision==0.14.1",
            "numpy==1.22.4",
            "pyyaml==5.3",
            "transformers==4.26.0"
        ],
        dependency_links=[
            "https://download.pytorch.org/whl/cpu/"
        ],
        python_requires='>=3.6',
        include_package_data=True,
        packages=find_packages())
