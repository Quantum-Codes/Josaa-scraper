# JOSAA scraper
Not exactly a scraper...
Created with [@AnmolSinha42](https://github.com/anmolsinha42)

I required JoSAA data for NITs in excel format for college counselling, However the JoSAA website didn't provide any download button or API.. By making this (within an hour), I was able to export data to an excel file by copying tables and pasting them into the respective files in `NITs` folder.
I have left the generated files in the folders so nobody has to run it again for 2023 JoSAA statistics (OPEN category, male, HS Trichy)
This was for my own use, If you want to use it, then you have to modify the code a bit

## How to use
1. Delete all files in `NITs` folder if you need stats other than 2023
2.  if there are no files in `/NITs` folder, Run `python NITs_list.py` to generate a list of NITs in the folder.

3. Go to `main.py` and edit the following:<br>
   ![image](https://github.com/Quantum-Codes/Josaa-scraper/assets/87054411/b3a900c4-2618-4ccd-b04c-23fb827d34ca) <br>
   Edit "Tiruchipalli" to your own homestate NIT's name (a part of the name is enogh if homestate NIT has a space in name. eg: if "Andhra Pradesh" is home state then just write `"Andhra"`<br>
   If you are from Jammu & Kashmir or Ladakh or Goa, then there are other Home state categories like "JK", "LA" and "GO" respectively. They are currently ignored. Remove your quota code from the list `("GO", "JK", "LA")` in the image.<br>

4. If you are female, edit in `main.py`<br>
   ![image](https://github.com/Quantum-Codes/Josaa-scraper/assets/87054411/6efe75de-9d70-49a6-8208-61e075416d10) <br>
   to `if not "female" in line.lower():`. Doing this will only show female quota seats. If you need both, then remove the 2 lines altogether.<br>
   Also if you have followed step 2, then you have to adjust all indexes in the code.<br>
   If you have deleted both the lines, then you need to  have 2 cases for handling male and female.<br>

5. From the JoSAA website, select round 6 and paste all table data for all the NITs into the files of `NITs` folder. <br>
2023 data for OPEN category is already present, so skip this step if you need 2023's stats

6. Run `main.py`. It will work if you have done all the steps properly

If it shows "access denied" error then close all csv or text files open on your device.
