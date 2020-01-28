# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb

class MySQLPipeline:
    """
    ItemをMySQLに保存するPipeline。→Zenで用いるDjango-modelsに従うよ。
    Tableは Auction, Set_auction, Asset, imageの四つ。
    """

    def open_spider(self, spider):
        """
        Spiderの開始時にMySQLサーバーに接続する。
        テーブルが存在しない場合は作成する。あった場合は一度テーブルを削除してからまた作成。
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
            DROP TABLE IF EXISTS `price_shower_image`;
            DROP TABLE IF EXISTS `price_shower_asset`;
            DROP TABLE IF EXISTS `price_shower_setauction`;
            DROP TABLE IF EXISTS `price_shower_auction`;
        """)


    # auction table 作成。
        self.c.execute("""
            CREATE TABLE IF NOT EXISTS `price_shower_auction` (
            `id` INTEGER NOT NULL AUTO_INCREMENT,
            `update_at` datetime ,
            `purchase_URL` varchar(200) NOT NULL,
            `is_active` BOOL NOT NULL,
            PRIMARY KEY (`id`)
            )
        """)

    # asset table 作成。
        self.c.execute("""
            CREATE TABLE IF NOT EXISTS `price_shower_asset` (
            `id` INTEGER NOT NULL AUTO_INCREMENT,
            `name` VARCHAR(200) ,
            CONSTRAINT `assets` FOREIGN KEY `price_shower_asset` (`id`)
            REFERENCES `price_shower_auction` (`id`) ON DELETE CASCADE ON UPDATE CASCADE ,
            PRIMARY KEY (`id`)
            )
        """)

    # setauction table 作成。
        self.c.execute("""
            CREATE TABLE IF NOT EXISTS `price_shower_setauction` (
            `id` INTEGER NOT NULL AUTO_INCREMENT,
            `price` FLOAT NOT NULL ,
            `currency` CHAR(3),
            CONSTRAINT `set_auction` FOREIGN KEY `price_shower_setauction` (`id`)
            REFERENCES `price_shower_auction` (`id`) ON DELETE CASCADE ON UPDATE CASCADE ,
            PRIMARY KEY (`id`)
            )
        """)
    # image table 作成。
        self.c.execute("""
            CREATE TABLE IF NOT EXISTS `price_shower_image` (
            `id` INTEGER NOT NULL AUTO_INCREMENT,
            `url` varchar(200) NOT NULL ,
            CONSTRAINT `image` FOREIGN KEY `price_shower_image` (`id`)
            REFERENCES `price_shower_asset` (`id`) ON DELETE CASCADE ON UPDATE CASCADE ,
            PRIMARY KEY (`id`)
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
        Itemをそれぞれのテーブルに挿入する。
        """

        self.c.execute("INSERT INTO `price_shower_auction`(`update_at`,`purchase_URL`, `is_active`) "
                       "VALUES (cast( now() as datetime), %(purchase_URL)s, TRUE )", dict(item))

        self.c.execute("INSERT INTO `price_shower_asset`(`name`) "
                       "VALUES (%(name)s)", dict(item))

        self.c.execute("INSERT INTO `price_shower_setauction`(`price`, `currency`) "
                       "VALUES (%(price)s, %(currency)s)", dict(item))

        self.c.execute("INSERT INTO `price_shower_image`(`url`) "
                       "VALUES (%(image_URL)s)", dict(item))

        self.conn.commit()

        return item
