# this is the master version number
import distrib_test2
VERSION = distrib_test2.__version__

SRC_DIR = 'distrib_test2'

if __name__ == '__main__':
  import setuptools
  setuptools.setup(
    version = VERSION,
    name = "distrib-test-2",
    url='https://github.com/pp-mo/distrib_test_2',
    packages = [SRC_DIR],
    author='ppmo',
    author_email='avd-support@metoffice.gov.uk',
)

