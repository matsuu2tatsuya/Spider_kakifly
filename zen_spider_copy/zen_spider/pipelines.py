# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb

class MySQLPipeline:
    """
    ItemをMySQLに保存するPipeline。
    {ID(auto),name(id or card_name),price(int),currency(ETH),purchase_URL,image_URL}の６つ。
    """

    def open_spider(self, spider):
        """
        Spiderの開始時にMySQLサーバーに接続する。
        itemsテーブルが存在しない場合は作成する。
        あった場合は一度itemテーブルを削除してからまた作成。
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
            `name` VARCHAR(200) ,
            `price` FLOAT ,
            `currency` VARCHAR(10),
            `purchase_URL` VARCHAR(200) NOT NULL ,
            `image_URL` VARCHAR(200),
            PRIMARY KEY (`purchase_URL`)
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
        self.c.execute("INSERT INTO `items`(`name`,`price`,`currency`,`purchase_URL`,`image_URL`) "
                       "VALUES (%(name)s,%(price)s,%(currency)s,%(purchase_URL)s,%(image_URL)s)", dict(item))

        self.conn.commit()

        return item
