Please find the following step for setup this project.

1. First you have to create 3 database following name

      postgresql = database1, database2

      mysql = database3, database4, database5

2. You have to add psql and mysql database credentials in config.ini file.

3. Add smtp credentials in config.ini file (it's not compulsory)

4. Run run.sh file using.

        Give permission :- sudo chmod 777 run.sh

         Run file :-           ./run.sh

and superuser username and password. (if you add already then press ctrl+c)

Then run http://localhost:8019/app/login

5. if you are login with super user so you can create user and check list of user and list of all product (All 5 database)

6. If you are login normal user so you can see list of product and add product form as same page.



Note : - All thing are tested on Ubuntu Os.
         Used Python 2.7 with Django 1.10

