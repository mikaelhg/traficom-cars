# Traficom katsastustilastot jne.

```
unzip -p TieliikenneAvoinData_5_8.zip TieliikenneAvoinData_5_8.csv | xz -T 0 -9e > TieliikenneAvoinData_5_8.csv.xz
```

http://pxnet2.stat.fi/api1.html

https://www.stat.fi/org/avoindata/pxweb.html

https://trafi2.stat.fi/PXWeb/pxweb/fi/TraFi/TraFi__Katsastuksen_vikatilastot/010_kats_tau_101.px/

https://trafi2.stat.fi/PXWeb/api/v1/fi/TraFi/Katsastuksen_vikatilastot/010_kats_tau_101.px

```
http -v POST https://trafi2.stat.fi/PXWeb/api/v1/fi/TraFi/Katsastuksen_vikatilastot/010_kats_tau_101.px query:='[]' response:='{"format":"px"}'
```

XLS to CSV UTF8 conversion

https://wiki.openoffice.org/wiki/Documentation/DevGuide/Spreadsheets/Filter_Options#Filter_Options_for_the_CSV_Filter

```
libreoffice --headless --convert-to csv:"Text - txt - csv (StarCalc)":44,34,76 Henkilöautojen-määräaikaiskatsastusten-vuositilasto-2016.xlsx
```
