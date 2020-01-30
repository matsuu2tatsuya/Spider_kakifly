# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb

class MySQL_ethmarket_Pipeline:
    """
    ItemをMySQLに保存するPipeline。→Zenで用いるDjango-modelsに従うよ。
    イーサマーケット（ETH）用です。
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

    # Game table 作成。
        self.c.execute("""
            CREATE TABLE IF NOT EXISTS `price_shower_game` (
            `id` INTEGER NOT NULL ,
            `name` VARCHAR (20) NOT NULL UNIQUE ,
            `contract` VARCHAR (100) NOT NULL ,
            PRIMARY KEY (`id`)
            )
        """)

    # Market table 作成。
        self.c.execute("""
            CREATE TABLE IF NOT EXISTS `price_shower_market` (
            `id` INTEGER NOT NULL ,
            `name` VARCHAR (20) NOT NULL UNIQUE ,
            PRIMARY KEY (`id`)
            )
        """)

    # auction table 作成。
        self.c.execute("""
            CREATE TABLE IF NOT EXISTS `price_shower_auction` (
            `id` INTEGER NOT NULL AUTO_INCREMENT,
            `update_at` datetime ,
            `purchase_URL` varchar(200) NOT NULL,
            `is_active` BOOL NOT NULL,
            `market_type_id` INTEGER NOT NULL ,
            CONSTRAINT `auction_market` FOREIGN KEY `price_shower_market` (`market_type_id`)
            REFERENCES `price_shower_market` (`id`) ON DELETE CASCADE ON UPDATE CASCADE ,
            PRIMARY KEY (`id`)
            )
        """)

    # asset table 作成。
        self.c.execute("""
            CREATE TABLE IF NOT EXISTS `price_shower_asset` (
            `id` INTEGER NOT NULL AUTO_INCREMENT,
            `name` VARCHAR(200) ,
            `auction_id` INTEGER NOT NULL ,
            CONSTRAINT `asset_auction` FOREIGN KEY `price_shower_asset` (`auction_id`)
            REFERENCES `price_shower_auction` (`id`) ON DELETE CASCADE ON UPDATE CASCADE ,
            `game_type_id` INTEGER NOT NULL ,
            CONSTRAINT `asset_game` FOREIGN KEY `price_shower_asset` (`game_type_id`)
            REFERENCES `price_shower_game` (`id`) ON DELETE CASCADE ON UPDATE CASCADE ,
            PRIMARY KEY (`id`)
            )
        """)

    # setauction table 作成。
        self.c.execute("""
            CREATE TABLE IF NOT EXISTS `price_shower_setauction` (
            `id` INTEGER NOT NULL AUTO_INCREMENT,
            `price` FLOAT NOT NULL ,
            `currency` CHAR(3),
            `auction_id` INTEGER NOT NULL ,
            CONSTRAINT `setauction_auction` FOREIGN KEY `price_shower_setauction` (`auction_id`)
            REFERENCES `price_shower_auction` (`id`) ON DELETE CASCADE ON UPDATE CASCADE ,
            PRIMARY KEY (`id`)
            )
        """)
    # image table 作成。
        self.c.execute("""
            CREATE TABLE IF NOT EXISTS `price_shower_image` (
            `id` INTEGER NOT NULL AUTO_INCREMENT,
            `url` varchar(200) NOT NULL ,
            `asset_id` INTEGER NOT NULL ,
            CONSTRAINT `image_asset` FOREIGN KEY `price_shower_image` (`asset_id`)
            REFERENCES `price_shower_asset` (`id`) ON DELETE CASCADE ON UPDATE CASCADE ,
            PRIMARY KEY (`id`)
            )
        """)
        self.conn.commit()  # 変更をコミット


    def process_item(self, item, spider):
        """
        Itemをそれぞれのテーブルに挿入する。
        """

        # price_shower_game　→デフォルト値はこっちで指定。
        game_id = 6
        game_name = 'CryptoSpells'
        game_contract = '0x67cbbb366a51fff9ad869d027e496ba49f5f6d55'

        self.c.execute(f"INSERT IGNORE INTO `price_shower_game`(`id`, `name`, `contract`) VALUES ({game_id} ,'{game_name}', '{game_contract}')")
        self.conn.commit()

        # price_shower_market　→デフォルト値はこっちで指定。
        market_id = 2
        marlet_name = 'イーサマーケット(ETH)'

        self.c.execute(f"INSERT IGNORE INTO `price_shower_market`(`id`, `name`) VALUES ({market_id}, '{marlet_name}')")
        self.conn.commit()

        # price_shower_auction
        self.c.execute(f"INSERT INTO `price_shower_auction`(`update_at`,`purchase_URL`, `is_active`, `market_type_id`) VALUES (cast( now() as datetime), %(purchase_URL)s, TRUE, '{market_id}' )", dict(item))

        self.conn.commit()
        auction_id = self.c.lastrowid

        # price_shower_asset
        self.c.execute(f"INSERT INTO `price_shower_asset`(`name`, `auction_id`, `game_type_id`) VALUES (%(name)s, {auction_id}, {game_id})", dict(item))
        self.conn.commit()
        asset_id = self.c.lastrowid

        # price_shower_setauction
        self.c.execute(f"INSERT INTO `price_shower_setauction`(`price`, `currency`, `auction_id`) VALUES (%(price)s, %(currency)s, {auction_id})", dict(item))

        self.conn.commit()

        # price_shower_image
        self.c.execute(f"INSERT INTO `price_shower_image`(`url`, `asset_id`) VALUES (%(image_URL)s, {asset_id})", dict(item))

        self.conn.commit()

        return item


    def close_spider(self, spider):
        """
        spiderの終了時にMySQLサーバー編接続を切断する。
        """
        self.conn.close()



class MySQL_ethmarketjpy_Pipeline:
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

    def process_item(self, item, spider):
        """
        Itemをそれぞれのテーブルに挿入する。
        """

        # price_shower_game　→デフォルト値はこっちで指定。
        game_id = 6
        game_name = 'CryptoSpells'
        game_contract = '0x67cbbb366a51fff9ad869d027e496ba49f5f6d55'

        self.c.execute(f"INSERT IGNORE INTO `price_shower_game`(`id`, `name`, `contract`) VALUES ({game_id} ,'{game_name}', '{game_contract}')")
        self.conn.commit()

        # price_shower_market　→デフォルト値はこっちで指定。
        market_id = 3
        marlet_name = 'イーサマーケット(JPY)'

        self.c.execute(f"INSERT IGNORE INTO `price_shower_market`(`id`, `name`) VALUES ({market_id}, '{marlet_name}')")
        self.conn.commit()

        # price_shower_auction
        self.c.execute(f"INSERT INTO `price_shower_auction`(`update_at`,`purchase_URL`, `is_active`, `market_type_id`) VALUES (cast( now() as datetime), %(purchase_URL)s, TRUE, '{market_id}' )", dict(item))

        self.conn.commit()
        auction_id = self.c.lastrowid

        # price_shower_asset
        self.c.execute(f"INSERT INTO `price_shower_asset`(`name`, `auction_id`, `game_type_id`) VALUES (%(name)s, {auction_id}, {game_id})", dict(item))
        self.conn.commit()
        asset_id = self.c.lastrowid

        # price_shower_setauction
        self.c.execute(f"INSERT INTO `price_shower_setauction`(`price`, `currency`, `auction_id`) VALUES (%(price)s, %(currency)s, {auction_id})", dict(item))

        self.conn.commit()

        # price_shower_image
        self.c.execute(f"INSERT INTO `price_shower_image`(`url`, `asset_id`) VALUES (%(image_URL)s, {asset_id})", dict(item))

        self.conn.commit()

        return item


    def close_spider(self, spider):
        """
        spiderの終了時にMySQLサーバー編接続を切断する。
        """
        self.conn.close()


class MySQL_magi_Pipeline:
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


    def process_item(self, item, spider):
        """
        Itemをそれぞれのテーブルに挿入する。
        """

        # price_shower_game　→デフォルト値はこっちで指定。
        game_id = 6
        game_name = 'CryptoSpells'
        game_contract = '0x67cbbb366a51fff9ad869d027e496ba49f5f6d55'

        self.c.execute(f"INSERT IGNORE INTO `price_shower_game`(`id`, `name`, `contract`) VALUES ({game_id} ,'{game_name}', '{game_contract}')")
        self.conn.commit()

        # price_shower_market　→デフォルト値はこっちで指定。
        market_id = 4
        marlet_name = 'magi'

        self.c.execute(f"INSERT IGNORE INTO `price_shower_market`(`id`, `name`) VALUES ({market_id}, '{marlet_name}')")
        self.conn.commit()

        # price_shower_auction
        self.c.execute(f"INSERT INTO `price_shower_auction`(`update_at`,`purchase_URL`, `is_active`, `market_type_id`) VALUES (cast( now() as datetime), %(purchase_URL)s, TRUE, '{market_id}' )", dict(item))

        self.conn.commit()
        auction_id = self.c.lastrowid

        # price_shower_asset
        self.c.execute(f"INSERT INTO `price_shower_asset`(`name`, `auction_id`, `game_type_id`) VALUES (%(name)s, {auction_id}, {game_id})", dict(item))
        self.conn.commit()
        asset_id = self.c.lastrowid

        # price_shower_setauction
        self.c.execute(f"INSERT INTO `price_shower_setauction`(`price`, `currency`, `auction_id`) VALUES (%(price)s, %(currency)s, {auction_id})", dict(item))

        self.conn.commit()

        # price_shower_image
        self.c.execute(f"INSERT INTO `price_shower_image`(`url`, `asset_id`) VALUES (%(image_URL)s, {asset_id})", dict(item))

        self.conn.commit()

        return item


    def close_spider(self, spider):
        """
        spiderの終了時にMySQLサーバー編接続を切断する。
        """
        self.conn.close()


class MySQL_cryspe_Pipeline:
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


    def process_item(self, item, spider):
        """
        Itemをそれぞれのテーブルに挿入する。
        """

        # price_shower_game　→デフォルト値はこっちで指定。
        game_id = 6
        game_name = 'CryptoSpells'
        game_contract = '0x67cbbb366a51fff9ad869d027e496ba49f5f6d55'

        self.c.execute(f"INSERT IGNORE INTO `price_shower_game`(`id`, `name`, `contract`) VALUES ({game_id} ,'{game_name}', '{game_contract}')")
        self.conn.commit()

        # price_shower_market　→デフォルト値はこっちで指定。
        market_id = 5
        marlet_name = 'CryptoSpells_Market'

        self.c.execute(f"INSERT IGNORE INTO `price_shower_market`(`id`, `name`) VALUES ({market_id}, '{marlet_name}')")
        self.conn.commit()

        # price_shower_auction
        self.c.execute(f"INSERT INTO `price_shower_auction`(`update_at`,`purchase_URL`, `is_active`, `market_type_id`) VALUES (cast( now() as datetime), %(purchase_URL)s, TRUE, '{market_id}' )", dict(item))

        self.conn.commit()
        auction_id = self.c.lastrowid

        # price_shower_asset
        self.c.execute(f"INSERT INTO `price_shower_asset`(`name`, `auction_id`, `game_type_id`) VALUES (%(name)s, {auction_id}, {game_id})", dict(item))
        self.conn.commit()
        asset_id = self.c.lastrowid

        # price_shower_setauction
        self.c.execute(f"INSERT INTO `price_shower_setauction`(`price`, `currency`, `auction_id`) VALUES (%(price)s, %(currency)s, {auction_id})", dict(item))

        self.conn.commit()

        # price_shower_image
        self.c.execute(f"INSERT INTO `price_shower_image`(`url`, `asset_id`) VALUES (%(image_URL)s, {asset_id})", dict(item))

        self.conn.commit()

        return item


    def close_spider(self, spider):
        """
        spiderの終了時にMySQLサーバー編接続を切断する。
        """
        self.conn.close()


class MySQL_DEX_Pipeline:
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


    def process_item(self, item, spider):
        """
        Itemをそれぞれのテーブルに挿入する。
        """

        # price_shower_game　→デフォルト値はこっちで指定。
        game_id = 6
        game_name = 'CryptoSpells'
        game_contract = '0x67cbbb366a51fff9ad869d027e496ba49f5f6d55'

        self.c.execute(f"INSERT IGNORE INTO `price_shower_game`(`id`, `name`, `contract`) VALUES ({game_id} ,'{game_name}', '{game_contract}')")
        self.conn.commit()

        # price_shower_market　→デフォルト値はこっちで指定。
        market_id = 6
        marlet_name = 'spider_DEX'

        self.c.execute(f"INSERT IGNORE INTO `price_shower_market`(`id`, `name`) VALUES ({market_id}, '{marlet_name}')")
        self.conn.commit()

        # price_shower_auction
        self.c.execute(f"INSERT INTO `price_shower_auction`(`update_at`,`purchase_URL`, `is_active`, `market_type_id`) VALUES (cast( now() as datetime), %(purchase_URL)s, TRUE, '{market_id}' )", dict(item))

        self.conn.commit()
        auction_id = self.c.lastrowid

        # price_shower_asset
        self.c.execute(f"INSERT INTO `price_shower_asset`(`name`, `auction_id`, `game_type_id`) VALUES (%(name)s, {auction_id}, {game_id})", dict(item))
        self.conn.commit()
        asset_id = self.c.lastrowid

        # price_shower_setauction
        self.c.execute(f"INSERT INTO `price_shower_setauction`(`price`, `currency`, `auction_id`) VALUES (%(price)s, %(currency)s, {auction_id})", dict(item))

        self.conn.commit()

        # price_shower_image
        self.c.execute(f"INSERT INTO `price_shower_image`(`url`, `asset_id`) VALUES (%(image_URL)s, {asset_id})", dict(item))

        self.conn.commit()

        return item


    def close_spider(self, spider):
        """
        spiderの終了時にMySQLサーバー編接続を切断する。
        """
        self.conn.close()
