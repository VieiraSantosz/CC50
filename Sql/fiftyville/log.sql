-- Keep a log of any SQL queries you execute as you solve the mystery.

*Buscar descrição do crime no dia 28 de Junho
select description from crime_scene_reports
where month = 7 and day = 28 and street = "Chamberlin Street";


*Buscar entrevistado que estavam presentes durante o crime
select name, transcript from interviews where month = 7 and day = 28;


*Placas de carro que saíram após 10 min do crime
select license_plate, hour, minute, activity from courthouse_security_logs where month = 7 and day = 28 and hour = 10 and minute between 15 and 25;


*Buscar possível número da conta do ladrão após sacar o dinheiro antes do crime
select atm_location, transaction_type, amount, account_number from atm_transactions where month = 7 and day = 28 and atm_location = 'Fifer Street';


*Buscar ligações que ladrão realizou após o crime
select caller, receiver, duration from phone_calls where month = 7 and day = 28 and duration < 60;


*Buscar primeiros voo saindo de Fiftyville no primeiro horário de manhã e o local para onde estar indo
select flights.id, airports.city, flights.origin_airport_id, destination_airport_id, hour, minute from flights
inner join airports on airports.id = flights.origin_airport_id
where month = 7 and day = 29 order by hour asc;

select flights.id, airports.city, flights.origin_airport_id, destination_airport_id, hour, minute from flights
inner join airports on airports.id = flights.destination_airport_id
where month = 7 and day = 29 order by hour asc;


*Possíveis nomes e passaportes dos ladrões pela placa de carro
select id, name, passport_number from people where license_plate = "5P2BI95";
select id, name, passport_number from people where license_plate = "94KL13X";
select id, name, passport_number from people where license_plate = "6P58WS2";
select id, name, passport_number from people where license_plate = "4328GD8";
select id, name, passport_number from people where license_plate = "G412CB7";
select id, name, passport_number from people where license_plate = "L93JTIZ";
select id, name, passport_number from people where license_plate = "322W7JE";
select id, name, passport_number from people where license_plate = "0NTHK55";
select id, name, passport_number from people where license_plate = "1106N58";


*Verificar as ligações feitas e associar com os possíveis nomes
select name, phone_number from people where name = "Patrick";
select name, phone_number from people where name = "Ernest";
select name, phone_number from people where name = "Amber";
select name, phone_number from people where name = "Danielle";
select name, phone_number from people where name = "Roger";
select name, phone_number from people where name = "Elizabeth";
select name, phone_number from people where name = "Russell";
select name, phone_number from people where name = "Evelyn";
select name, phone_number from people where name = "Madison";


*Analisar os números das contas se alguma está ligada com os possíveis nomes que fizeram o saque antes do crime
select people.name, bank_accounts.account_number from people
inner join bank_accounts on bank_accounts.person_id = people.id
where bank_accounts.account_number = 28500762;

select people.name, bank_accounts.account_number from people
inner join bank_accounts on bank_accounts.person_id = people.id
where bank_accounts.account_number = 28296815;

select people.name, bank_accounts.account_number from people
inner join bank_accounts on bank_accounts.person_id = people.id
where bank_accounts.account_number = 76054385;

select people.name, bank_accounts.account_number from people
inner join bank_accounts on bank_accounts.person_id = people.id
where bank_accounts.account_number = 49610011;

select people.name, bank_accounts.account_number from people
inner join bank_accounts on bank_accounts.person_id = people.id
where bank_accounts.account_number = 16153065;

select people.name, bank_accounts.account_number from people
inner join bank_accounts on bank_accounts.person_id = people.id
where bank_accounts.account_number = 25506511;

select people.name, bank_accounts.account_number from people
inner join bank_accounts on bank_accounts.person_id = people.id
where bank_accounts.account_number = 81061156;

select people.name, bank_accounts.account_number from people
inner join bank_accounts on bank_accounts.person_id = people.id
where bank_accounts.account_number = 26013199;


*Analisar os passaportes com os nomes dos possíveis ladrões que estão indo para London
select flights.id, passengers.passport_number from flights
inner join passengers on passengers.flight_id = flights.id
where flights.id = 36;
