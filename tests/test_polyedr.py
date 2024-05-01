import unittest
from unittest.mock import patch, mock_open

from shadow.polyedr import Polyedr


class TestPolyedr(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        fake_file_content = """200.0	45.0	45.0	30.0
8	4	16
-0.5	-0.5	0.5
-0.5	0.5	0.5
0.5	0.5	0.5
0.5	-0.5	0.5
-0.5	-0.5	-0.5
-0.5	0.5	-0.5
0.5	0.5	-0.5
0.5	-0.5	-0.5
4	5    6    2    1
4	3    2    6    7
4	3    7    8    4
4	1    4    8    5"""
        fake_file_path = 'data/holey_box.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            cls.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_num_vertexes(self):
        self.assertEqual(len(self.polyedr.vertexes), 8)

    def test_num_facets(self):
        self.assertEqual(len(self.polyedr.facets), 4)

    def test_num_edges(self):
        self.assertEqual(len(self.polyedr.edges), 16)

    def test_box1(self):
        fake_file_content = """200.0   45.0    45.0    30.0
8       6       24
-5    -5    5
-5    5     5
5     5     5
5     -5    5
-5    -5    -5
-5    5     -5
5     5     -5
5     -5    -5
4       1    2    3    4
4       5    6    2    1
4       3    2    6    7
4       3    7    8    4
4       1    4    8    5
4       8    7    6    5
"""
        fake_file_path = 'data/ccc.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)
        self.assertEqual(self.polyedr.area, 0)

    def test_box2(self):
        fake_file_content = """1   0    0    0
8       6       24
-1.5    -1.5    0
-1.5    0     0
0     0     0
0     -1.5    0
-1.5    -1.5    -1.5
-1.5    0     -1.5
0     0     -1.5
0     -1.5    -1.5
4       1    2    3    4
4       5    6    2    1
4       3    2    6    7
4       3    7    8    4
4       1    4    8    5
4       8    7    6    5
"""
        fake_file_path = 'data/ccc.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)
        self.assertAlmostEqual(self.polyedr.area, 6 * (1.5 ** 2))

    def test_half_good_box1(self):
        fake_file_content = """1   0    0   0
8       6       24
-1    -1    2
-1    2     2
2     2     2
2     -1    2
-1    -1    -1
-1    2     -1
2     2     -1
2     -1    -1
4       1    2    3    4
4       5    6    2    1
4       3    2    6    7
4       3    7    8    4
4       1    4    8    5
4       8    7    6    5
"""
        fake_file_path = 'data/ccc.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)
        self.assertAlmostEqual(self.polyedr.area, 5 * (3 ** 2))

    def test_half_good_box2(self):
        fake_file_content = """1   0    0   0
8       6       24
4    4    1
4    1     1
1     1     1
1     4    1
4    4    4
4    1     4
1     1     4
1     4    4
4       1    2    3    4
4       5    6    2    1
4       3    2    6    7
4       3    7    8    4
4       1    4    8    5
4       8    7    6    5
"""
        fake_file_path = 'data/ccc.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)
        self.assertAlmostEqual(self.polyedr.area, 5 * (3 ** 2))
