import setuptools
from pathlib import Path

PATH_ROOT = Path(__file__).parent.resolve()


def get_long_description():
    description = (PATH_ROOT / "README.md").read_text(encoding="utf-8")
    # replace relative repository path to absolute link to the release
    static_url = f"https://github.com/DefTruth/lite.ai.toolkit/blob/main/pylitex"
    description = description.replace("docs/res/", f"{static_url}/docs/res/")
    return description


setuptools.setup(
    name="litex",
    version="0.0.1",
    author="DefTruth",
    author_email="qyjdef@163.com",
    description="A Python version of lite.ai.toolkit based on opencv and onnxruntime.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/DefTruth/lite.ai.toolkit",
    packages=setuptools.find_packages(),
    install_requires=[
        "opencv-python=4.5.2",
        "numpy>=1.14.4",
        "torch>=1.6.0",
        "onnxruntime>=1.7.0",
        "onnx>=1.8.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    include_package_data=True
)
