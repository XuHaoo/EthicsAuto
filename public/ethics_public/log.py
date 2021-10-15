import logging
import unittest


class MyTestCase(unittest.TestCase):
    #
    # def test_something(self):
    #
    #     self.assertEqual(True, False)

    # 创建Logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # 创建Handler

    # 终端Handler
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.DEBUG)

    # 文件Handler
    fileHandler = logging.FileHandler('log.log', mode='w', encoding='UTF-8')
    fileHandler.setLevel(logging.NOTSET)

    # Formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    consoleHandler.setFormatter(formatter)
    fileHandler.setFormatter(formatter)

    # 添加到Logger中
    logger.addHandler(consoleHandler)
    logger.addHandler(fileHandler)


if __name__ == '__main__':
    unittest.main()
