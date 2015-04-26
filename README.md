# Generator-hashes-of-Android-patterns
Script in python that generate a database (sqlite) with all hashes of Android graphical patterns.

Android store the pattern lock in a file (data/system/gesture.key) but this file is crypted with unsalted sha1 hash, so, this script try all combination and generate a database with pattern an its hash.

So, if could access to the previous file and could see inside, you would see a hash like 98fa924cc75742045b615cac92598bf72c76ece6. Now you can run the script without argument and it will generate a file called hashes.db, now you could open the database with SQLite Database Broswer (in Linux system) and you could execute SELECT * FROM Hashes WHERE hash="98fa924cc75742045b615cac92598bf72c76ece6" in the database and you will get 8576143 as pattern.

Each number is a point in the lock window, for example 0 is the top left point, 1 is the following right to point 0 and so on.
