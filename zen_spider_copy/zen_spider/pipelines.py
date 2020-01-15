# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb

class MySQLPipeline:
    """
    ItemをMySQLに保存するPipeline。
    """

    def open_spider(self, spider):
        """
        Spiderの開始時にMySQLサーバーに接続する。
        itemsテーブルが存在しない場合は作成する。
        """
        settings = spider.settings  # settings.pyから設定を読み込む。
        params = {
            'host': settings.get('MYSQL_HOST', 'localhost'),  # ホスト
            'db': settings.get('MYSQL_DATABASE', 'scraping'),  # データベース名
            'user': settings.get('MYSQL_USER', ''),  # ユーザー名
            'passwd': settings.get('MYSQL_PASSWORD', ''),  # パスワード
            'charset': settings.get('MYSQL_CHARSET', 'utf8mb4')  # 文字コード
        }

        self.conn = MySQLdb.connect(**params)  # MYSQLサーバーに接続。
        self.c = self.conn.cursor()  # カーソルを取得
        self.c.execute("""
            DROP TABLE IF EXISTS `items`
        """)

        # itemsテーブルが存在しない場合は作成。
        self.c.execute("""
            CREATE TABLE IF NOT EXISTS `items` (
            `ids` INT NOT NULL AUTO_INCREMENT,
            `ID` INTEGER ,
            `name` VARCHAR(200) ,
            `price_ETH` FLOAT ,
            `price_SPL` INTEGER ,
            `price_JPY` INTEGER ,
            `buy_transaction_URL` VARCHAR(200) NOT NULL ,
            `sell_transaction_URL_ETH` VARCHAR(200),
            `buy_transaction_URL_JPY` VARCHAR(200),
            `image_URL` VARCHAR(200),
            PRIMARY KEY (`ids`)
            )
        """)
        self.conn.commit()  # 変更をコミット


    def close_spider(self, spider):
        """
        spiderの終了時にMySQLサーバー編接続を切断する。
        """
        self.conn.close()


    def process_item(self, item, spider):
        """
        Itemをitemsテーブルに挿入する。
        """
        self.c.execute('INSERT INTO `items`(`ids`,`ID`,`name`,`price_ETH`, `price_SPL`,`price_JPY`,`buy_transaction_URL`,`sell_transaction_URL_ETH`,`buy_transaction_URL_JPY`,`image_URL`) '
                       'VALUES (%(ids)s,%(ID)s,%(name)s,%(price_ETH)s,%(price_SPL)s,%(price_JPY)s,%(buy_transaction_URL)s,%(sell_transaction_URL_ETH)s,%(buy_transaction_URL_JPY)s,%(image_URL)s)', dict(item))

        self.conn.commit()

        return item
