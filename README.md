## Przypomnienie o zwrocie pożyczonej książki

Program korzysta z bazy danych stworzonej w ramach SQLite, przechowującej informację o ID, imieniu oraz e-mailu czytelnika. Dodatkowo posiada informacje o  książce, którą czytelnik wypożyczył oraz datę zwrotu.
Program wysyła wiadomości e-mail czytelnikowi z przypomnieniem.
Jeśli czytelnik uruchomi program w dniu, który przypada na dzień zwrotu lub w dniach późniejszych, program wyśle do tej osoby email z komunikatem przypominającym o konieczności zwrotu pożyczonej książki.

### Zmienne środowiskowe
W pliku .env.dist zawarty jest szablon, mówiący jak powinny wyglądać zmienne środowiskowe, z których korzysta program.
Aby program działał należy stworzyć plik .env i dostosować zmienne do własnych potrzeb.
Program obsługuje połączenia z protokołem sieciowym SSL. Domyślnie w zmiennych środowiskowych opcja ta jest wyłączona. W przypadku potrzeby korzystania z SSL, należy ustawić na TRUE wartość zmiennej środowiskowej "SSL_ENABLED".
W szablonie dane portu i smtp server podane zostały dla MailTrap'a. W przypadku korzystania z innych serwisów pocztowych należy te zmienne ustawić tak, aby były zgodne z danym serwisem pocztowym. Na przykład dla MailTrapa : port = 2525, smtp_server = 'smtp.mailtrap.io' a dla poczty GMAIL: port = 465, smtp_server = 'smtp.gmail.com'. Zmienne  MAIL_USERNAME,MAIL_PASSWORD powinny być usatwione na osobisty login oraz hasło do poczty. Zmienna DB_NAME domyślnie przyjmuje wartość, kórą jest plik bazy danych dołączony do repozytorium. Chcąc korzystać z własnej bazy danych należy w tym miejscu podmenić bazę danych na pożądaną.
Z zmiennej SENDER należy ustawić informacje, kto jest nadawcą wiadomości.

### Zmiana treści wysyłanego komunikatu

W pliku main.py znajduje się metoda "send_reminder_to_borrowers", a w niej zmienna template. Przyjmuje ona wartość wysyłanego komunikatu. Przesyłany tekst można skonfigurowac według własnego pomysłu.

### Dodatkowe informacje: 
Program porównuje daty z bazy danych, które ustawiono "sztywno" (ustawione w zmiennej "borowers" w pliku main.py). Zabieg ten służy ukazaniu działania programu przy przykładowej bazie danych dołączonej do repozytorium.
Docelowo program korzysta z aktualnej daty w chwili uruchomienia programu.
 
 ### Wykorzystane technologie:
 Python,
 SQLite

