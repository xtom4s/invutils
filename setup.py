from setuptools import setup, find_packages

setup(name = "invutils",
      description = "Tools aimed at investing and portfolio tracking, mainly for cryptocurrency",
      version = "1.0.1",
      url = "https://github.com/xtom4s/inverutilities",
      license = "MIT License",
      author = "Tom4s",
      author_email = "tom4s.rr@gmail.com",
      packages = find_packages(),
      install_requires = [  # Fails with ["time", "base64"] - They are removed as they are built-in modules
	      "requests",
	      "pandas",
	      "datetime",
      	],
      classifiers = [
	      "Programming Language :: Python",
	      "Development Status :: 1 - Beta",
	      "Intended Audience :: Anyone who knows python",
	      "License :: OSI Approved :: MIT License",
	      "Operating System :: OS Independent"
      	]
)
