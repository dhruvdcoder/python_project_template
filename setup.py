from setuptools import setup, find_packages
import os

PATH_ROOT = os.path.dirname(__file__)
with open("README.md", "r") as fh:
    long_description = fh.read()


def load_requirements(path_dir=PATH_ROOT, comment_char='#'):
    with open(os.path.join(path_dir, 'core_requirements.txt'), 'r') as file:
        lines = [ln.strip() for ln in file.readlines()]
    reqs = []

    for ln in lines:
        # filer all comments

        if comment_char in ln:
            ln = ln[: ln.index(comment_char)]

        if ln:  # if requirement is not empty
            reqs.append(ln)

    return reqs


install_requires = load_requirements()

setup(
    name='<<[.custom.project.package_name]>>',
    version='0.0.1',
    author="<<[(index .custom.project.authors 0).name ]>>",
    author_email="<<[(index .custom.project.authors 0).email ]>>",
    description='<<[.custom.project.description]>>',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="<<[.custom.project.url]>>",
    project_urls={
        'Documentation': '<<[.custom.project.project_urls.documentation]>>',
        'Source Code': '<<[.custom.project.project_urls.source_code]>>',
    },
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests", "examples"]
    ),
    package_data={'box_embeddings': ['py.typed']},
    install_requires=install_requires,
    keywords=[<<[range .custom.project.keywords ]>>"<<[.]>>", <<[ end ]>>],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Development Status :: 3 - Alpha' 'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    python_requires='>=3.5',
)
