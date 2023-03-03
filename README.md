## Przypomnienie o zwrocie pożyczonej rzeczy!

Program korzysta z baza danych stworzonej w ramach SQLite przechowującej informację o id, imieniu oraz e-mailu czytelnika. Dodatkowo baza przechowuje danę jaką książke czytelnik wypożyczył oraz date, kiedy powinnien ją zwrócić.
Celem programu jest wysyłanie wiadomości e-mail czytelnikowi z przypomnieniem o zwrocie książki.
Jeśli uruchomisz program w dniu, który przypada na dzień zwrotu lub w dniach późniejszych program wyśle do tej osoby email z komunikatem przypominającym o konieczności zwrotu pożyczonej książki.

### Zmienne środowiskowe
Program korzysta z zmiennych środowiskowych. W pliku .env.dist pokazany jest szablon jak powinny wyglądać zmienne środowiskowe.
Aby program działał nalęzy stworzyć plik .env i dostosować zmienne środowiskowe do własnych potrzeb.
Program jest dostosowany do obsługi połączeń z protokołem sieciowym SSL, jednakże domyślnie w zmiennych środowiskowych opcja ta jest wyłączona. W przypadku potrzeby korzystania z SSL należy wartość zmiennej środowiskowej "SSL_ENABLED" usatwić na TRUE.
W szablonie dane portu i smtp server podane zostały dla MailTrap'a. W przypadku korzystania z innych serwisów pocztowych należy te zmienne ustawić tak aby były zgodne z danym serwisem pocztowym. Naprzykład dla MailTrapa : port = 2525, smtp_server = 'smtp.mailtrap.io' a dla poczty GMAIL: port = 465, smtp_server = 'smtp.gmail.com'.Zmienne  MAIL_USERNAME,MAIL_PASSWORD powinny być usatwione na Twój login oraz hasło do poczty. Zmienna DB_NAME domyślnie przyjmuje wartość, jaką jest plik bazy danych dołączony do repozytorium. Chcąc korzystać z własnej bazy danych należy w tym miejscu podmenić bazę danych na pożądaną.
Z zmiennej SENDER nalęzy ustawić informacje kto jest nadawcą wiadomości.

### Zmiana treści wysyłanego komnikatu

W pliku main.py znajduje się metoda "send_reminder_to_borrowers" a w niej zmienna template. Przyjmuje ona wartość wysyłanego komunikatu. Przesyłany tekst można skonfigurowac według własnego pomysłu.

### Dodatkowe informacje: 
 Date, z którą program porównuje daty z datami z bazy danych ustawiono "sztywno" (ustawione w zmiennej "borowers" w pliku main.py). Zabieg ten służy ukazaniu działania programu przy przykładowej bazie danych dołączonych do repozytorium.
 Docelowo program korzysta z daty w chwili uruchomienia programu.
 
 ### Wykorzystane technologie:
 Python,
 SQLite

