# This is an ADIF parser in Python.

## Actual usage

Main result of parsing: List of QSOs:

* Each QSO is represented by one Python dict.
* Keys in that dict are ADIF field names in upper case,
* value for a key is whatever was found in the ADIF, as a string.

Order of QSOs in the list is same as in ADIF file.

Secondary result of parsing: The ADIF headers. This is returned as a Python dict.

Normally, you'd call `adif_io.read_from_file(filename)`.  But you can
also provide a string with an ADI-file's content, as follows:

```
import adif_io

qsos, header =  adif_io.read_from_string(
    "A sample ADIF content for demonstration.\n"
    "<adif_ver:5>3.1.0<eoh>\n"
    
    "<QSO_DATE:8>20190714 <TIME_ON:4>1140<CALL:5>LY0HQ"
    "<MODE:2>CW<BAND:3>40M<RST_SENT:3>599<RST_RCVD:3>599"
    "<STX_STRING:2>28<SRX_STRING:4>LRMD<EOR>\n"

    "<QSO_DATE:8>20190714<TIME_ON:4>1130<CALL:5>SE9HQ<MODE:2>CW<FREQ:1>7"
    "<BAND:3>40M<RST_SENT:3>599<RST_RCVD:3>599"
    "<SRX_STRING:3>SSA<DXCC:3>284<EOR>")

print("QSOs: {}\nADIF Header: {}".format(qsos, header))
```

This will print out


> QSOs: [{'RST_SENT': '599', 'CALL': 'LY0HQ', 'MODE': 'CW', 'RST_RCVD': '599', 'QSO_DATE': '20190714', 'TIME_ON': '1140', 'BAND': '40M', 'STX_STRING': '28', 'SRX_STRING': 'LRMD'}, {'DXCC': '284', 'RST_SENT': '599', 'CALL': 'SE9HQ', 'MODE': 'CW', 'RST_RCVD': '599', 'BAND': '40M', 'FREQ': '7', 'QSO_DATE': '20190714', 'TIME_ON': '1130', 'SRX_STRING': 'SSA'}]     
> ADIF Header: {'ADIF_VER': '3.1.0'}


## Time on and time off

Given one `qso` dict, you can also have the QSO's start time calculated as a Python `datetime.datetime` value:

    adif_io.time_on(qsos[0])

If your QSO data also includes `TIME_OFF` fields (and, ideally, though
not required, `QSO_DATE_OFF`), this will also work:

    adif_io.time_off(qsos[0])

## ADIF version

This was written with the ADIF version 3.1.0 in mind, but there is
little ADIF-version-specific here.

## Not supported: ADIF data types.

This parser knows nothing about ADIF data types or enumerations.
Everything is a string. So in that sense, this parser is fairly simple.

But it does correcly handle things like:

    <notes:66>In this QSO, we discussed ADIF and in particular the <eor> marker.

So, in that sense, this parser is somewhat sophisticated.

## Only ADI.

This parser only handles ADI files. It knows nothing of the ADX file format.

## For now: input only

There may be an ADIF output facility some time later.

## Sample code

Here is some sample code:

```
import adif_io

qsos_raw, adif_header = adif_io.read_from_file("log.adi")

# The QSOs are probably sorted by QSO time already, but make sure:
for qso in qsos_raw:
    qso["t"] = adif_io.time_on(qso)
qsos_raw_sorted = sorted(qsos_raw, key = lambda qso: qso["t"])
```

Pandas / Jupyter users may want to add `import pandas as pd`
up above and continue like this:

```
qsos = pd.DataFrame(qsos_raw_sorted)
qsos.info()
```
