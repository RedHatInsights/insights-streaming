from setuptools import setup, find_packages


runtime = set([
    'insights-core',
    'six',
])


develop = set([
    'flake8',
    'pytest',
    'ipython',
])


if __name__ == "__main__":
    setup(
        name="insights_streaming",
        version="0.0.1",
        description="Insights Streaming is an analysis framework for streaming data.",
        long_description=open("README.md").read(),
        url="https://github.com/redhatinsights/insights-streaming",
        author="Red Hat, Inc.",
        author_email="csams@redhat.com",
        packages=find_packages(),
        install_requires=list(runtime),
        package_data={'': ['LICENSE']},
        license='Apache 2.0',
        extras_require={
            'develop': list(runtime | develop),
        },
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Natural Language :: English',
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6'
        ],
        include_package_data=True
    )
