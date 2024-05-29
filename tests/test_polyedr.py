import unittest
from unittest.mock import patch, mock_open

from shadow.polyedr import Polyedr


class TestPolyedrBox(unittest.TestCase):

    @classmethod
    def setUpClass(self):
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
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_num_vertexes(self):
        self.assertEqual(len(self.polyedr.vertexes), 8)

    def test_num_facets(self):
        self.assertEqual(len(self.polyedr.facets), 4)

    def test_num_edges(self):
        self.assertEqual(len(self.polyedr.edges), 16)

    def test_area(self):
        self.assertAlmostEqual(self.polyedr.get_area(), 4.0)


class TestPolyedrSurfaceCf200(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        fake_file_content = """200.0	0.0	0.0	0.0
4	1	4
3.0     0.0     0.0
3.0     0.0     4.0
8.0     0.0     4.0
8.0     0.0     0.0
4	1    2    3    4"""
        fake_file_path = 'data/surface200.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_num_vertexes(self):
        self.assertEqual(len(self.polyedr.vertexes), 4)

    def test_num_facets(self):
        self.assertEqual(len(self.polyedr.facets), 1)

    def test_num_edges(self):
        self.assertEqual(len(self.polyedr.edges), 4)

    def test_area(self):
        self.assertAlmostEqual(self.polyedr.get_area(), 20.0)


class TestPolyedrSurfaceCf2000(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        fake_file_content = """2000.0	0.0	0.0	0.0
4	1	4
3.0     0.0     0.0
3.0     0.0     4.0
8.0     0.0     4.0
8.0     0.0     0.0
4	1    2    3    4"""
        fake_file_path = 'data/surface2000.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_num_vertexes(self):
        self.assertEqual(len(self.polyedr.vertexes), 4)

    def test_num_facets(self):
        self.assertEqual(len(self.polyedr.facets), 1)

    def test_num_edges(self):
        self.assertEqual(len(self.polyedr.edges), 4)

    def test_area(self):
        self.assertAlmostEqual(self.polyedr.get_area(), 20.0)


class TestPolyedrSurfaceRotation(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        fake_file_content = """200.0	45.0	11.0	115.0
4	1	4
3.0     0.0     0.0
3.0     0.0     4.0
8.0     0.0     4.0
8.0     0.0     0.0
4	1    2    3    4"""
        fake_file_path = 'data/surface2000.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_num_vertexes(self):
        self.assertEqual(len(self.polyedr.vertexes), 4)

    def test_num_facets(self):
        self.assertEqual(len(self.polyedr.facets), 1)

    def test_num_edges(self):
        self.assertEqual(len(self.polyedr.edges), 4)

    def test_area(self):
        self.assertAlmostEqual(self.polyedr.get_area(), 20.0)


class TestPolyedrSurfaceYZ(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        fake_file_content = """200.0	0.0	0.0	0.0
4	1       4
3.0     0.0     0.0
3.0     4.0     0.0
8.0     4.0     0.0
8.0     0.0     0.0
4	1    2    3    4"""
        fake_file_path = 'data/surface2000.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_num_vertexes(self):
        self.assertEqual(len(self.polyedr.vertexes), 4)

    def test_num_facets(self):
        self.assertEqual(len(self.polyedr.facets), 1)

    def test_num_edges(self):
        self.assertEqual(len(self.polyedr.edges), 4)

    def test_area(self):
        self.assertAlmostEqual(self.polyedr.get_area(), 20.0)
