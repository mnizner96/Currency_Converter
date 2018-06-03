# Description
This project is my implementation of Currency_Converter in Python programming language. The goal is to transform amount of the input currency 
to amount of the concerned output currency and then print the result in JSON format. The script supports all known currencies and has two versions: <strong>Application programming interface (API) </strong> and <strong>Command-line interface (CLI) </strong> version. The script gets data from remote <a href="http://www.ecb.int/stats/eurofxref/eurofxref-daily.xml">XML file </a> by the requests module. Obtained data are transformed
to the JSON format by using <strong>json_dumps</strong> function.

# Usage
## Cli
<strong>-h</strong> prints help <br>
<strong>--amount=float</strong> amount of the input_currency<br>
<strong>--input_currency=currency</strong> 3 words short cut or symbol of the input currency <br>
<strong>--output_currency=currency</strong> 3 words short cut or symbol of the output currency 

### Convention of usage
    python ./cli -h 
    python ./cli --amount=<float> --input_currency=<3 words shortcut or symbol> [--output_currency=<3 words shortcut or symbol>]

### Examples
    python ./cli --input_currency=EUR --amount=50.125 --output_currency=CZK 
    python ./cli --input_currency=$ --amount=50.125 --output_currency=Kč

### Return codes
<strong> 0 </strong> No error <br>
<strong> 1 </strong> Wrong input currency <br>
<strong> 2 </strong> Wrong output currency <br>
<strong> 3 </strong> Negative value of amount 

## Api

### Examples
    First we neeed to run api script: 
    python ./api 
    and then we can test commands in urlencode: 
    http://localhost:5000/currency_converter?amount=0.9&input_currency=%C2%A5&output_currency=AUD 
    http://localhost:5000/currency_converter?amount=0.9&input_currency=EUR&output_currency=AUD

### Return codes
<strong> 200 </strong> No error <br>
<strong> 201 </strong> Wrong input currency <br>
<strong> 202 </strong> Wrong output currency <br>
<strong> 203 </strong> Negative value of amount 





