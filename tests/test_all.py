#!/usr/bin/python3
"""Unit test of the requirements for the project in general"""

import unittest
import os


class Test_all(unittest.TestCase):
    """Class to test the project"""

    def test_all(self):
        """Check the project requirements
        """
        self.assertTrue(os.path.isfile('README.md'))
        self.assertTrue(os.path.isfile('./models/__init__.py'))
        self.assertTrue(os.path.isfile('./models/engine/__init__.py'))
        self.assertTrue(os.path.isfile('./tests/__init__.py'))
        self.assertTrue(os.path.isfile('./tests/test_models/__init__.py'))
        self.assertTrue(os.path.isfile(
            './tests/test_models/test_engine/__init__.py'))

        flist = ['console.py', './models/base_model.py',
                 './models/city.py', './models/place.py',
                 './models/review.py', './models/state.py',
                 './models/user.py',
                 './models/engine/file_storage.py']

        for filee in flist:
            pep8 = "pep8 --count {}".format(filee)
            self.assertEqual(os.system(pep8), 0, filee)
            self.assertTrue(os.path.isfile(filee), filee)
            self.assertTrue(os.access(filee, os.X_OK), filee)
            with open(filee) as f:
                first = f.readline()
                last = f.read()[-1]
                self.assertTrue(first == '#!/usr/bin/python3\n', filee)
            self.assertTrue(len(filee.__doc__) > 5)


if __name__ == '__main__':
    unittest.main()
