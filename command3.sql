/* How many Aadhar generated for each gender */

select Gender, count(AadhaarGenerated) from uidai group by Gender;

/*
F|174748
Gender|1
M|185958
T|19
*/
