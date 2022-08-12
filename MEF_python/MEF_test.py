
import unittest
import MEF as mef

class TestMef(unittest.TestCase):

    def test_start(self):
        self.assertEqual(mef.start(''), False, msg="Retorno Falso no start")
        self.assertEqual(mef.start('a'), False, msg="Retorno falso no S0")
        self.assertEqual(mef.start('aa'), False, msg="Retorno falso no S4")
        self.assertEqual(mef.start('bbaa'), False, msg="Retorno falso no S4")
        self.assertEqual(mef.start('aabb'), False, msg="Retorno falso no S4")
        self.assertEqual(mef.start('bb'), True, msg="Retorno verdadeiro no s3")
        self.assertEqual(mef.start('abb'), True, msg="Retorno verdadeiro no s2")
        self.assertEqual(mef.start('bba'), False, msg="Retorno falso no s0")
        self.assertEqual(mef.start('abbbc'), False, msg="Retorno falso no s0")

    def test_s0(self):
        self.assertEqual(mef.s0(''), False, msg="Retorno falso no s0")
        self.assertEqual(mef.s0('aaaa'), False, msg="Retorno falso no s4")
        self.assertEqual(mef.s0('abba'), False, msg="Retorno falso no s0")
        self.assertEqual(mef.s0('b'), False, msg="Retorno falso no s1")
        self.assertEqual(mef.s0('a'), False, msg="Retorno Falso no s0")
        self.assertEqual(mef.s0('c'), False, msg="Retorno Falso no s0")
    def test_s1(self):
        self.assertEqual(mef.s1(''), False, msg="Retorno falso no s1")
        self.assertEqual(mef.s1('a'), False, msg="Retorno falso no s0")
        self.assertEqual(mef.s1('abb'), False, msg="Retorno falso no s4")
        self.assertEqual(mef.s1('b'), True, msg="Retorno verdadeiro no s2")
        self.assertEqual(mef.s1('ba'), False, msg="Retorno falso no s0")
        self.assertEqual(mef.s1('cba'), False, msg="Retorno falso no s0")

    def test_check_language(self):
        self.assertEqual(mef.check_language('aaabb'), 'aaabb: não pertence')
        self.assertEqual(mef.check_language('aaababb'), 'aaababb: não pertence')
        self.assertEqual(mef.check_language('aaab'), 'aaab: não pertence')
        self.assertEqual(mef.check_language('ababa'), 'ababa: não pertence')
        self.assertEqual(mef.check_language('abbabba'), 'abbabba: não pertence')
        self.assertEqual(mef.check_language('abbabb'), 'abbabb: pertence')
        self.assertEqual(mef.check_language('bb'), 'bb: pertence')
        self.assertEqual(mef.check_language('abb'), 'abb: pertence')
        self.assertEqual(mef.check_language('abbc'), 'abbc: não pertence')
if __name__ == '__main__':
    unittest.main()