import sqlite3


# Инициализация БД
def init_db():
    conn = sqlite3.connect('arthaven.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS Arts (
            Art_ID INTEGER PRIMARY KEY,
            Name TEXT NOT NULL,
            ArtPhoto BLOB NOT NULL,
            Price INT NOT NULL,
            Width INT NOT NULL,
            Height INT NOT NULL,
            Artist_ID INT NOT NULL,
            Creation_year INT NOT NULL,
            Technique INT NOT NULL,
            Description TEXT,
            Sold BOOLEAN,
            Framing TEXT NOT NULL,
            FOREIGN KEY (Artist_ID) REFERENCES Artists(Artist_ID)
            FOREIGN KEY (Technique) REFERENCES Techniques(Technique_ID)
        )
    ''')          

    c.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            User_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            First_name TEXT NOT NULL,
            Last_name TEXT NOT NULL,
            Email TEXT NOT NULL,
            Password TEXT NOT NULL,
            Phone TEXT
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS Artists (
            Artist_ID INT PRIMARY KEY,
            Name TEXT NOT NULL,
            ArtistPhoto BLOB NOT NULL,
            Birth_year INT,
            Bio TEXT
        );
    ''')

    c.execute('''              
        CREATE TABLE IF NOT EXISTS Techniques (
            Technique_ID INT PRIMARY KEY,
            Name TEXT NOT NULL
        );
    ''')

    c.execute('''  
        CREATE TABLE IF NOT EXISTS Themes (
            Theme_ID INT PRIMARY KEY,
            Name TEXT NOT NULL
        );
    ''')

    c.execute('''              
        CREATE TABLE IF NOT EXISTS Arts_themes (
            Art_theme_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Art_ID INT,
            Theme_ID INT,
            FOREIGN KEY (Art_ID) REFERENCES Arts(Art_ID),
            FOREIGN KEY (Theme_ID) REFERENCES themes(Theme_ID)
        );
    ''')



    c.execute('''
        CREATE TABLE IF NOT EXISTS Cart (
            Cart_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            User_ID INT,
            FOREIGN KEY (User_id) REFERENCES Users(User_ID)
        );
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS Cart_items (
            Cart_item_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Cart_ID INT,
            Art_ID INT,
            FOREIGN KEY (Cart_ID) REFERENCES Cart(Cart_ID),
            FOREIGN KEY (Art_ID) REFERENCES Arts(Art_ID)
        );
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS Favorites (
            Favorites_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            User_ID INT,
            Art_ID INT,
            FOREIGN KEY (User_ID) REFERENCES Users(User_ID),
            FOREIGN KEY (Art_ID) REFERENCES Arts(Art_ID)
        );
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS Orders (
            Order_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            User_ID INT,
            User_Phone_number TEXT,
            Delivery_address TEXT,
            Total_amount INT,
            Order_date DATETIME,
            status CHECK(status IN ('Сборка заказа', 'В пути', 'Отменен')),
            FOREIGN KEY (User_ID) REFERENCES Users(User_ID)
        );
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS Order_items (
            Order_item_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Order_ID INT,
            Art_ID INT,
            FOREIGN KEY (Order_ID) REFERENCES Orders(Order_ID),
            FOREIGN KEY (Art_ID) REFERENCES Arts(Art_ID)
        );
    ''')

init_db()


def convertToBinaryData(filename):
    try:
        with open(filename, 'rb') as file:
            blobData = file.read()
        return blobData
    except FileNotFoundError:
        print(f"Файл не найден: {filename}")
        return None
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None


# Функция для вставки данных в таблицы
def insertData(table_name, **kwargs):
    try:
        conn = sqlite3.connect('arthaven.db')
        c = conn.cursor()

        # Проверка наличия изображения для преобразования в BLOB
        if 'ArtPhoto' in kwargs and kwargs['ArtPhoto']:
            kwargs['ArtPhoto'] = convertToBinaryData(kwargs['ArtPhoto'])

        if 'ArtistPhoto' in kwargs and kwargs['ArtistPhoto']:
            kwargs['ArtistPhoto'] = convertToBinaryData(kwargs['ArtistPhoto'])

        # Формирование запроса на вставку
        columns = ', '.join(kwargs.keys())
        placeholders = ', '.join(['?' for _ in kwargs])
        sqlite_insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

        # Выполнение запроса
        c.execute(sqlite_insert_query, tuple(kwargs.values()))
        conn.commit()
        print(f"Данные успешно вставлены в таблицу {table_name}")

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if conn:
            conn.close()




insertData('Techniques', Technique_ID=1, Name='Холст, акрил')
insertData('Techniques', Technique_ID=2, Name='Холст, масло')
insertData('Techniques', Technique_ID=3, Name='Картон, масло')
insertData('Techniques', Technique_ID=4, Name='Дерево, масло')
insertData('Techniques', Technique_ID=5, Name='Холст, акрил, масло')
insertData('Techniques', Technique_ID=6, Name='Холст, темпера')
insertData('Techniques', Technique_ID=7, Name='Дерево, акрил')
insertData('Techniques', Technique_ID=8, Name='Бумага, акрил')
insertData('Techniques', Technique_ID=9, Name='Ткань, акрил')
insertData('Techniques', Technique_ID=10, Name='Бумага, масло')

# Таблица категорий
insertData('Themes', Theme_ID=1, Name='Лето')
insertData('Themes', Theme_ID=2, Name='Одежда')
insertData('Themes', Theme_ID=3, Name='Весна')
insertData('Themes', Theme_ID=4, Name='Осень')
insertData('Themes', Theme_ID=5, Name='Постинтернет')
insertData('Themes', Theme_ID=6, Name='Техника')
insertData('Themes', Theme_ID=7, Name='Переферия')
insertData('Themes', Theme_ID=8, Name='Мышь')
insertData('Themes', Theme_ID=9, Name='Микрофон')
insertData('Themes', Theme_ID=10, Name='Спорт')
insertData('Themes', Theme_ID=11, Name='Украшения')
insertData('Themes', Theme_ID=12, Name='Зима')
insertData('Themes', Theme_ID=13, Name='Монитор')
insertData('Themes', Theme_ID=14, Name='Принты')
insertData('Themes', Theme_ID=15, Name='Нижнее белье')
insertData('Themes', Theme_ID=16, Name='История')
insertData('Themes', Theme_ID=17, Name='Искусство про искусство')
insertData('Themes', Theme_ID=18, Name='На злобу дня')

# Таблица Магазина
insertData('Artists', Artist_ID=1, Name='Supreme', ArtistPhoto='C:/Users/kkolu/Desktop/дипломы/вввв/artists/avatar-2.png', Birth_year=1994,
           Bio='Supreme — это культовый бренд уличной одежды, основанный в Нью-Йорке в 1994 году. Он известен своими ограниченными выпусками, уникальным дизайном и сотрудничеством с другими известными брендами и художниками. Supreme предлагает разнообразные товары, включая одежду, аксессуары и скейтборд-экипировку. Бренд стал символом уличной культуры и моды, привлекая внимание как молодежи, так и коллекционеров. Высокий спрос на продукцию Supreme и ограниченные тиражи создают эффект эксклюзивности, что делает его одним из самых желаемых брендов в мире уличной моды.'
           )
insertData('Artists', Artist_ID=2, Name='NIKE', ArtistPhoto='C:/Users/kkolu/Desktop/дипломы/вввв/artists/avatar-1.png', Birth_year=1964,
           Bio='Nike — это один из крупнейших и самых известных брендов спортивной одежды и обуви в мире, основанный в 1964 году под названием Blue Ribbon Sports, а затем переименованный в Nike в 1971 году. Бренд стал символом спортивной культуры и активного образа жизни, предлагая широкий ассортимент продукции, включая кроссовки, спортивную одежду, аксессуары и оборудование для различных видов спорта.'
           )
insertData('Artists', Artist_ID=3, Name='Logitech', ArtistPhoto='C:/Users/kkolu/Desktop/дипломы/вввв/artists/avatar-5.png', Birth_year=1981,
           Bio='Logitech — это швейцарская компания, основанная в 1981 году, специализирующаяся на производстве компьютерной периферии и аксессуаров. Бренд известен своими инновационными решениями в области технологий, предлагая широкий ассортимент продукции, включая мыши, клавиатуры, веб-камеры, наушники и игровые устройства.'
           )
insertData('Artists', Artist_ID=4, Name='FIFIne', ArtistPhoto='C:/Users/kkolu/Desktop/дипломы/вввв/artists/avatar-6.png', Birth_year=2005,
           Bio='FiFine — это бренд, специализирующийся на производстве аудиотехники, включая микрофоны, наушники и другие звуковые устройства. Компания была основана с целью предоставить пользователям доступные и качественные решения для записи и воспроизведения звука. FiFine быстро завоевала популярность благодаря своим продуктам, которые подходят как для профессионалов, так и для любителей.'
           )
insertData('Artists', Artist_ID=5, Name='Digma', ArtistPhoto='C:/Users/kkolu/Desktop/дипломы/вввв/artists/avatar-7.png', Birth_year=2002,
           Bio='Дигма (Digma) — это российский бренд, который занимается производством и продажей электроники и цифровых устройств. Компания была основана в 1999 году и с тех пор зарекомендовала себя как надежный производитель, предлагающий широкий ассортимент продукции, включая планшеты, электронные книги, смартфоны, аксессуары и другие устройства.'
           )
insertData('Artists', Artist_ID=6, Name='SAMSUNG', ArtistPhoto='C:/Users/kkolu/Desktop/дипломы/вввв/artists/samsung.png', Birth_year=1954,
           Bio='SAMSUNG — это один из крупнейших и самых известных брендов электроники, основанный в 1954 году.'
           )

# Таблица товаров
insertData('Arts', Art_ID=2, Name='Худи Supreme', ArtPhoto='C:/Users/kkolu/Desktop/дипломы/вввв/arts/art-smart.png', Price=50000, Width=1,Height=120,  Artist_ID=1, Creation_year=2023, Technique=2,
           Description='Теплое и качественное худи, сделано из прочного и хорошего материала.',
           Sold=False, Framing='Подрамник')
insertData('Arts_themes', Art_ID=2, Theme_ID=2)
insertData('Arts_themes', Art_ID=2, Theme_ID=11)
insertData('Arts_themes', Art_ID=2, Theme_ID=14)
insertData('Arts_themes', Art_ID=13, Theme_ID=12)
insertData('Arts', Art_ID=3, Name='Спортивные штаны Supreme', ArtPhoto='C:/Users/kkolu/Desktop/дипломы/вввв/arts/art-8.png', Price=250000, Width=1,Height=120,  Artist_ID=1, Creation_year=2024, Technique=2,
           Description='Теплые и качественные штаны, сделанные из прочных материалов',
           Sold=False, Framing='Подрамник')
insertData('Arts_themes', Art_ID=3, Theme_ID=2)
insertData('Arts_themes', Art_ID=3, Theme_ID=11)
insertData('Arts_themes', Art_ID=3, Theme_ID=14)
insertData('Arts_themes', Art_ID=13, Theme_ID=12)
insertData('Arts', Art_ID=11, Name='Непромокаемая куртка Supreme', ArtPhoto='C:/Users/kkolu/Desktop/дипломы/вввв/arts/art-15.jpg', Price=120000, Width=1,Height=120,  Artist_ID=1, Creation_year=2016, Technique=2,
           Description='Непромокаемая куртка, сшитая из гидрофобного материала',
           Sold=False, Framing='Подрамник')
insertData('Arts_themes', Art_ID=11, Theme_ID=2)
insertData('Arts_themes', Art_ID=11, Theme_ID=3)
insertData('Arts_themes', Art_ID=11, Theme_ID=11)
insertData('Arts_themes', Art_ID=11, Theme_ID=14)
insertData('Arts', Art_ID=12, Name='Перчатки Supreme', ArtPhoto='C:/Users/kkolu/Desktop/дипломы/вввв/arts/art-16.jpg', Price=10000, Width=1,Height=120,  Artist_ID=1, Creation_year=2021, Technique=2,
           Description='Отличные согревающие перчатки, которые не дадут вашим рукам замерзнуть зимой',
           Sold=False, Framing='Подрамник')
insertData('Arts_themes', Art_ID=12, Theme_ID=2)
insertData('Arts_themes', Art_ID=12, Theme_ID=11)
insertData('Arts_themes', Art_ID=12, Theme_ID=12)
insertData('Arts_themes', Art_ID=12, Theme_ID=14)
insertData('Arts', Art_ID=13, Name='Ботинки Supreme', ArtPhoto='C:/Users/kkolu/Desktop/дипломы/вввв/arts/art-17.png', Price=50000, Width=1,Height=120,  Artist_ID=1, Creation_year=2020, Technique=2,
           Description='Ботинки весенние - зимние',
           Sold=False, Framing='Подрамник, Багет, Авторское оформление')
insertData('Arts_themes', Art_ID=13, Theme_ID=2)
insertData('Arts_themes', Art_ID=13, Theme_ID=3)
insertData('Arts_themes', Art_ID=13, Theme_ID=11)
insertData('Arts_themes', Art_ID=13, Theme_ID=14)
insertData('Arts_themes', Art_ID=13, Theme_ID=12)

insertData('Arts', Art_ID=4, Name='Nike P-6000', ArtPhoto='C:/Users/kkolu/Desktop/дипломы/вввв/arts/art-9.png', Price=16000, Width=1,Height=120,  Artist_ID=2, Creation_year=2010, Technique=5,
           Description='Нет описания.',
           Sold=False, Framing='Подрамник')
insertData('Arts_themes', Art_ID=4, Theme_ID=2)
insertData('Arts_themes', Art_ID=4, Theme_ID=10)
insertData('Arts_themes', Art_ID=4, Theme_ID=11)
insertData('Arts', Art_ID=5, Name='Ветровка Nike M Sportswear Windrunner Hooded Jacket DA0001-010', ArtPhoto='C:/Users/kkolu/Desktop/дипломы/вввв/arts/art-10.jfif', Price=20000, Width=1,Height=120,  Artist_ID=2, Creation_year=2016, Technique=5,
           Description='Нет описания.',
           Sold=False, Framing='Подрамник')
insertData('Arts_themes', Art_ID=5, Theme_ID=2)
insertData('Arts_themes', Art_ID=5, Theme_ID=3)
insertData('Arts_themes', Art_ID=5, Theme_ID=4)
insertData('Arts_themes', Art_ID=5, Theme_ID=14)
insertData('Arts', Art_ID=6, Name='Брюки спортивные M NK CLUB FT OVERSIZED PANT', ArtPhoto='C:/Users/kkolu/Desktop/дипломы/вввв/arts/art-11.jpg', Price=7000, Width=1,Height=120,  Artist_ID=2, Creation_year=2011, Technique=5,
           Description='Нет описания.',
           Sold=False, Framing='Подрамник')
insertData('Arts_themes', Art_ID=6, Theme_ID=1)
insertData('Arts_themes', Art_ID=6, Theme_ID=2)
insertData('Arts_themes', Art_ID=6, Theme_ID=3)
insertData('Arts_themes', Art_ID=6, Theme_ID=4)
insertData('Arts_themes', Art_ID=6, Theme_ID=14)
insertData('Arts', Art_ID=7, Name='Шапка Nike Terra Beanie', ArtPhoto='C:/Users/kkolu/Desktop/дипломы/вввв/arts/art-12.png', Price=4199, Width=1,Height=120,  Artist_ID=2, Creation_year=2018, Technique=5,
           Description='Нет описания.',
           Sold=False, Framing='Подрамник')
insertData('Arts_themes', Art_ID=7, Theme_ID=2)
insertData('Arts_themes', Art_ID=7, Theme_ID=4)
insertData('Arts_themes', Art_ID=7, Theme_ID=12)
insertData('Arts', Art_ID=8, Name='Трусы Nike E-Day Slip 2-Pack', ArtPhoto='C:/Users/kkolu/Desktop/дипломы/вввв/arts/art-13.jfif', Price=4000, Width=1,Height=120,  Artist_ID=2, Creation_year=2023, Technique=1,
           Description='Нет описания.',
           Sold=False, Framing='Подрамник')
insertData('Arts_themes', Art_ID=8, Theme_ID=13)
insertData('Arts_themes', Art_ID=8, Theme_ID=15)



insertData('Arts', Art_ID=1, Name='Мышка Logitech G-102', ArtPhoto='C:/Users/kkolu/Desktop/дипломы/вввв/arts/art-6.png', Price=2000, Width=1,Height=120,  Artist_ID=3, Creation_year=2023, Technique=2,
           Description='Нет описания.',
           Sold=False, Framing='Багет')
insertData('Arts_themes', Art_ID=1, Theme_ID=6)
insertData('Arts_themes', Art_ID=1, Theme_ID=7)
insertData('Arts_themes', Art_ID=1, Theme_ID=8)

insertData('Arts', Art_ID=22, Name='Микрофон FIFINE K730', ArtPhoto='C:/Users/kkolu/Desktop/дипломы/вввв/arts/art-2.jpg', Price=5000, Width=1,Height=120, Artist_ID=4, Creation_year=2022, Technique=1,
           Description='Нет описания.',
           Sold=False, Framing='Подрамник, Багет')
insertData('Arts_themes', Art_ID=9, Theme_ID=6)
insertData('Arts_themes', Art_ID=9, Theme_ID=7)
insertData('Arts_themes', Art_ID=9, Theme_ID=9)
insertData('Arts', Art_ID=23, Name='Подставка для ноутбука с охлаждением', ArtPhoto='C:/Users/kkolu/Desktop/arthaven/arts/art-14.png', Price=5000, Width='Хлопок',  Artist_ID=4, Creation_year=2021, Technique=1,
           Description='Нет описания',
           Sold=False, Framing='Подрамник')
insertData('Arts_themes', Art_ID=10, Theme_ID=1)
insertData('Arts_themes', Art_ID=10, Theme_ID=11)
insertData('Arts_themes', Art_ID=10, Theme_ID=14)

insertData('Arts', Art_ID=24, Name='27" Монитор Digma Overdrive 27P511F', ArtPhoto='C:/Users/kkolu/Desktop/дипломы/вввв/arts/art-18.png', Price=25000, Width=1,Height=120, Artist_ID=5, Creation_year=2024, Technique=2,
           Description='Нет описания.',
           Sold=False, Framing='Подрамник')
insertData('Arts_themes', Art_ID=14, Theme_ID=6)
insertData('Arts_themes', Art_ID=14, Theme_ID=7)
insertData('Arts_themes', Art_ID=14, Theme_ID=13)
insertData('Arts', Art_ID=25, Name='Велосипед', ArtPhoto='C:/Users/kkolu/Desktop/дипломы/вввв/arts/velik.webp', Price=30000, Width='Хлопок',  Artist_ID=5, Creation_year=2022, Technique=2,
           Description='Горный велосипед',
           Sold=False, Framing='Подрамник')
insertData('Arts_themes', Art_ID=15, Theme_ID=2)
insertData('Arts_themes', Art_ID=15, Theme_ID=12)
insertData('Arts_themes', Art_ID=16, Theme_ID=13)
insertData('Arts_themes', Art_ID=15, Theme_ID=14)
insertData('Arts', Art_ID=26, Name='Сетевой коммутатор', ArtPhoto='C:/Users/kkolu/Desktop/дипломы/вввв/arts/kommutator.webp', Price=40000, Width='Хлопок', Artist_ID=5, Creation_year=2023, Technique=2,
           Description='Нет описания.',
           Sold=False, Framing='Подрамник')
insertData('Arts_themes', Art_ID=15, Theme_ID=2)
insertData('Arts_themes', Art_ID=15, Theme_ID=8)
insertData('Arts_themes', Art_ID=16, Theme_ID=11)
insertData('Arts_themes', Art_ID=15, Theme_ID=14)

insertData('Arts', Art_ID=27, Name='Микрофон FIFINE Конденсаторный', ArtPhoto='C:/Users/kkolu/Desktop/дипломы/вввв/arts/microfif.webp', Price=4000, Width=1,Height=120, Artist_ID=4, Creation_year=2022, Technique=1,
           Description='Нет описания.',
           Sold=False, Framing='Подрамник, Багет')
insertData('Arts_themes', Art_ID=9, Theme_ID=6)
insertData('Arts_themes', Art_ID=9, Theme_ID=7)
insertData('Arts_themes', Art_ID=9, Theme_ID=9)

insertData('Arts', Art_ID=28, Name='Samsung Смартфон Galaxy S24 Ultra', ArtPhoto='C:/Users/kkolu/Desktop/дипломы/вввв/arts/microfif.webp', Price=4000, Width=1,Height=120, Artist_ID=6, Creation_year=2022, Technique=1,
           Description='(РСТ) 12/512 ГБ, серый',
           Sold=False, Framing='Подрамник, Багет')
insertData('Arts_themes', Art_ID=9, Theme_ID=6)
insertData('Arts_themes', Art_ID=9, Theme_ID=7)
insertData('Arts_themes', Art_ID=9, Theme_ID=9)

insertData('Arts', Art_ID=29, Name='Samsung Наушники беспроводные с микрофоном Samsung Galaxy Buds 3 Pro', ArtPhoto='C:/Users/kkolu/Desktop/дипломы/вввв/arts/naushnik.webp', Price=10000, Width=1,Height=120, Artist_ID=6, Creation_year=2022, Technique=1,
           Description='Bluetooth, USB Type-C, белый',
           Sold=False, Framing='Подрамник, Багет')
insertData('Arts_themes', Art_ID=9, Theme_ID=6)
insertData('Arts_themes', Art_ID=9, Theme_ID=7)
insertData('Arts_themes', Art_ID=9, Theme_ID=9)

insertData('Arts', Art_ID=30, Name='Samsung 27" Монитор, черный', ArtPhoto='C:/Users/kkolu/Desktop/дипломы/вввв/arts/samsamonitor.webp', Price=40000, Width=1,Height=120, Artist_ID=6, Creation_year=2022, Technique=1,
           Description=' 27" Монитор, черный',
           Sold=False, Framing='Подрамник, Багет')
insertData('Arts_themes', Art_ID=9, Theme_ID=6)
insertData('Arts_themes', Art_ID=9, Theme_ID=7)
insertData('Arts_themes', Art_ID=9, Theme_ID=9)
