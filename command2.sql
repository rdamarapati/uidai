/* To see how many Aadhar generated from each state */

select State, count(AadhaarGenerated) from uidai group by State;

/*

Andaman and Nicobar Islands|3
Andhra Pradesh|46093
Assam|79
Bihar|2822
Chandigarh|390
Chhattisgarh|704
Dadra and Nagar Haveli|96
Daman and Diu|6
Delhi|8056
Goa|258
Gujarat|18625
Haryana|18958
Himachal Pradesh|4688
Jammu and Kashmir|133
Jharkhand|17829
Karnataka|30413
Kerala|10294
Madhya Pradesh|41282
Maharashtra|65058
Manipur|22
Meghalaya|5
Mizoram|2
Nagaland|615
Odisha|6892
Others|718
Puducherry|486
Punjab|20510
Rajasthan|35938
Sikkim|147
State|1
Tamil Nadu|10998
Tripura|31
Uttar Pradesh|7808
Uttarakhand|1086
West Bengal|9680
*/
