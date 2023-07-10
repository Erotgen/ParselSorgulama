# ParselSorgulama
## Before You Start
In order for this program to work appropriately, Python 3.10 and the necessary Python libraries must be installed. All requirements are specified in the requirements.txt file.
In addition, the necessary databases must also be located in the file. A sample database is provided within the program.
## How Does It Work
ParselSorgulama is a database program designed to manage data in specific Microsoft Access files with two tables. 
The program pulls data from all or some databases in the "Veri Tabanları" folder. It detects all subfolders within the main folder. If one of these subfolders is selected in the combobox on the interface screen, it searches only from the databases in that subfolder, if "Tümü" is left selected, it searches from the databases in all subfolders.
The program will receive the information entered in the textboxes on the interface screen and filter the first table with the information entered for it. Then it matches the data in this table with the second table, filters if any information is entered for the second table, and retrieves the necessary data from the two tables.
In addition, if double-click on any cell on the screen, the information of the people associated with that data will be displayed on a second screen.
An example is shared below. 
![Ekran görüntüsü 10-07-2023 09 46 16](https://github.com/Erotgen/ParselSorgulama/assets/106821354/1bf917a8-1526-4273-b20c-7f86c34e037c)

