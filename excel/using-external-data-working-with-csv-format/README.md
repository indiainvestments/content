---
description: >-
  A close look at how to parse CSV data dumps and process the same in your excel
  sheet or spreadsheet
---

# Using External Data : Working with CSV Format

## Prelude

In the previous chapter, we've seen how to get historical market data from Google Finance API.

We used `GOOGLEFINANCE()` function to get NASDAQ ticker data, over a given period of time.

However, you might have also noticed that this is not a _highly_ _available_ function. Often it can error out, and we might have to manually fix these `#NA` errors.  
  
This is true for most publicly freely available APIs - it'd either be rate-limited, or not always be available.  
  
In the real world, when we want to achieve something solving a common pain-point, external data might not be always available from a REST \(or SOAP\) API endpoint. It might not even be desirable to have it be available from a REST endpoint.

Imagine if the problem statement were to compare your portfolio performance against that of an index.  
  
In that case, there would be two aspects to this exercise:

* importing your existing transaction history
* simulating purchase or sell transactions against an index

The first aspect - _importing your existing transactions_ - might not be available from an API endpoint.

You might be using a broker or distributor or advisor, who provides you a transaction reports in a specific format, periodically.

Basically, you’d have a file which has your transactions in a specific format, and before you run any operations on that; you’d have to import that into your spreadsheet.

We could, for instance, just open the file and copy-paste data from there into our spreadsheet. But this can be error-prone, and might require more work.

Fortunately, most spreadsheet / excel applications have in-built functionalities to do a _best-effort_ import for common data formats that your broker / distributor / advisor would typically use to send you these transaction histories.  
  
We'd go over some interesting calculations that can be done upon your transaction history, that's available in CSV format, in these chapters:

{% page-ref page="csv-format.md" %}

{% page-ref page="computing-ltcg-eligible-equity-units.md" %}

{% page-ref page="process-for-estimating-tax.md" %}

