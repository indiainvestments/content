---
description: >-
  Pick a screener which doesn't bias you for or against a stock. But you should
  compute the ratios yourself, from ARs, to understand the assumptions behind
  those computations.
---

# Which screener\(s\) should I use?

## Introduction

Though stock-screeners calculate a lot of things, you must do your own calculations too. You will miss a lot of good opportunities or make some expensive mistakes if you consider only the pre-calculated values.

The objective of this article is to explain the importance of your own calculations. The article provides examples where the screening portals might not give right results. The examples are not to demean any portal but to explain the reasons for the difference in numbers across websites.

## Examples of dividend yield

Lets consider the dividend yield of Britannia Industries as on 29th April 2021 \(\#britannia-industries-dividend-yield\):

```text
Screener.in:    4.18%
MoneyControl:   0.95%
MorningStar.in: 1.78%

Correct value:  ~2-5%
Depends on your judgement on how repeatable these dividends are
```

The differences are because of different treatments of interim dividends. While `screener.in` considers all the interim dividends of FY21, `MoneyControl` considers only FY20's dividends. `MorningStar` considered only one of the two interim dividends \(probably assuming the other one as a one time special dividend\).

Another interesting case is that of Majesco. The dividend yield as on 29th April 2021 on various websites is \(\#majesco-dividend-yield\):

```text
Screener.in:              1,353 %
MorningStar.in:           1,351 %
ValueResearchOnline.com:  1,355 %
(Yeah, 1000+% in all the cases)

Correct value:            ~0-5%
```

The company sold off its US subsidiary and distributed most of the proceeds from the sale. The US subsidiary contributed over 90% of the company's revenues and assets. Thus it is safe to assume it was a one time dividend. The future dividend yield in such a case would be around 0 to 5%.

Relying on _any_ screener and buying highest dividend yields shares blindly can make costly errors in such cases.

## Examples of PE Ratio

Let's consider PE ratio of ONGC on different websites as on 29th April 2021 \(\#ongc-pe-ratio\):

```text
MorningStar.in:           shows blank
Screener.in:              13
ValueResearchOnline.com:  144
NseIndia:                 79
MoneyControl.com:         146
```

The company reported:

```text
Standalone TTM EPS:       ₹ 1.32
Consolidated TTM EPS:     ₹ 0.73
The price was:            ₹ 104
Exceptional losses:     ~ ₹ 7.98 / share

Exception losses were of 4899 Cr pre-tax on an old GST liability.
```

The differences across websites is because:

* `ValueResearchOnline` and `MoneyControl` considered _consolidated_ EPS as reported by the company.
* `Screener.in` considered _consolidated_ EPS but added back the exceptional losses.
* `BseIndia.com` and `NseIndia.com` considered _standalone_ EPS. 

The correct PE depends on your individual judgement on how you interpret the impact of exceptional items on future earnings.

The PE based on last 5 years average earnings will be 8.29. This is what Benjamin Graham recommends to use in such cases.

## Operating margins and gross margins

The text-book definition of gross profit margin \(GPM\) is `sales - cogs`.

`COGS` is cost of goods sold.

Most websites will show the gross margins on this standard definition. However, this can sometimes be misleading.

Example in case of TCS - `screener.in` shows the GPM as 100%. This is because TCS has no inventory. But the correct metric for `COGS` in this case should be their employee cost.

Similarly in case of banks, most websites \(eg `screener.in`\), don't consider their interest cost in OPM \(operating profit margin\) and GPM \(gross profit margin\). Thus these numbers are shown exceptionally high.

Screening companies on margins can often yield incorrect results for:

* Insurance companies
* Banks
* Finance companies
* Mining companies

## Return ratios

In case of Abbott India, the ROIC reported as on 29th April 2021 is \(\#abbott-india-roic\):

```text
Screener.in:        22.90%
MorningStar.in:     21.53%
TijoriFinance.com:  131%
Correct value:     ~138%
```

The company held fixed-deposits \(cash equivalents\) of ₹ 2,197 Cr in FY20. While `TijoriFinance` excluded these cash-equivalents in the calculation of capital employed, other two websites didn't exclude it.

These differences in the methods of calculating ROCE, ROIC, ROA and other return ratios can yield wildly different results. You can sometimes miss some interesting companies because their calculated return might be much lower than their economic return ratios.

## Summary and Wrap-up

The auto-calculated ratios on websites can often be different from manual calculations. Those calculations will often miss sector specific adjustments or "special cases" which are too frequent in the investing world.

Don’t rely blindly on any portal or report. Do your own due-diligence.Cross-check the numbers with your calculations.

_**Trust, but verify.**_

Though the websites and portals do their best, there are lots of nuances in the footnotes and schedules which are hard to capture. This mandates the due diligence from the investors and also provides opportunities to them.

To understand how to use a screener, you might want to check this out

{% page-ref page="../../stocks/using-screeners.md" %}

{% hint style="info" %}
We've reached out to some of the teams behind these screeners and have pointed out these issues. They've assured us that they're looking into this.

Tijori Finance moved to paid subscription model now
{% endhint %}

## Footnotes

### Web-archives for case studies

#### Britannia Industries dividend yield

* [Company's dividend history](https://github.com/indiainvestments/content/tree/580d58f1c585b33003c38a56fc5f88ebde23fd10/.gitbook/assets/britannia-bseindia.png)
* [Screener.in](https://web.archive.org/web/20210430170137/https://www.screener.in/company/BRITANNIA/consolidated/)
* [MoneyControl](https://web.archive.org/web/20210430170457/https://www.moneycontrol.com/india/stockpricequote/food-processing/britanniaindustries/BI)
* [MorningStar.in](https://github.com/indiainvestments/content/tree/580d58f1c585b33003c38a56fc5f88ebde23fd10/.gitbook/assets/britannia-morningstar.png)

#### Majesco dividend yield

* [Company's sale of its US subsidiary](https://www.business-standard.com/article/markets/majesco-hits-upper-circuit-on-board-nod-to-sell-us-arm-mastek-surges-20-120072100526_1.html)
* [Company's presentation about dividend](https://www.bseindia.com/xml-data/corpfiling/AttachHis/ff82752d-3368-4413-8c00-7238c5dc17d3.pdf)
* [Screener.in](https://web.archive.org/web/20210430172013/https://www.screener.in/company/MAJESCO/consolidated/)
* [MorningStar.in](https://github.com/indiainvestments/content/tree/580d58f1c585b33003c38a56fc5f88ebde23fd10/.gitbook/assets/majesco-morningstar.png)
* [ValueResearchOnline.com](https://github.com/indiainvestments/content/tree/580d58f1c585b33003c38a56fc5f88ebde23fd10/.gitbook/assets/majesco-vro.png)

#### ONGC PE Ratio

* [Company's exceptional losses](https://www.bseindia.com/xml-data/corpfiling/AttachHis/eef5c229-4190-43f2-8ac7-31092008db57.pdf#page=7)
* [MorningStar.in](https://github.com/indiainvestments/content/tree/580d58f1c585b33003c38a56fc5f88ebde23fd10/.gitbook/assets/ongc-morningstar.png)
* [Screener.in](https://web.archive.org/web/20210430172013/https://www.screener.in/company/MAJESCO/consolidated/)
* [ValueResearchOnline.com](https://github.com/indiainvestments/content/tree/580d58f1c585b33003c38a56fc5f88ebde23fd10/.gitbook/assets/ongc-vro.png)
* [NseIndia](https://github.com/indiainvestments/content/tree/580d58f1c585b33003c38a56fc5f88ebde23fd10/.gitbook/assets/ongc-nseindia.png)
* [MoneyControl.com](https://github.com/indiainvestments/content/tree/580d58f1c585b33003c38a56fc5f88ebde23fd10/.gitbook/assets/ongc-moneycontrol.png)

#### Abbott India ROIC

* [Screener.in](https://github.com/indiainvestments/content/tree/580d58f1c585b33003c38a56fc5f88ebde23fd10/.gitbook/assets/screener-roic-light.png)
* [MorningStar.in](https://github.com/indiainvestments/content/tree/580d58f1c585b33003c38a56fc5f88ebde23fd10/.gitbook/assets/morningstar-roic-light.png)
* [TijoriFinance.com](https://github.com/indiainvestments/content/tree/580d58f1c585b33003c38a56fc5f88ebde23fd10/.gitbook/assets/tijori-roic-light.png)

