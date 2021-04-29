---
description: >-
  Pick a screener which doesn't bias you for or against a stock. But you should
  compute the ratios yourself, from ARs. If you've not computed it from the
  annual reports yourself, it might be wrong.
---

# Which screener\(s\) should I use?

## Introduction

Though stock-screeners calculate a lot of things, you must do you own calculations too. You will miss a lot of good opportunities or make some expensive mistakes if you consider only the pre-calculated values.

The objective of this article is not to demean the websites but to show the importance of your own calculations.

----

## Examples of dividend yield

Lets consider the dividend yield of Britannia Industries as on 29th April 2021:

```
Screener.in:    4.18%
MoneyControl:   0.95%
MorningStar.in: 1.78%

Correct value:  ~2-5%
Depends on your judgement on how repeatable these dividends are
```

The differences are because of different treatments of interim dividends. While `screener.in` considers all the interim dividends of FY21, the `MoneyControl` considers only FY20's dividends. `MorningStar` considered only one of the two interim dividends (probably assuming the other one as a one time special dividend).


Another interesting case is of Majesco. The dividend yield as on 29th April 2021 on various websites is:

```
Screener.in:              1,353 %
MorningStar.in:           1,351 %
ValueResearchOnline.com:  1,355 %
(Yeah, 1000+% in all the cases)

Correct value: ~0%
```

The company sold off its entire business and distributed all of it as dividend. This is probably a one time dividend and the correct dividend yield should be around 0%.

Relying on *any* screener and buying highest dividend yields shares blindly can make costly errors in such cases.

----

## Examples of PE Ratio

Let's consider PE ratio of ONGC on different websites as on 29th April 2021:

```
MorningStar.in:           shows blank
Screener.in:              13
ValueResearchOnline.com:  144
NseIndia:                 79
MoneyControl.com:         146
```

The company reported:
```
Standalone TTM EPS:       ₹ 1.32
Consolidated TTM EPS:     ₹ 0.73
The price was:            ₹ 104
Exceptional losses:     ~ ₹ 7.98 / share

Exception losses were of 4899 Cr pre-tax on an old GST liability.
```

The differences across websites is because:
- `ValueResearchOnline` and `MoneyControl` considered EPS as reported by the company.
- `Screener.in` considered consolidated EPS but added back the exceptional losses.
- `BseIndia.com` and `NseIndia.com` considered standalone EPS. 

The correct PE depends on your individual judgement on how you interpret the impact of exceptional items on future earnings.

The PE based on last 5 years average earnings will be 8.29. This is what Benjamin Graham recommends to use in such cases.

----

## Operating margins and gross margins

The text-book definition of gross profit margin (GPM) is `sales - cogs`.

`COGS` is cost of goods sold.

Most websites will show the gross margins on this standard definition. However, this can sometimes be misleading.

Example in case of TCS - `screener.in` shows the GPM as 100%. This is because TCS has no inventory. But the correct metric for `COGS` in this case should be their employee cost.

Similarly in case of banks, most websites (eg `screener.in`), don't consider their interest cost in OPM (operating profit margin) and GPM (gross profit margin). Thus these numbers are shown exceptionally high.

Screening companies on margins can often yield incorrect results for:
- Insurance companies
- Banks
- Finance companies
- Mining companies

----

## Return ratios

In case of Abbott India, the ROIC reported as on 29th April 2021 is:

```
Screener.in:        22.90%
MorningStar.in:     21.53%
TijoriFinance.com:  131%
Correct value:     ~138%
```

The company held fixed-deposits (cash equivalents) of ₹ 2,197 Cr in FY20. While `TijoriFinance` excluded these cash-equivalents in the calculation of capital employed, other two websites didn't exclude it.

These differences in the methods of calculating ROCE, ROIC, ROA and other return ratios can yield wildly different results. You can sometimes miss some interesting companies because their calculated return might be much lower than their economic return ratios.

----

## Summary and Wrap-up

The auto-calculated ratios on websites can often be wrong. Those calculations will often miss "special cases" which are too frequent in finance world. Screening and relying on auto-calculated ratios can thus be *injurious*.

Don’t rely on any of the ready-made screeners. Don’t trust the numbers you see on a screener that’s been prepared by someone else.

The next time you’re doing due diligence on a company, cross-check all calculations yourself.

_**Trust, but verify.**_

To understand how to use a screener, you might want to check this out

{% page-ref page="../../stocks/using-screeners.md" %}

{% hint style="info" %}
We've reached out to some of the teams behind these screeners and have pointed out these issues. They've assured us that they're looking into this.

Tijori Finance moved to paid subscription model now
{% endhint %}
