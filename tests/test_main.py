import unittest

from db_learning import configuration

class TestConfig(unittest.TestCase):
    def test_config(self):
        config = configuration.get_db_config('../data/config.json')

        self.assertEqual(config['dbName'], 'testdb')
        self.assertEqual(config['user'], 'testdb')
        self.assertEqual(config['token'], 'testdb')
        self.assertEqual(config['host'], 'localhost')
        self.assertEqual(config['port'], 5432)

if __name__ == '__main__':
    unittest.main()
